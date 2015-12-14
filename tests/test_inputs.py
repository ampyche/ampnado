#!/usr/bin/python3
import os, unittest
import unittest.mock as mock
import ampnadoo.inputs as inputs

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