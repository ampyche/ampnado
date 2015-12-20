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
import ampnadoo.albumartscan

class TestAlbumArtScanTestCase(unittest.TestCase):
	def setUp(self):
		self.AlbumArtScan = ampnadoo.albumartscan.AlbumArtScan()
		self.searchfile = {'filename': '/usr/share/ampnado/ampnado.py'}
		self.albs_result = {'NoTagArt': 1, 'filename': '/usr/share/ampnado/ampnado.py',
			'albumartPath': '/usr/share/ampnado/folder.jpg'}
		self.albsn_result = {'NoTagArt': 0, 'filename': '/usr/share/ampnado/ampnado.py',
			'albumartPath': '/usr/share/ampnado/NOTAGART'}
	
	def tearDown(self):
		self.AlbumArtScan = None
		self.searchfile = None
		
	@mock.patch('os.path.isfile', return_value=True)
	@mock.patch('ampnadoo.albumartscan.AlbumArtScan.insert', return_value='inserted')
	def test_album_art_scan_isfile(self, os_function, ins_function):
		albs = self.AlbumArtScan._albumart_search(self.searchfile)
		self.assertEqual(albs, self.albs_result)

	@mock.patch('os.path.isfile', return_value=False)
	@mock.patch('ampnadoo.albumartscan.AlbumArtScan.insert', return_value='inserted')
	def test_album_art_scan_isNOTfile(self, os_function, ins_function):
		albsn = self.AlbumArtScan._albumart_search(self.searchfile)
		self.assertEqual(albsn, self.albsn_result)

	def suite(self):
		TestAlbumArtScanTestSuite = unittest.TestSuite()
		TestAlbumArtScanTestSuite.addTest(TestAlbumArtScanTestCase('test_album_art_scan_isfile',
			'test_album_art_scan_isNOTfile'))