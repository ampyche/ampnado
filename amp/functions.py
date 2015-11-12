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
import os, re, sys, glob, json, shutil, random, time, hashlib, uuid, base64, logging
import amp.artistview as artv
import amp.albumview as albvv
import amp.songview as songv
import amp.ampmulti as amul
from multiprocessing import Pool
try:
	import pymongo
	from pymongo import MongoClient, ASCENDING, DESCENDING
except ImportError: print('ImportError:  PyMongo is not installed')
try: from PIL import Image
except ImportError: print('ImportError:  PIL is not installed')
try: from mutagen import File
except ImportError: from mutagenx import File
else: print('ImportError:  Mutagen or mutagenx is not installed')

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
				if low == '.mp3':
					self.mp3list.append(fn)
				elif low == '.ogg':
					self.ogglist.append(fn)
				elif low == '.m4v' or low == '.mp4': 
					self.vidlist.append(fn)
				else: pass
		logging.info('Finding music complete')
		return self.mp3list, self.ogglist, self.vidlist

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

	def _create_catalog_db(self, cdict, aupd):
		bytes = self._get_bytes(aupd)
		cdict['catobjList'] = self._get_ids(aupd)
		cdict['catTotal'] = self._convert_bytes(bytes['result'][0]['total']),
		self._insert_catalog_info(cdict)
		self._update_tagsdb_with_cat_info(cdict, aupd)
		logging.info('create_catalog_db is complete')

	def add_artistids(self):		
		artlist = [{'artist' : a, 'artistid' : self.gen_uuid()} for a in db.tags.distinct('artist')]
		[db.tags.update({'artist': n['artist']}, {'$set': {'artistid': n['artistid']}}, multi=True) for n in artlist] 
		logging.info('add_artistids complete')

	def add_albumids(self):
		alblist = [{'album': a, 'albumid': self.gen_uuid()} for a in db.tags.distinct('album')]
		[db.tags.update({'album': alb['album']}, {'$set': {'albumid': alb['albumid']}}, multi=True) for alb in alblist]
		logging.info('add_albumids complete')

	def db_stats(self):
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
		db.ampnado_stats.insert(x)
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
		hash4 = ''.join((hash1, hash2, hash3))
		hash5 = self._hash_func(hash4)
		return auname, hash2, hash5

	def insert_user(self, a_uname, a_pword):
		h = self.gen_hash(a_uname, a_pword)
		db.user_creds.insert({'username': a_uname, 'password': h[1], 'user_id': h[2]})
		logging.info('insert_user is complete')

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

	def gettime(self, at):
		b = time.time()
		return (b - at)

	def run_setup(self, aopt, apath, a_time):
		logging.info('Setup Started')
		PATHS = apath
		OPT = aopt
		logging.info('Finding music started')
		print("Constants Setup Complete\nSetup Started\nFinding Music")
		FM = self._find_music_video(PATHS['musiccatPath'])
		print('this is  _find_music_video    time')
		print(self.gettime(a_time))
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
			B = amul.FindIt()
			Bmp3 = B.main(FM[0], OPT, PATHS)
		else: pass
		print('this is _get_tags and Insert tags     time')
		print(self.gettime(a_time))
		logging.info('Getting tag info complete')
		C = amul.HttpMusicPath()
		ZoLu = C.main(PATHS)
		print('this is   add_http_music_path_to_db     time')
		print(self.gettime(a_time))
		addartistid = self.add_artistids()
		print('this is   addartistid     time')
		print(self.gettime(a_time))
		addalbumid = self.add_albumids()
		print('this is   addalbumid     time')
		print(self.gettime(a_time))
		D = amul.GetAlbumArtLists()
		ZeBe = D.main()
		E = amul.GetAlbumArt()
		Zero = E.main(ZeBe, PATHS)
		F = amul.SetNoArtPic()
		Zoo = F.main()
		print('this is   get_albumart     time')
		print(self.gettime(a_time))
		logging.info('Finding videos has started')
		print('Finding Video')
		if filesfound_vid:
			G = amul.CreateVidDict()
			H = amul.GetVideoPoster()
			VID = G.main(FM[2], OPT)
			VIDI = H.main(VID, PATHS)
		print('this is   find and insert vid info     time')
		print(self.gettime(a_time))
		logging.info('Finding video is complete')
		logging.info('Creating artistview has started')
		print('Creating artistView')
		ArtV = artv.ArtistView()
		ArtV.create_artistView_db(OPT['offset'])
		print('this is   ArtistView     time')
		print(self.gettime(a_time))
		logging.info('Creating albumview has completed')
		print('Creating albumview')
		AlbV = albvv.AlbumView()
		albv = AlbV.main(OPT['offset'])
		albv2 = albvv.ChunkIt()
		chunk = albv2.main(albv, OPT['offset'])
		print('this is   AlbumView     time')
		print(self.gettime(a_time))
		logging.info('Creating songview has completed')
		print('Creating songview')
		SongV = songv.SongView()
		SongV.create_songView_db(OPT['offset'])
		print('this is   SongView     time')
		print(self.gettime(a_time))
		logging.info('Creating indexes has started')
		creat_indexes = self._creat_db_indexes()
		print('this is   creat_indexes     time')
		print(self.gettime(a_time))
		logging.info('Creating indexes has completed')
		logging.info('Creating random art has started')
		cradb = self._create_random_art_db()
		print('this is   cradb     time')
		print(self.gettime(a_time))
		logging.info('Creating random art has completed')
		stats = self.db_stats()
		print('this is   db_stats     time')
		print(self.gettime(a_time))