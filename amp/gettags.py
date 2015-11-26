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
import logging
from multiprocessing import Pool
try: from mutagen import File
except ImportError: from mutagenx import File

class GetMP3Tags():

	def get_audio_tag_info(self, fn):
		audio = File(fn['filename'])
		try: fn['track'] = audio['TRCK'].text[0]
		except KeyError: fn['track'] = '50'
		
		try: fn['artist'] = audio["TPE1"].text[0]
		except KeyError: 
			fn['artist'] = 'Fuck Artist'
			print(''.join(("KeyError: No TPE1 tag... ", fn['filename'])))
			logging.info(''.join(("KeyError: No TPE1 tag... ", fn['filename'])))
			
		try: fn['album'] = audio["TALB"].text[0]
		except KeyError: 
			fn['album'] = 'Fuck Album'
			print(''.join(("KeyError No TALB tag ... ", fn['filename'])))
			logging.info(''.join(("KeyError No TALB tag ... ", fn['filename'])))
			
		try: fn['song'] = audio['TIT2'].text[0]
		except KeyError: 
			fn['song'] = 'Fuck Song'
			print(''.join(("KeyError: No TIT2 tag... ", fn['filename'])))
			logging.info(''.join(("KeyError: No TIT2 tag... ", fn['filename'])))
		return fn

	def _get_audio_tag_info_main(self, files, acores):
		pool = Pool(processes=acores)
		pm = pool.map(self.get_audio_tag_info, files)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned