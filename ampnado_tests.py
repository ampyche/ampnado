#!/usr/bin/python3

import os, unittest, shutil
import ampnado_setup as AMPS
import functions as FUN
import pymongo
from pymongo import MongoClient

from pprint import pprint

class TestUserInputTestCase(unittest.TestCase):
	def setUp(self):	
		self.amps = AMPS.GetInputs()
	
	def tearDown(self):
		self.amps = None

	def test_music_path(self): 
		a = '/home/foobar/Desktop/Music'
		self.assertEqual(self.amps._check_music_path(a), None)
		
	def test_get_uuid(self):
		uuid1 = self.amps._get_uuid()
		uuid2 = self.amps._get_uuid()
		self.assertNotEqual(uuid1, uuid2)
	
	def test_get_regex(self):
		self.assertEqual(self.amps._get_regex('ampnado'), 'ampnado')

	def test_get_regex_two(self):
		self.assertNotEqual(self.amps._get_regex('amp*nado'), 'AMPNADO')

	def test_cat_name(self):
		self.assertEqual(self.amps._check_cat_name('boo', '123123123')[0], 'BOO_123123123')

	def test_user_name_one(self):
		self.assertEqual(self.amps._check_uname('ampnado'), 'ampnado')

	def test_user_name_two(self):
		self.assertNotEqual(self.amps._check_uname('amp*nado'), 'ampnado')

	def test_pass_word_one(self):
		self.assertEqual(self.amps._check_pword('ampnado'), 'ampnado')

	def test_pass_word_two(self):
		self.assertNotEqual(self.amps._check_pword('amp*nado'), 'ampnado')

	def test_check_server_addr(self):
		self.assertEqual(self.amps._check_server_addr('http://MySite/ampnado'), 'http://MySite/ampnado')
		
	def test_check_offset_size_one(self):
		self.assertEqual(self.amps._check_offset_size(20), 20)
		 
	def test_check_offset_size_two(self):
		self.assertEqual(self.amps._check_offset_size(10), 15)

	def test_get_port_one(self):
		self.assertEqual(self.amps._get_port('http://MySite:8080/ampnado'), 8080)

	def test_get_port_two(self):
		self.assertEqual(self.amps._get_port('http://MySite/ampnado'), 80)

	def test_create_catalog_dict(self):
		mpath = '/home/myfiles/ampnado'
		cname = 'CATA'
		cid   = '123123'
		ppath = '/usr/share/ampnado'
		cat_dict1 = {}
		cat_dict1['musicpath'] = mpath
		cat_dict1['catname']   = cname
		cat_dict1['catid']     = cid
		cat_dict1['catpath']   = '/'.join((ppath, 'static', 'MUSIC', cname))
		cat_dict2 = self.amps.create_catalog_dict(mpath, cname, cid, ppath)
		self.assertEqual(cat_dict1, cat_dict2)

	def test_create_paths_dict(self):
		aprogpath = '/usr/share/ampnado'
		ahttp = 'http://192.168.1.110:8080/ampnado'
		p1 = {}
		p1['programPath']    = aprogpath
		p1['httppath']       = ahttp
		p1['jsonPath']       = '/'.join((aprogpath, 'static', 'json'))
		p1['jsonoffsetPath'] = '/'.join((aprogpath, 'static', 'json', 'offset'))
		p1['thumbnailsPath'] = '/'.join((aprogpath, 'static', 'thumbnails'))
		p1['httpmusicPath']  = '/'.join((ahttp, 'Music'))
		p1['httpthumbPath']  = '/'.join((ahttp, 'static', 'thumbnails'))
		p1['artistjsonPath'] = '/'.join((aprogpath, 'static', 'json', 'artist'))
		p1['albumjsonPath']  = '/'.join((aprogpath, 'static', 'json', 'album'))
		p1['songjsonPath']   = '/'.join((aprogpath, 'static', 'json', 'song'))
		p1['tempPath']       = '/'.join((aprogpath, 'static', 'TEMP'))
		p2 = self.amps.create_paths_dict(aprogpath, ahttp)
		self.assertEqual(p1, p2)

	def suite(self):
		TestUserInputTestSuite = unittest.TestSuite()
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_music_path'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_uuid'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_regex'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_regex_two'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_cat_name'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_user_name_one'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_user_name_two'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_pass_word_one'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_pass_word_two'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_check_server_addr'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_check_offset_size_one'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_check_offset_size_two'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_port_one'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_get_port_two'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_create_catalog_dict'))
		TestUserInputTestSuite.addTest(TestUserInputTestCase('test_create_paths_dict'))
		return TestUserInputTestSuite

#class TestGenerateHashTestCase(unittest.TestCase):
#	def setUp(self):	
#		self.amps = AMPS.GenerateUserHash()
#		
#	def tearDown(self):
#		self.amps = None
#	
#	def test_generate_user_name_hash(self):
#		uname = 'admin'
#		uname1 = self.amps._gen_uname_hash(uname)
#		uname2 = self.amps._gen_uname_hash(uname)
#		self.assertEqual(uname1, uname2)
#	
#	def test_generate_pass_word_hash(self):
#		pword = 'ampnado'
#		pword1 = self.amps._gen_pword_hash(pword)
#		pword2 = self.amps._gen_pword_hash(pword)
#		self.assertEqual(pword1, pword2)
#
#	def test_generate_salt_hash(self):
#		salt1 = self.amps._gen_salt()
#		salt2 = self.amps._gen_salt()
#		self.assertNotEqual(salt1, salt2)
#
#	def suite():
#		TestGenerateHashTestSuite = unittest.TestSuite()
#		TestGenerateHashTestSuite.addTest(TestGenerateHashTestCase('test_generate_user_name_hash'))
#		TestGenerateHashTestSuite.addTest(TestGenerateHashTestCase('test_generate_pass_word_hash'))
#		TestGenerateHashTestSuite.addTest(TestGenerateHashTestCase('test_generate_salt_hash'))
#		return TestGenerateHashTestSuite
#
#class TestRemoveOldTestCase(unittest.TestCase):		
#	def setUp(self):
#		self.fro = FUN.RemoveOld()
#		self.ppa = '/usr/share/ampnado/tests'
#		self.pA = {
#			'programPath': self.ppa,
#			'static' : '/'.join((self.ppa, 'static')),
#			'MUSIC' : '/'.join((self.ppa, 'static', 'MUSIC')),
#			'jsonPath' : '/'.join((self.ppa, 'json')),
#			'jsonoffsetPath' : '/'.join((self.ppa, 'offset')),
#		}
#		if not os.path.exists(self.ppa): os.mkdir(self.ppa)
#		if not os.path.exists(self.pA['jsonPath']): os.mkdir(self.pA['jsonPath'])
#		if not os.path.exists(self.pA['jsonoffsetPath']): os.mkdir(self.pA['jsonoffsetPath'])
#		if not os.path.exists(self.pA['static']): os.mkdir(self.pA['static'])
#		if not os.path.exists(self.pA['MUSIC']): os.mkdir(self.pA['MUSIC'])
#		
#	def tearDown(self):
#		if os.path.exists('/'.join((self.pA['jsonPath'], 'offset'))): os.rmdir('/'.join((self.pA['jsonPath'], 'offset')))
#		if os.path.exists(self.pA['jsonPath']): os.rmdir(self.pA['jsonPath'])
#		if os.path.exists(self.pA['jsonoffsetPath']): os.rmdir(self.pA['jsonoffsetPath'])
#		if os.path.exists(self.pA['MUSIC']): os.rmdir(self.pA['MUSIC'])
#		if os.path.exists(self.pA['static']): os.rmdir(self.pA['static'])
#		self.fro = None
#
#	def test_remove_json(self):
#		boo = self.fro._remove_json(self.pA)
#		if os.path.exists(self.pA['jsonPath']):
#			if os.path.exists(self.pA['jsonoffsetPath']):
#				x = True
#			else:
#				x = False
#		self.assertTrue(x)
#		
#	def test_remove_symlinks(self):
#		boof = self.fro._remove_symlinks(self.pA)
#		if os.path.exists(self.pA['MUSIC']):
#			x = True
#		else:
#			x = False
#		self.assertTrue(x)
#	
#	def suite(self):
#		TestRemoveOldTestSuite = unittest.TestSuite()
#		TestRemoveOldTestSuite.addTest(TestRemoveOldTestCase('test_remove_json'))
#		TestRemoveOldTestSuite.addTest(TestRemoveOldTestCase('test_remove_symlinks'))
#
#
#class TestSetupTestCase(unittest.TestCase):
#	def setUp(self):
#		self.su = FUN.SetUp()
#		self.mpath = '/usr/share/ampnado/tests/TestMusic'
#		self.amp = (
#				[
#					'/usr/share/ampnado/tests/TestMusic/test_mp3_one/08_-_ZZ_Top_-_Tres_Hombres_-_La_Grange.mp3',
#					'/usr/share/ampnado/tests/TestMusic/test_mp3_two/04_-_ZZ_Top_-_Tres_Hombres_-_Master_Of_Sparks.mp3',
#					'/usr/share/ampnado/tests/TestMusic/test_mp3_three/07_-_ZZ_Top_-_Tres_Hombres_-_Precious_And_Grace.mp3',
#				],
#				[],
#				[],
#			)
#		self.dic1 = {
#			'songid': '0b18c495694d4ee4be9f009ec456bac3',
#			'albumartPath': '/usr/share/ampnado/tests/TestMusic/test_mp3_one/folder.jpg',
#			'NoTagArt': 1,
#			'album': 'Tres Hombres',
#			'song': 'La Grange',
#			'filename': '/usr/share/ampnado/tests/TestMusic/test_mp3_one/08_-_ZZ_Top_-_Tres_Hombres_-_La_Grange.mp3',
#			'filesize': 7480311,
#			'programPath': '/usr/share/ampnado/tests',
#			'dirpath': '/usr/share/ampnado/tests/TestMusic/test_mp3_one',
#			'artist': 'Zz Top',
#			}
#		self.dic2 = {
#			'songid': '3846541fc62e4bfc86f3cfbfd854a527',
#			'albumartPath': '/usr/share/ampnado/tests/TestMusic/test_mp3_two/folder.jpg',
#			'NoTagArt': 1, 'album': 'Tres Hombres',
#			'song': 'Master of Sparks',
#			'filename': '/usr/share/ampnado/tests/TestMusic/test_mp3_two/04_-_ZZ_Top_-_Tres_Hombres_-_Master_Of_Sparks.mp3',
#			'filesize': 6803217,
#			'programPath': '/usr/share/ampnado/tests',
#			'dirpath': '/usr/share/ampnado/tests/TestMusic/test_mp3_two',
#			'artist': 'Zz Top',
#			}
#		self.dic3 = {
#			'songid': '96275e376e794a649071b28843d4183b',
#			'albumartPath': '/usr/share/ampnado/tests/TestMusic/test_mp3_three/folder.jpg',
#			'NoTagArt': 1, 'album': 'Tres Hombres',
#			'song': 'Precious and Grace',
#			'filename': '/usr/share/ampnado/tests/TestMusic/test_mp3_three/07_-_ZZ_Top_-_Tres_Hombres_-_Precious_And_Grace.mp3',
#			'filesize': 6096030,
#			'programPath': '/usr/share/ampnado/tests',
#			'dirpath': '/usr/share/ampnado/tests/TestMusic/test_mp3_three',
#			'artist': 'Zz Top',
#			}
#
#		self.ppa = '/usr/share/ampnado/tests'
#		self.pA = {
#			'programPath': self.ppa,
#			'static' : '/'.join((self.ppa, 'static')),
#			'MUSIC' : '/'.join((self.ppa, 'static', 'MUSIC')),
#			'jsonPath' : '/'.join((self.ppa, 'json')),
#			'jsonoffsetPath' : '/'.join((self.ppa, 'offset')),
#			}
#
#	def tearDown(self):
#		self.su = None
#
#	def test_find_music_video(self):
#		AMPmv = self.su._find_music_video(self.mpath)
#		self.assertEqual(self.amp, AMPmv)
#	
#	def test_gen_uuid(self):
#		g1 = self.su.gen_uuid()
#		g2 = self.su.gen_uuid
#		self.assertNotEqual(g1, g2)
#		
#	def test_gen_size(self):
#		f = '/usr/share/ampnado/static/images/112.png'
#		a = 71476
#		g = self.su.gen_size(f)
#		self.assertEqual(a, g)
#		
#	def test_gen_dirname(self):
#		f = '/home/ampnado/boo.mp3'
#		a = '/home/ampnado'
#		g = self.su.gen_dirname(f)
#		self.assertEqual(a, g)
#
#	def test_convert_bytes(self):
#		bytes = (1299711627776, 1573841824, 1558576, 1924, 1000)
#		answer = ['1.18T', '1.47G', '1.49M', '1.88K', '1000.00b']
#		blist = []
#		for b in bytes:
#			CV = self.su._convert_bytes(b)
#			blist.append(CV)
#		self.assertEqual(blist, answer)
#
#	def test_get_tags(self):
#		AMPmv = self.su._find_music_video(self.mpath)
#		AMP = self.su._get_tags(AMPmv[0], self.pA)
#		self.assertNotEqual(AMP[0]['songid'], self.dic1['songid'])
#		self.assertEqual(AMP[0]['albumartPath'], self.dic1['albumartPath'])
#		self.assertEqual(AMP[0]['NoTagArt'], self.dic1['NoTagArt'])
#		self.assertEqual(AMP[0]['album'], self.dic1['album'])
#		self.assertEqual(AMP[0]['song'], self.dic1['song'])
#		self.assertEqual(AMP[0]['filename'], self.dic1['filename'])
#		self.assertEqual(AMP[0]['filesize'], self.dic1['filesize'])
#		self.assertEqual(AMP[0]['programPath'], self.dic1['programPath'])
#		self.assertEqual(AMP[0]['dirpath'], self.dic1['dirpath'])
#		self.assertEqual(AMP[0]['artist'], self.dic1['artist'])
#		
#
#	def test_create_catalog_db(self):
#		client = MongoClient()
#		db = client.ampnadoDBtest
#		db.tags.insert(self.dic1)
#		db.tags.insert(self.dic2)
#		db.tags.insert(self.dic3)
#				
#
#		self.su._create_catalog_db()
#
#
#
##def create_catalog_dict(self, mpath, cname, cid, ppath):
##		cat_dict = {
##			'musicpath' : mpath,
##			'catname'   : cname,
##			'catid'     : cid,
##			'catpath'   : '/'.join((ppath, 'static', 'MUSIC', cname)),
##		}
##		logging.info('Catalog dict created')
##		return cat_dict
##
##		self.ppa = '/usr/share/ampnado/tests'
##		self.pA = {
##			'programPath': self.ppa,
##			'static' : '/'.join((self.ppa, 'static')),
##			'MUSIC' : '/'.join((self.ppa, 'static', 'MUSIC')),
##			'jsonPath' : '/'.join((self.ppa, 'json')),
##			'jsonoffsetPath' : '/'.join((self.ppa, 'offset')),
##			}
#
#
#
#		
#	def suite(self):
#		TestSetupTestSuite = unittest.TestSuite()
#		TestSetupTestSuite.addTest(TestSetupTestCase('test_find_music_video'))
#		TestSetupTestSuite.addTest(TestSetupTestCase('test_gen_uuid'))
#		TestSetupTestSuite.addTest(TestSetupTestCase('test_gen_size'))
#		TestSetupTestSuite.addTest(TestSetupTestCase('test_gen_dirname'))
#		TestSetupTestSuite.addTest(TestSetupTestCase('test_convert_bytes'))
#		TestSetupTestSuite.addTest(TestSetupTestCase('test_get_tags'))
#		TestSetupTestSuite.addTest(TestSetupTestCase('test_create_catalog_db'))
#
#
#

	
user_input_testsuite    = unittest.TestLoader().loadTestsFromTestCase(TestUserInputTestCase)		
#generate_hash_testsuite = unittest.TestLoader().loadTestsFromTestCase(TestGenerateHashTestCase)
#remove_old_testsuite    = unittest.TestLoader().loadTestsFromTestCase(TestRemoveOldTestCase)
#setup_testsuite         = unittest.TestLoader().loadTestsFromTestCase(TestSetupTestCase)

if __name__ == '__main__':
	unittest.main()	