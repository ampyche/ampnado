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
import os
import bson.son
from multiprocessing import Pool
from ampnadoo.data import Data
try: from mutagen import File
except ImportError: from mutagenx import File

class AlbumArtScan:
	
	def insert(self, a):
		Data().tags_insert(a)

	def _albumart_search(self, x):
		ppath = '/'.join((os.path.dirname(x['filename']), "folder.jpg"))
		if os.path.isfile(ppath):
			x['albumartPath'] = ppath
			x['NoTagArt'] = 1
		else:
			try:
				audio = File(x['filename'])
				artwork = audio.tags[u'APIC:'].data
				with open(ppath, 'wb') as img: img.write(artwork)
			except (KeyError, TypeError, AttributeError):
				x['NoTagArt'] = 0
				x['albumartPath'] = '/'.join((os.path.dirname(x['filename']), "NOTAGART"))
			else:
				if not os.path.isfile(ppath):
					x['NoTagArt'] = 0
					x['albumartPath'] = '/'.join((os.path.dirname(x['filename']), "NOTAGART"))
		self.insert(dict(x))		
		return x

	def albumart_search_main(self, afile, acores):
		pool = Pool(processes=acores)
		pm = pool.map(self._albumart_search, afile)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned