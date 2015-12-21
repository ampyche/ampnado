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
import src.gettags as gt
from pymongo import MongoClient
client = MongoClient()
db = client.ampnadoDB

GT = gt.GetMP3Tags()

class UpdateTagsDB():
	
	def _get_file_tags(self, afile):
		return GT.get_audio_tag_info(afile)

	def check(self, x, y):
		if x != y: return False
		else: return True

	def comp_tags(self, tags):
		ftags = self._get_file_tags(tags)
		c1 = self.check(ftags['filename'], tags['filename'])
		c2 = self.check(ftags['artist'], tags['artist'])
		c3 = self.check(ftags['album'], tags['album'])
		c4 = self.check(ftags['song'], tags['song'])					
		if c1 and c2 and c3 and c4:
			pass
		else:
			db.tags.update({'_id': tags['_id']}, {'$set', {'filename': ftags['filename'], 'artist': ftags['artist'], 'album': ftags['album'], 'song': ftags['song']}})
			Data().tags_update_new_tag_info(tags, ftags)

	def update_tags_main(self, acores):
		faas = Data().tags_all_filename_artist_album_song()
		tags = []
		for x in faas:
			tags.append(x)
		pool = Pool(processes=acores)
		pm = pool.map(self.comp_tags, tags)
		pool.close()
		pool.join()