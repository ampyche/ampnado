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
from ampnadoo.data import Data

class HttpMusicPath:
		
	def add_http_music_path_to_db(self, t):
		fn2 = ''.join((t[2], t[0].split(t[1])[1]))
		Data().tags_update_httpmusicpath(t[0], fn2)

	def main(self, a_path, acores):
		alltags = Data().tags_all()
		p = []
		for n in alltags:
			foo = (n['filename'], a_path['musiccatPath'], a_path['httpmusicPath']) 
			p.append(foo)
		pool = Pool(processes=acores)
		yahoo = pool.map(self.add_http_music_path_to_db, p)
		pool.close()
		pool.join()