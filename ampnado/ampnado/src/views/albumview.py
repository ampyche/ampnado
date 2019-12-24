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
import multiprocessing as mu
from src.data import Data
import pymongo

v = pymongo.version
version = v.split('.')[0]
version = int(version)
cores = mu.cpu_count()

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
		
	def pichttp(self, x):
		return Data().get_picid(x)

	def create_albumView_db(self, a):
		info = self.fone_tags_albumid(a)
		boo = self.aggregate_albumid(info)
		info["AlbumArtHttpPath"] = self.pichttp(a)
		info['NumSongs'] = len(boo)
		info['Songs'] = boo
		self.viewsdb_insert(info)		
		return info		

	def main(self):
		albid = self.distinct_albumview()
		pool = Pool(processes=cores)
		poogle = pool.map(self.create_albumView_db, albid)
		cleaned = [x for x in poogle if x != None]
		pool.close()
		pool.join()
		return cleaned

class AlbumChunkIt:
	def chunks(self, l, nn):
		n = int(nn)
		if n < 1:
			n = 1
		return [l[i:i + n] for i in range(0, len(l), n)]		

	def insert_albalpha(self, a):
		Data().viewsdb_albalpha_insert(dict(a))

	def get_alphaoffset(self, chunks):		
		count = 0
		albidPlist = []
		albalphaoffsetlist = []
		for chu in chunks:
			count += 1
			for c in chu:
				albid_page = c['AlbumId'], str(count)
				albidPlist.append(albid_page)
			albalphaoffsetlist.append(str(count))
		self.insert_albalpha(dict(albalpha=albalphaoffsetlist))
		return albidPlist
			
	def get_pages(self, c):
		Data().viewsdb_albumview_update(c)

	def main(self, albv, OFC):
		chunks = self.chunks(albv, OFC)
		gaos = self.get_alphaoffset(chunks)
		pool = Pool(processes=cores)
		voodoo = pool.map(self.get_pages, gaos)
		pool.close()
		pool.join()