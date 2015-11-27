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
import os, random, time, hashlib, uuid, logging
from pymongo import MongoClient, ASCENDING, DESCENDING
client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

try: from mutagen import File
except ImportError: from mutagenx import File

class Functions():
	def __init__(self):
		mp3list = []
		ogglist = []
		vidlist = []
		self.mp3list = mp3list
		self.ogglist = ogglist
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
					self.mp3list.append({'filename': fn})
				elif low == '.ogg':
					self.ogglist.append({'filename': fn})
				elif low == '.m4v' or low == '.mp4': 
					self.vidlist.append(fn)
				else: pass
		logging.info('SETUP: Finding music complete')
		return (self.mp3list, self.ogglist, self.vidlist)

	def _get_bytes(self):
		return db.tags.aggregate({'$group': {'_id': 'soup', 'total' : {'$sum': '$filesize'}}})
		logging.info('SETUP: _get_bytes is complete')

	def _get_ids(self):
		return [o['_id'] for o in db.tags.find({})]
		logging.info('SETUP: _get_ids is now complete')

	def _insert_catalog_info(self, adict):
		db.catalogs.insert(adict)
		logging.info('SETUP: _insert_catalog_info is complete')

	def _create_catalog_db(self, cdict):
		bytes = self._get_bytes()
		cdict['catobjList'] = self._get_ids()
		cdict['catTotal'] = self._convert_bytes(bytes['result'][0]['total']),
		self._insert_catalog_info(cdict)
		logging.info('SETUP: create_catalog_db is complete')

	def add_artistids(self):		
		artlist = [{'artist' : a, 'artistid' : self.gen_uuid()} for a in db.tags.distinct('artist')]
		[db.tags.update({'artist': n['artist']}, {'$set': {'artistid': n['artistid']}}, multi=True) for n in artlist] 
		logging.info('SETUP: add_artistids complete')

	def add_albumids(self):
		alblist = [{'album': a, 'albumid': self.gen_uuid()} for a in db.tags.distinct('album')]
		[db.tags.update({'album': alb['album']}, {'$set': {'albumid': alb['albumid']}}, multi=True) for alb in alblist]
		logging.info('SETUP: add_albumids complete')

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
		logging.info('SETUP: db stats complete')							

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
		logging.info('SETUP: creditials hash has been created')
		return auname, hash2, hash5

	def insert_user(self, a_uname, a_pword):
		h = self.gen_hash(a_uname, a_pword)
		db.user_creds.insert({'username': a_uname, 'password': h[1], 'user_id': h[2]})
		logging.info('SETUP: insert_user is complete')

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
		logging.info('SETUP: _create_random_art_db is complete')

	def _creat_db_indexes(self):
#		db.tags.create_index([('artist', DESCENDING), ('album', ASCENDING)])
#		db.tags.create_index([('artistid', DESCENDING), ('albumid', ASCENDING)])
#		db.tags.create_index([('album', DESCENDING), ('song', ASCENDING)])
#		db.tags.create_index([('album', DESCENDING), ('songid', ASCENDING)])
#		db.tags.create_index([('album', DESCENDING), ('thumbnail', ASCENDING)])
#		db.tags.create_index([('albumid', DESCENDING), ('thumbnail', ASCENDING)])
#		db.tags.create_index([('albumid', DESCENDING), ('song', ASCENDING)])
#		db.tags.create_index([('albumid', DESCENDING), ('songid', ASCENDING)])
#		db.video.create_index([('vid_id', DESCENDING), ('vid_name', ASCENDING)])
#		viewsdb.albumView.create_index([('artistid', DESCENDING), ('albumid', ASCENDING)])
#		viewsdb.albumView.create_index([('albumid', DESCENDING), ('songs', ASCENDING)])
		import pymongo
		pymongo.TEXT='text'
		db.tags.create_index([('song', 'text')])
		viewsdb.artistView.create_index([('artist', 'text')])
		viewsdb.albumView.create_index([('album', 'text')])
		logging.info('SETUP: _creat_db_indexes is complete')

	def gettime(self, at):
		b = time.time()
		return str(b - at)