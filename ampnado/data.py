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
import pymongo
import bson.son

v = pymongo.version
version = v.split('.')[0]
version = int(version)

class Data:
	"""
	This creates a data layer essentially all the programs data base calls.
	This will assist with unit testing
	"""
	def usercreds_insert_user_pword(self, a_uname, a_pword, a_hash):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		
		if version < 3:
			data.user_creds.insert({'username': a_uname, 'password': a_pword, 'user_id': a_hash})
		else:
			data.user_creds.insert_one({'username': a_uname, 'password': a_pword, 'user_id': a_hash})

	def usercreds_remove_user_pword(self, anid):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			data.user_creds.remove(anid)
		else:
			data.user_creds.delete_many(anid)

	def fone_usercreds_user_pword(self, auname, apword):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.user_creds.find_one({'username': auname, 'password': apword})

###############################################################################		
		
	def fone_prog_paths(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.prog_paths.find_one({})	

###############################################################################

	def tags_distinct_albumid(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.distinct('AlbumId')

	def tags_distinct_artist(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB	
		return data.main.distinct('Artist')

	def tags_distinct_album(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.distinct('Album')

	def tags_all_thumb_size(self):
		data = pymongo.MongoClient("mongodb://db:27017/picdb").picdb
		return data.pics.find({}, {'AlbumArtSize':1, '_id':0})

	def tags_all_filesize(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find({}, {'Size':1, '_id':0})

	def tags_all_filetype_mp3(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find({'Extension': '.mp3'}).count()

	def tags_all_song(self, d):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find({'Song':d}, {'Song':1, 'SongId':1, '_id':0})

	def tags_all_song_songid_artist(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find({}, {'Song':1, 'SongId':1, 'Artist':1, '_id':0})

	def fone_tags_albumid(self, albid):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find_one({'AlbumId':albid}, {'Album':1, 'AlbumId': 1, 'Artist':1, 'ArtistId':1, '_id':0})

	def fone_tags_albumartPath(self, albpath):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find_one({'albumartPath':albpath}, {'albumid':1, 'album':1, '_id':0})

	def fone_tags_artist(self, art):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find_one({'Artist': art}, {'ArtistId': 1, '_id': 0})

	def fone_tags_album(self, alb):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.find_one({'Album':alb}, {'AlbumId':1, '_id':0})

	def tags_aggregate_artist(self, art):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		return data.main.aggregate([
			{'$match': {'Artist': art}},
			{'$group': {'_id': 'Album', 'albumz': {'$addToSet': '$Album'}}},
			{'$project': {'albumz' :1}}
		])

	def tags_aggregate_albumid(self, alb):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		zoo = data.main.find({'AlbumId': alb['AlbumId']}, {'_id':0, 'Song':1, 'SongId':1})
		return [(z['Song'], z['SongId']) for z in zoo]

	def tags_aggregate_filesize(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		foo = [int(s['filesize']) for s in data.tags.find({}, {'filesize':1, '_id':0})]
		return sum(foo)

	def tags_update_artistid(self, artlist):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			[data.main.update({'Artist': n['artist']}, {'$set': {'ArtistId': n['artistid']}}, multi=True) for n in artlist] 
		else:
			[data.main.update_many({'Artist': n['Artist']}, {'$set': {'ArtistId': n['ArtistId']}}) for n in artlist] 

	def tags_update_albumid(self, alblist):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			[data.main.update({'Album': alb['Album']}, {'$set': {'AlbumId': alb['AlbumId']}}, multi=True) for alb in alblist]
		else:
			[data.main.update_many({'Album': alb['Album']}, {'$set': {'AlbumId': alb['AlbumId']}}) for alb in alblist]

	def tags_update_artID(self, alist):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			[data.main.update({'DirPath': a['DirPath']}, {'$set': {'PicId': a['PicId']}}, multi=True) for a in alist]
		else:
			[data.main.update_many({'DirPath': a['DirPath']}, {'$set': {'PicId': a['PicId']}}) for a in alist]		

	def tags_update_httpmusicpath(self, x, z):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			data.tags.update({'filename':x}, {'$set': {'httpmusicpath':z}})
		else:
			data.tags.update_one({'filename':x}, {'$set': {'httpmusicpath':z}})

###############################################################################

	def stats_insert(self, x):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			data.ampnado_stats.insert(x)
		else:
			data.ampnado_stats.insert_one(x)

###############################################################################

	def viewsdb_artalpha_insert(self, x):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.artalpha.insert(x)
		else:
			data2.artalpha.insert_one(x)

	def viewsdb_albalpha_insert(self, v):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.albalpha.insert(v)
		else:
			data2.albalpha.insert_one(v)

	def viewsdb_insert(self, av):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.albumView.insert(av)
		else:
			data2.albumView.insert_one(av)

	def viewsdb_albumview_update(self, albid):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.albumView.update({'AlbumId': albid[0]}, {'$set': {'Page': albid[1]}})
		else:
			data2.albumView.update_one({'AlbumId': albid[0]}, {'$set': {'Page': albid[1]}})

	def viewsdb_artistview_insert(self, z):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.artistView.insert(z)
		else:
			data2.artistView.insert_one(z)

	def viewsdb_artistview_update(self, c):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.artistView.update({'Artist': c[0]}, {'$set': {'Page': c[1]}})
		else:
			data2.artistView.update_one({'Artist': c[0]}, {'$set': {'Page': c[1]}})

	def viewsdb_songalpha_insert(self, x):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.songalpha.insert(x)
		else:
			data2.songalpha.insert_one(x)
	
	def viewsdb_songview_insert(self, svl):
		data2 = pymongo.MongoClient("mongodb://db:27017/ampviewsDB").ampviewsDB
		if version < 3:
			data2.songView.insert(svl)
		else:
			data2.songView.insert_many(svl)
		
###############################################################################

	def randthumb_insert(self, x):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			data.randthumb.insert(x)
		else:
			data.randthumb.insert_many(x)

	def randthumb_rm(self):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		if version < 3:
			data.randthumb.drop()
		else:
			data.randthumb.drop()
			
###############################################################################		

	def get_picid(self, x):
		data = pymongo.MongoClient("mongodb://db:27017/ampnadoDB").ampnadoDB
		pdata = pymongo.MongoClient("mongodb://db:27017/picdb").picdb
		if version < 3:
			pid = [d for d in data.main.find({"AlbumId":x}, {"PicId":1, "_id":0})]
			phttp = pdata.pics.find_one({"PicId":pid[0]["PicId"]}, {"_id":0, "AlbumArtHttpPath":1})
			return phttp["AlbumArtHttpPath"]
		else:
			pid = [d for d in data.main.find({"AlbumId":x}, {"PicId":1, "_id":0})]
			phttp = pdata.pics.find_one({"PicId":pid[0]["PicId"]}, {"_id":0, "AlbumArtHttpPath":1})
			return phttp["AlbumArtHttpPath"]
			
			
