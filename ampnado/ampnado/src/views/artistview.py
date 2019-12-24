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
import multiprocessing as mu
from src.data import Data
import os, pymongo
v = pymongo.version
version = v.split('.')[0]
version = int(version)

cores = mu.cpu_count()

class ArtistView:
	def __init__(self):
		self.art = Data().tags_distinct_artist()

	def create_artistView_db(self, art):
		z = {}
		z['Artist'] = art
		artistid = Data().fone_tags_artist(art)
		z['ArtistId'] = artistid['ArtistId']
		
		if version < 3:
			boo = Data().tags_aggregate_artist(art)			
			doo = boo['result'][0]['albumz']
		else:
			boo = [a['albumz'] for a in Data().tags_aggregate_artist(art)]
			doo = boo[0]
		new_alb_list = []
		for d in doo:
			albid = Data().fone_tags_album(d)
			moo = d, albid['AlbumId']
			new_alb_list.append(moo)
		z['Albums'] = new_alb_list
		Data().viewsdb_artistview_insert(z)
		return z 

	def main(self):
		pool = Pool(processes=cores)
		artv = pool.map(self.create_artistView_db, self.art)
		cleaned = [x for x in artv if x != None]
		pool.close()
		pool.join()
		return cleaned
	
class ArtistChunkIt:
	def chunks(self, l, nn):
		n = int(nn)
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
				albid_page = c['Artist'], str(count)
				artidPlist.append(albid_page)
			artalphaoffsetlist.append(str(count))
		Data().viewsdb_artalpha_insert(dict(artalpha=artalphaoffsetlist))
		return artidPlist
			
	def _get_pages(self, c):
		Data().viewsdb_artistview_update(c)

	def main(self, artv, OFC):
		chunks = self.chunks(artv, OFC)
		gaos = self._get_alphaoffset(chunks)
		pool = Pool(processes=cores)
		voodoo = pool.map(self._get_pages, gaos)
		pool.close()
		pool.join()