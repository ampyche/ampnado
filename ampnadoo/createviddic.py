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
import os, uuid
from multiprocessing import Pool
from ampnadoo.data import Data
#from pymongo import MongoClient
#client = MongoClient()
#db = client.ampnadoDB

class CreateVidDict:
	def __init__(self):
		crap = ('.2011', '.2012', '.2014', '.2015', '.720p', '.1080p', '.BluRay','.Bluray',
			'.Brrip', '.x264', '.X264', '.YIFY')
		self.crap = crap
		
	def insert(self, x):
		Data().video_insert(x)

	def uuidd(self):
		return str(uuid.uuid4().hex)

	def _create_vid_dict(self, avid):
		vid = {}
		vid['catname'] = avid[1]	
		vid['filename'] = avid[0]
		vid['filesize'] = os.path.getsize(avid[0])
		vid['dirpath'] = os.path.dirname(avid[0])
		cat_name = avid[1]
		split_fn = os.path.splitext(avid[0])
		extension = split_fn[1]
		vn = split_fn[0].rsplit('/', 1)
		vid_name1 = vn[1]
		ln = vn[0].split(cat_name)
		ln1 = ln[1].split('/', 2)
		link_addr = ln1[1]
		front = ln[0]
		middle = ln1[2]
		p1 = '/'.join(('Music', cat_name, link_addr, middle, vid_name1))
		vid['vid_playpath'] = ''.join((p1, extension))
		for c in self.crap: vid_name1.replace(c, '')
		viddy1 = vid_name1.replace('.', ' ')
		viddy = viddy1.replace('_', ' ')
		vid_name2 = viddy.split(' ')
		vid_name3 = [v.capitalize() for v in vid_name2]
		vid['vid_name'] = ' '.join(vid_name3)
		vid['vid_id'] = self.uuidd()
		self.insert(vid)
		return vid


	def add_catname(self, avlist, opt):
		new_avidlist = []
		for av in avlist:
			z = (av, opt['catname'])
			new_avidlist.append(z)
		return new_avidlist



	def create_vid_dic_main(self, avidlist, opt, acores):
		#avid = [(avid, opt['catname']) for avid in avidlist]
		avid = self.add_catname(avidlist, opt)
		pool = Pool(processes=acores)
		booty = pool.map(self._create_vid_dict, avid)
		cleaned = [x for x in booty if x != None]
		pool.close()
		pool.join()
		return cleaned	