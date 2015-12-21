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
import os, base64, glob
from PIL import Image
from multiprocessing import Pool
from src.data import Data

class GetAlbumArt:
	def _get_smallthumb(self, location, filename, size):
		im2 = Image.open(filename)
		im2.thumbnail(size, Image.ANTIALIAS)
		im2.save(location, "JPEG")

	def _get_thumb_size(self, location): return os.stat(location).st_size
		
	def _get_b64_image(self, location):	
		with open(location, 'rb') as imagefile:
			 return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))

	def _img_size_check_and_save(self, img, size, location):
		im = Image.open(img)
		sim = im.size
		if sim[0] > 200 and sim[1] > 200:
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(location, "JPEG")
		else:
			im.save(location, "JPEG")

	def create_thumbs(self, p):
		dthumb = (200, 200)
		d2thumb = (100, 100)
		loc2 = ''.join((p[1], p[0][1], '200x200.jpg'))
		loc1 = ''.join((p[1], p[0][1], '100x100.jpg'))
		im2 = self._get_smallthumb(loc1, p[0][0], d2thumb)
		x = {}
		x['albumartPath'] = p[0][0]
		x['albumid'] = p[0][1]
		x['album'] = p[0][2]
		x['smallthumb_size'] = self._get_thumb_size(loc1)
		x['smallthumb'] = self._get_b64_image(loc1)
		self._img_size_check_and_save(p[0][0], dthumb, loc2)
		x['largethumb_size'] = self._get_thumb_size(loc2)
		x['largethumb'] = self._get_b64_image(loc2)
		a = (p[0][0], x['smallthumb'], x['smallthumb_size'], x['largethumb'], x['largethumb_size'])
		Data().tags_update_sthumb_lthumb_and_sizes(a)

		
	def get_albumart_main(self, alblist, apaths, acores):
		sl10 = ''.join([apaths['tempPath'], '/'])
		alist = [(x, sl10) for x in alblist]
		pool = Pool(processes=acores)
		boogle = pool.map(self.create_thumbs, alist)
		cleaned = [x for x in boogle if x != None]
		pool.close()
		pool.join()
		sl11 = ''.join([apaths['tempPath'], '/', '*.jpg'])
		rmlist = glob.glob(sl11)
		for r in rmlist: os.remove(r)
		return cleaned	