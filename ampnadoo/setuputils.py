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
import ampnadoo.artistview as artv
import ampnadoo.albumview as albvv
import ampnadoo.songview as songv




from ampnadoo.httpmusicpath import HttpMusicPath
from ampnadoo.filemeta import GetFileMeta
from ampnadoo.gettags import GetMP3Tags
from ampnadoo.gettags import GetOGGTags
from ampnadoo.albumartscan import AlbumArtScan



import ampnadoo.albumartlist as aal







import ampnadoo.getalbumart as gaa
import ampnadoo.setnoartpic as snap
import ampnadoo.createviddic as cvd
import ampnadoo.videoposter as vp



from ampnadoo.functions import Functions
from ampnadoo.functions import FindMedia
from ampnadoo.functions import AddArtistId
from ampnadoo.functions import AddAlbumId



import logging, pymongo
client = pymongo.MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class SetupUtils:

	def run_setup(self, aopt, apath, a_time, CORES):
		logging.info('Setup Started')
		
		PATHS = apath
		OPT = aopt
		
		logging.info('Finding music started')
		print("Constants Setup Complete\nSetup Started\nFinding Music")
		
		
		FM = FindMedia().find_music_video(PATHS['musiccatPath'])
		
		print('this is  _find_music_video    time')
		print(Functions().gettime(a_time))
		
		if len(FM[0]) >= 1: filesfound_mp3 = True
		else: filesfound_mp3 = False
		if len(FM[1]) >= 1: filesfound_ogg = True
		else: filesfound_ogg = False
		if len(FM[2]) >= 1: filesfound_vid = True
		else: filesfound_vid = False

		print("Finding music complete")
		logging.info('Finding music complete')
		logging.info('Getting tag info started')
		print('Getting tag info started')
		
		if filesfound_mp3: 
			print('filesfound complete')
			files = []
			for f in FM[0]:
				f['catname'] = OPT['catname']
				f['programPath'] = PATHS['programPath']
				files.append(f)

			print('newmeta started')

			FILEMETA = GetFileMeta().file_meta_main(files, CORES)
			
			print('newmeta complete')
			print('newtags started')

			MP3TAGS = GetMP3Tags().get_audio_tag_info_main(FILEMETA, CORES)
			
			print('newtags complete')
			print('insert media started')
			
			ALBUMARTSCAN = AlbumArtScan().albumart_search_main(MP3TAGS, CORES)
			
			print('insert media complete')
		else: pass
		
		print('this is _get_tags and Insert tags     time')
		print(Functions().gettime(a_time))
		logging.info('Getting tag info complete')


		if filesfound_ogg:
			ofiles = []
			for f in FM[1]:
				f['catname'] = OPT['catname']
				f['programPath'] = PATHS['programPath']
				ofiles.append(f)
			OGGFILEMETA = GetFileMeta().file_meta_main(ofiles, CORES)
			OGGTAGS = GetOGGTags().get_ogg_tag_info_main(OGGFILEMETA, CORES)
			OGGALBUMARTSCAN = AlbumArtScan().albumart_search_main(OGGTAGS, CORES)
		else: pass

		HTTPMP = HttpMusicPath().main(PATHS, CORES)

		print('this is   add_http_music_path_to_db     time')
		print(Functions().gettime(a_time))

		addartistid = AddArtistId().add_artistids()

		print('this is   addartistid     time')
		print(Functions().gettime(a_time))

		addalbumid = AddAlbumId().add_albumids()
		
		print('this is   addalbumid     time')
		print(Functions().gettime(a_time))
		
		print('start ALBUMARTLIST')
		
		
		
		
		
		
		
		
		
		Aal = aal.GetAlbumArtLists()
		ALBUMARTLIST = Aal.get_albumart_list_main(CORES)
		
		
		
		
		
		
		
		
		
		
		
		
		print('end ALBUMARTLIST')

		print('start GETALBUMART')
		Gaa = gaa.GetAlbumArt()
		GETALBUMART = Gaa.get_albumart_main(ALBUMARTLIST, PATHS, CORES)
		print('end GETALBUMART')

		print('start noartpic')
		Snap = snap.SetNoArtPic()
		SETNOARTPIC = Snap.set_no_art_pic_main(CORES)
		print('end noartpic')


		print('this is   get_albumart     time')
		print(Functions().gettime(a_time))
		logging.info('Finding videos has started')
		print('Finding Video')
		print('VIDEO SHIT IS FUCKED UP FIX IT')
		if filesfound_vid:
			
			Cvd = cvd.CreateVidDict()
			CREATEVIDDIC = Cvd.create_vid_dic_main(FM[2], OPT, CORES)

			Vp = vp.GetVideoPoster()
			GETVIDEOPOSTER = Vp.get_video_poster_main(CREATEVIDDIC, PATHS, CORES)
			
		print('this is   find and insert vid info     time')
		print(Functions().gettime(a_time))
		logging.info('Finding video is complete')
		logging.info('Creating artistview has started')
		print('Creating artistView')
		
		ArtV = artv.ArtistView()
		av = ArtV.main(CORES)
		
		ArtC = artv.ArtistChunkIt()		
		ArtC.main(av, OPT['offset'], CORES)

		print('this is   ArtistView     time')
		print(Functions().gettime(a_time))
		logging.info('Creating albumview has completed')
		print('Creating albumview')
		
		AlbV = albvv.AlbumView()		
		albv = AlbV.main(CORES)
		albv2 = albvv.AlbumChunkIt()
		chunk = albv2.main(albv, OPT['offset'], CORES)

		print('this is   AlbumView     time')
		print(Functions().gettime(a_time))
		logging.info('Creating songview has completed')
		print('Creating songview')
		
		SongV = songv.SongView()
		SongV.create_songView_db(OPT['offset'])
		
		print('this is   SongView     time')
		print(Functions().gettime(a_time))
		logging.info('Creating indexes has started')
		
		creat_indexes = Functions()._creat_db_indexes()
		
		print('this is   creat_indexes     time')
		print(Functions().gettime(a_time))
		logging.info('Creating indexes has completed')
		logging.info('Creating random art has started')
		
		cradb = Functions()._create_random_art_db()
		
		print('this is   cradb     time')
		print(Functions().gettime(a_time))
		logging.info('Creating random art has completed')
		
		stats = Functions().db_stats()
		
		print('this is   db_stats     time')
		print(Functions().gettime(a_time))