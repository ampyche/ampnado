#!/usr/bin/python3
import unittest
import unittest.mock as mock
import ampnadoo.httpmusicpath

def mock_alltags():
	return [
		{'filename': '/home/bogus/b/bogus.ogg'},
		{'filename': '/home/bogus2/b2/bogus2.ogg'},
		{'filename': '/home/bogus3/b3/bogus3.ogg'}]

def mock_insert(x, y):
	g = 'mock httpmusicpath db insert complete'
	return g

def mock_gettags():
	return [
		{'song' : 'Test Song One', 'songid' : '123456', 'artist' : 'Test On A Stick'},
			{'song' : 'Test Song Two', 'songid' : '789123', 'artist' : 'Test On A Stick'}]

class TestHttpMusicPathTestCase(unittest.TestCase):
	def setUp(self):
		self.HttpMusicPath = ampnadoo.httpmusicpath.HttpMusicPath()
		self.a = '/usr/share/ampnado/cat/music/goo.ogg'
		self.b = '/usr/share/ampnado/catb/music/goob.ogg'
		self.a_path = {'musiccatPath': self.a, 'httpmusicPath': self.b}
		self.acores = 2
		self.a_result = [
			('/home/bogus/b/bogus.ogg', '/usr/share/ampnado/cat/music/goo.ogg', '/usr/share/ampnado/catb/music/goob.ogg'),
			('/home/bogus2/b2/bogus2.ogg', '/usr/share/ampnado/cat/music/goo.ogg', '/usr/share/ampnado/catb/music/goob.ogg'),
			('/home/bogus3/b3/bogus3.ogg', '/usr/share/ampnado/cat/music/goo.ogg', '/usr/share/ampnado/catb/music/goob.ogg')]

	def tearDown(self):
		self.HttpMusicPath = None
		self.a = None
		self.b = None
		self.a_path = None
		self.acores = None
		self.a_result = None

	@mock.patch('ampnadoo.httpmusicpath.HttpMusicPath.alltags', side_effect=mock_alltags)
	def test_add_path(self, insert_function):
		koo = self.HttpMusicPath.alltags()
		kokoo = self.HttpMusicPath.add_paths(self.a_path, koo)
		self.assertEqual(kokoo, self.a_result)

	@mock.patch('ampnadoo.httpmusicpath.HttpMusicPath.insert', side_effect=mock_insert)
	def test_add_http_music_path_to_db(self, insert_function):
		moo = self.HttpMusicPath.add_http_music_path_to_db(self.a_result[0])
		self.assertEqual(moo, 'add_http_music_path_to_db complete')

	def suite(self):
		TestHttpMusicPathTestSuite = unittest.TestSuite()
		TestHttpMusicPathTestSuite.addTest(TestHttpMusicPathTestCase('test_add_path', 'test_add_http_music_path_to_db'))
		return TestHttpMusicPathTestSuite