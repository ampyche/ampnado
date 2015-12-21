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

data = pymongo.MongoClient().ampnadoDB
data2 = pymongo.MongoClient().ampviewsDB

class Data:
	"""
	This creates a data layer essentially all the programs data base calls.
	This will assist with unit testing
	"""
	
	def usercreds_insert_user_pword(self, a_uname, a_pword, a_hash):
		if version < 3:
			data.user_creds.insert({'username': a_uname, 'password': a_pword, 'user_id': a_hash})
		else:
			data.user_creds.insert_one({'username': a_uname, 'password': a_pword, 'user_id': a_hash})

	def usercreds_remove_user_pword(self, anid):
		if version < 3:
			data.user_creds.remove(anid)
		else:
			data.user_creds.delete_many(anid)

	def fone_usercreds_user_pword(self, auname, apword):
		return data.user_creds.find_one({'username': auname, 'password': apword})

###############################################################################		
		
	def fone_prog_paths(self):
		return data.prog_paths.find_one({})	

###############################################################################

	def catalogs_insert(self, x):
		return data.catalogs.insert(x)

###############################################################################

	def tags_insert(self, x):
		if version < 3:
			data.tags.insert(x)
		else:
			data.tags.insert_one(x)

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

	def tags_all_song_songid_artist(self):
		return data.tags.find({}, {'song':1, 'songid':1, 'artist':1, '_id':0})

	def tags_all_filename_artist_album_song(self):
		return data.tags.find({}, {'_id':1, 'filename':1, 'artist':1, 'album':1, 'song':1})

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
#	
#	def tags_aggregate_filesize(self):
#		return data.tags.aggregate({'$group': {'_id': 'soup', 'total' : {'$sum': '$filesize'}}})
#

	def tags_aggregate_filesize(self):
		foo = [int(s['filesize']) for s in data.tags.find({}, {'filesize':1, '_id':0})]
		return sum(foo)

	def tags_update_artistid(self, artlist):
		if version < 3:
			[data.tags.update({'artist': n['artist']}, {'$set': {'artistid': n['artistid']}}, multi=True) for n in artlist] 
		else:
			[data.tags.update_many({'artist': n['artist']}, {'$set': {'artistid': n['artistid']}}) for n in artlist] 

	def tags_update_albumid(self, alblist):
		if version < 3:
			[data.tags.update({'album': alb['album']}, {'$set': {'albumid': alb['albumid']}}, multi=True) for alb in alblist]
		else:
			[data.tags.update_many({'album': alb['album']}, {'$set': {'albumid': alb['albumid']}}) for alb in alblist]

	def tags_update_sthumb_lthumb_and_sizes(self, a):
		if version < 3:
			data.tags.update({'albumartPath': a[0]}, {'$set': {'sthumbnail': a[1], 'smallthumb_size': a[2], 'lthumbnail' : a[3], 'largethumb_size': a[4]}}, multi=True)
		else:
			data.tags.update_many({'albumartPath': a[0]}, {'$set': {'sthumbnail': a[1], 'smallthumb_size': a[2], 'lthumbnail' : a[3], 'largethumb_size': a[4]}})

	def tags_update_thumbs_and_sizes2(self, nt):
		if version < 3:
			data.tags.update({'_id':nt[0]}, {'$set': {'sthumbnail': nt[1], 'lthumbnail': nt[3], 'smallthumb_size': nt[2], 'largethumb_size': nt[4]}}) 
		else:
			data.tags.update_one({'_id':nt[0]}, {'$set': {'sthumbnail': nt[1], 'lthumbnail': nt[3], 'smallthumb_size': nt[2], 'largethumb_size': nt[4]}}) 

	def tags_update_httpmusicpath(self, x, z):
		if version < 3:
			data.tags.update({'filename':x}, {'$set': {'httpmusicpath':z}})
		else:
			data.tags.update_one({'filename':x}, {'$set': {'httpmusicpath':z}})

#
#
#	def tags_update_new_tag_info(self, tags, ftags):
#		print(type(tags))
#		print(type(ftags))
#		if version < 3:
#			data.tags.update({'_id': tags['_id']}, {'$set', {'filename': ftags['filename'], 'artist': ftags['artist'], 'album': ftags['album'], 'song': ftags['song']}})
#		else:
#			data.tags.update_one({'_id': tags['_id']}, {'$set', {'filename': ftags['filename'], 'artist': ftags['artist'], 'album': ftags['album'], 'song': ftags['song']}})
#
#











###############################################################################

	def video_insert(self, x):
		if version < 3:
			data.video.insert(x)
		else:
			data.video.insert_one(x)

	def video_all_filesize(self):
		return data.video.find({}, {'filesize':1, '_id':0})

	def video_distinct_vid_name(self):
		return data.video.distinct('vid_name')

	def video_update_video_posterstring_origposter(self, v):
		if version < 3:
			data.video.update({'filename':v['filename']}, {'$set': {'vid_poster_string':v['vid_poster_string'], 'vid_orig_poster': v['vid_orig_poster']}})		
		else:
			data.video.update_one({'filename':v['filename']}, {'$set': {'vid_poster_string':v['vid_poster_string'], 'vid_orig_poster': v['vid_orig_poster']}})		

	def video_update_noposter_string(self, v):
		if version < 3:
			data.video.update({'filename':v['filename']}, {'$set': {'vid_poster_string':v['vid_poster_string']}})
		else:
			data.video.update_one({'filename':v['filename']}, {'$set': {'vid_poster_string':v['vid_poster_string']}})

###############################################################################

	def stats_insert(self, x):
		if version < 3:
			data.ampnado_stats.insert(x)
		else:
			data.ampnado_stats.insert_one(x)

###############################################################################

	def viewsdb_artalpha_insert(self, x):
		if version < 3:
			data2.artalpha.insert(x)
		else:
			data2.artalpha.insert_one(x)

	def viewsdb_albalpha_insert(self, v):
		if version < 3:
			data2.albalpha.insert(v)
		else:
			data2.albalpha.insert_one(v)

	def viewsdb_insert(self, av):
		if version < 3:
			data2.albumView.insert(av)
		else:
			data2.albumView.insert_one(av)

	def viewsdb_albumview_update(self, albid):
		if version < 3:
			data2.albumView.update({'albumid': albid[0]}, {'$set': {'page': albid[1]}})
		else:
			data2.albumView.update_one({'albumid': albid[0]}, {'$set': {'page': albid[1]}})

	def viewsdb_artistview_insert(self, z):
		if version < 3:
			data2.artistView.insert(z)
		else:
			data2.artistView.insert_one(z)

	def viewsdb_artistview_update(self, c):
		if version < 3:
			data2.artistView.update({'artist': c[0]}, {'$set': {'page': c[1]}})
		else:
			data2.artistView.update_one({'artist': c[0]}, {'$set': {'page': c[1]}})

	def viewsdb_songalpha_insert(self, x):
		if version < 3:
			data2.songalpha.insert(x)
		else:
			data2.songalpha.insert_one(x)
	
	def viewsdb_songview_insert(self, svl):
		if version < 3:
			data2.songView.insert(svl)
		else:
			data2.songView.insert_many(svl)
		
###############################################################################

	def randthumb_insert(self, x):
		if version < 3:
			data.randthumb.insert(x)
		else:
			data.randthumb.insert_one(x)

	def randthumb_rm(self):
		if version < 3:
			data.randthumb.remove({})
		else:
			data.randthumb.delete_many({})