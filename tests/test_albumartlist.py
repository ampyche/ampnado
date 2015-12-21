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
import src.albumartlist

def mock_distinct_albumartpath1():
	return "/usr/share/ampnado/static/MUSIC/cat1/30a455a6c5f947a0a35af7807830dc12/gordon.lightfoot/Gordon.Lightfoot.Complete.Greatest.Hits/NOTAGART"

def mock_distinct_albumartpath2():
	return "/usr/share/ampnado/static/MUSIC/cat1/584bc8e2c0bb4749b17202486232712e/hidden.in.plain.view/hidden.in.plain.view/folder.jpg"

def mock_fone_tags_albumartpath1(z):
	return {"album" : "Gordon Lightfoot Complete Greatest Hits", "albumid" : "3b17777e15054a3a8e1e4001b86a374c"}

def mock_fone_tags_albumartpath2(z):
	return { "album" : "Life in Dreaming", "albumid" : "ffe35adc900b4dc7bd3f35279654d075" }

class TestAlbumArtListTestCase(unittest.TestCase):
	def setUp(self):
		self.GetAlbumArtLists =  src.albumartlist.GetAlbumArtLists()
		self.result1 = ('/usr/share/ampnado/static/MUSIC/cat1/584bc8e2c0bb4749b17202486232712e/hidden.in.plain.view/hidden.in.plain.view/folder.jpg',
			'ffe35adc900b4dc7bd3f35279654d075', 'Life in Dreaming')
			
	def tearDown(self):
		self.GetAlbumArtLists = None
		self.result1 = None

	@mock.patch('src.albumartlist.GetAlbumArtLists.distinct_albumartpath', side_effect=mock_distinct_albumartpath1)
	@mock.patch('src.albumartlist.GetAlbumArtLists.fone_tags_albumartpath', side_effect=mock_fone_tags_albumartpath1)
	def test_get_albumart_lists_withoutart(self, dist_function, fone_function):
		t1 = self.GetAlbumArtLists.distinct_albumartpath()
		t2 = self.GetAlbumArtLists.get_albumart_lists(t1)
		self.assertEqual(t2, None)

	@mock.patch('src.albumartlist.GetAlbumArtLists.distinct_albumartpath', side_effect=mock_distinct_albumartpath2)
	@mock.patch('src.albumartlist.GetAlbumArtLists.fone_tags_albumartpath', side_effect=mock_fone_tags_albumartpath2)
	def test_get_albumart_lists_withart(self, dist_function, fone_function):
		t3 = self.GetAlbumArtLists.distinct_albumartpath()
		t4 = self.GetAlbumArtLists.get_albumart_lists(t3)
		self.assertEqual(t4, self.result1)

	def suite(self):
		TestAlbumArtListTestSuite = unittest.TestSuite()
		TestAlbumArtListTestSuite.addTest(TestAlbumArtListTestCase('test_get_albumart_lists_withoutart', 'test_get_albumart_lists_withart'))
		return TestAlbumArtListTestSuite
		