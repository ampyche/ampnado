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
import os, time, argparse
import src.ips.inputs as gp
import src.functions as fun
import src.findjpgs as fj
from pymongo import MongoClient
from pprint import pprint
from src.data import Data

client = MongoClient()
client.drop_database("ampnadoDB")
client.drop_database("ampviewsDB")
#client.drop_database("config")
client.drop_database("picdb")

db = client.ampnadoDB

class SetUp():
	def __init__(self):
		print("SetUp HAS STARTED")
		parser = argparse.ArgumentParser()
		parser.add_argument('-pi',
					action='store_true',
                    default=False,
                    dest='boolean_pi',
                    help='Set a switch to true')
		results = parser.parse_args()
		print(results.boolean_pi)
		if results.boolean_pi :
			print("USING PI CONFIGURATION")
			CONFIG_PATH = "./config/ampnado_pi.config"
		else:
			print("USING REGULAR CONFIGURATION")
			CONFIG_PATH = "./config/ampnado.config"
		config = None
		self.config = config
		FUN = fun.FindMedia()
		GI = gp.GetInputs()
		if os.path.isfile(CONFIG_PATH):
			self.config = GI.read_config(CONFIG_PATH)
			GI.sanity_checks(self.config)
		self.FUN = FUN

	def gettime(self, at): return (time.time() - at)

	def set_env_vars(self):
		os.environ['AMP_HTTP_THUMBNAIL_DIR_PATH'] = self.config["http_thumbnail_dir_path"]
		os.environ['AMP_PROGRAM_PATH'] = self.config["program_path"]
		os.environ["AMP_THUMBNAIL_DIR_PATH"] = self.config['thumbnail_dir_path']
		os.environ["AMP_NO_ART_PIC_PATH"] = self.config["no_art_pic_path"]
		os.environ["AMP_MEDIA_PATH"] = self.config["media_path"]
		os.environ["AMP_OFFSET_SIZE"] = self.config["offset_size"]
		os.environ["AMP_SERVER_PORT"] = self.config["server_port"]

	def main(self):
		atime = time.time()
		self.set_env_vars()
		self.FUN.find_music(self.config["media_path"])
		
		FJ = fj.FindMissingArt(self.config, self.config["media_path"])
		FJ.globstuff()
		picdics = FJ.PicDics
		Data().tags_update_artID(picdics)

		btime = time.time()
		maintime = btime - atime
		print("Main DB setup time %s" % maintime)
		
		from src.functions import AddArtistId
		AddArtistId().add_artistids()
		ctime = time.time()
		artidtime = ctime - atime
		print("AddArtistId time %s" % artidtime)

		from src.functions import AddAlbumId
		AddAlbumId().add_albumids()
		dtime = time.time()
		albidtime = dtime - atime
		print("AddAlbumId time %s" % albidtime)

		from src.views.artistview import ArtistView
		from src.views.artistview import ArtistChunkIt
		AV = ArtistView().main()
		ArtistChunkIt().main(AV, self.config['offset_size'])
		etime = time.time()
		artistviewtime = etime - atime
		print("Artistview time %s" % artistviewtime)		

		from src.views.albumview import AlbumView
		from src.views.albumview import AlbumChunkIt
		ALBV = AlbumView().main()
		AlbumChunkIt().main(ALBV, self.config['offset_size'])
		ftime = time.time()
		albviewtime = ftime - atime
		print("Albumview time %s" % albviewtime)		

		from src.views.songview import SongView
		SongView().create_songView_db(self.config['offset_size'])
		gtime = time.time()
		songviewtime = gtime - atime
		print("Songview time %s" % songviewtime)
		
		from src.functions import Indexes
		Indexes().creat_db_indexes()
		htime = time.time()
		indextime = htime - atime
		print("Index time %s" % indextime)
		
		from src.functions import DbStats
		DbStats().db_stats()
		itime = time.time()
		statstime = itime - atime
		print("DBStats time is %s" % statstime)

		from src.functions import RandomArtDb
		RandomArtDb().create_random_art_db()
		jtime = time.time()
		ranarttime = jtime - atime
		print("RandomArtDB time is %s" % ranarttime)

		try:
			if self.args.add_user_name and self.args.add_user_password:
				h = self.FUN.gen_hash(self.args.add_user_name, self.args.add_user_password)
				self.GI.insert_user(h[0], h[1], h[2], self.args.add_user_password)
		except AttributeError: pass


#		#this is for removeuser
#		try:
#			if self.args.remove_user_name and self.args.remove_user_password:
#				h = self.FUN.gen_hash(self.args.remove_user_name, self.args.remove_user_password)
#				ruser = self.GI._remove_user(h[0], h[1])
#		except AttributeError: pass

		ptime = time.time()
		t = ptime - atime
		print("SETUP HAS BEEN COMPLETED IN %s SECONDS" % t)

if __name__ == "__main__":
	su = SetUp()
	su.main()
	import ampserver as app
	app.main()
