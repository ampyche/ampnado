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
import os, sys
from pymongo import MongoClient
from pprint import pprint

class TagsFromFilename():
	
	def __init__(self):
		client1 = MongoClient()
		db = client1.ampnadoDB
		self.db = db
		
		client2 = MongoClient()
		dba = client2.fnDB
		self.dba = dba
		
	def get_files(self):
		return [d['filename'] for d in self.db.tags.find({}, {'filename': 1, '_id':0})]
		
	def _get_sp_filenames(self):
		file_list = self.get_files()
		result = []
		for fn in file_list:
			fne = os.path.splitext(fn)
			fnn = fne[0].split('/')
			fno = len(fnn) - 1
			ao = fnn[fno]
			bs = ao.split('_-_')
			lbs = len(bs)
			if lbs == 1:
				pass
			elif lbs == 2:
				bs1 = bs[0].replace(' ', '').replace('.', ' ').replace('_', ' ')
				bs2 = bs[1].replace(' ', '').replace('.', ' ').replace('_', ' ')
				x = {'track' : '01', 'artist' : bs1, 'album' : bs1, 'song' : bs2, 'ext' : fne[1]}
			elif lbs == 3:
				bs1 = bs[1].replace(' ', '').replace('.', ' ').replace('_', ' ')
				bs2 = bs[2].replace(' ', '').replace('.', ' ').replace('_', ' ')
				x = {'track' : bs[0], 'artist' : bs1, 'album' : bs1, 'song' : bs2, 'ext' : fne[1]}
				result.append(x)
			elif lbs == 4:
				bs1 = bs[1].replace(' ', '').replace('.', ' ').replace('_', ' ')
				bs2 = bs[2].replace(' ', '').replace('.', ' ').replace('_', ' ')
				bs3 = bs[3].replace(' ', '').replace('.', ' ').replace('_', ' ')
				x = {'track' : bs[0], 'artist' : bs1, 'album' : bs2, 'song' : bs3, 'ext' : fne[1]}
				result.append(x)
			else:
				print('boooooo')
				print(fn)
		pprint(result)
		self.dba.tags.insert(result)
		return result
		
		
if __name__ == "__main__":
	TFF = TagsFromFilename()
	tff = TFF._get_sp_filenames()




