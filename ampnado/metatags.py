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
import uuid
import mutagen
try:
	from mutagen import File
except ImportError:
	from mutagenx import File
try:
	from mutagen.oggvorbis import OggVorbis
except ImportError:
	from mutagenx.oggvorbis import OggVorbis

class FileMeta:
	SongId = None
	DirPath = None
	Size = None
	
	def __init__(self, fn):
		# type(self).SongId = str(uuid.uuid4().hex)
		# type(self).DirPath = os.path.dirname(fn)
		# type(self).Size = os.path.getsize(fn)

		self.SongId = str(uuid.uuid4().hex)
		self.DirPath = os.path.dirname(fn)
		self.Size = os.path.getsize(fn)

class MP3Tags:
	Track = None
	Artist = None
	Album = None
	Song = None
	
	def __init__(self, fn):
		self.fn = fn

		try:
			self.audio = File(self.fn)
		except KeyError:
			print(self.fn)
			pass

		try:
			# type(self).Track = self.audio['TRCK'].text[0]
			self.Track = self.audio['TRCK'].text[0]
		except KeyError:
			# type(self).Track = '50'
			self.Track = '50'
	
		try:
			# type(self).Artist = self.audio["TPE1"].text[0]
			self.Artist = self.audio["TPE1"].text[0]
		except KeyError: 
			# type(self).Artist = 'Fuck Artist'
			self.Artist = 'Fuck Artist'
			print(''.join(("KeyError: No TPE1 tag... ", self.fn)))
	
		try:
			# type(self).Album = self.audio["TALB"].text[0]
			self.Album = self.audio["TALB"].text[0]
		except KeyError: 
			# type(self).Album = 'Fuck Album'
			self.Album = 'Fuck Album'
			print(''.join(("KeyError No TALB tag ... ", self.fn)))
			
		try:
			# type(self).Song = self.audio['TIT2'].text[0]
			self.Song = self.audio['TIT2'].text[0]
		except KeyError: 
			# type(self).Song = 'Fuck Song'
			self.Song = 'Fuck Song'
			print(''.join(("KeyError: No TIT2 tag... ", self.fn)))