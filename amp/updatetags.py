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
import amp.gettags as gt
import amp.mdfivegen as mfg
from pymongo import MongoClient
client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

GT = gt.GetMP3Tags()
MD5 = mfg.MD5Gen()

class UpdateTagsDB():
	def check_func(self, x, y):
		if x != y: return False 
		else: return True

	def comp_tags(self, afile):
		new_tags = GT.get_audio_tag_info(afile)
		NewTags = MD5.gen_md5(new_tags)
		nt1 = NewTags['filename']
		nt2 = NewTags['artist']
		nt3 = NewTags['album']
		nt4 = NewTags['song']
		nt5 = NewTags['md5' ]
		fnc = self.check_func(nt1, afile['filename'])
		artc = self.check_func(nt2, afile['artist'])
		albc = self.check_func(nt3, afile['album'])
		sonc = self.check_func(nt4, afile['song'])
		md5c = self.check_func(nt5, afile['md5'])
		if fnc and artc and albc and sonc and md5c:
			pass
		else:
			db.tags.update({'_id': afile['_id']},
				{'$set', {'filename': nt1, 'artist': nt2, 'album': nt3, 'song': nt4, 'md5': nt5}})

	def update_tags_main(self, acores):
		tags = [x for x in db.tags.find({}, {'_id':1, 'filename':1, 'artist':1, 'album':1, 'song':1, 'md5':1})]
		pool = Pool(processes=acores)
		pm = pool.map(self.comp_tags, tags)
		pool.close()
		pool.join()