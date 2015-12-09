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
from pymongo import MongoClient
client = MongoClient()
data = client.ampnadoDB
data2 = client.ampviewsDB

class Data:
	"""
	This creates a data layer essentially all the programs data base calls.
	This will assist with unit testing
	"""
	
	def fone_usercreds_user_pword(self, auname, apword):
		return data.user_creds.find_one({'username': auname, 'password': apword})

	def usercreds_insert_user_pword(self, a_uname, a_pword, a_hash):
		data.user_creds.insert({'username': a_uname, 'password': a_pword, 'user_id': a_hash})

	def usercreds_remove_user_pword(self, anid):
		data.user_creds.remove(anid)
		
###############################################################################		
		
	def fone_prog_paths(self):
		return data.prog_paths.find_one({})	

###############################################################################

	def catalogs_insert(self, x):
		return data.catalogs.insert(x)

###############################################################################

	def tags_insert(self, x):
		data.tags.insert(x)
		
	def tags_distinct_albumartPath(self):
		return data.tags.distinct('albumartPath')
		
	def tags_distinct_albumid(self):
		return data.tags.distinct('albumid')
		
	def tags_distinct_artist(self):		
		return data.tags.distinct('artist')
		
	def tags_distinct_album(self):
		return data.tags.distinct('album')
		
	def tags_distinct_song(self):
		return data.tags.distinct('song')
		
	def tags_all(self):
		return data.tags.find({})
			
	def tags_all_id(self):
		return data.tags.find({}, {'_id':1})
	
	def tags_all_lthumb_size(self):
		return data.tags.find({}, {'largethumb_size':1, '_id':0})
		
	def tags_all_sthumb_size(self):
		return data.tags.find({}, {'smallthumb_size':1, '_id':0})
	
	def tags_all_filesize(self):
		return data.tags.find({}, {'filesize':1, '_id':0})

	def tags_all_filetype_mp3(self):
		return data.tags.find({'filetype': '.mp3'}).count()
		
	def tags_all_filetype_ogg(self):
		return data.tags.find({'filetype': '.ogg'}).count()

	def tags_all_song(self, d):
		return data.tags.find({'song':d}, {'song':1, 'songid':1, '_id':0})

	def tags_all_notagart(self):
		return data.tags.find({'NoTagArt': 0}, {'_id':1})




	def fone_tags_albumid(self, albid):
		return data.tags.find_one({'albumid':albid}, {'album':1, 'albumid': 1, 'artist':1, 'artistid':1, 'sthumbnail':1, '_id':0})

	def fone_tags_albumartPath(self, albpath):
		return data.tags.find_one({'albumartPath':albpath}, {'albumid':1, 'album':1, '_id':0})

	def fone_tags_artist(self, art):
		return data.tags.find_one({'artist': art}, {'artistid': 1, '_id': 0})

	def fone_tags_album(self, alb):
		return data.tags.find_one({'album':alb}, {'albumid':1, '_id':0})



	def tags_aggregate_artist(self, art):
		return data.tags.aggregate([
			{'$match': {'artist': art}},
			{'$group': {'_id': 'album', 'albumz': {'$addToSet': '$album'}}},
			{'$project': {'albumz' :1}}
		])
		
	def tags_aggregate_albumid(self, albid):
		return data.tags.aggregate([
			{'$match': {'albumid': albid}},
			{'$group': {'_id': 'song', 'songz': {'$addToSet': '$song'}}},
			{'$project': {'songz' :1}}
		])	
		
	def tags_aggregate_filesize(self):
		return data.tags.aggregate({'$group': {'_id': 'soup', 'total' : {'$sum': '$filesize'}}})



	def tags_update_artistid(self, artlist):
		[data.tags.update({'artist': n['artist']}, {'$set': {'artistid': n['artistid']}}, multi=True) for n in artlist] 

	def tags_update_albumid(self, alblist):
		[data.tags.update({'album': alb['album']}, {'$set': {'albumid': alb['albumid']}}, multi=True) for alb in alblist]


	def tags_update_sthumb_lthumb_and_sizes(self, a):
		data.tags.update({'albumartPath': a[0]}, {'$set': {'sthumbnail': a[1], 'smallthumb_size': a[2], 'lthumbnail' : a[3], 'largethumb_size': a[4]}}, multi=True)



	def tags_update_thumbs_and_sizes2(self, nt):
		data.tags.update({'_id':nt[0]}, {'$set': {'sthumbnail': nt[1], 'lthumbnail': nt[3], 'smallthumb_size': nt[2], 'largethumb_size': nt[4]}}) 

	def tags_update_httpmusicpath(self, x, z):
		data.tags.update({'filename':x}, {'$set': {'httpmusicpath':z}})



###############################################################################
	def video_insert(self, x):
		data.video.insert(x)

	def video_all_filesize(self):
		return data.video.find({}, {'filesize':1, '_id':0})

	def video_distinct_vid_name(self):
		return data.video.distinct('vid_name')
		

###############################################################################

	def stats_insert(self, x):
		data.ampnado_stats.insert(x)

###############################################################################


	def viewsdb_artalpha_insert(self, x):
		data2.artalpha.insert(x)

	def viewsdb_albalpha_insert(self, v):
		data2.albalpha.insert(v)

	def viewsdb_insert(self, av):
		data2.albumView.insert(av)

	def viewsdb_albumview_updata(self, albid):
		data2.albumView.update({'albumid': albid[0]}, {'$set': {'page': albid[1]}})
		
	def viewsdb_artistview_insert(self, z): 
		data2.artistView.insert(z)
		
	def viewsdb_artistview_update(self, c):
		data2.artistView.update({'artist': c[0]}, {'$set': {'page': c[1]}})
		
###############################################################################
		
	def randthumb_rm(self):
		data.randthumb.remove({})
		
	def randthumb_insert(self, x):
		db.randthumb.insert(x)		