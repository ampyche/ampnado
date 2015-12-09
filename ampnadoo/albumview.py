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
import os, logging
from multiprocessing import Pool
from ampnadoo.data import Data
import pymongo
v = pymongo.version
version = v.split('.')[0]
version = int(version)

client = pymongo.MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class AlbumView():
	def __init__(self):
		albid = Data().tags_distinct_albumid()
		self.albid = albid

	def create_albumView_db(self, a):
		info = Data().fone_tags_albumid(a)
		av = {}
		av['albumid'] = info['albumid']
		av['album'] = info['album']
		av['artist'] = info['artist']
		av['artistid'] = info['artistid']
		av['thumbnail'] = info['sthumbnail']
		if version < 3:
			boo = Data().tags_aggregate_albumid(a)
			doo = boo['result'][0]['songz']
		else:
			boo = [a['songz'] for a in Data().tags_aggregate_albumid(a)]
			doo = boo[0]
		av['numsongs'] = len(doo)
		new_song_list = []
		for d in doo:
			voo = Data().tags_all_song(d)
			sids = []
			for s in voo:
				x = (s['song'], s['songid'])
				sids.append(x)
			new_song_list.append(sids)
		av['songs'] = new_song_list
		Data().viewsdb_insert(av)
		return av

	def main(self, cores):
		pool = Pool(processes=cores)
		poogle = pool.map(self.create_albumView_db, self.albid)
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
		Data().viewsdb_albalpha_insert(dict(albalpha=albalphaoffsetlist))
		#viewsdb.albalpha.insert(dict(albalpha=albalphaoffsetlist))
		return albidPlist
			
	def _get_pages(self, c):
		#viewsdb.albumView.update({'albumid': c[0]}, {'$set': {'page': c[1]}})
		Data().viewsdb_albumview_updata(c)
		

	def main(self, albv, OFC, cores):
		chunks = self.chunks(albv, OFC)
		gaos = self._get_alphaoffset(chunks)
		pool = Pool(processes=cores)
		voodoo = pool.map(self._get_pages, gaos)
		pool.close()
		pool.join()