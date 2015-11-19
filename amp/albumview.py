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
db = client.ampnadoDB
viewsdb = client.ampviewsDB

import multiprocessing, logging
cores = multiprocessing.cpu_count()

from multiprocessing import Pool

class AlbumView():
	def create_albumView_db(self, a):
		info = db.tags.find_one({'albumid':a}, {'album':1, 'albumid': 1, 'artist':1, 'artistid':1, 'sthumbnail':1, '_id':0})
		av = {}
		av['albumid'] = info['albumid']
		av['album'] = info['album']
		av['artist'] = info['artist']
		av['artistid'] = info['artistid']
		av['thumbnail'] = info['sthumbnail']
		doo = [
			a['songz'] for a in db.tags.aggregate([
				{'$match': {'albumid': a}},
				{'$group': {'_id': 'song', 'songz': {'$addToSet': '$song'}}},
				{'$project': {'songz' :1}}
			])
		]	
		av['numsongs'] = len(doo)
		new_song_list = []
		for d in doo[0]:
			sids = [(s['song'], s['songid']) for s in db.tags.find({'song':d}, {'song':1, 'songid':1, '_id':0})]
			new_song_list.append(sids)
		av['songs'] = new_song_list
		viewsdb.albumView.insert(av)
		return av
	
	def main(self, OFC):
		albid = db.tags.distinct('albumid')
		pool = Pool(processes=cores)
		poogle = pool.map(self.create_albumView_db, albid)
		cleaned = [x for x in poogle if x != None]
		pool.close()
		pool.join()
		return cleaned

class AlbumChunkIt():
	def chunks(self, l, n):
		if n < 1:
			n = 1
		return [l[i:i + n] for i in range(0, len(l), n)]		

	def _get_alphaoffset(self, chunks):		
		count = 0
		albidPlist = []
		albalphaoffsetlist = []
		for chu in chunks:
			count += 1
			for c in chu:
				albid_page = c['albumid'], str(count)
				albidPlist.append(albid_page)
			albalphaoffsetlist.append(str(count))
		viewsdb.albalpha.insert(dict(albalpha=albalphaoffsetlist))
		return albidPlist
			
	def _get_pages(self, c):
		viewsdb.albumView.update({'albumid': c[0]}, {'$set': {'page': c[1]}})

	def main(self, albv, OFC):
		chunks = self.chunks(albv, OFC)
		gaos = self._get_alphaoffset(chunks)
		pool = Pool(processes=cores)
		voodoo = pool.map(self._get_pages, gaos)
		pool.close()
		pool.join()