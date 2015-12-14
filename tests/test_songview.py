#!/usr/bin/python3
import unittest
import unittest.mock as mock
import ampnadoo.songview

def mock_gettags():
	return [
		{'song' : 'Test Song One', 'songid' : '123456', 'artist' : 'Test On A Stick'},
			{'song' : 'Test Song Two', 'songid' : '789123', 'artist' : 'Test On A Stick'}]

class TestSongViewTestCase(unittest.TestCase):
	
	def setUp(self):
		self.songview = ampnadoo.songview.SongView()
		self.art_so_soid = [
			{'song' : 'Test Song One', 'songid' : '123456', 'artist' : 'Test On A Stick'},
				{'song' : 'Test Song Two', 'songid' : '789123', 'artist' : 'Test On A Stick'}]
		self.svresult = [
			{'page': 1, 'artist': 'Test On A Stick', 'song': 'Test Song One', 'songid': '123456'},
				{'page': 1, 'artist': 'Test On A Stick', 'song': 'Test Song Two', 'songid': '789123'}]

	def tearDown(self):
		self.songview = None
		self.art_so_soid = None
		self.svresult = None
	
	@mock.patch('ampnadoo.songview.SongView.get_tags', side_effect=mock_gettags)
	@mock.patch('ampnadoo.songview.SongView.insert_songalpha', return_value='inserted')
	@mock.patch('ampnadoo.songview.SongView.insert_songview', return_value='inserted')
	def test_create_songView_db(self, gettags_function, sa_function, sv_function):
		hoo = self.songview.create_songView_db(self.art_so_soid)
		self.assertEqual(hoo, self.svresult)

	def suite(self):
		TestSongViewTestSuite = unittest.TestSuite()
		TestSongViewTestSuite.addTest(TestSongViewTestCase('test_create_songView_db'))
		return TestSongViewTestSuite