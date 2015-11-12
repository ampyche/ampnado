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
import os, time, argparse, uuid, logging
from pymongo import MongoClient
import amp.get_inputs as gp
import amp.functions as fun
import amp.remove_old as rmOld
import amp.drop_db_indexes as dDBi

ALNEW_ERROR_MESSAGE = """
	Please only enter alpha numeric characters."""
MODE_ERROR_MESSAGE = """
	Please enter 'Install/Update/AddUser/RemoveUser'."""
MUSIC_PATH_ERROR_MESSAGE = """
	This path does not exist"""
SERVER_ADDR_ERROR_MESSAGE = """
	Enter a valid http address in the form of http://mysite.com/ampnado"""
MODE_HELP = """
Please select which mode to use (Install/Update/AddUser/RemoveUser). Install is used
to initial setup AmpNado.  Update is used when adding new media to AmpNado. AddUser is used to
add new users to AmpNado, and RemoveUser, removes users from AmpNado."""
MEDIA_PATH_HELP = """
	Path to the music collection, multiple paths may be entered
	for example: '-m /home/fred/Music /home/fred/MyOtherMusicFolder'"""
SERVER_ADDR_HELP = """
	The Server Address. ex: http://192.168.1.100/ampnado"""
CAT_NAME_HELP = """
	Catalog Name or Music collection name, default is current date"""
OFFSET_SIZE_HELP = """
	Items per page to show, default is 15"""
UNAME_HELP = """
	Initial user username, 'Admin' is the default"""
PWORD_HELP = """
	Initial user password, 'ampnado' is the default"""
ADD_UNAME_HELP = """
	Add additional users, username, 'Admin' is the default"""
ADD_PWORD_HELP = """
	Add additional users, password, 'ampnado' is the default"""
RM_UNAME_HELP = """
	Remove user, username, 'Admin' is the default"""
RM_PWORD_HELP = """
	Remove user, password, 'ampnado' is the default"""	

class SetUp():
	def __init__(self):
		client = MongoClient()
		db = client.ampnadoDB
		GI = gp.GetInputs()
		SU = fun.SetUp()
		RM = rmOld.RemoveOld()
		DBI = dDBi.DropDBIndexes()
		DB = dDBi.DropDBs()
		UPDATE = False
		
		self.UPDATE = UPDATE
		self.db = db
		self.GI = GI
		self.SU = SU
		self.RM = RM
		self.DBI = DBI
		self.DB = DB
		
	def _get_uuid(self):
		return str(uuid.uuid4().hex)
	
	def _get_args(self, a_ppath):
		a_uuid = ''.join(('CAT1', self._get_uuid()))
		parser = argparse.ArgumentParser(description="Setup AmpNado")
		subparsers = parser.add_subparsers(title="Setup AmpNado", description="AmpNado SubCommands", help='this is the help message')
		parser_install = subparsers.add_parser('Install')
		parser_install.add_argument("-s", "--serv-addr", required=True, help=SERVER_ADDR_HELP)
		parser_install.add_argument("-m", "--media-path", nargs="*", required=True, help=MEDIA_PATH_HELP)
		parser_install.add_argument("-c", "--install_catalog-name", default=a_uuid, help=CAT_NAME_HELP)
		parser_install.add_argument("-o", "--offset-size", type=int, default=15, help=OFFSET_SIZE_HELP)
		parser_install.add_argument("-u", "--username", default='Admin', help=UNAME_HELP)
		parser_install.add_argument("-p", "--password", default='ampnado', help=PWORD_HELP)
		
#		
#		#Need to re think this
#		parser_addmusic = subparsers.add_parser('AddMusic')
#		parser_addmusic.add_argument("-mp", "--music-path", required=True, help=MEDIA_PATH_HELP)
#		parser_addmusic.add_argument("-mc", "--music-catalog-name", default=a_uuid, help=CAT_NAME_HELP)
#		
#		
#		
#		#Need to re think this
#		parser_addAlbumArt = subparsers.add_parser('AddAlbumArt')
#		parser_addAlbumArt.add_argument("-mart", "--albumart-path", help='not implemented yet')
#		parser_addAlbumArt.add_argument("-alb", "--album", help='not implemented yet')
#		
#		
#		#Need to re think this
#		parser_addvideo = subparsers.add_parser('AddVideo')
#		parser_addvideo.add_argument("-v", "--video-path", required=True, help=MEDIA_PATH_HELP)
#		parser_addvideo.add_argument("-vc", "--video-catalog-name", default=a_uuid, help=CAT_NAME_HELP)
#		
#		
#		#Need to re think this
#		parser_addvideoart = subparsers.add_parser('AddVideoArt')
#		parser_addvideoart.add_argument("-vart", "--videoart-path", help='not implemented yet')
#		parser_addvideoart.add_argument("-vid", "--video", help='not implemented yet')
#		
#		
#		
#		
		
		parser_utils = subparsers.add_parser('Utils')
		parser_utils.add_argument("-aun", "--add-user-name", help=ADD_UNAME_HELP)
		parser_utils.add_argument("-aup", "--add-user-password", help=ADD_PWORD_HELP)
		parser_utils.add_argument("-rmn", "--remove-user-name", help=RM_UNAME_HELP)
		parser_utils.add_argument("-rmp", "--remove-user-password", help=RM_PWORD_HELP)
		args = parser.parse_args()
		return args

	def _is_vid_in_db(self, apath):
		vdb = self.db.tags.find_one({'filename': apath})
		if vdb != None:
			return True
		else:
			return False

	def symlink_cronPY(self):
		pp = self.db.progpath.find_one({})
		path1 = pp['progpath'] + '/ampnado_cron.sh'
		path2 = '/etc/cron.hourly/ampnado'
		try: os.remove(path2)
		except FileNotFoundError: os.symlink(path1, path2)
		
	def gettime(self, at):
		b = time.time()
		return (b - at)

	def main(self):
		atime = time.time()
		
		logging.basicConfig(filename='/usr/share/ampnado/logs/setup.log', 
			format='%(asctime)s %(levelname)s:%(message)s', filemode='w', level=logging.INFO)
		ppath = os.path.dirname(os.path.abspath(__file__))
		progpath = {'progpath': ppath}
		self.db.progpath.insert(progpath)
		args = self._get_args(ppath)
		
		#this is for install
		try:
			if args.install_catalog_name and args.media_path and args.offset_size and args.username and args.password:
				gi = self.GI.run_get_install_inputs(args)
				print('Creating the DB')
				logging.info('Creating the DB')
				self.db.options.insert(gi[0])#OPT 
				print('this is   db.options.insert   time')
				print(self.gettime(atime))
				
				self.db.prog_paths.insert(gi[1])#PATHS
				print('this is   db.prog_paths.insert   time')
				print(self.gettime(atime))
				
				music = self.SU.run_setup(gi[0], gi[1], atime)
				print('this is  run_setup    time')
				print(self.gettime(atime))
		except AttributeError: pass
		#this is for addmusic
		try:
			if args.music_path and args.music_catalog_name:
				self.UPDATE = True
				gi = self.GI.run_get_add_music_inputs(args)
				new_music = self.SU.run_setup(gi[0], gi[1], gi[2], self.UPDATE)
		except AttributeError: pass
		#this is for addalbumart
		try:
			if args.albumart_path and args.album:
				aagi = self.GI.run_get_add_albumart_inputs(args)#returns album objectID if album is in database
				if not os.path.exists(args.albumart_path):
					print('Path to albumart does not exist.')
				else:
					l_1 = self.db.prog_paths.find_one({}, {'tempPath':1})
					Sloc = '/'.join((l_1['tempPath'], 'smalltemp'))
					Lloc = '/'.join((l_1['tempPath'], 'largetemp'))
					Ssize = (100, 100)
					self.SU._get_smallthumb(Sloc, args.albumart_path, Ssize)
					small_b64 = self.SU._get_b64_image(Sloc)
					os.remove(Sloc)
					Lsize = (200, 200)
					self.SU._img_size_check_and_save(args.albumart_path, Lsize, Lloc)
					large_b64 = self.SU._get_b64_image(Lloc)
					os.remove(Lloc)
					self.db.tags.update({'_id': aagi}, {'sthumbnail': small_b64, 'lthumbnail': large_b64})#update db with new small thumb
		except AttributeError: pass
		#this if for addvideo
		try:
			opt = self.db.user_options.find_one({})
			if args.video_catalog_name:
				vcn = self.db.catalogs.find_one({'origcatname': args.video_catalog_name})
				acatid = self._get_uuid()
				if vcn != None: acat = vcn
				else: acat = {'catname': args.video_catalog_name + "_" + acatid, 'musicpath': args.video_path}
			else: print('Please enter a catalog name.')
			if args.video_path:
				vidlist = []
				avidlist = self.SU._find_music_video(args.video_path)
				self.UPDATE = True
				udp = self.UPDATE
				vvinfo = self.SU._create_vid_dict(avidlist[2], opt, acat, udp)
				pp = self.db.progpath.find_one({})
				path = {'programPath': pp['progpath']}
				find_VP = self.SU.find_video_posters(vvinfo, path)
				insert_video = self.db.video.insert(find_VP)			
			else: print('Please enter path to video')
		except AttributeError: pass
		#this is for addvideoart
		try:
			path = self.db.prog_paths.find_one({})
			if args.video_art_path:
				if os.path.isfile(args.video_art_path):
					vidposterString = self._get_b64_image(args.video_art_path)	
				else:
					print('Video poster path does not exist')
			else:
				print('Please enter path to video poster')
			if args.video:
				#need regex check here
				vid = self.db.video.find({'vid_name': args.video})
				if vid != None:
					self.db.video.update({'vid_name': args.video}, {'$set': {'video_poster_string': vidposterString}})
				else:
					print('Video is not in the Database')
			else:
				print('Please enter a video name')
		except AttributeError: pass
		#this is for adduser
		try:
			if args.add_user_name and args.add_user_password:
				h = self.SU.gen_hash(args.add_user_name, args.add_user_password)
				users = self.GI.insert_user(h[0], h[1], h[2], args.add_user_password)
		except AttributeError: pass
		#this is for removeuser
		try:
			if args.remove_user_name and args.remove_user_password:
				h = self.SU.gen_hash(args.remove_user_name, args.remove_user_password)
				ruser = self.GI._remove_user(h[0], h[1])
		except AttributeError: pass

		sc = self.symlink_cronPY()	
		ptime = time.time()
		t = ptime - atime
		print(t)
		logging.info(t)

if __name__ == "__main__":
	su = SetUp()
	sm = su.main()