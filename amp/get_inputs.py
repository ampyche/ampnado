#!/usr/bin/python
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
import os, re, sys, uuid, logging
from urllib.parse import urlparse
from pymongo import MongoClient
import amp.functions as fun
import amp.remove_old as rmOld
import amp.drop_db_indexes as dDBi

class GetInputs():
	def __init__(self):
		RM = rmOld.RemoveOld()
		FUN = fun.SetUp()
		client = MongoClient()
		db = client.ampnadoDB
		DBI = dDBi.DropDBIndexes()
		DB = dDBi.DropDBs()

		self.RM = RM
		self.FUN = FUN
		self.db = db
		self.DBI = DBI
		self.DB = DB

	def _get_uuid(self):
		return str(uuid.uuid4().hex)

	def _check_media_path(self, a_path):
		if a_path is None:
			print("Please enter a path to the music collection")
			sys.exit()
		else:
			if not os.path.exists(a_path):
				logging.error("%s path does not exist" % a_path)
				print("%s path does not exist" % a_path)
				sys.exit()
			else: return a_path	

	def _get_regex(self, a_name):
		un = re.match(r'^[\w]+$', a_name)
		try:
			if un.group(0): return a_name
		except AttributeError:
			print(ALNEW_ERROR_MESSAGE)
			logging.error("Please only enter Alpha Numeric Characters")
			
	def _get_num_regex(self, a_input):
		nn = re.match(r'^[0-9]*$', str(a_input))
		try:
			if nn.group(0): return a_input
		except AttributeError:
			print("need error message here")
			#need a log message here also

	def _check_cat_name(self, a_catname, a_uuid):
		catname = self._get_regex(a_catname)
		return (self._get_regex(a_catname), a_uuid, ''.join((catname.upper(), '_', a_uuid)))

	def _check_uname(self, a_uname):
		return self._get_regex(a_uname)

	def _check_pword(self, a_pword):
		return self._get_regex(a_pword)

	def _addr_split(self, addr):
		asp = addr.split('/')[0]
		if asp == 'http:': return addr
		else:
			logging.error("%s is not a valid http address.  Please use the form http://mysite.com/ampnado" % addr)
			sys.exit()

	def _check_server_addr(self, a_server_addr):
		if a_server_addr is None: 			
			print(SERVER_ADDR_ERROR_MESSAGE)
			sys.exit()
		else: return self._addr_split(a_server_addr)
	
	def _get_port(self, addr):
		po = urlparse(addr)
		if po.port is None: return 80
		else: return po.port

	def create_catalog_dict(self, mpath, cname, cid, ppath, ocat):
		cat_dict = {
			'musicpath' : mpath,
			'catname'   : cname,
			'catid'     : cid,
			'origcatname' : ocat,
			'catpath'   : '/'.join((ppath, 'static', 'MUSIC', cname)),
		}
		logging.info('Catalog dict created')
		return cat_dict

	def create_options_dict(self, a_args, mupath, caname, caid):
		options_dict = {
			"musicpath"   : mupath,
			'catname'     : caname,
			'catids'      : caid,
			"hostaddress" : self._check_server_addr(a_args.serv_addr),
			"uname"       : self._check_uname(a_args.username),
			"pword"       : self._check_pword(a_args.password),
			"offset"      : a_args.offset_size,
			"port"        : self._get_port(self._check_server_addr(a_args.serv_addr)),
		}
		logging.info('Options dict created')
		return options_dict

	def create_paths_dict(self, aprogpath, ahttp):
		prog_paths = {
			'programPath'    : aprogpath,
			'httppath'       : ahttp,
			'httpmusicPath'  : '/'.join((ahttp, 'Music')),
			'setupLog'       : '/'.join((aprogpath, 'logs', 'setup.log')),
			'jsonPath'       : '/'.join((aprogpath, 'static', 'json')),
			'jsonoffsetPath' : '/'.join((aprogpath, 'static', 'json', 'offset')),
			'artistjsonPath' : '/'.join((aprogpath, 'static', 'json', 'artist')),
			'albumjsonPath'  : '/'.join((aprogpath, 'static', 'json', 'album')),
			'songjsonPath'   : '/'.join((aprogpath, 'static', 'json', 'song')),
			'tempPath'       : '/'.join((aprogpath, 'static', 'TEMP')),
			'musiccatPath'   : '/'.join((aprogpath, 'static', 'MUSIC')),
			'isoPath'        : '/'.join((aprogpath, 'static', 'TEMP', 'ISO')),
			'musicPath'      : '/'.join((aprogpath, 'static', 'TEMP', 'MUSIC')),	
		}
		logging.info('Paths dict created')
		return prog_paths

	def _check_if_uname_already_in_db(self, auname, apword):
		try:
			ace = self.db.user_creds.find_one({'username': auname, 'password': apword})
			if ace['username'] != '':
				a = True
		except TypeError:
			a = False
		return a

	def insert_user(self, a_uname, a_pword, a_hash, txt_pword):
		if self._check_if_uname_already_in_db(a_uname, a_pword):
			print("The user %s with password %s already exist in the database" % (a_uname, txt_pword))
		else:
			self.db.user_creds.insert({'username': a_uname, 'password': a_pword, 'user_id': a_hash})
			print("The user   %s   with password   %s   has been created" % (a_uname, a_pword))

	def _remove_user(self, a_uname, a_pword):
		aid = self.db.user_creds.find_one({'username': a_uname, 'password': a_pword}, {'_id':1})
		self.db.user_creds.remove(aid['_id'])
		print("The user   %s   with password   %s   has been removed" % (a_uname, a_pword))

	def run_get_install_inputs(self, args):
		h = self.FUN.gen_hash(args.username, args.password)
		progpath = self.db.progpath.find_one({}, {'_id':0, 'progpath':1})
		progpath = progpath['progpath']
		musicpath = self._check_media_path(args.media_path)
		cname = self._check_cat_name(args.install_catalog_name, self._get_uuid())
		catname = cname[0]
		catid = cname[1]
		origcat = cname[2]
		CAT = self.create_catalog_dict(musicpath, catname, catid, progpath, origcat)
		OPT = self.create_options_dict(args, musicpath, catname, catid)
		httpaddr = OPT['hostaddress']
		http1 = httpaddr.split('/', 3)
		http = ''.join([http1[0], '//', http1[2]])
		PATHS = self.create_paths_dict(progpath, http)
		RM_OLD = self.RM._remove_all_old(PATHS)
		RMDBI = self.DBI.drop_all_indexes()
		RMDB = self.DB.rm_all_dbs()
		os.symlink(OPT['musicpath'], CAT['catpath'])
		if args.username and args.password:
			users = self.insert_user(h[0], h[1], h[2], args.password)
		return OPT, PATHS, CAT

	def check_if_cat_is_in_db(self, u_cat_orig):
		dbcatslist = [dbc for dbc in self.db.catalogs.find({}) if u_cat_orig == dbc['origcatname']]
		if len(dbcatslist) > 0: return dbcatslist
		else: return None

	def run_get_add_music_inputs(self, args):
		OPT = self.db.user_options.find_one({})
		PATHS = self.db.prog_paths.find_one({})
		progpath = self.db.progpath.find_one({}, {'_id':0, 'progpath':1})
		progpath = progpath['progpath']
		usn = self._check_cat_name(args.music_catalog_name, self._get_uuid())
		user_cat_name = usn[0]
		user_cat_id = usn[1]
		user_cat_orig = usn[2]
		cat_check = self.check_if_cat_is_in_db(user_cat_orig)
		user_cat_path = args.music_path
		print('this is user_cat_path')
		
		if cat_check is None:
			CAT = self.create_catalog_dict(user_cat_path, user_cat_name, user_cat_id, progpath, user_cat_orig)
			os.symlink(user_cat_path, CAT['catpath'])
			return OPT, PATHS, CAT
		else:
			os.symlink(user_cat_path, cat_check['catpath'])
			return OPT, PATHS, cat_check
		
	def run_get_add_albumart_inputs(self, args):
		album = self._get_regex(args.album)
		alb_exists = self.db.tags.find_one({'album': album}, {'_id':1})
		if alb_exists is None: print("The album %s does not exist in the database" % album)
		else: return alb_exists['_id']