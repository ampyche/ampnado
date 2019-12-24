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
import src.albumview

def mock_distinct_albumview():
	return ['456456456456']

def mock_fone_tags_albumid(a):
	return {"album" : "4",
		"artist" : "Foreigner",
		"artistid" : "16b82623c06548158d9a7fd71ad8965a",
		"albumid" : "f4d2eb6fbec2419ab1ab1f7bd556e88e",
		"sthumbnail" : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBD"}

def mock_aggregate_albumid(b):
	return [{'songz': ['Falls on Me'], '_id': 'song'}]

def mock_tags_all_song(c):
	return [{'song': 'Amnesia', 'songid': 'cfa7cfd22799403499df833d5bf8338c'}]

class TestAlbumViewTestCase(unittest.TestCase):
	
	def setUp(self):
		self.AlbumView = src.albumview.AlbumView()
		self.distinct_albumid = ['456456456456']

	def tearDown(self):
		self.AlbumView = None
		self.distinct_albumid = None

	@mock.patch('src.albumview.AlbumView.distinct_albumview', side_effect=mock_distinct_albumview)
	@mock.patch('src.albumview.AlbumView.fone_tags_albumid', side_effect=mock_fone_tags_albumid)
	@mock.patch('src.albumview.AlbumView.aggregate_albumid', side_effect=mock_aggregate_albumid)
	@mock.patch('src.albumview.AlbumView.tags_all_song', side_effect=mock_tags_all_song)
	@mock.patch('src.albumview.AlbumView.viewsdb_insert', return_value='inserted')
	def test_create_albumView_db(self, dist_function, fone_function, agg_function, tagsall_function, insert_function):
		albumview = self.AlbumView.create_albumView_db(self.distinct_albumid)

	def suite(self):
		TestAlbumViewTestSuite = unittest.TestSuite()
		TestAlbumViewTestSuite.addTest(TestAlbumViewTestCase('test_create_albumView_db'))
		return TestAlbumViewTestSuite