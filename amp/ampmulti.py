#!/usr/bin/python3
import os, sys, uuid, base64, glob, logging, pymongo, hashlib, multiprocessing
from multiprocessing import Pool
from PIL import Image
cores = multiprocessing.cpu_count()
from pymongo import MongoClient, ASCENDING, DESCENDING
client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

try: from mutagen import File
except ImportError: from mutagenx import File

class FindIt():
	def gen_md5(self, afile):
		with open(afile['filename'], 'rb') as mp: 
			afile['md5'] = str(hashlib.md5(mp.read()).hexdigest())
		return afile

	def _gen_md5_main(self, alist):
		pool = Pool(processes=cores)
		pm = pool.map(self.gen_md5, alist)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned
	
	def get_file_meta(self, fn):
		fn['filesize'] = os.stat(fn['filename']).st_size
		fn['dirpath'] = os.path.dirname(fn['filename'])
		fn['filetype'] = os.path.splitext(fn['filename'])[1].lower()
		fn['songid'] = str(uuid.uuid4().hex)
		return fn 
		
	def _file_meta_main(self, files):		
		pool = Pool(processes=cores)
		pm = pool.map(self.get_file_meta, files)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned

	def get_audio_tag_info(self, fn):
		audio = File(fn['filename'])
		try: fn['track'] = audio['TRCK'].text[0]
		except KeyError: fn['track'] = '50'
		try: fn['artist'] = audio["TPE1"].text[0]
		except KeyError: 
			fn['artist'] = 'Fuck Artist'
			print(fn['filename'])
			logging.info(''.join(("KeyError: No TPE1 tag... ", fn['filename'])))	
		try: fn['album'] = audio["TALB"].text[0]
		except KeyError: 
			fn['album'] = 'Fuck Album'
			print(fn['filename'])
			logging.info(''.join(("KeyError No TALB tag ... ", fn['filename'])))	
		try: fn['song'] = audio['TIT2'].text[0]
		except KeyError: 
			fn['song'] = 'Fuck Song'
			print(fn['filename'])
			logging.info(''.join(("KeyError: No TIT2 tag... ", fn['filename'])))
		return fn

	def _get_audio_tag_info_main(self, files):
		pool = Pool(processes=cores)
		pm = pool.map(self.get_audio_tag_info, files)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned

	def _albumart_search(self, x):
		ppath = '/'.join((os.path.dirname(x['filename']), "folder.jpg"))
		if os.path.isfile(ppath):
			x['albumartPath'] = ppath
			x['NoTagArt'] = 1
		else:
			try:
				audio = File(x['filename'])
				artwork = audio.tags[u'APIC:'].data
				with open(ppath, 'wb') as img: img.write(artwork)
			except (KeyError, TypeError):
				x['NoTagArt'] = 0
				x['albumartPath'] = '/'.join((os.path.dirname(x['filename']), "NOTAGART"))
			else:
				if not os.path.isfile(ppath):
					x['NoTagArt'] = 0
					x['albumartPath'] = '/'.join((os.path.dirname(x['filename']), "NOTAGART"))
		db.tags.insert(x)			
		return x

	def albumart_search_main(self, afile):
		pool = Pool(processes=cores)
		pm = pool.map(self._albumart_search, afile)
		cleaned = [x for x in pm if x != None]
		pool.close()
		pool.join()
		return cleaned

class HttpMusicPath():
	def add_http_music_path_to_db(self, t):
		#fn1 = t[0].split(t[1])[1]
		fn2 = ''.join((t[2], t[0].split(t[1])[1]))
		db.tags.update({'filename':t[0]}, {'$set': {'httpmusicpath':fn2}})

	def main(self, a_path):
		httpmusicpath = a_path['httpmusicPath']
		musiccatpath = a_path['musiccatPath']
		p = [(p['filename'], musiccatpath, httpmusicpath) for p in db.tags.find({})]
		pool = Pool(processes=cores)
		yahoo = pool.map(self.add_http_music_path_to_db, p)
		cleaned = [x for x in yahoo if x != None]
		pool.close()
		pool.join()

class GetAlbumArtLists():
	def get_albumart_lists(self, a):
		asp = a.split('/')
		if asp[-1:][0] == 'NOTAGART':
			pass
		else:
			albinfo = db.tags.find_one({'albumartPath':a}, {'albumid':1, 'album':1, '_id':0})
			ainfo = a, albinfo['albumid'], albinfo['album']
			return ainfo

	def main(self):
		albumartPaths = db.tags.distinct('albumartPath')
		pool = Pool(processes=cores)
		google = pool.map(self.get_albumart_lists, albumartPaths)
		cleaned = [x for x in google if x != None]
		pool.close()
		pool.join()		
		return cleaned

class GetAlbumArt():
	def _get_smallthumb(self, location, filename, size):
		im2 = Image.open(filename)
		im2.thumbnail(size, Image.ANTIALIAS)
		im2.save(location, "JPEG")

	def _get_thumb_size(self, location): return os.stat(location).st_size
		
	def _get_b64_image(self, location):	
		with open(location, 'rb') as imagefile:
			 return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))

	def _img_size_check_and_save(self, img, size, location):
		im = Image.open(img)
		sim = im.size
		if sim[0] > 200 and sim[1] > 200:
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(location, "JPEG")
		else:
			im.save(location, "JPEG")

	def create_thumbs(self, p):
		dthumb = (200, 200)
		d2thumb = (100, 100)
		loc2 = ''.join((p[1], p[0][1], '200x200.jpg'))
		loc1 = ''.join((p[1], p[0][1], '100x100.jpg'))
		im2 = self._get_smallthumb(loc1, p[0][0], d2thumb)
		x = {}
		x['albumartPath'] = p[0][0]
		x['albumid'] = p[0][1]
		x['album'] = p[0][2]
		x['smallthumb_size'] = self._get_thumb_size(loc1)
		x['smallthumb'] = self._get_b64_image(loc1)
		self._img_size_check_and_save(p[0][0], dthumb, loc2)
		x['largethumb_size'] = self._get_thumb_size(loc2)
		x['largethumb'] = self._get_b64_image(loc2)
		db.tags.update({'albumartPath': p[0][0]}, {'$set': {'sthumbnail': x['smallthumb'], 'smallthumb_size': x['smallthumb_size'], 'lthumbnail' : x['largethumb'], 'largethumb_size': x['largethumb_size']}}, multi=True)
		
	def main(self, alblist, apaths):
		sl10 = ''.join([apaths['tempPath'], '/'])
		alist = [(x, sl10) for x in alblist]
		pool = Pool(processes=cores)
		boogle = pool.map(self.create_thumbs, alist)
		cleaned = [x for x in boogle if x != None]
		pool.close()
		pool.join()
		sl11 = ''.join([apaths['tempPath'], '/', '*.jpg'])
		rmlist = glob.glob(sl11)
		for r in rmlist: os.remove(r)
		return cleaned	

class SetNoArtPic():
	def _get_b64_image(self, location):	
		with open(location, 'rb') as imagefile:
			 return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))

	def nat100(self, path):
		NAP1 = '/'.join((path, 'static', 'images', 'no_art_pic_100x100.png'))
		NAP1_size = os.stat(NAP1).st_size
		NAP1imgstr = self._get_b64_image(NAP1)
		return NAP1imgstr, NAP1_size

	def nat200(self, path):
		NAP2 = '/'.join((path, 'static', 'images', 'no_art_pic_200x200.png'))
		NAP2_size = os.stat(NAP2).st_size
		NAP2imgstr = self._get_b64_image(NAP2)
		return NAP2imgstr, NAP2_size

	def get_no_art_ids(self, nt):
		moo = db.tags.update({'_id':nt[0]}, {'$set': {'sthumbnail': nt[1], 'lthumbnail': nt[3], 'smallthumb_size': nt[2], 'largethumb_size': nt[4]}}) 

	def main(self):
		pp = db.prog_paths.find_one({})
		path = pp['programPath']
		nat100 = self.nat100(path)
		nat200 = self.nat200(path)
		ntaid = [(nta['_id'], nat100[0], nat100[1], nat200[0], nat200[1]) for nta in db.tags.find({'NoTagArt': 0}, {'_id':1})]
		
		pool = Pool(processes=cores)
		moogle = pool.map(self.get_no_art_ids, ntaid)
		cleaned = [x for x in moogle if x != None]
		pool.close()
		pool.join()
		return cleaned	

class CreateVidDict():
	def __init__(self):
		crap = ('.2011', '.2012', '.2014', '.2015', '.720p', '.1080p', '.BluRay','.Bluray', '.Brrip', '.x264', '.X264', '.YIFY')
		self.crap = crap

	def gen_uuid(self): return str(uuid.uuid4().hex)
	
	def _create_vid_dict(self, avid):
		vid = {}
		vid['catname'] = avid[1]	
		vid['filename'] = avid[0]
		vid['filesize'] = os.stat(avid[0]).st_size
		vid['dirpath'] = os.path.dirname(avid[0])
		cat_name = avid[1]
		split_fn = os.path.splitext(avid[0])
		extension = split_fn[1]
		vn = split_fn[0].rsplit('/', 1)
		vid_name1 = vn[1]
		ln = vn[0].split(cat_name)
		ln1 = ln[1].split('/', 2)
		link_addr = ln1[1]
		front = ln[0]
		middle = ln1[2]
		p1 = '/'.join(('Music', cat_name, link_addr, middle, vid_name1))
		pussy = ''.join((p1, extension))	#as in cat
		vid['vid_playpath'] = pussy
		for c in self.crap: vid_name1.replace(c, '')
		viddy1 = vid_name1.replace('.', ' ')
		viddy = viddy1.replace('_', ' ')
		vid_name2 = viddy.split(' ')
		vid_name3 = [v.capitalize() for v in vid_name2]
		vid_name = ' '.join(vid_name3)
		vid['vid_name'] = vid_name
		vid['vid_id'] = self.gen_uuid()
		db.video.insert(vid)
		return vid

	def main(self, avidlist, opt):
		avid = [(avid, opt['catname']) for avid in avidlist]
		pool = Pool(processes=cores)
		booty = pool.map(self._create_vid_dict, avid)
		cleaned = [x for x in booty if x != None]
		pool.close()
		pool.join()
		return cleaned	

class GetVideoPoster():
	def _img_size_check_and_save(self, img, size, location):
		im = Image.open(img)
		sim = im.size
		if sim[0] > 200 and sim[1] > 200:
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(location, "JPEG")
		else:
			im.save(location, "JPEG")

	def _get_b64_image(self, location):	
		with open(location, 'rb') as imagefile:
			 return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))

	def find_video_posters(self, v):
		vname = v[0]['vid_name'].lower()
		vpRS = v[0]['filename'].rsplit('/', 1)
		posterP = vpRS[1][:-4].lower().replace('.', '_')
		PP = ''.join((vpRS[0], '/poster_', posterP, '.jpg'))
		tpath = '/'.join((v[1], 'static', 'TEMP', ''.join(('poster_', posterP, '.jpg'))))
		if os.path.exists(PP):
			v[0]['vid_orig_poster'] = PP
			vthumb = 100, 100
			self._img_size_check_and_save(PP, vthumb, tpath)
			v[0]['vid_poster_string'] = self._get_b64_image(tpath)
			db.video.update({'filename':v[0]['filename']}, {'$set': {'vid_poster_string':v[0]['vid_poster_string'], 'vid_orig_poster': v[0]['vid_orig_poster']}})
		else:
			default = '/'.join((v[1], 'static', 'images', 'no_art_pic_100x100.png'))
			v[0]['vid_poster_string'] = self._get_b64_image(default)
			db.video.update({'filename':v[0]['filename']}, {'$set': {'vid_poster_string':v[0]['vid_poster_string']}})

	def main(self, vinfo, PATH):
		vid = [(v, PATH['programPath']) for v in vinfo]
		pool = Pool(processes=cores)
		booty = pool.map(self.find_video_posters, vid)
		pool.close()
		pool.join()
		
		
class UpdateTags():
	def get_all_db_tags(self):
		return db.tags.find({}, {'_id':1, 'filename':1, 'artist':1, 'album':1, 'song':1})
		
	def tag_check(self, af, ft):
		if af == ft:
			return True
		else:
			return False

	def get_file_tags(self, afile):
		gt = FindIt()
		file_tags = gt.get_mp3(afile['filename'])
		art_check = self.tag_check(file_tags['artist'], afile['artist'])
		alb_check = self.tag_check(file_tags['album'], afile['album'])
		song_check = self.tag.check(file_tags['song'], afile['song'])
		if art_check and alb_check and song_check:
			pass
		else:
			db.tags.update({'filename': afile['filename']}, {'$set' ,{'artist': file_tags['artist'], 'album': file_tags['album'], 'song': file_tags['song']}})
		return file_tags
		
	
	def main(self):
		fns = get_all_db_tags()
		pool = Pool(processes=cores)
		booty = pool.map(self.get_file_tags, fns)
		pool.close()
		pool.join()
		