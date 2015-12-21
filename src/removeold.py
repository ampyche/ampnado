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
import os, shutil, logging

SYMLINKS = """REMOVEOLD: Music symlinks removed, dir created"""
TEMPDIR = """REMOVEOLD: Temp dir has been removed"""
MKDIRS = """REMOVEOLD: All needed dirs have been created"""
ALLRM = """REMOVEOLD: All old files have been removed"""

class RemoveOld:
	
	def remove_symlinks(self, apath):
		try: shutil.rmtree(apath['musiccatPath'], ignore_errors=True)
		except OSError: os.mkdir(apath['musiccatPath'])
		logging.info(SYMLINKS)
		print(SYMLINKS)

	def remove_temp(self, apath):
		static_TEMP = '/'.join((apath['tempPath']))
		try: shutil.rmtree(apath['tempPath'], ignore_errors=True)
		except OSError: os.mkdir(apath['tempPath'])
		logging.info(TEMPDIR)
		print(TEMPDIR)

	def make_needed_dirs(self, apath):
		if not os.path.isdir(apath['musiccatPath']): os.mkdir(apath['musiccatPath'])
		if not os.path.isdir(apath['tempPath']): os.mkdir(apath['tempPath'])
		if not os.path.isdir(apath['isoPath']): os.mkdir(apath['isoPath'])
		if not os.path.isdir(apath['musicPath']): os.mkdir(apath['musicPath'])
		logging.info(MKDIRS)
		print(MKDIRS)

	def remove_all_old(self, path):
		self.remove_symlinks(path)
		self.remove_temp(path)
		self.make_needed_dirs(path)
		logging.info(ALLRM)
		print(ALLRM)	