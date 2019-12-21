#!/usr/bin/python3
import os
import glob
import uuid
import src.createthumbnail as ct
from src.data import Data
from pymongo import MongoClient

try: from mutagen import File
except ImportError: from mutagenx import File
from PIL import Image

client = MongoClient()
pdb = client.picdb

class FindMissingArt:

	def __init__(self, config, mpath):
		self.config = config
		self.thumbnail_path = self.config['thumbnail_dir_path']
		self.http_thumbnail_path = self.config['http_thumbnail_dir_path']
		self.media_path = self.config["media_path"]
		self.ArtWork = None
		self.MP3List = []
		self.NoArtList = []
		self.PicDics = []
		mlist = []
		for (paths, dirs, files) in os.walk(mpath, followlinks=True):
			for filename in files:
				fp = os.path.join(paths, filename)
				ext = fp[-4:]
				if ext == ".mp3":
					mlist.append(paths)
					self.MP3List.append(fp)
		self.Mp3DIRList = mlist

	def extArt(self, apath):
		ext = os.path.splitext(apath)
		op = os.path.split(ext[0])
		newpath = op[0] + "/folder.jpg"
		if os.path.exists(newpath):
			self.ArtWork = newpath
		else:
			try:
				audio = File(apath)
				artwork = audio.tags[u'APIC:'].data
				with open(newpath, 'wb') as img:
					img.write(artwork)
				self.ArtWork = newpath
			except (KeyError, TypeError, AttributeError):
				self.ArtWork = self.config["no_art_pic_path"]
				pass
		return

	# def convert_pngs(self, fpath):
	# 	pngglob = glob.glob(fpath + "/*.png")
	# 	if not len(pngglob) == 0:
	# 		for p in pngglob:
	# 			noext = p[:-4]
	# 			newpath = noext + ".jpg"
	# 			size = (100, 100)
	# 			with Image.open(p) as img:
	# 				img.convert("RGB")
	# 				img.thumbnail(size, Image.ANTIALIAS)
	# 				img.save(newpath)

	def get_globs(self, mpath):
		#self.convert_pngs(mpath)
		x = {}
		picid = str(uuid.uuid4().hex)
		x['PicId'] = picid
		x['DirPath'] = mpath
		x["NewPicPath"] = self.thumbnail_path + "/" + picid + ".jpg"
		x["AlbumArtHttpPath"] = self.http_thumbnail_path + "/" + picid + ".jpg"
		#check to see if there is a pic
		jpgGlob = glob.glob(mpath + "/*.jpg")
		#if no pic exists, extract it from mp3
		if len(jpgGlob) == 0:
			mp3glob = glob.glob(mpath + "/*.mp3")
			x['mp3glob'] = mp3glob
			mp3 = mp3glob[0]
			#mpath is a dir
			self.extArt(mp3)
			x['PicPath'] = self.ArtWork
			x['ext'] = '.jpg'
			x['AlbumArtSize'] = os.path.getsize(self.ArtWork)
		else:
			x['PicPath'] = jpgGlob[0]
			x['ext'] = 'jpg'
			x['AlbumArtSize'] = os.path.getsize(jpgGlob[0])
		return x

	def globstuff(self):
		mg = map(self.get_globs, self.Mp3DIRList)
		my_globs = list(mg)
		Thumb = ct.Thumbnails(self.config)
		mythumbs = [Thumb.create_thumbs(m) for m in my_globs]
		pdb.pics.insert_many(mythumbs)
		Data().tags_update_artID(my_globs)