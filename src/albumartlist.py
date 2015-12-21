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
from src.data import Data

class GetAlbumArtLists:
	
	def distinct_albumartpath(self):
		return Data().tags_distinct_albumartPath()
		
	def fone_tags_albumartpath(self, x):
		return Data().fone_tags_albumartPath(x)
	
	def get_albumart_lists(self, a):
		asp = a.split('/')
		if asp[-1:][0] == 'NOTAGART':
			pass
		else:
			albinfo = self.fone_tags_albumartpath(a)
			ainfo = a, albinfo['albumid'], albinfo['album']
			return ainfo

	def get_albumart_list_main(self, acores):
		albumartPaths = self.distinct_albumartpath()
		pool = Pool(processes=acores)
		google = pool.map(self.get_albumart_lists, albumartPaths)
		cleaned = [x for x in google if x != None]
		pool.close()
		pool.join()		
		return cleaned