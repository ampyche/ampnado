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
from pprint import pprint

class RemoveOld():
	def _remove_json(self, apath):
		try: shutil.rmtree(apath['jsonPath'], ignore_errors=True)
		except OSError:
			os.mkdir(apath['jsonPath'])
			os.mkdir(apath['jsonoffsetPath'])
		logging.info('remove json complete')

	def _remove_symlinks(self, apath):
		try: shutil.rmtree(apath['musiccatPath'], ignore_errors=True)
		except OSError: os.mkdir(apath['musiccatPath'])
		logging.info('Music symlinks removed, dir created')

	def _remove_logs(self, apath):
		if os.path.isfile(apath['setupLog']): os.remove(apath['setupLog'])
		logging.info('Logs have been removed')

	def _remove_temp(self, apath):
		static_TEMP = '/'.join((apath['tempPath']))
		try: shutil.rmtree(apath['tempPath'], ignore_errors=True)
		except OSError: os.mkdir(apath['tempPath'])
		logging.info('Temp dir has been removed')

	def _make_needed_dirs(self, apath):
		if not os.path.isdir(apath['jsonPath']): os.mkdir(apath['jsonPath'])
		if not os.path.isdir(apath['jsonoffsetPath']): os.mkdir(apath['jsonoffsetPath'])
		if not os.path.isdir(apath['musiccatPath']): os.mkdir(apath['musiccatPath'])
		if not os.path.isdir(apath['tempPath']): os.mkdir(apath['tempPath'])
		if not os.path.isdir(apath['isoPath']): os.mkdir(apath['isoPath'])
		if not os.path.isdir(apath['musicPath']): os.mkdir(apath['musicPath'])
		logging.info("All needed dirs have been created")

	def _remove_all_old(self, path):
		self._remove_json(path)
		self._remove_symlinks(path)
		self._remove_logs(path)
		self._remove_temp(path)
		self._make_needed_dirs(path)
		logging.info('All old files have been removed')