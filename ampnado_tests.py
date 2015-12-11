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
import os, unittest
import unittest.mock as mock 
import ampnadoo.inputs as inputs
import ampnadoo.filemeta as filemeta

from ampnadoo.httpmusicpath import HttpMusicPath

class TestInputsTestCase(unittest.TestCase):
	def setUp(self):	
		self.gi = inputs.GetInputs()
	
	def tearDown(self):
		self.gi = None

	def test_get_uuid(self):
		uuid1 = self.gi._get_uuid()
		uuid2 = self.gi._get_uuid()
		self.assertNotEqual(uuid1, uuid2)

	def test_music_path(self):
		hoo = os.getcwd()
		boo = [hoo + '/static/images/112.png',]
		boo2 = hoo + '/static/images/112.png'
		self.assertEqual(self.gi._check_media_path(boo), [boo2])

	def test_get_regex(self):
		self.assertEqual(self.gi._get_regex('ampnado'), 'ampnado')

	def test_cat_name(self):
		self.assertEqual(self.gi._check_cat_name('ampnadocat'), 'ampnadocat')

	def test_user_name_one(self):
		self.assertEqual(self.gi._check_uname('ampnado'), 'ampnado')

	def test_pass_word_one(self):
		self.assertEqual(self.gi._check_pword('ampnado'), 'ampnado')

	def test_check_server_addr(self):
		self.assertEqual(self.gi._check_server_addr('http://MySite/ampnado'), 'http://MySite/ampnado')

	def test_get_port_one(self):
		self.assertEqual(self.gi._get_port('http://MySite:8080/ampnado'), 8080)

	def test_get_port_two(self):
		self.assertNotEqual(self.gi._get_port('http://MySite/ampnado'), 8080)

	def test_create_paths_dict(self):
		aprogpath = '/usr/share/ampnado'
		ahttp = 'http://192.168.1.110:8080/ampnado'
		p1 = {}
		p1['programPath']    = aprogpath
		p1['httppath']       = ahttp
		p1['httpmusicPath']  = '/'.join((ahttp, 'Music'))
		p1['setupLog']       = '/'.join((aprogpath, 'logs', 'setup.log'))
		p1['tempPath']       = '/'.join((aprogpath, 'static', 'TEMP'))	
		p1['musiccatPath']   = '/'.join((aprogpath, 'static', 'MUSIC'))
		p1['isoPath']        = '/'.join((aprogpath, 'static', 'TEMP', 'ISO'))
		p1['musicPath']      = '/'.join((aprogpath, 'static', 'TEMP', 'MUSIC'))
		p2 = self.gi.create_paths_dict(aprogpath, ahttp)
		self.assertEqual(p1, p2)

	def suite(self):
		TestInputsTestSuite = unittest.TestSuite()
		TestInputsTestSuite.addTest(TestInputsTestCase('test_music_path', 
			'test_get_uuid', 'test_get_regex', 'test_cat_name',
			'test_user_name_one', 'test_pass_word_one', 'test_get_port_one',
			'test_get_port_two', 'test_create_paths_dict',
		))
		return TestInputsTestSuite
		
class TestFileMetaTestCase(unittest.TestCase):
	def setUp(self):	
		self.fm = filemeta.GetFileMeta()
		self.bogus = '/bogus/path/to/file/boo.ogg'
		self.bogus1 = {'filename': self.bogus}
		self.bogus_dir = '/bogus/path/to/file'
	
	def tearDown(self):
		self.fm = None
		self.bogus = None
		self.bogus1 = None
		self.bogus_dir = None

	def test_size(self):
		self.assertEqual(self.fm.size(self.bogus), '001')

	def test_dirpath(self):
		self.assertEqual(self.fm.dirpath(self.bogus), self.bogus_dir)

	def test_split_lower(self):
		self.assertEqual(self.fm.split_lower(self.bogus), '.ogg')

	def test_uuidd(self):
		uuid1 = self.fm.uuidd()
		uuid2 = self.fm.uuidd()
		self.assertNotEqual(uuid1, uuid2)

	def test_get_file_meta(self):
		boo = self.fm.get_file_meta(self.bogus1)
		self.assertEqual(boo['filesize'], '001')
		self.assertEqual(boo['dirpath'], self.bogus_dir)
		self.assertEqual(boo['filetype'], '.ogg')
		self.assertNotEqual(boo['songid'], '456456')

	def suite(self):
		TestFileMetaTestSuite = unittest.TestSuite()
		TestFileMetaTestSuite.addTest(TestFileMetaTestCase('test_size', 'test_dirpath',
			'test_split_lower', 'test_uuidd', 'test_get_file_meta',
		))		

def mock_alltags():
	return [
		{'filename': '/home/bogus/b/bogus.ogg'},
		{'filename': '/home/bogus2/b2/bogus2.ogg'},
		{'filename': '/home/bogus3/b3/bogus3.ogg'},
	]

def mock_insert(x, y):
	g = 'mock httpmusicpath db insert complete'
	return g

class TestHttpMusicPathTestCase(unittest.TestCase):
	def setUp(self):
		self.HttpMusicPath = HttpMusicPath()
		self.a = '/usr/share/ampnado/cat/music/goo.ogg'
		self.b = '/usr/share/ampnado/catb/music/goob.ogg'
		self.a_path = {'musiccatPath': self.a, 'httpmusicPath': self.b}
		self.acores = 2
		self.a_result = [
			('/home/bogus/b/bogus.ogg', '/usr/share/ampnado/cat/music/goo.ogg', '/usr/share/ampnado/catb/music/goob.ogg'),
			('/home/bogus2/b2/bogus2.ogg', '/usr/share/ampnado/cat/music/goo.ogg', '/usr/share/ampnado/catb/music/goob.ogg'),
			('/home/bogus3/b3/bogus3.ogg', '/usr/share/ampnado/cat/music/goo.ogg', '/usr/share/ampnado/catb/music/goob.ogg'),
		]

	def tearDown(self):
		self.fm = None

	@mock.patch('__main__.HttpMusicPath.alltags', side_effect=mock_alltags)
	def test_add_path(self, insert_function):
		koo = self.HttpMusicPath.alltags()
		kokoo = self.HttpMusicPath.add_paths(self.a_path, koo)
		self.assertEqual(kokoo, self.a_result)

	@mock.patch('__main__.HttpMusicPath.insert', side_effect=mock_insert)
	def test_add_http_music_path_to_db(self, insert_function):
		moo = self.HttpMusicPath.add_http_music_path_to_db(self.a_result[0])
		self.assertEqual(moo, 'add_http_music_path_to_db complete')

	def suite(self):
		TestHttpMusicPathTestSuite = unittest.TestSuite()
		TestHttpMusicPathTestSuite.addTest(TestHttpMusicPathTestCase('test_add_path', 'test_add_http_music_path_to_db'))




input_ts    = unittest.TestLoader().loadTestsFromTestCase(TestInputsTestCase)		
filemeta_ts = unittest.TestLoader().loadTestsFromTestCase(TestFileMetaTestCase)		
httpmusicpath_ts = unittest.TestLoader().loadTestsFromTestCase(TestHttpMusicPathTestCase)		

if __name__ == '__main__':
	unittest.main()	