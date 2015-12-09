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
	
	def fone_usercreds_user_pword(self, auname, apword):
		return data.user_creds.find_one({'username': auname, 'password': apword})

	def usercreds_insert_user_pword(self, a_uname, a_pword, a_hash):
		data.user_creds.insert({'username': a_uname, 'password': a_pword, 'user_id': a_hash})

	def usercreds_remove_user_pword(self, anid):
		data.user_creds.remove(anid)

#######################################################################

	def tags_distinct_albumartPath(self):
		return data.tags.distinct('albumartPath')
		
	def tags_distinct_albumid(self):
		return data.tags.distinct('albumid')
		
	def tags_distinct_artist(self):		
		return data.tags.distinct('artist')

	def tags_insert(self, x):
		data.tags.insert(x)
	


	def tags_all_song(self, d):
		return data.tags.find({'song':d}, {'song':1, 'songid':1, '_id':0})

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