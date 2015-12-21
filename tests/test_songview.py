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
import unittest
import unittest.mock as mock
import src.songview

def mock_gettags():
	return [
		{'song' : 'Test Song One', 'songid' : '123456', 'artist' : 'Test On A Stick'},
			{'song' : 'Test Song Two', 'songid' : '789123', 'artist' : 'Test On A Stick'}]

class TestSongViewTestCase(unittest.TestCase):
	
	def setUp(self):
		self.songview = src.songview.SongView()
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
	
	@mock.patch('src.songview.SongView.get_tags', side_effect=mock_gettags)
	@mock.patch('src.songview.SongView.insert_songalpha', return_value='inserted')
	@mock.patch('src.songview.SongView.insert_songview', return_value='inserted')
	def test_create_songView_db(self, gettags_function, sa_function, sv_function):
		hoo = self.songview.create_songView_db(self.art_so_soid)
		self.assertEqual(hoo, self.svresult)

	def suite(self):
		TestSongViewTestSuite = unittest.TestSuite()
		TestSongViewTestSuite.addTest(TestSongViewTestCase('test_create_songView_db'))
		return TestSongViewTestSuite