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
import hashlib
from multiprocessing import Pool

class MD5Gen():
	
	def gen_md5(self, afile):
		with open(afile['filename'], 'rb') as mp: 
			afile['md5'] = str(hashlib.md5(mp.read()).hexdigest())
		return afile

	def _gen_md5_main(self, alist, acores):
		pool = Pool(processes=acores)
		pm = pool.map(self.gen_md5, alist)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned