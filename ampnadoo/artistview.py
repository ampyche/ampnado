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
from multiprocessing import Pool
from ampnadoo.data import Data
import os, logging, pymongo
v = pymongo.version
version = v.split('.')[0]
version = int(version)

client = pymongo.MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class ArtistView():
	def __init__(self):
		art = Data().tags_distinct_artist()
		self.art = art
		
	
	def create_artistView_db(self, art):
		z = {}
		z['artist'] = art
		
		
		#artistid = db.tags.find_one({'artist': art}, {'artistid': 1, '_id': 0})
		artistid = Data().fone_tags_artist(art)
		
		
		z['artistid'] = artistid['artistid']
		if version < 3:
			
			boo = Data().tags_aggregate_artist(art)
#			boo = db.tags.aggregate([
#				{'$match': {'artist': art}},
#				{'$group': {'_id': 'album', 'albumz': {'$addToSet': '$album'}}},
#				{'$project': {'albumz' :1}}
#			])
			
			
			
			
			doo = boo['result'][0]['albumz']
		else:
			boo = [
			
				a['albumz'] for a in Data().tags_aggregate_artist(art)
#				a['albumz'] for a in db.tags.aggregate([
#					{'$match': {'artist': art}},
#					{'$group': {'_id': 'album', 'albumz': {'$addToSet': '$album'}}},
#					{'$project': {'albumz' :1}}
#				])
				
				
			]
			doo = boo[0]
		new_alb_list = []
		for d in doo:
			
			
			#albid = db.tags.find_one({'album':d}, {'albumid':1, '_id':0})
			albid = Data().fone_tags_album(d)
			
			moo = d, albid['albumid']
			new_alb_list.append(moo)
		z['albums'] = new_alb_list
		
		
		Data().viewsdb_artistview_insert(z)
		
		
		return z 

	def main(self, cores):
		pool = Pool(processes=cores)
		artv = pool.map(self.create_artistView_db, self.art)
		cleaned = [x for x in artv if x != None]
		pool.close()
		pool.join()
		return cleaned
	
class ArtistChunkIt():
	def chunks(self, l, n):
		if n < 1:
			n = 1
		return [l[i:i + n] for i in range(0, len(l), n)]		

	def _get_alphaoffset(self, chunks):		
		count = 0
		artidPlist = []
		artalphaoffsetlist = []
		for chu in chunks:
			count += 1
			for c in chu:
				albid_page = c['artist'], str(count)
				artidPlist.append(albid_page)
			artalphaoffsetlist.append(str(count))
			
			
		viewsdb.artalpha.insert(dict(artalpha=artalphaoffsetlist))
		
		
		return artidPlist
			
	def _get_pages(self, c):
		
		
		viewsdb.artistView.update({'artist': c[0]}, {'$set': {'page': c[1]}})


 
	def main(self, artv, OFC, cores):
		chunks = self.chunks(artv, OFC)
		gaos = self._get_alphaoffset(chunks)
		pool = Pool(processes=cores)
		voodoo = pool.map(self._get_pages, gaos)
		pool.close()
		pool.join()