#!/usr/bin/python3
import unittest, pymongo
import unittest.mock as mock
import ampnadoo.data
import tests.data_setuputils




class TestDataTestCase(unittest.TestCase):
	def setUp(self):
		#clean out the db
				
		self.Data = ampnadoo.data.Data()
		self.db = pymongo.MongoClient().ampnadoDB
		self.viewsdb = pymongo.MongoClient().ampviewsDB
		self.db.user_creds.drop()
		self.db.ampnado_stats.drop()
		self.db.options.drop()
		self.db.prog_paths.drop()
		self.db.progpath.drop()
		self.db.randthumb.drop()
		self.db.video.drop()
		self.db.tags.drop()
		self.viewsdb.albalpha.drop()
		self.viewsdb.albumView.drop()
		self.viewsdb.artalpha.drop()
		self.viewsdb.artistView.drop()
		self.viewsdb.songView.drop()
		self.viewsdb.songalpha.drop()


		
		self.user_creds_uname = "charlie"
		self.prog_path_httpmusicPath = "http://192.168.1.115/Music"
		self.prog_path_setupLog = "/usr/share/ampnado/logs/setup.log"
		self.prog_path_musiccatPath = "/usr/share/ampnado/static/MUSIC"
		self.prog_path_musicPath = "/usr/share/ampnado/static/TEMP/MUSIC"
		self.prog_path_programPath = "/usr/share/ampnado"
		self.prog_path_tempPath = "/usr/share/ampnado/static/TEMP"
		self.prog_path_httppath = "http://192.168.1.115"
		self.prog_path_isoPath = "/usr/share/ampnado/static/TEMP/ISO"
		self.user_creds_pword = tests.data_setuputils.ds_user_creds_pword()
		self.user_creds_userid = tests.data_setuputils.ds_user_creds_userid()
		self.pp = tests.data_setuputils.ds_pp()
		self.tags_all = tests.data_setuputils.ds_tags_all()
		


	def tearDown(self):
		self.rmucdb = self.db.user_creds.drop()
		self.rmtagsdb = self.db.tags.drop()
		
		nonelist = [self.rmucdb, self.rmtagsdb, self.user_creds_pword, self.user_creds_uname, 
			self.user_creds_userid, self.prog_path_httpmusicPath, self.prog_path_setupLog, 
			self.prog_path_musiccatPath, self.prog_path_musicPath, self.prog_path_programPath, 
			self.prog_path_tempPath, self.prog_path_httppath, self.prog_path_isoPath,
			self.pp, self.tags_all]
		for x in nonelist:
			x = None
	
	
	
	
	
		
	def test_usercreds_insert_user_pword(self):
		"""Test insertion of username and password into the database."""
		
		self.Data.usercreds_insert_user_pword(self.user_creds_uname, self.user_creds_pword, self.user_creds_userid)
		unpw = self.db.user_creds.find_one({}, {'username':1, 'password':1, 'user_id':1, '_id':0})
		self.assertEqual(unpw['username'], self.user_creds_uname)
		self.assertEqual(unpw['password'], self.user_creds_pword)
		self.assertEqual(unpw['user_id'], self.user_creds_userid)

	def test_usercreds_remove_user_pword(self):
		"""Test the removal of username and password from the database"""
		
		unpwrm = self.Data.usercreds_insert_user_pword(self.user_creds_uname, self.user_creds_pword, self.user_creds_userid)
		unpwrm1 = self.db.user_creds.find_one({})
		unpwrm2 = self.Data.usercreds_remove_user_pword(unpwrm1)
		unpwrm3 = self.db.user_creds.find_one({})
		self.assertEqual(unpwrm3, None)
		
	def test_fone_usercreds_user_pword(self):
		"""Test the retrieval of a single username and password"""
		
		self.Data.usercreds_insert_user_pword(self.user_creds_uname, self.user_creds_pword, self.user_creds_userid)
		foo = self.Data.fone_usercreds_user_pword(self.user_creds_uname, self.user_creds_pword)
		self.assertEqual(foo['username'], self.user_creds_uname)
		self.assertEqual(foo['password'], self.user_creds_pword)
		self.assertEqual(foo['user_id'], self.user_creds_userid)

	def test_fone_prog_paths(self):
		"""Test everthing except the ObjectId which will be unique with each setup
			and tear down.
		"""
		
		self.db.prog_paths.insert_one(self.pp)
		moo = self.Data.fone_prog_paths()
		self.assertEqual(moo['httpmusicPath'], self.prog_path_httpmusicPath)
		self.assertEqual(moo['setupLog'], self.prog_path_setupLog)
		self.assertEqual(moo['musiccatPath'], self.prog_path_musiccatPath)
		self.assertEqual(moo['musicPath'], self.prog_path_musicPath)
		self.assertEqual(moo['programPath'], self.prog_path_programPath)
		self.assertEqual(moo['tempPath'], self.prog_path_tempPath)
		self.assertEqual(moo['httppath'], self.prog_path_httppath)
		self.assertEqual(moo['isoPath'], self.prog_path_isoPath)
		
	def test_tags_insert(self):
		"""Test the insertion of data into the tags db"""
		
		[self.Data.tags_insert(s) for s in self.tags_all]
		t1 = self.db.tags.find_one({'songid': 'c2c96e01a93945f2a440b59db68013f3'}, {'_id':0})
		t2 = tests.data_setuputils.ds_tags_all_results()
		t2 = t2[0]
		self.assertEqual(t1['NoTagArt'], t2['NoTagArt'])
		self.assertEqual(t1['album'], t2['album'])
		self.assertEqual(t1['albumartPath'], t2['albumartPath'])
		self.assertEqual(t1['albumid'], t2['albumid'])
		self.assertEqual(t1['artist'], t2['artist'])
		self.assertEqual(t1['artistid'], t2['artistid'])
		self.assertEqual(t1['catname'], t2['catname'])
		self.assertEqual(t1['dirpath'], t2['dirpath'])
		self.assertEqual(t1['filename'], t2['filename'])
		self.assertEqual(t1['filesize'], t2['filesize'])
		self.assertEqual(t1['filetype'], t2['filetype'])
		self.assertEqual(t1['httpmusicpath'], t2['httpmusicpath'])
		self.assertEqual(t1['largethumb_size'], t2['largethumb_size'])
		self.assertEqual(t1['lthumbnail'], t2['lthumbnail'])
		self.assertEqual(t1['track'], t2['track'])

	def test_tags_distinct_albumartPath(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		foobar = self.Data.tags_distinct_albumartPath()
		foobar2 = tests.data_setuputils.ds_tags_distinct_albumartPath_result()
		self.assertEqual(foobar, foobar2)
	
	def test_tags_distinct_albumid(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		boo = self.Data.tags_distinct_albumid()
		hoo = tests.data_setuputils.ds_tags_distinct_albumid()
		self.assertEqual(boo, hoo)

	def test_tags_distinct_artist(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		moo = self.Data.tags_distinct_artist()
		moo2 = tests.data_setuputils.ds_tags_distinct_artist()
		self.assertEqual(moo, moo2)

	def test_tags_distinct_album(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		ttda = self.Data.tags_distinct_album()
		ttda2 = tests.data_setuputils.ds_tags_distinct_album()
		self.assertEqual(ttda, ttda2)

	def test_tags_distinct_song(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		tds = self.Data.tags_distinct_song()
		tds2 = tests.data_setuputils.ds_tags_distinct_song()
		self.assertEqual(tds, tds2)

	def test_tags_all_tags(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		songs = [s for s in self.Data.tags_all()]
		songs2 = tests.data_setuputils.ds_tags_all_tags()
		self.assertEqual(songs[0]['filename'], songs2[0]['filename'])
		self.assertEqual(songs[0]["NoTagArt"], songs2[0]["NoTagArt"])
		self.assertEqual(songs[0]["song"], songs2[0]["song"])
		self.assertEqual(songs[0]["dirpath"], songs2[0]["dirpath"])
		self.assertEqual(songs[0]["songid"], songs2[0]["songid"])
		self.assertEqual(songs[0]["track"], songs2[0]["track"])
		self.assertEqual(songs[0]["filename"], songs2[0]["filename"])
		self.assertEqual(songs[0]["programPath"], songs2[0]["programPath"])
		self.assertEqual(songs[0]["artist"], songs2[0]["artist"])
		self.assertEqual(songs[0]["catname"], songs2[0]["catname"])
		self.assertEqual(songs[0]["filesize"], songs2[0]["filesize"])
		self.assertEqual(songs[0]["filetype"], songs2[0]["filetype"])
		self.assertEqual(songs[0]["album"], songs2[0]["album"])
		self.assertEqual(songs[0]["albumartPath"], songs2[0]["albumartPath"])
		self.assertEqual(songs[0]["httpmusicpath"], songs2[0]["httpmusicpath"])
		self.assertEqual(songs[0]["artistid"], songs2[0]["artistid"])
		self.assertEqual(songs[0]["albumid"], songs2[0]["albumid"])
		self.assertEqual(songs[0]["sthumbnail"], songs2[0]["sthumbnail"])
		self.assertEqual(songs[0]["lthumbnail"], songs2[0]["lthumbnail"])
		self.assertEqual(songs[0][   "largethumb_size"], songs2[0]["largethumb_size"])
		self.assertEqual(songs[0]["smallthumb_size"], songs2[0]["smallthumb_size"])

	def test_tags_all_id(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		allid = [s for s in self.Data.tags_all_id()]
		self.assertEqual(len(allid), 5)

	def test_tags_all_lthumb_size(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		thumb = [s for s in self.Data.tags_all_lthumb_size()]
		thumb2 = tests.data_setuputils.ds_tags_all_lthumb_size()
		self.assertEqual(thumb, thumb2)

	def test_tags_all_sthumb_size(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		th = [s for s in self.Data.tags_all_sthumb_size()]
		th2 = tests.data_setuputils.ds_tags_all_sthumb_size()
		self.assertEqual(th, th2)

	def test_tags_all_filesize(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		taf = [s for s in self.Data.tags_all_filesize()]
		taf2 = tests.data_setuputils.ds_tags_all_filesize()
		self.assertEqual(taf, taf2)

	def test_tags_all_filetype_mp3(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		tafm = self.Data.tags_all_filetype_mp3()
		self.assertEqual(tafm, 5)

	def test_tags_all_filetype_ogg(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		tafo = self.Data.tags_all_filetype_ogg()
		self.assertEqual(tafo, 0)

	def test_tags_all_song(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		song = [s for s in self.Data.tags_all_song("The Angel Song")]
		song1 = tests.data_setuputils.ds_tags_all_song()
		self.assertEqual(song, song1)

	def test_tags_all_notagart(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		nta = [s for s in self.Data.tags_all_notagart()]
		self.assertNotEqual(len(nta), 1)

	def test_tags_all_song_songid_artist(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		tassa = [s for s in self.Data.tags_all_song_songid_artist()]
		tassa2 = tests.data_setuputils.ds_tags_all_song_songid_artist()
		self.assertEqual(tassa, tassa2)



	def test_tags_all_filename_artist_album_song(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		tafaas = [(s['filename'], s['artist'], s['album'], s['song']) for s in self.Data.tags_all_filename_artist_album_song()]
		tafaas2 = tests.data_setuputils.ds_tags_all_filename_artist_album_song()
		self.assertEqual(tafaas, tafaas2)

	def test_fone_tags_albumid(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		fta = self.Data.fone_tags_albumid('c1dd0a3134e344a6b23493a55f83856f')
		fta2 = tests.data_setuputils.ds_fone_tags_albumid()
		self.assertEqual(fta, fta2)		

	def test_fone_tags_artist(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		artist = self.Data.fone_tags_artist("Humble Pie")
		artist2 = tests.data_setuputils.ds_fone_tags_artist()
		self.assertEqual(artist, artist2)

	def test_fone_tags_album(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		alb = self.Data.fone_tags_album("Groove Coverage")
		alb2 = tests.data_setuputils.ds_fone_tags_album()
		self.assertEqual(alb, alb2)

	def test_tags_aggregate_artist(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		art_agg = [s for s in self.Data.tags_aggregate_artist("Humble Pie")]
		art_agg2 = tests.data_setuputils.ds_tags_aggregate_artist()
		self.assertEqual(art_agg, art_agg2)


	def test_tags_aggregate_albumid(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		alb_agg = [s for s in self.Data.tags_aggregate_albumid("c1dd0a3134e344a6b23493a55f83856f")]
		alb_agg2 = tests.data_setuputils.ds_tags_aggregate_albumid()
		self.assertEqual(alb_agg, alb_agg2)


	def test_tags_aggregate_filesize(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		fs_agg = self.Data.tags_aggregate_filesize()
		fs_agg2 = tests.data_setuputils.ds_tags_aggregate_filesize()
		self.assertEqual(fs_agg, fs_agg2)


	def test_tags_update_artistid(self):
		[self.Data.tags_insert(s) for s in self.tags_all]
		#clear artistid out of db
		self.db.tags.update_many({}, {'$set': {'artistid': ''}})
		baseline = [s for s in self.db.tags.find({}, {'artist':1, 'artistid':1, '_id':0})]
		artlist = [s for s in self.db.tags.find({}, {'artist':1, '_id':0})]
		cc = [{'artist': a['artist'], 'artistid': '123456789'} for a in artlist]
		self.Data.tags_update_artistid(cc)
		result = [s for s in self.db.tags.find({}, {'artist':1, 'artistid':1, '_id':0})]
		self.assertNotEqual(baseline, result)











		

	def suite(self):
		TestDataTestSuite = unittest.TestSuite()
		TestDataTestSuite.addTest(TestDataTestCase('test_usercreds_insert_user_pword',
		'test_usercreds_remove_user_pword', 'test_fone_usercreds_user_pword', 
		'test_fone_prog_paths', 'test_tags_insert', 'test_tags_distinct_albumartPath', 
		'test_tags_distinct_albumid', 'test_tags_distinct_artist', 'test_tags_distinct_album', 
		'test_tags_distinct_song', 'test_tags_all', 'test_tags_all_id', 'test_tags_all_lthumb_size',
		'test_tags_all_sthumb_size', 'test_tags_all_filesize', 'test_tags_all_filetype_mp3',
		'test_tags_all_filetype_ogg', 'test_tags_all_song', 'test_tags_all_notagart',
		'test_tags_all_song_songid_artist', 'test_tags_all_filename_artist_album_song',
		'test_fone_tags_albumid', 'test_fone_tags_artist', 'test_fone_tags_album',
		'test_tags_aggregate_artist', 'test_tags_aggregate_albumid', 'test_tags_aggregate_filesize',
		'test_tags_update_artistid'))
		return TestHttpMusicPathTestSuite







