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
from src.data import Data
from PIL import Image
#from pymongo import MongoClient
#client = MongoClient()
#db = client.ampnadoDB

class GetVideoPoster:
	def _img_size_check_and_save(self, img, size, location):
		im = Image.open(img)
		sim = im.size
		if sim[0] > 200 and sim[1] > 200:
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(location, "JPEG")
		else:
			im.save(location, "JPEG")

	def _get_b64_image(self, location):	
		with open(location, 'rb') as imagefile:
			 return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))

	def find_video_posters(self, v):
		vname = v[0]['vid_name'].lower()
		vpRS = v[0]['filename'].rsplit('/', 1)
		posterP = vpRS[1][:-4].lower().replace('.', '_')
		PP = ''.join((vpRS[0], '/poster_', posterP, '.jpg'))
		tpath = '/'.join((v[1], 'static', 'TEMP', ''.join(('poster_', posterP, '.jpg'))))
		if os.path.exists(PP):
			v[0]['vid_orig_poster'] = PP
			vthumb = 100, 100
			self._img_size_check_and_save(PP, vthumb, tpath)
			v[0]['vid_poster_string'] = self._get_b64_image(tpath)
			
			
			#db.video.update({'filename':v[0]['filename']}, {'$set': {'vid_poster_string':v[0]['vid_poster_string'], 'vid_orig_poster': v[0]['vid_orig_poster']}})
			Data().video_update_video_posterstring_origposter(v[0])
		
		else:
			default = '/'.join((v[1], 'static', 'images', 'no_art_pic_100x100.png'))
			v[0]['vid_poster_string'] = self._get_b64_image(default)
			
			
			
			Data().video_update_noposter_string(v[0])
			#db.video.update({'filename':v[0]['filename']}, {'$set': {'vid_poster_string':v[0]['vid_poster_string']}})



	def get_video_poster_main(self, vinfo, PATH, acores):
		vid = [(v, PATH['programPath']) for v in vinfo]
		pool = Pool(processes=acores)
		booty = pool.map(self.find_video_posters, vid)
		pool.close()
		pool.join()