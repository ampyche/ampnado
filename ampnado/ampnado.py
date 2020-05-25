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
#import inputs as gp
import functions as fun
import findjpgs as fj
from pymongo import MongoClient
from pprint import pprint
from data import Data

ampDBClient = MongoClient("mongodb://db:27017/ampnadoDB")
ampDBClient.drop_database("ampnadoDB")

ampvDBClient = MongoClient("mongodb://db:27017/ampviewsDB")
ampvDBClient.drop_database("ampviewsDB")
#client.drop_database("config")

picDBClient = MongoClient("mongodb://db:27017/picdb")
picDBClient.drop_database("picdb")

db = ampDBClient.ampnadoDB

class SetUp():
	def __init__(self):
		self.setup_status = os.environ["AMP_SETUP"]
		print("SetUp HAS STARTED")
		FUN = fun.FindMedia()
		self.FUN = FUN
		FUNKY = fun.Functions()
		FUNKY.insert_user(os.environ["AMP_USERNAME"], os.environ["AMP_PASSWORD"])


	def gettime(self, at):
		return (time.time() - at)

	def main(self):
		atime = time.time()
		print(os.environ)
		#self.set_env_vars()
		self.FUN.find_music(os.environ["AMP_MEDIA_PATH"])
		
		FJ = fj.FindMissingArt()
		FJ.globstuff()
		picdics = FJ.PicDics
		Data().tags_update_artID(picdics)

		btime = time.time()
		maintime = btime - atime
		print("Main DB setup time %s" % maintime)
		
		#import functions as funct
		#from functions import AddArtistId
		fun.AddArtistId()
		#AddArtistId().add_artistids()
		ctime = time.time()
		artidtime = ctime - atime
		print("AddArtistId time %s" % artidtime)

		# from functions import AddAlbumId
		# AddAlbumId().add_albumids()
		fun.AddAlbumId()
		dtime = time.time()
		albidtime = dtime - atime
		print("AddAlbumId time %s" % albidtime)

		from artistview import ArtistView
		from artistview import ArtistChunkIt
		AV = ArtistView().main()
		ArtistChunkIt().main(AV, os.environ["AMP_OFFSET_SIZE"])
		etime = time.time()
		artistviewtime = etime - atime
		print("Artistview time %s" % artistviewtime)		

		from albumview import AlbumView
		from albumview import AlbumChunkIt
		ALBV = AlbumView().main()
		AlbumChunkIt().main(ALBV, os.environ["AMP_OFFSET_SIZE"])
		ftime = time.time()
		albviewtime = ftime - atime
		print("Albumview time %s" % albviewtime)		

		from songview import SongView
		SongView().create_songView_db(os.environ["AMP_OFFSET_SIZE"])
		gtime = time.time()
		songviewtime = gtime - atime
		print("Songview time %s" % songviewtime)
		
		#from functions import Indexes
		fun.Indexes().creat_db_indexes()
		htime = time.time()
		indextime = htime - atime
		print("Index time %s" % indextime)
		
		#from functions import DbStats
		fun.DbStats().db_stats()
		itime = time.time()
		statstime = itime - atime
		print("DBStats time is %s" % statstime)

		#from functions import RandomArtDb
		fun.RandomArtDb().create_random_art_db()
		jtime = time.time()
		ranarttime = jtime - atime
		print("RandomArtDB time is %s" % ranarttime)




#		#this is for removeuser
#		try:
#			if self.args.remove_user_name and self.args.remove_user_password:
#				h = self.FUN.gen_hash(self.args.remove_user_name, self.args.remove_user_password)
#				ruser = self.GI._remove_user(h[0], h[1])
#		except AttributeError: pass

		ptime = time.time()
		t = ptime - atime
		print("SETUP HAS BEEN COMPLETED IN %s SECONDS" % t)
	
	def setup_status_check(self):
		import glob

		# setup_status = os.environ["AMP_SETUP"]
		db_status = len(glob.glob("/data/db/*.wt"))
		pic_status = len(glob.glob("/usr/share/Ampnado/static/images/thumbnails/*.jpg"))
		
		if  db_status != 0 and pic_status != 0:
			import ampserver as app
			app.main()
		else:
			self.main()
			import ampserver as app
			app.main()

if __name__ == "__main__":
	su = SetUp()
	su.setup_status_check()