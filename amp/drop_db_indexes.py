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

class DropDBIndexes():
	def __init__(self):
		client = MongoClient()
		db = client.ampnadoDB
		self.db = db 
		
	def drop_albumView_index(self): self.db.albumView.drop_indexes()
		
	def drop_ampnado_stats_index(self): self.db.ampnado_stats.drop_indexes()

	def drop_artistView_index(self): self.db.artistView.drop_indexes()
		
	def drop_catalogs_index(self): self.db.catalogs.drop_indexes()

	def drop_prog_paths_index(self): self.db.prog_paths.drop_indexes()

	def drop_randthumb_index(self): self.db.randthumb.drop_indexes()

	def drop_tags_index(self): self.db.tags.drop_indexes()

	def drop_tempTags_index(self): self.db.tempTags.drop_indexes()

	def drop_tempVideo_index(self): self.db.tempVideo.drop_indexes()

	def drop_tempalbumView_index(self): self.db.tempalbumView.drop_indexes()

	def drop_tempartistView_index(self): self.db.tempartistView.drop_indexes()

	def drop_user_creds_index(self): self.db.user_creds.drop_indexes()

	def drop_user_options_index(self): self.db.user_options.drop_indexes()

	def drop_video_index(self): self.db.video.drop_indexes()

	def drop_all_indexes(self):
		self.drop_albumView_index()
		self.drop_ampnado_stats_index()
		self.drop_artistView_index()
		self.drop_catalogs_index()
		self.drop_prog_paths_index()
		self.drop_randthumb_index()
		self.drop_tags_index()
		self.drop_tempTags_index()
		self.drop_tempVideo_index()
		self.drop_tempalbumView_index()
		self.drop_tempartistView_index()
		self.drop_user_creds_index()
		self.drop_user_options_index()
		self.drop_video_index()
		logging.info('All indexes dropped')
		print('All indexes dropped')

class DropDBs():
	def __init__(self):
		client = MongoClient()
		db = client.ampnadoDB
		self.db = db 

	def rm_db_albumView(self): self.db.albumView.remove({})
		
	def rm_db_ampnado_stats(self): self.db.ampnado_stats.remove({})
		
	def rm_db_artistView(self): self.db.artistView.remove({})
		
	def rm_db_catalogs(self): self.db.catalogs.remove({})
		
	def rm_db_prog_paths(self): self.db.prog_paths.remove({})
		
	def rm_db_randthumb(self): self.db.randthumb.remove({})
		
	def rm_db_tags(self): self.db.tags.remove({})
		
	def rm_db_tempTags(self): self.db.tempTags.remove({})
		
	def rm_db_tempVideo(self): self.db.tempVideo.remove({})
		
	def rm_db_tempalbumView(self): self.db.tempalbumView.remove({})
		
	def rm_db_tempartistView(self): self.db.tempartistView.remove({})
		
	def rm_db_user_creds(self): self.db.user_creds.remove({})
		
	def rm_db_user_options(self): self.db.user_options.remove({})
		
	def rm_db_video(self): self.db.video.remove({})

	def rm_all_dbs(self):
		self.rm_db_ampnado_stats()
		self.rm_db_artistView()
		self.rm_db_catalogs()
		self.rm_db_prog_paths()
		self.rm_db_randthumb()
		self.rm_db_tags()
		self.rm_db_tempTags()
		self.rm_db_tempVideo()
		self.rm_db_tempalbumView()
		self.rm_db_tempartistView()
		self.rm_db_user_creds()
		self.rm_db_user_options()
		self.rm_db_video()
		logging.info('All databases dropped')
		print('All Databases dropped')