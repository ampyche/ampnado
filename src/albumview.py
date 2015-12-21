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
from src.data import Data
import pymongo
v = pymongo.version
version = v.split('.')[0]
version = int(version)

class AlbumView:
	def distinct_albumview(self):
		return Data().tags_distinct_albumid()
		
	def fone_tags_albumid(self, x):
		return Data().fone_tags_albumid(x)
	
	def aggregate_albumid(self, z):
		return Data().tags_aggregate_albumid(z)
	
	def tags_all_song(self, w):
		return Data().tags_all_song(w)
	
	def viewsdb_insert(self, u):
		return Data().viewsdb_insert(u)

	def create_albumView_db(self, a):
		info = self.fone_tags_albumid(a)
		av = {}
		av['albumid'] = info['albumid']
		av['album'] = info['album']
		av['artist'] = info['artist']
		av['artistid'] = info['artistid']
		av['thumbnail'] = info['sthumbnail']
		if version < 3:
			boo = self.aggregate_albumid(a)
			doo = boo['result'][0]['songz']
		else:
			boo = [b['songz'] for b in self.aggregate_albumid(a)]
			doo = boo[0]
		av['numsongs'] = len(doo)
		new_song_list = []
		for d in doo:
			voo = self.tags_all_song(d)
			sids = []
			for s in voo:
				x = (s['song'], s['songid'])
				sids.append(x)
			new_song_list.append(sids)
		av['songs'] = new_song_list
		self.viewsdb_insert(av)
		return av

	def main(self, cores):
		albid = self.distinct_albumview()
		pool = Pool(processes=cores)
		poogle = pool.map(self.create_albumView_db, albid)
		cleaned = [x for x in poogle if x != None]
		pool.close()
		pool.join()
		return cleaned

class AlbumChunkIt:
	def chunks(self, l, n):
		if n < 1:
			n = 1
		return [l[i:i + n] for i in range(0, len(l), n)]		

	def insert_albalpha(self, a):
		Data().viewsdb_albalpha_insert(dict(a))

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
		self.insert_albalpha(dict(albalpha=albalphaoffsetlist))
		return albidPlist
			
	def _get_pages(self, c):
		Data().viewsdb_albumview_update(c)

	def main(self, albv, OFC, cores):
		chunks = self.chunks(albv, OFC)
		gaos = self._get_alphaoffset(chunks)
		pool = Pool(processes=cores)
		voodoo = pool.map(self._get_pages, gaos)
		pool.close()
		pool.join()