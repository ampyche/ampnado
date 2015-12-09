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

class GetFileMeta():
	
	def size(self, x):
		return os.stat(x).st_size
		
	def dirpath(self, x):
		return os.path.dirname(x)
		
	def split_lower(self, x):
		return os.path.splitext(x)[1].lower()
		
	def uuidd(self):
		return str(uuid.uuid4().hex)

	def get_file_meta(self, fn):
		fn['filesize'] = self.size(fn['filename'])
		fn['dirpath'] = self.dirpath(fn['filename'])
		fn['filetype'] = self.split_lower(fn['filename'])
		fn['songid'] = self.uuidd()
		return fn 
		
	def _file_meta_main(self, files, acores):		
		pool = Pool(processes=acores)
		pm = pool.map(self.get_file_meta, files)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned