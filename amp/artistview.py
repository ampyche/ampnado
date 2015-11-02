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
import logging
from pymongo import MongoClient

client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class ArtistView():
	def create_artistView_db(self, u_date, OFC):
		count = 0
		page = 1
		art_artid_list = []
		artalphaoffsetlist = []
		if not u_date:
			for art in db.tags.distinct('artist'):
				z = {}
				z['artist'] = art
				count += 1
				if count == OFC:
					page += 1
					count = 0
				artalphaoffsetlist.append(page)
				z['page'] = page
				artistid = db.tags.find_one({'artist': art}, {'artistid': 1, '_id': 0})
				z['artistid'] = artistid['artistid']
				boo = db.tags.aggregate([
					{'$match': {'artist': art}},
					{'$group': {'_id': 'album', 'albumz': {'$addToSet': '$album'}}},
					{'$project': {'albumz' :1}}
					])
				doo = boo['result'][0]['albumz']
				new_alb_list = []
				for d in doo:
					albid = db.tags.find_one({'album':d}, {'albumid':1, '_id':0})
					moo = d, albid['albumid']
					new_alb_list.append(moo)
				z['albums'] = new_alb_list
				art_artid_list.append(z)
				artalphaoffsetlist = list(set(artalphaoffsetlist))
			viewsdb.artalpha.insert(dict(artalpha=artalphaoffsetlist))
			viewsdb.artistView.insert(art_artid_list)
		else:
			for art in db.tempTags.distinct('artist'):
				z = {}
				z['artist'] = art
				count += 1
				if count == OFC:
					page += 1
					count = 0
					artalphaoffsetlist.append(page)
				z['page'] = page
				artistid = db.tempTags.find_one({'artist': art}, {'artistid': 1, '_id': 0})
				z['artistid'] = artistid['artistid']
				boo = db.tempTags.aggregate([
					{'$match': {'artist': art}},
					{'$group': {'_id': 'album', 'albumz': {'$addToSet': '$album'}}},
					{'$project': {'albumz' :1}}
					])
				doo = boo['result'][0]['albumz']
				new_alb_list = []
				for d in doo:
					albid = db.tempTags.find_one({'album':d}, {'albumid':1, '_id':0})
					moo = d, albid['albumid']
					new_alb_list.append(moo)
				z['albums'] = new_alb_list
				art_artid_list.append(z)
			viewsdb.artalpha.insert(dict(artalpha=artalphaoffsetlist))
			viewsdb.tempartistView.insert(art_artid_list)
		logging.info('create_artistView_db')