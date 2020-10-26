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
from data import Data

class SongView:
	def __init__(self):
		self.tags = Data().tags_all_song_songid_artist()
		self.songalphaoffsetlist = []
		self.songviewlist = []

	def rm_dups_songalpha(self, x): return list(set(x))
	
	def insert_songalpha(self, z):
		Data().viewsdb_songalpha_insert(dict(songalpha=z))
	
	def insert_songview(self, w):
		Data().viewsdb_songview_insert(w)
		
	def create_songView_db(self, OFC):
		count = 0
		page = 1
		for s in self.tags:
			count += 1
			if count == int(OFC):
				page += 1
				count = 0
			self.songalphaoffsetlist.append(page)
			x = {}
			x['Page'] = page
			x['Song'] = s['Song']
			x['SongId'] = s['SongId']
			x['Artist'] = s['Artist']
			self.songviewlist.append(x)
		songalphaoffsetlist1 = self.rm_dups_songalpha(self.songalphaoffsetlist)
		self.insert_songalpha(songalphaoffsetlist1)
		self.insert_songview(self.songviewlist)
		return self.songviewlist