#!/usr/bin/python3
import unittest
import unittest.mock as mock
import ampnadoo.albumview

class TestAlbumChunkItTestCase(unittest.TestCase):
	
	def setUp(self):
		self.AlbumChunkIt = ampnadoo.albumview.AlbumChunkIt()
		self.chunk = {'albumid': 'f4d2eb6fbec2419ab1ab1f7bd556e88e', 'thumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBD',
		'numsongs': 1, 'artist': 'Foreigner', 'songs': [[('Amnesia', 'cfa7cfd22799403499df833d5bf8338c')]],
			'album': '4', 'artistid': '16b82623c06548158d9a7fd71ad8965a'},
		self.chunklist = self.chunk * 20
		self.result = [
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '1'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '1'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '1'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '1'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '1'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '2'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '2'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '2'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '2'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '2'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '3'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '3'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '3'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '3'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '3'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '4'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '4'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '4'),
			('f4d2eb6fbec2419ab1ab1f7bd556e88e', '4'), ('f4d2eb6fbec2419ab1ab1f7bd556e88e', '4')
		]		

	def tearDown(self):
		self.AlbumChunkIt = None
		self.chunk = None 
		self.chunklist = None 
		self.result = None 

	def test_chunks(self):
		aci = self.AlbumChunkIt.chunks(self.chunklist, 5)
		aci2 = len(aci)
		self.assertEqual(aci2, 4)

	@mock.patch('ampnadoo.albumview.AlbumChunkIt.insert_albalpha', return_value='inserted')		
	def test__get_alphaoffset(self, alba_function):
		aci = self.AlbumChunkIt.chunks(self.chunklist, 5)
		chunk_t = self.AlbumChunkIt._get_alphaoffset(aci)
		self.assertEqual(chunk_t, self.result)

	def suite(self):
		TestAlbumChunkItTestSuite = unittest.TestSuite()
		TestAlbumChunkItTestSuite.addTest(TestAlbumChunkItTestCase('test_chunks', 'test_get_alphaoffset'))
		return TestAlbumChunkItTestSuite