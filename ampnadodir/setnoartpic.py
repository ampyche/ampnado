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
import os, base64
from multiprocessing import Pool
from pymongo import MongoClient
client = MongoClient()
db = client.ampnadoDB

class SetNoArtPic():
	def _get_b64_image(self, location):	
		with open(location, 'rb') as imagefile:
			 return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))

	def nat100(self, path):#programPath
		NAP1 = '/'.join((path, 'static', 'images', 'no_art_pic_100x100.png'))
		NAP1_size = os.stat(NAP1).st_size
		NAP1imgstr = self._get_b64_image(NAP1)
		return NAP1imgstr, NAP1_size

	def nat200(self, path):#programPath
		NAP2 = '/'.join((path, 'static', 'images', 'no_art_pic_200x200.png'))
		NAP2_size = os.stat(NAP2).st_size
		NAP2imgstr = self._get_b64_image(NAP2)
		return NAP2imgstr, NAP2_size

	def get_no_art_ids(self, nt):
		moo = db.tags.update({'_id':nt[0]}, {'$set': {'sthumbnail': nt[1], 'lthumbnail': nt[3], 'smallthumb_size': nt[2], 'largethumb_size': nt[4]}}) 

	def set_no_art_pic_main(self, acores):
		pp = db.prog_paths.find_one({})
		path = pp['programPath']
		nat100 = self.nat100(path)
		nat200 = self.nat200(path)
		ntaid = [(nta['_id'], nat100[0], nat100[1], nat200[0], nat200[1]) for nta in db.tags.find({'NoTagArt': 0}, {'_id':1})]
		pool = Pool(processes=acores)
		moogle = pool.map(self.get_no_art_ids, ntaid)
		cleaned = [x for x in moogle if x != None]
		pool.close()
		pool.join()
		return cleaned	