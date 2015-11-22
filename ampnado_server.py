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
import os, json, random, hashlib, re, time, uuid, shutil, glob, subprocess, pymongo
from urllib.parse import urlparse, parse_qs
from PIL import Image
from pymongo import MongoClient
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import amp.functions as Fun
import amp.remove_old as Rm
from pprint import pprint

try: from mutagen import File
except ImportError: from mutagenx import File

mclient = MongoClient()
db = mclient.ampnadoDB
viewsdb = mclient.ampviewsDB

FUN = Fun.SetUp()
RM = Rm.RemoveOld()

US_OP = db.options.find_one({})
define('port', default=US_OP['port'], help='run on the given port', type=int)
off_set = US_OP['offset']

class Application(tornado.web.Application):
	def __init__(self):
		mpath = db.user_options.find_one({}, {'musicpath': 1, '_id': 0})
		progpath = db.prog_paths.find_one({}, {'programPath':1, '_id':0})
		progpath2 = '/'.join([progpath['programPath'], 'static', 'MUSIC'])
		handlers = [
			(r"/Music/(.*)", tornado.web.StaticFileHandler, {'path': progpath2}),
			(r"/ampnado", MainHandler),
			(r"/login", LoginHandler),
			(r"/logout", LogoutHandler),
			(r"/RandomPics", RandomPicsHandler),
			(r"/GetArtistAlpha", GetArtistAlphaHandler),
			(r"/GetInitialArtistInfo", GetInitialArtistInfoHandler),
			(r"/GetArtistInfo", GetArtistInfoHandler),
			(r"/GetAlbumAlpha", GetAlbumAlphaHandler),
			(r"/GetInitialAlbumInfo", GetInitialAlbumInfoHandler),
			(r"/GetAlbumInfo", GetAlbumInfoHandler),
			(r"/GetSongAlpha", GetSongAlphaHandler),
			(r"/GetInitialSongInfo", GetInitialSongInfoHandler),
			(r"/GetSongInfo", GetSongInfoHandler),
			(r"/GetImageSongsForAlbum", GetImageSongsForAlbumHandler),
			(r"/GetPathArt", GetPathArtHandler),
			(r"/GetAllPlaylists", GetAllPlaylistsHandler),
			(r"/GetAllPlaylistSongsFromDB", GetAllPlaylistSongsFromDBHandler),
			(r"/GetStats", GetStatsHandler),
			(r"/AddRandomPlaylist", AddRandomPlaylistHandler),
			(r"/AddPlayListNameToDB", AddPlayListNameToDBHandler),
			(r"/AddSongsToPlistDB", AddSongsToPlistDBHandler),
			(r"/CreatePlayerPlaylist", CreatePlayerPlaylistHandler),
			(r"/DeletePlaylistFromDB", DeletePlaylistFromDBHandler),
			(r"/DeleteSongFromPlaylist", DeleteSongFromPlaylistHandler),
			(r"/ArtistSearch", ArtistSearchHandler),
			(r"/AlbumSearch", AlbumSearchHandler),
			(r"/SongSearch", SongSearchHandler),
			(r"/Download", DownloadPlaylistHandler),
			(r"/GetAllVideo", GetAllVideoHandler),
			(r"/RamdomAlbumPicPlaySong", RamdomAlbumPicPlaySongHandler),
		]
		settings = dict(
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			login_url = "/login",
			cookie_secret = hashlib.sha512(str(random.randrange(100)).encode('utf-8')).hexdigest(),
			xsrf_cookies = True,
			debug = True,
		)
		tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('ampnado')

class MainHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render('ampnado.html')

class LoginHandler(BaseHandler):
	def get(self):
		self.render('login.html')	

	def check_value(self, a_phrase):
		dbun = re.match(r'^[\w]+$', a_phrase)
		if dbun.group(0): return True
		else: return False

	def post(self):
		creds = self.get_argument('username'), self.get_argument('password')
		if self.check_value(creds[0]) and self.check_value(creds[1]):
			phash = str(hashlib.sha512(creds[1].encode('utf-8')).hexdigest())
			try:
				uid = db.user_creds.find_one({'username': creds[0], 'password': phash})
				self.set_secure_cookie('ampnado', uid['user_id'])
				self.redirect('/ampnado')
			except TypeError:
				self.render('login.html')
		else:
			self.render('login.html')
	
class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("ampnado")
		self.redirect(self.get_argument('next', 'login'))

class GetAllPlaylistsHandler(BaseHandler):
	@tornado.gen.coroutine
	def getpls(self):
		try: return [(d['playlistname'], d['playlistid']) for d in db.playlists.find({}).sort([('playlistname', pymongo.ASCENDING)])]
		except KeyError: return []
		
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		plname = yield self.getpls()
		plnamez = u"Please create a playlist"
		if plname != []: self.write(dict(plnames=plname))
		else: self.write(dict(plnames=plnamez))

class GetArtistAlphaHandler(BaseHandler):
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		artal = viewsdb.artalpha.find_one({}, {'artalpha':1, '_id':0})
		artal = artal['artalpha']
		self.write(dict(artal=artal))

class GetInitialArtistInfoHandler(BaseHandler):
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		ia = [artist for artist in viewsdb.artistView.find({}, {'_id':0}).sort([('artist', pymongo.ASCENDING)]).limit(off_set)]
		self.write(dict(ia=ia))	
		
class GetArtistInfoHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_art_info(self, sel):
		sel = str(sel)
		artinfo = [art for art in viewsdb.artistView.find({'page': sel}, {'_id':0}).sort([('artist', pymongo.ASCENDING)]).limit(off_set)]
		return artinfo

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		arts = yield self._get_art_info(int(p['selected'][0]))
		self.write(dict(arts=arts))

class GetAlbumAlphaHandler(BaseHandler):
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		albal = viewsdb.albalpha.find_one({}, {'albalpha':1, '_id':0})
		albal = albal['albalpha']
		self.write(dict(albal=albal))

class GetInitialAlbumInfoHandler(BaseHandler):
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		ial = [album for album in viewsdb.albumView.find({}, {'_id':0}).limit(off_set)]
		random.shuffle(ial)
		self.write(dict(ial=ial))

class GetAlbumInfoHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_alb_info(self, sel):
		albinfo = [alb for alb in viewsdb.albumView.find({'page': sel}, {'_id':0})]
		return albinfo

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		albs = yield self._get_alb_info(p['selected'][0])
		self.write(dict(albs=albs))

class GetSongAlphaHandler(BaseHandler):
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		songal = viewsdb.songalpha.find_one({}, {'songalpha':1, '_id':0})
		songal = songal['songalpha']
		self.write(dict(songal=songal))

class GetInitialSongInfoHandler(BaseHandler):
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		ias = [song for song in viewsdb.songView.find({}, {'_id':0}).limit(off_set)]		
		random.shuffle(ias)
		self.write(dict(ias=ias))

class GetSongInfoHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_song_info(self, sel):
		songinfo = [song for song in viewsdb.songView.find({'page': sel}, {'_id':0})]
		return songinfo

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		song = yield self._get_song_info(int(p['selected'][0]))
		self.write(dict(song=song))

class GetImageSongsForAlbumHandler(BaseHandler):
	@tornado.gen.coroutine
	def getsongsongid(self, a_query):
		foo = {}
		tn = db.tags.find_one({'albumid':a_query}, {'sthumbnail':1, '_id':0})
		foo['thumbnail'] = tn['sthumbnail']
		songs = [(t['song'], t['songid']) for t in db.tags.find({'albumid':a_query}, {'song':1, 'songid':1, '_id':0})]			
		foo['songs'] = songs
		return foo

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		songs = yield self.getsongsongid(p['selected'][0])
		self.write(dict(getimgsonalb=songs))

class GetPathArtHandler(BaseHandler):
	@tornado.gen.coroutine
	def get_song_songid_path_art(self, a_query):
		info = db.tags.find_one({'songid':a_query}, {'_id':0})
		return {'album': info['album'], 'song': info['song'], 'songid': info['songid'], 'httpmusicpath': info['httpmusicpath'], 'albumart': info['sthumbnail']}

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		getpathart = yield self.get_song_songid_path_art(p['selected'][0])
		self.write(getpathart)

class GetAllPlaylistSongsFromDBHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_songs_for_playlist(self, aplid):
		try:
			for playlist in db.playlists.find({'playlistid': aplid}):
			 return [[pl['song'], pl['songid']] for pl in playlist['songs']]
		except KeyError: return []
		except TypeError: return []

	@tornado.web.authenticated
	@tornado.gen.coroutine		
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		taz = yield self._get_songs_for_playlist(p['playlistid'][0])
		self.write(dict(taz=taz))

class GetStatsHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_stats(self):
		return db.ampnado_stats.find_one({}, {'_id': 0})

	@tornado.gen.coroutine
	def get(self):
		stats = yield self._get_stats()
		self.write(dict(stats=stats))

class AddPlayListNameToDBHandler(BaseHandler):
	@tornado.gen.coroutine	
	def _insert_plname(self, pln):
		db.playlists.insert({'playlistname': pln, 'playlistid': str(uuid.uuid4().hex)})

	@tornado.gen.coroutine
	def _get_playlists(self):
		return [{'playlistname': pl['playlistname'], 'playlistid': pl['playlistid']} for pl in db.playlists.find({})]

	@tornado.web.authenticated
	@tornado.gen.coroutine		
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		print('this is p')
		print(p)
		insert_it = yield self._insert_plname(p['playlistname'][0])
		pls = yield self._get_playlists()
		self.write(dict(pnames=pls))

class AddSongsToPlistDBHandler(BaseHandler):
	@tornado.gen.coroutine	
	def insert_song_into_playlist(self, a_song_name, a_songid, a_plid):
		song = db.tags.find_one({'songid': a_songid})
		playlist = db.playlists.find_one({'playlistid': a_plid})
		try:
			playlist['songs'].append(song)
			db.playlists.update({'playlistid' : a_plid},
				{'playlistname' : playlist['playlistname'], 'playlistid' : a_plid, 'songs' : playlist['songs']})
		except KeyError:
			playlist['songs'] = [song]
			db.playlists.update({'playlistid': a_plid},
				{'playlistname' : playlist['playlistname'], 'playlistid' : a_plid, 'songs' : playlist['songs']})

	@tornado.web.authenticated
	@tornado.gen.coroutine	
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		isipl = yield self.insert_song_into_playlist(p['songname'][0], p['songid'][0], p['playlistid'][0])
		self.write("Insertion complete")

class AddRandomPlaylistHandler(BaseHandler):
	@tornado.gen.coroutine	
	def create_random_playlist(self, aplname, aplcount):
		pl = {}
		aplcount = int(aplcount)
		ids = db.tags.distinct('_id')
		random.shuffle(ids)
		random_ids = random.sample(ids, aplcount)
		new_song_list = []
		for r in random_ids:
			songs = db.tags.find_one({'_id': r}, {'_id':0})
			new_song_list.append(songs)
		random.shuffle(new_song_list)
		pl['songs'] = new_song_list
		pl['playlistname'] = aplname
		pl['playlistid'] = str(uuid.uuid4().hex)
		db.playlists.insert(pl)
		return [{'playlistname': pl['playlistname'], 'playlistid': pl['playlistid']} for pl in db.playlists.find({}, {'_id':0})]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		create_random_playlist = yield self.create_random_playlist(p['playlistname'][0], p['playlistcount'][0])
		self.write(dict(plists=create_random_playlist))

class CreatePlayerPlaylistHandler(BaseHandler):
	@tornado.gen.coroutine
	def _make_playlist(self, a_plid):
		playlist = db.playlists.find_one({'playlistid':a_plid})
		fart = []
		try:
			for pl in playlist['songs']:
				plp = pl['httpmusicpath'].split('/', 4)
				plp = '/' + os.path.splitext(plp[4])[0]
				z = {
					'name': pl['song'], 
					#'file': pl['playlistpath'],
					'file': plp,
					'thumbnail': pl['lthumbnail'], 
					'album': pl['album'],
				}		
				fart.append(z)
			return fart
		except KeyError: return []

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		makePL = yield self._make_playlist(p['playlistid'][0])
		self.write(dict(makePL=makePL))

class DeletePlaylistFromDBHandler(BaseHandler):
	@tornado.gen.coroutine
	def _delete_playlist(self, plid):
		db.playlists.remove({'playlistid': plid})
		return u'Playlist Dropped From DB'

	@tornado.gen.coroutine
	def get_pl_list(self, plid):
		return [{'playlistname': pl['playlistname'], 'playlistid': pl['playlistid']} for pl in db.playlists.find({})]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		print('this is playlistid')
		print(p['playlistid'][0])
		deleted = yield self._delete_playlist(p['playlistid'][0])
		npl = yield self.get_pl_list(p['playlistid'][0])
		self.write(dict(npl=npl))

class DeleteSongFromPlaylistHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_rec_id(self, snameid):
		rec_id = db.tags.find_one({'songid': snameid})
		return rec_id['_id']
		
	@tornado.gen.coroutine
	def _get_playlist_info(self, plname):
		return db.playlists.find_one({'playlistname': plname})

	@tornado.gen.coroutine
	def _delete_song(self, pl, rid):
		pl['songs'] = [asong for asong in pl['songs'] if asong['_id'] != rid]
		db.playlists.update({'_id': pl['_id']}, {'$set': {'songs': pl['songs']}})

	@tornado.gen.coroutine
	def _get_new_playlist(self, pln):
		return [playlist['songs'] for playlist in db.playlists.find({'playlistname': pln}, {'songs.song':1, 'songs.songid':1})]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		rec_id = yield self._get_rec_id(p['delsongid'][0])
		plist = yield self._get_playlist_info(p['playlistname'][0])
		delsong = yield self._delete_song(plist, rec_id)
		result = yield self._get_new_playlist(plist['playlistname'])
		self.write(dict(result=result))

class ArtistSearchHandler(BaseHandler):
	@tornado.gen.coroutine
	def get_search(self, artsv):
		search = viewsdb.command('text', 'artistView', search=artsv)
		return [{ 'artist': sea['obj']['artist'],  'artistid': sea['obj']['artistid'], 'albums': sea['obj']['albums']} for sea in search['results']]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		wsearch = yield self.get_search(p['artsearchval'][0])
		self.write(dict(wsearch=wsearch))

class AlbumSearchHandler(BaseHandler):
	@tornado.gen.coroutine
	def get_search(self, albsv):
		search = viewsdb.command('text', 'albumView', search=albsv)
		return [{'artist': sea['obj']['artist'], 'album': sea['obj']['album'], 'albumid': sea['obj']['albumid'], 'thumbnail': sea['obj']['thumbnail'], 'songs': sea['obj']['songs'], 'numsongs': sea['obj']['numsongs']} for sea in search['results']]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		ysearch = yield self.get_search(p['albsearchval'][0])
		print(ysearch)
		self.write(dict(ysearch=ysearch))

class SongSearchHandler(BaseHandler):
	@tornado.gen.coroutine
	def get_search(self, sv):
		search = db.command('text', 'tags', search=sv)
		return [{'artist': sea['obj']['artist'], 'song': sea['obj']['song'], 'songid': sea['obj']['songid']} for sea in search['results']]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		xsearch = yield self.get_search(p['searchval'][0])
		self.write(dict(xsearch=xsearch))

class DownloadPlaylistHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_iso_paths(self):
		return db.prog_paths.find_one({})

	@tornado.gen.coroutine
	def _clean_temp(self, apath):
		RM._remove_temp(apath)

	@tornado.gen.coroutine
	def _make_temp_dirs(self, apath):
		RM._make_needed_dirs(apath)

	@tornado.gen.coroutine
	def _clean_dirs(self):
		paths = yield self._get_iso_paths()
		clean = yield self._clean_temp(paths)
		creat_new_dirs = yield self._make_temp_dirs(paths)
		return paths
		
	@tornado.gen.coroutine	
	def _get_playlist(self, aplid):
		return db.playlists.find_one({'playlistid':bplid}, {'_id':0, 'songs.filename':1, 'songs.filesize':1})

	@tornado.gen.coroutine
	def _get_filename(self, afn):
		fnsplit = afn['filename'].split('/')
		fncount = len(fnsplit) - 1
		return fnsplit[fncount]

	@tornado.gen.coroutine
	def _get_save_loc(self, aapath, fnn):
		return '/'.join((aapath['musicPath'], fnn))

	@tornado.gen.coroutine
	def _copy_files(self, plid, apath):
		pl = yield self._get_playlist(plid)
		fsize = []
		for p in pl['songs']:
			fn = yield self._get_filename(p)
			saveloc = yield self._get_save_loc(apath, fn)	
			try: shutil.copyfile(p['filename'], saveloc)
			except IOError:
				print('This is an IOError')
				print(p['filename'])
				print(saveloc)

	@tornado.gen.coroutine
	def _gen_iso_image_paths(self, apaths, aplid):
		outfile =  ''.join((aplid, ".iso"))
		isopf = ''.join((apaths['isoPath'], '/', outfile))
		indir = apaths['musicPath']
		return outfile, isopf, indir
		
	@tornado.gen.coroutine
	def _gen_iso_image_(self, aapaths, aisopaths):
		os.chdir(aapaths['isoPath'])
		cmd = 'genisoimage -o %s %s' % (aisopaths[0], aisopaths[2])
		retcode = subprocess.call(cmd, shell=True)
		os.chdir(aapaths['programPath'])

	@tornado.gen.coroutine
	def _create_iso_image(self, apaths, plid):
		isopaths = yield self._gen_iso_image_paths(apaths, plid)
		gii = yield self._gen_iso_image_(apaths, isopaths)
		isopf_split = isopaths[1].split(apaths['programPath'])
		return isopf_split[1]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		npaths = yield self._clean_dirs()
		cfl = yield self._copy_files(p['selectedplid'][0], npaths)
		iso_image = yield self._create_iso_image(npaths, p['selectedplid'][0])
		#self.set_header('Content-Type', 'application/force-download')
		self.set_header('Content-Type', 'application/x-iso9660-image')
		fnn = "attachement; filename='%s'" % iso_image
		self.set_header('Content-Disposition', fnn)
		self.write(dict(zfile=iso_image))

class GetAllVideoHandler(BaseHandler):
	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		vlist = [vid for vid in db.video.find({}, {'vid_playpath': 1, 'vid_id': 1, 'vid_name':1, 'vid_poster_string': 1, '_id':0}).sort([('vid_name', pymongo.ASCENDING)])]
		self.write(dict(vlist=vlist))

class RamdomAlbumPicPlaySongHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_song(self, apid):
		mp = db.tags.find_one({'songid':apid}, {'httpmusicpath':1, 'lthumbnail':1, 'song':1, 'album':1, '_id':0})
		return mp['httpmusicpath'], mp['lthumbnail'], mp['song'], mp['album']

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		p = parse_qs(urlparse(self.request.full_url()).query)
		soho = yield self._get_song(p['sid'][0])
		self.write(dict(soho=soho))

class RandomPicsHandler(BaseHandler):
	@tornado.gen.coroutine
	def _get_count(self):
		return len([d['_id'] for d in db.randthumb.find({'displayed':'NOTSHOWN'})])

	@tornado.gen.coroutine
	def _get_chunk(self):
		t5 = db.randthumb.find_one({'displayed': 'NOTSHOWN'})
		return t5['_id'], t5['chunk'], t5['displayed']

	@tornado.gen.coroutine
	def _update_db(self, aid):
		db.randthumb.update({'_id': aid}, {'$set': {'displayed':'SHOWN'}})

	@tornado.gen.coroutine
	def _reset_displayed(self):
		FUN._create_random_art_db()
		print('creating random art DB')
		
	@tornado.gen.coroutine
	def _get_rand_alb_list(self):
		count = yield self._get_count()
		if count < 2:
			rset = yield self._reset_displayed()
			tid = yield self._get_chunk()
			updb = yield self._update_db(tid[0])
			return tid[1]
		else:
			tid = yield self._get_chunk()
			updb = yield self._update_db(tid[0])
			return tid[1]

	@tornado.web.authenticated
	@tornado.gen.coroutine
	def get(self):
		print('getting random pics')
		rs = yield self._get_rand_alb_list()
		art = []
		for r in rs:
			x = {}
			ace = db.tags.find_one({'albumid':r}, {'lthumbnail':1, '_id':0})
			x['thumbnail'] = ace['lthumbnail']
			x['songs'] = [(song['song'], song['songid']) for song in db.tags.find({'albumid':r}, {'song':1, 'songid':1, '_id':0})]
			art.append(x)
		self.write(dict(rsamp=art))

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()