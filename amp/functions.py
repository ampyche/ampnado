#!/usr/bin/python3
###############################################################################
###############################################################################
	# LICENSE: GNU General Public License, version 2 (GPLv2)
	# Copyright 2015, Charlie J. Smotherman
	#
	# This program is free software; you can redistribute it and/or
	# modify it under the terms of the GNU General Public License v2
	# as published by the Free Software Foundation.
	#
	# This program is distributed in the hope that it will be useful,
 	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.
	#
	# You should have received a copy of the GNU General Public License
	# along with this program; if not, write to the Free Software
	# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
###############################################################################
###############################################################################
import os, re, sys, glob, json, shutil, random, time, hashlib, uuid, base64 
import logging, pymongo
from pymongo import MongoClient, ASCENDING, DESCENDING
from PIL import Image
try: from mutagen import File
except ImportError: from mutagenx import File

import amp.artistview as artv
import amp.albumview as albv
import amp.songview as songv

from pprint import pprint

client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class SetUp():
	def __init__(self):
		mp3list = []
		self.mp3list = mp3list
		
		ogglist = []
		self.ogglist = ogglist
		
		vidlist = []
		self.vidlist = vidlist

	def gen_size(self, f): return os.stat(f).st_size
		
	def gen_dirname(self, f): return os.path.dirname(f)
	
	def gen_uuid(self): return str(uuid.uuid4().hex)

	def _get_lthumb_bytes(self): return sum([int(s['largethumb_size']) for s in db.tags.find({}, {'largethumb_size':1, '_id':0})])

	def _get_sthumb_bytes(self): return sum([int(l['smallthumb_size']) for l in db.tags.find({}, {'smallthumb_size':1, '_id':0})])

	def _get_mp3_bytes(self): return sum([int(t['filesize']) for t in db.tags.find({}, {'filesize':1, '_id':0})])

	def _get_vid_bytes(self): return sum([int(v['filesize']) for v in db.video.find({}, {'filesize':1, '_id':0})])

	def _get_artist_count(self): return len(db.tags.distinct('artist'))

	def _get_album_count(self): return len(db.tags.distinct('album'))

	def _get_song_count(self): return len(db.tags.distinct('song'))

	def _get_video_count(self): return len(db.video.distinct('vid_name'))

	def _get_temp_lthumb_bytes(self): return sum([int(s['largethumb_size']) for s in db.tempTags.find({}, {'largethumb_size':1, '_id':0})])

	def _get_temp_sthumb_bytes(self): return sum([int(l['smallthumb_size']) for l in db.tempTags.find({}, {'smallthumb_size':1, '_id':0})])

	def _get_temp_mp3_bytes(self): return sum([int(t['filesize']) for t in db.tempTags.find({}, {'filesize':1, '_id':0})])

	def _get_temp_vid_bytes(self): return sum([int(v['filesize']) for v in db.tempVideo.find({}, {'filesize':1, '_id':0})])

	def _get_temp_artist_count(self): return len(db.tempTags.distinct('artist'))

	def _get_temp_album_count(self): return len(db.tempTags.distinct('album'))

	def _get_temp_song_count(self): return len(db.tempTags.distinct('song'))

	def _get_temp_video_count(self): return len(db.tempVideo.distinct('vid_name'))

	def _convert_bytes(self, abytes):
		if abytes >= 1099511627776:
			terabytes = abytes / 1099511627776
			size = str('%.2fT' % terabytes)
		elif abytes >= 1073741824:
			gigabytes = abytes / 1073741824
			size = str('%.2fG' % gigabytes)
		elif abytes >= 1048576:
			megabytes = abytes / 1048576
			size = str('%.2fM' % megabytes)
		elif abytes >= 1024:
			kilobytes = abytes / 1024
			size = str('%.2fK' % kilobytes)
		else:
			size = str('%.2fb' % abytes)
		return size

	def _find_music_video(self, path_to_music):
		for (paths, dirs, files) in os.walk(path_to_music, followlinks=True):
			for filename in files:
				fn = os.path.join(paths, filename)
				fnse = os.path.splitext(fn)
				low = fnse[1].lower()
				x = {}
				x['filename'] = fn
				x['filesize'] = self.gen_size(fn)
				x['dirpath'] = self.gen_dirname(fn)
				x['filetype'] = low
				if low == '.mp3':
					self.mp3list.append(x)
				elif low == '.ogg':
					self.ogglist.append(x)
				elif low == '.m4v' or low == '.mp4': 
					self.vidlist.append(x)
				else: pass
		logging.info('Finding music complete')
		return self.mp3list, self.ogglist, self.vidlist

	def _get_tags(self, a_list, apath):
		zlist = []
		for a in a_list:
			audio  = File(a['filename'])
			try: track = audio['TRCK'].text[0]
			except KeyError:	pass
			try: artist = audio["TPE1"].text[0]
			except KeyError: logging.info(''.join(("KeyError: No TPE1 tag... ", fn)))
			try: album = audio["TALB"].text[0]
			except KeyError: logging.info(''.join(("KeyError No TALB tag ... ", a)))
			try: song = audio['TIT2'].text[0]
			except KeyError: logging.info(''.join(("KeyError: No TIT2 tag... ", song)))
			a['track'] = track
			a['artist'] = artist
			a['album'] = album
			a['song'] = song
			a['songid'] = self.gen_uuid()
			a['programPath'] = apath['programPath']
			ppath = '/'.join((os.path.dirname(a['filename']), "folder.jpg"))
			if os.path.isfile(ppath):
				a['albumartPath'] = ppath
				a['NoTagArt'] = 1
			else:
				try:
					artwork = audio.tags[u'APIC:'].data
					with open(ppath, 'wb') as img: img.write(artwork)
				except (KeyError, TypeError):
					a['NoTagArt'] = 0
					a['albumartPath'] = '/'.join((os.path.dirname(a['filename']), "NOTAGART"))
				else:
					if not os.path.isfile(ppath):
						a['NoTagArt'] = 0
						a['albumartPath'] = '/'.join((os.path.dirname(a['filename']), "NOTAGART"))
		logging.info('Getting tags complete')
		return a_list

	def _get_bytes(self, upd):
		if not upd:
			return db.tags.aggregate({'$group': {'_id': 'soup', 'total' : {'$sum': '$filesize'}}})
		else: 
			return db.tempTags.aggregate({'$group': {'_id': 'soup', 'total' : {'$sum': '$filesize'}}})
		logging.info('_get_bytes is complete')

	def _get_ids(self, bupd):
		if not bupd: return [o['_id'] for o in db.tags.find({})]
		else: return [o['_id'] for o in db.tempTags.find({})]
		logging.info('_get_ids is now complete')

	def _insert_catalog_info(self, adict):
		db.catalogs.insert(adict)
		logging.info('_insert_catalog_info is complete')
		
	def _update_tagsdb_with_cat_info(self, adict, upd):
		if not upd: db.tags.update({}, {'$set': {'catid': adict['catid']}}, multi=True)
		else: db.tempTags.update({}, {'$set': {'catid': adict['catid']}}, multi=True)
		logging.info('_update_tagsdb_with_cat_info is complete')

	def _create_catalog_db(self, cdict, aupd):
		bytes = self._get_bytes(aupd)
		cdict['catobjList'] = self._get_ids(aupd)
		cdict['catTotal'] = self._convert_bytes(bytes['result'][0]['total']),
		self._insert_catalog_info(cdict)
		self._update_tagsdb_with_cat_info(cdict, aupd)
		logging.info('create_catalog_db is complete')
	
	def add_http_music_path_to_db(self, a_opt, a_path, a_cat, u_date):
		new_path_list = []
		cat_name = a_cat['catname']
		httpmusicpath = a_path['httpmusicPath']
		if not u_date:
			for p in db.tags.find({}):
				fn1 = p['filename'].split(a_opt['musicpath'])
				fn2 = '/'.join((httpmusicpath, ''.join((cat_name, fn1[1]))))
				fn3 = ''.join(('/', cat_name, fn1[1]))
				fn4 = fn3[:-4]
				n = p['filename'], fn2, fn4
				new_path_list.append(n)
			[db.tags.update({'filename':new[0]}, {'$set': {'httpmusicpath':new[1], 'playlistpath':new[2]}}) for new in new_path_list]
		else:
			for p in db.tempTags.find({}):
				fn1 = p['filename'].split(a_cat['musicpath'])
				fn2 = '/'.join((httpmusicpath, ''.join((cat_name, fn1[1]))))
				fn3 = ''.join(('/', cat_name, fn1[1]))
				fn4 = fn3[:-4]
				n = p['filename'], fn2, fn4
				new_path_list.append(n)
			
			[db.tempTags.update({'filename':new[0]}, {'$set': {'httpmusicpath':new[1], 'playlistpath':new[2]}}) for new in new_path_list]
		logging.info('add_http_music_path_to_tags_db complete')

	def add_artistids(self, u_date):
		if not u_date:
			artlist = [{'artist' : a, 'artistid' : self.gen_uuid()} for a in db.tags.distinct('artist')]
			[db.tags.update({'artist': n['artist']}, {'$set': {'artistid': n['artistid']}}, multi=True) for n in artlist] 
		else:
			artlist = [{'artist' : a, 'artistid' : self.gen_uuid()} for a in db.tempTags.distinct('artist')]
			[db.tempTags.update({'artist': n['artist']}, {'$set': {'artistid': n['artistid']}}, multi=True) for n in artlist] 
		logging.info('add_artistids complete')

	def add_albumids(self, u_date):
		if not u_date:
			alblist = [{'album': a, 'albumid': self.gen_uuid()} for a in db.tags.distinct('album')]
			[db.tags.update({'album': alb['album']}, {'$set': {'albumid': alb['albumid']}}, multi=True) for alb in alblist]
		else:
			alblist = [{'album': a, 'albumid': self.gen_uuid()} for a in db.tempTags.distinct('album')]
			[db.tempTags.update({'album': alb['album']}, {'$set': {'albumid': alb['albumid']}}, multi=True) for alb in alblist]
		logging.info('add_albumids complete')

	def get_albumart_lists(self, u_date):
		if not u_date:
			albinfolist = []
			for a in db.tags.distinct('albumartPath'):
				asp = a.split('/')
				if asp[-1:][0] == 'NOTAGART':
					logging.info(''.join(['no tag art found', a]))
				else:
					albinfo = db.tags.find_one({'albumartPath':a}, {'albumid':1, 'album':1, '_id':0})
					ainfo = a, albinfo['albumid'], albinfo['album']
					albinfolist.append(ainfo)
			return albinfolist
		else:
			albinfolist = []
			for a in db.tempTags.distinct('albumartPath'):
				asp = a.split('/')
				if asp[-1:][0] == 'NOTAGART':
					logging.info(''.join(['no tag art found', a]))
				else:
					albinfo = db.tempTags.find_one({'albumartPath':a}, {'albumid':1, 'album':1, '_id':0})
					ainfo = a, albinfo['albumid'], albinfo['album']
					albinfolist.append(ainfo)
			return albinfolist
		logging.info('get_albumart_lists complete')

	def _get_smallthumb(self, location, filename, size):
		im2 = Image.open(filename)
		im2.thumbnail(size, Image.ANTIALIAS)
		im2.save(location, "JPEG")

	def _get_thumb_size(self, location): return os.stat(location).st_size
		
	def _get_b64_image(self, location):	
		with open(location, 'rb') as imagefile:
			 return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))

	def _img_size_check_and_save(self, img, size, location):
		im = Image.open(img)
		sim = im.size
		if sim[0] > 200 and sim[1] > 200:
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(location, "JPEG")
		else:
			im.save(location, "JPEG")

	def create_thumbs(self, plist, save_loc10, paths, u_date):
		dthumb = (200, 200)
		d2thumb = (100, 100)
		loc2 = ''.join((save_loc10, '200x200.jpg'))
		loc1 = ''.join((save_loc10, '100x100.jpg'))
		for p in plist:
			im2 = self._get_smallthumb(loc1, p[0], d2thumb)	
			x = {}
			x['albumartPath'] = p[0]
			x['albumid'] = p[1]
			x['album'] = p[2]
			x['smallthumb_size'] = self._get_thumb_size(loc1)
			x['smallthumb'] = self._get_b64_image(loc1)
			os.remove(loc1)
			self._img_size_check_and_save(p[0], dthumb, loc2)
			x['largethumb_size'] = self._get_thumb_size(loc2)
			x['largethumb'] = self._get_b64_image(loc2)
			os.remove(loc2)
			if not u_date:
				db.tags.update({'albumartPath': p[0]}, {'$set': {'sthumbnail': x['smallthumb'], 'smallthumb_size': x['smallthumb_size'], 'lthumbnail' : x['largethumb'], 'largethumb_size': x['largethumb_size']}}, multi=True)
			else:
				db.tempTags.update({'albumartPath': p[0]}, {'$set': {'sthumbnail': x['smallthumb'], 'smallthumb_size': x['smallthumb_size'], 'lthumbnail' : x['largethumb'], 'largethumb_size': x['largethumb_size']}}, multi=True)
		NAP1 = '/'.join([paths['programPath'], 'static', 'images', 'no_art_pic_100x100.png'])
		NAP1_size = os.stat(NAP1).st_size
		NAP1imgstr = self._get_b64_image(NAP1)	
		NAP2 = '/'.join([paths['programPath'], 'static', 'images', 'no_art_pic_200x200.png'])
		NAP2_size = os.stat(NAP2).st_size
		NAP2imgstr = self._get_b64_image(NAP2)
		if not u_date:
			ntaid = [nta['_id'] for nta in db.tags.find({'NoTagArt': 0}, {'_id':1})]
			[db.tags.update({'_id':nt}, {'$set': {'sthumbnail': NAP1imgstr, 'lthumbnail': NAP2imgstr, 'smallthumb_size': NAP1_size, 'largethumb_size': NAP2_size}}) for nt in ntaid]
		else:
			ntaid = [nta['_id'] for nta in db.tempTags.find({'NoTagArt': 0}, {'_id':1})]
			[db.tempTags.update({'_id':nt}, {'$set': {'sthumbnail': NAP1imgstr, 'lthumbnail': NAP2imgstr, 'smallthumb_size': NAP1_size, 'largethumb_size': NAP2_size}}) for nt in ntaid]
		logging.info('create_thumbs is complete')

	def get_albumart(self, apaths, u_date):
		alblist = self.get_albumart_lists(u_date)
		sl10 = ''.join([apaths['tempPath'], '/'])
		create_thumbs = self.create_thumbs(alblist, sl10, apaths, u_date)
		logging.info('get_albumart is complete')

	def db_stats(self, u_date):
		picbytes = 	sum([self._get_lthumb_bytes(), self._get_sthumb_bytes()])
		totdisk = sum([picbytes, self._get_mp3_bytes(), self._get_vid_bytes()])
		x = {}
		x['total_pic_size'] = self._convert_bytes(picbytes)
		x['total_music_size'] = self._convert_bytes(self._get_mp3_bytes())
		x['total_video_size'] = self._convert_bytes(self._get_vid_bytes())
		x['total_disk_size'] = self._convert_bytes(totdisk)
		x['total_artists'] = self._get_artist_count()
		x['total_albums'] = self._get_album_count()
		x['total_songs'] = self._get_song_count()
		x['total_videos'] = self._get_video_count()
		if not u_date:
			db.ampnado_stats.insert(x)
		else:	
			db.ampnado_stats.update({}, {'$set': {
				'total_pic_size': x['total_pic_size'],
				'total_music_size': x['total_music_size'],
				'total_video_size': x['total_video_size'],
				'total_disk_size': x['total_disk_size'],
				'total_artists': x['total_artists'],
				'total_albums': x['total_albums'],
				'total_songs': x['total_songs'],
				'total_videos': x['total_videos'],
			}})
		logging.info('db stats complete')							

	#This takes a list and splits it up into a tup of chunks, n="number per list"	
	def chunks(self, l, n):
		if n < 1:
			n = 1
		return [l[i:i + n] for i in range(0, len(l), n)]

	def _hash_func(self, a_string):
		return str(hashlib.sha512(a_string.encode('utf-8')).hexdigest())

	def gen_hash(self, auname, apword):
		hash1 = self._hash_func(auname)
		hash2 = self._hash_func(apword)
		hash3 = self._hash_func(str(time.time()))
		hash4 =  ''.join((hash1, hash2, hash3))
		hash5 = self._hash_func(hash4)
		return auname, hash2, hash5

	def insert_user(self, a_uname, a_pword):
		h = self.gen_hash(a_uname, a_pword)
		db.user_creds.insert({'username': a_uname, 'password': h[1], 'user_id': h[2]})
		logging.info('insert_user is complete')

	def _create_vid_dict(self, avidlist, opt, acat, upd):
		vid_dict_list = []
		if not upd:
			for avid in avidlist:
				avids = avid['filename'].split(opt['musicpath'])
				avid['vid_playpath'] = ''.join(('/static/MUSIC/', opt['catname'], avids[1]))
				avid['catname'] = opt['catname']
				avs2 = avid['filename'].replace('.2011', '').replace('2012', '').replace('.2014','').replace('.2015','').replace('.720p','').replace('.1080p', '')
				avs1 = avs2.replace('.BluRay', '').replace('.Bluray', '').replace('Brrip', '').replace('.x264', '').replace('.X264', '').replace('.YIFY', '')
				avs = avs1[:-3].split('/')
				nav = len(avs) - 1
				van = re.sub('[\_\.]', " ", avs[nav]).split(' ')
				if len(van) > 2:
					boo = [v.capitalize() for v in van]
					avid['vid_name'] = ' '.join(boo)
				else:
					avid['vid_name'] = van[0].capitalize()
				vid_dict_list.append(avid)
		else:
			for avid in avidlist:
				avids = avid['filename'].split(acat['musicpath'])
				avid['vid_playpath'] = ''.join(('/static/MUSIC/', acat['catname'], avids[1]))
				avid['catname'] = acat['catname']
				avs2 = avid['filename'].replace('.2011', '').replace('2012', '').replace('.2014','').replace('.2015','').replace('.720p','').replace('.1080p', '')
				avs1 = avs2.replace('.BluRay', '').replace('.Bluray', '').replace('Brrip', '').replace('.x264', '').replace('.X264', '').replace('.YIFY', '')
				avs = avs1[:-3].split('/')
				nav = len(avs) - 1
				van = re.sub('[\_\.]', " ", avs[nav]).split(' ')
				if len(van) > 2:
					boo = [v.capitalize() for v in van]
					avid['vid_name'] = ' '.join(boo)
				else:
					avid['vid_name'] = van[0].capitalize()
				vid_dict_list.append(avid)
		logging.info('_create_vid_dict is complete')
		return vid_dict_list

	def find_video_posters(self, vinfo, path):
		vplist = []
		for v in vinfo:
			vname = v['vid_name'].lower()
			vp = v['filename']
			vpRS = vp.rsplit('/', 1)
			posterP1 = vpRS[1][:-4].lower()
			posterP = re.sub('[\.]', '_', posterP1)
			PP = ''.join((vpRS[0], '/poster_', posterP, '.jpg'))
			tpath = '/'.join((path['programPath'], 'static', 'TEMP', ''.join(('poster_', posterP, '.jpg'))))
			if os.path.exists(PP):
				v['vid_orig_poster'] = PP
				vthumb = 100, 100
				self._img_size_check_and_save(PP, vthumb, tpath)
				v['vid_poster_string'] = self._get_b64_image(tpath)
				os.remove(tpath)
			else:
				default = '/'.join((path['programPath'], 'static', 'images', 'no_art_pic_100x100.png'))
				v['vid_poster_string'] = self._get_b64_image(default)
			vplist.append(v)
		logging.info('find_video_posters is complete')
		return vplist

	def _create_random_art_db(self):
		db.randthumb.remove({})
		alist = db.tags.distinct('albumid')
		random.shuffle(alist)
		bean = self.chunks(alist, 5)
		mc = []
		for b in bean:
			x = {}
			c = len(b)
			if c == 5:
				x['chunk'] = b 
				x['displayed'] = 'NOTSHOWN'
				mc.append(x)
			elif c < 5:
				print('chunk has less than 5 entries')
			else:
				print('something fucked up')
		db.randthumb.insert(mc)		
		logging.info('_create_random_art_db is complete')

	def _creat_db_indexes(self):
		pymongo.TEXT='text'
		db.tags.create_index([('artist', DESCENDING), ('album', ASCENDING)])
		db.tags.create_index([('artistid', DESCENDING), ('albumid', ASCENDING)])
		db.tags.create_index([('album', DESCENDING), ('song', ASCENDING)])
		db.tags.create_index([('album', DESCENDING), ('songid', ASCENDING)])
		db.tags.create_index([('album', DESCENDING), ('thumbnail', ASCENDING)])
		db.tags.create_index([('albumid', DESCENDING), ('thumbnail', ASCENDING)])
		db.tags.create_index([('albumid', DESCENDING), ('song', ASCENDING)])
		db.tags.create_index([('albumid', DESCENDING), ('songid', ASCENDING)])
		db.tags.create_index([('song', 'text')])
		db.video.create_index([('vid_id', DESCENDING), ('vid_name', ASCENDING)])
		viewsdb.artistView.create_index([('artist', 'text')])
		viewsdb.albumView.create_index([('album', 'text')])
		viewsdb.albumView.create_index([('artistid', DESCENDING), ('albumid', ASCENDING)])
		viewsdb.albumView.create_index([('albumid', DESCENDING), ('thumbnail', ASCENDING)])
		viewsdb.albumView.create_index([('albumid', DESCENDING), ('songs', ASCENDING)])
		logging.info('_creat_db_indexes is complete')

	def run_setup(self, aopt, apath, acat, aupdate):
		logging.info('Setup Started')
		paths = apath
		OPT = aopt
		
		logging.info('Finding music started')
		print("Constants Setup Complete\nSetup Started")
		print("Finding Music")
		if aupdate: FM = self._find_music_video(acat['musicpath'])
		else: FM = self._find_music_video(OPT['musicpath'])
		
		if len(FM[0]) >= 1: filesfound_mp3 = True
		else: filesfound_mp3 = False
		if len(FM[1]) >= 1: filesfound_ogg = True
		else: filesfound_ogg = False
		if len(FM[2]) >= 1: filesfound_vid = True
		else: filesfound_vid = False
		print("Finding music complete")
		logging.info('Finding music complete')

		logging.info('Getting tag info started')
		if filesfound_mp3: 
			tags = self._get_tags(FM[0], paths)
			if not aupdate: db.tags.insert(tags)
			else: db.tempTags.insert(tags)
			print('Inserting tags into tags DB')
		else: pass
		logging.info('Getting tag info complete')
		
		logging.info('Finding videos has started')
		print('Finding Video')
		if filesfound_vid:
			if not aupdate:
				VID = self._create_vid_dict(FM[2], OPT, acat, aupdate)
				VP = self.find_video_posters(VID, paths)
				db.video.insert(VP)
			else:
				VID = self._create_vid_dict(FM[2], OPT, acat, aupdate)
				VP = self.find_video_posters(VID, paths)
				db.tempVideo.insert(VP)
		else: pass
		logging.info('Finding video is complete')

		logging.info('Getting album art has started')
		print("Getting Album Art")
		cat = self._create_catalog_db(acat, aupdate)
		add_http_music_path_to_db = self.add_http_music_path_to_db(OPT, paths, acat, aupdate)
		addartistid = self.add_artistids(aupdate)
		addalbumid = self.add_albumids(aupdate)
		addalbumart = self.get_albumart(paths, aupdate)
		logging.info('Getting album art has completed')
		
		logging.info('Creating artistview has started')
		print('Creating artistView')
		ArtV = artv.ArtistView()
		ArtV.create_artistView_db(aupdate, OPT['offset'])
		logging.info('Creating artistview has completed')
		AlbV = albv.AlbumView()
		AlbV.create_albumView_db(aupdate, OPT['offset'])
		logging.info('Creating albumview has completed')
		SongV = songv.SongView()
		SongV.create_songView_db(aupdate, OPT['offset'])
		logging.info('Creating songview has completed')
		
		logging.info("Copying tempDBs to main DB has started")
		if aupdate:
			ttags = db.tempTags.find({}, {'_id':0})
			talbv = viewsdb.tempalbumView.find({}, {'_id':0})
			tartv = viewsdb.tempartistView.find({}, {'_id':0})
			ttv = db.tempVideo.find({}, {'_id':0})
			db.tags.insert(ttags)
			db.video.insert(ttv)
			viewsdb.albumView.insert(talbv)
			viewsdb.artistView.insert(tartv)
			db.tempTags.remove({})
			viewsdb.tempalbumView.remove({})
			viewsdb.tempartistView.remove({})
		logging.info("Copying tempDBs to main DB has completed")
		
		logging.info('Creating indexes has started')
		creat_indexes = self._creat_db_indexes()
		logging.info('Creating indexes has completed')
		
		logging.info('Getting Stats has started')
		print('Getting Stats')
		dbstats = self.db_stats(aupdate)
		logging.info('Getting Stats has completed')

		logging.info('Creating initial user has started')
		print('Creating initial user')
		adduser = self.insert_user(OPT['uname'], OPT['pword'])
		logging.info('Creating initial user has completed')
		
		logging.info('Creating random art has started')
		cradb = self._create_random_art_db()
		logging.info('Creating random art has completed')