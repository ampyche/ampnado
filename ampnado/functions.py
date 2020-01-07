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
import os, random, time, hashlib, uuid
from data import Data
from pymongo import MongoClient, ASCENDING, DESCENDING
try: from mutagen import File
except ImportError: from mutagenx import File
import metatags as MT

ampDBClient = MongoClient("mongodb://db:27017/ampnadoDB")
db = ampDBClient.ampnadoDB

ampVDBClient = MongoClient("mongodb://db:27017/ampviewsDB")
viewsdb = ampVDBClient.ampviewsDB

class FindMedia:
		
	def find_music(self, ptm):
		try:
			mlist = []
			for (paths, dirs, files) in os.walk(ptm, followlinks=True):
				for filename in files:
					print("Processing:\n %s" % filename)
					fnn = os.path.join(paths, filename)
					ext = os.path.splitext(fnn)[1].lower()
					if ext == ".mp3":
						Meta = MT.FileMeta(fnn)
						Mp3 = MT.MP3Tags(fnn)
						x = {
							"Filename": fnn,
							"Extension": ext,
							"Size": Meta.Size,
							"DirPath": Meta.DirPath,
							"SongId": Meta.SongId,
							"Artist": Mp3.Artist,
							"Album": Mp3.Album,
							"Song": Mp3.Song,
							"Track": Mp3.Track,
							"PicId": "",
							"ArtistId": "",
							"AlbumId": "",
							"HttpMusicPath": "/" + fnn.split("/", 4)[4],
						}
						mlist.append(x)
			db.main.insert_many(mlist)
		except TypeError:
			exit()

class AddArtistId:
	def __init__(self):

		self.artist = Data().tags_distinct_artist()
		# self.artlist = []
		self.artlist = [{"Artist":a, "ArtistId": str(uuid.uuid4().hex) } for a in self.artist]
		Data().tags_update_artistid(self.artlist)
	
	# def add_artistids(self):
	# 	self.artlist = [{"Artist":a, "ArtistId": self.artistId } for a in self.artist]
	# 	Data().tags_update_artistid(self.artlist)

class AddAlbumId:
	def __init__(self):
		self.album = Data().tags_distinct_album()
		self.albumlist = []
		
	def add_albumids(self):
		self.albumlist = [{"Album":a, "AlbumId":str(uuid.uuid4().hex)} for a in self.album]	
		Data().tags_update_albumid(self.albumlist)

class Indexes:
	def creat_db_indexes(self):
		import pymongo
		db.main.create_index([('Artist', pymongo.DESCENDING), ('Album', pymongo.ASCENDING)])
		db.main.create_index([('ArtistId', pymongo.DESCENDING), ('AlbumId', pymongo.ASCENDING)])
		db.main.create_index([('Album', pymongo.DESCENDING), ('Song', pymongo.ASCENDING)])
		db.main.create_index([('Album', pymongo.DESCENDING), ('SongId', pymongo.ASCENDING)])
		db.main.create_index([('AlbumId', pymongo.DESCENDING), ('Song', pymongo.ASCENDING)])
		db.main.create_index([('AlbumId', pymongo.DESCENDING), ('SongId', pymongo.ASCENDING)])
		pymongo.TEXT='text'
		db.main.create_index([('Song', 'text')])
		viewsdb.artistView.create_index([('Artist', 'text')])
		viewsdb.albumView.create_index([('Album', 'text')])

class RandomArtDb:
	def __init__(self):
		Data().randthumb_rm()
		self.alist = Data().tags_distinct_albumid()
		self.mc = []
		
	#This takes a list and splits it up into a tup of chunks, n="number per list"	
	def chunks(self, l, n):
		if n < 1:
			n = 1
		return [l[i:i + n] for i in range(0, len(l), n)]

	def create_random_art_db(self):
		Data().randthumb_rm()
		random.shuffle(self.alist)
		bean = self.chunks(self.alist, 5)
		for b in bean:
			x = {}
			c = len(b)
			if c == 5:
				x['chunk'] = b
				x['chunkid'] = str(uuid.uuid4().hex)
				x['displayed'] = 'NOTSHOWN'
				self.mc.append(x)
			elif c < 5:
				x['chunk'] = b 
				x['chunkid'] = str(uuid.uuid4().hex)
				x['displayed'] = 'NOTSHOWN'
				self.mc.append(x)
				print('chunk has less than 5 entries but is added anyway')
			else:
				print('something fucked up')
		db.randthumb.insert(self.mc)		

class DbStats:
	def __init__(self):
		self.thumblist = Data().tags_all_thumb_size()
		self.nltl = []
		self.fs = Data().tags_all_filesize()
		self.nfs = []
		self.artist_count = len(Data().tags_distinct_artist())
		self.album_count = len(Data().tags_distinct_album())
		self.mp3_count = Data().tags_all_filetype_mp3()
		
	def gen_size(self, f): return os.path.getsize(f)
		
	def gen_dirname(self, f): return os.path.dirname(f)
	
	def gen_uuid(self): return str(uuid.uuid4().hex)

	def get_thumb_bytes(self):
		return sum([int(s['AlbumArtSize']) for s in self.thumblist])

	def get_mp3_bytes(self):
		return sum([int(t['Size']) for t in self.fs])

	def convert_bytes(self, abytes):
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

	def db_stats(self):
		picbytes = 	self.get_thumb_bytes()
		totdisk = sum([picbytes, self.get_mp3_bytes()])
		x = {}
		x['total_pic_size'] = self.convert_bytes(picbytes)
		x['total_music_size'] = self.convert_bytes(self.get_mp3_bytes())
		x['total_disk_size'] = self.convert_bytes(totdisk)
		x['total_artists'] = self.artist_count
		x['total_albums'] = self.album_count
		x['total_mp3'] = self.mp3_count
		x['total_ogg'] = 0
		Data().stats_insert(x)

class Functions:
	def get_bytes(self):
		return Data().tags_aggregate_filesize()

	def hash_func(self, a_string):
		return str(hashlib.sha512(a_string.encode('utf-8')).hexdigest())

	def gen_hash(self, auname, apword):
		hash1 = self.hash_func(auname)
		hash2 = self.hash_func(apword)
		hash3 = self.hash_func(str(time.time()))
		hash4 = ''.join((hash1, hash2, hash3))
		hash5 = self.hash_func(hash4)
		return auname, hash2, hash5

	def insert_user(self, a_uname, a_pword):
		h = self.gen_hash(a_uname, a_pword)
		Data().usercreds_insert_user_pword(a_uname, h[1], h[2])

	def gettime(self, at):
		b = time.time()
		return str(b - at)