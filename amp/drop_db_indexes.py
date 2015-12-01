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
from pymongo import MongoClient
client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class DropDBIndexes():
	def drop_albumView_index(self): viewsdb.albumView.drop_indexes()
	
	def drop_artistView_index(self): viewsdb.artistView.drop_indexes()
	
	def drop_ampnado_stats_index(self): db.ampnado_stats.drop_indexes()

	def drop_catalogs_index(self): db.catalogs.drop_indexes()

	def drop_prog_paths_index(self): db.prog_paths.drop_indexes()

	def drop_randthumb_index(self): db.randthumb.drop_indexes()

	def drop_tags_index(self): db.tags.drop_indexes()

	def drop_user_creds_index(self): db.user_creds.drop_indexes()

	def drop_user_options_index(self): db.user_options.drop_indexes()

	def drop_video_index(self): db.video.drop_indexes()
	
	def drop_all_indexes(self):
		self.drop_albumView_index()
		self.drop_ampnado_stats_index()
		self.drop_artistView_index()
		self.drop_catalogs_index()
		self.drop_prog_paths_index()
		self.drop_randthumb_index()
		self.drop_tags_index()		
		self.drop_user_creds_index()
		self.drop_user_options_index()
		self.drop_video_index()
		logging.info('All indexes dropped')
		print('All indexes dropped')

class DropDBs():
	def rm_db_albumView(self): viewsdb.albumView.remove({})

	def rm_db_artistView(self): viewsdb.artistView.remove({})
	
	def rm_db_albalpha(self): viewsdb.albalpha.remove({})

	def rm_db_artalpha(self): viewsdb.artalpha.remove({})

	def rm_db_songView(self): viewsdb.songView.remove({})

	def rm_db_songalpha(self): viewsdb.songalpha.remove({})
		
	def rm_db_ampnado_stats(self): db.ampnado_stats.remove({})

	def rm_db_catalogs(self): db.catalogs.remove({})

	def rm_db_prog_paths(self): db.prog_paths.remove({})

	def rm_progpath(self): db.progpath.remove({})

	def rm_db_randthumb(self): db.randthumb.remove({})

	def rm_db_tags(self): db.tags.remove({})
	
	def rm_db_user_creds(self): db.user_creds.remove({})
	
	def rm_db_user_options(self): db.user_options.remove({})
		
	def rm_db_video(self): db.video.remove({})
		
	def rm_all_dbs(self):
		self.rm_db_ampnado_stats()
		self.rm_db_artistView()
		self.rm_db_catalogs()
		self.rm_db_prog_paths()
		self.rm_db_randthumb()
		self.rm_db_tags()		
		self.rm_db_user_creds()
		self.rm_db_user_options()
		self.rm_db_video()
		self.rm_db_albalpha()
		self.rm_db_artalpha()
		self.rm_db_songView()
		self.rm_db_songalpha()
		print('All Databases dropped')
		logging.info('All databases dropped')