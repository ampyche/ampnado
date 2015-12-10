#!/usr/bin/python3

import os, unittest, shutil
import ampnadoo.inputs as inputs
#import functions as FUN
#import pymongo
#from pymongo import MongoClient
#
#from pprint import pprint

class TestUserInputTestCase(unittest.TestCase):
	def setUp(self):	
		self.gi = inputs.GetInputs()
	
	def tearDown(self):
		self.amps = None

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

#	def test_create_catalog_dict(self):
#		mpath = '/home/myfiles/ampnado'
#		cname = 'CATA'
#		cid   = '123123'
#		ppath = '/usr/share/ampnado'
#		cat_dict1 = {}
#		cat_dict1['musicpath'] = mpath
#		cat_dict1['catname']   = cname
#		cat_dict1['catid']     = cid
#		cat_dict1['catpath']   = '/'.join((ppath, 'static', 'MUSIC', cname))
#		cat_dict2 = self.gi.create_catalog_dict(mpath, cname, cid, ppath)
#		self.assertEqual(cat_dict1, cat_dict2)

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
		TestUserInputTestSuite = unittest.TestSuite()
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_music_path'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_uuid'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_regex'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_cat_name'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_user_name_one'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_pass_word_one'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_port_one'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_port_two'))
		#TestUserInputTestSuite.addTest(TestUserInputTestCase('test_create_catalog_dict'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_create_paths_dict'))
		return TestUserInputTestSuite




	
user_input_testsuite    = unittest.TestLoader().loadTestsFromTestCase(TestUserInputTestCase)		

if __name__ == '__main__':
	unittest.main()	