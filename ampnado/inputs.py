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
import os, re, sys, uuid, logging
from urllib.parse import urlparse
import amp.functions as fun
import amp.remove_old as rmOld
import amp.drop_db_indexes as dDBi

from pymongo import MongoClient
client = MongoClient()
db = client.ampnadoDB


class GetInputs():
	def __init__(self):
		RM = rmOld.RemoveOld()
		FUN = fun.Functions()
		DBI = dDBi.DropDBIndexes()
		DB = dDBi.DropDBs()
		self.RM = RM
		self.FUN = FUN
		self.DBI = DBI
		self.DB = DB

	def _get_uuid(self):
		return str(uuid.uuid4().hex)

	def _check_media_path(self, a_path):
		if a_path is None:
			print("Please enter a path to the music collection")
			sys.exit()
		else:
			plist = []
			for a in a_path:
				if not os.path.exists(a):
					logging.error("%s path does not exist" % a)
					print("%s path does not exist" % a)
					sys.exit()
				else:
					plist.append(a)
		return plist

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

	def _check_cat_name(self, a_catname):
		return self._get_regex(a_catname)

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

	def create_options_dict(self, a_args, cm, cn):
		options_dict = {
			'catmeta'     : cm,
			'catname'     : cn,
			"hostaddress" : self._check_server_addr(a_args.serv_addr),
			"offset"      : a_args.offset_size,
			"port"        : self._get_port(self._check_server_addr(a_args.serv_addr)),
		}
		return options_dict

	def create_paths_dict(self, aprogpath, ahttp):
		prog_paths = {
			'programPath'    : aprogpath,
			'httppath'       : ahttp,
			'httpmusicPath'  : '/'.join((ahttp, 'Music')),
			'setupLog'       : '/'.join((aprogpath, 'logs', 'setup.log')),
			'tempPath'       : '/'.join((aprogpath, 'static', 'TEMP')),
			'musiccatPath'   : '/'.join((aprogpath, 'static', 'MUSIC')),
			'isoPath'        : '/'.join((aprogpath, 'static', 'TEMP', 'ISO')),
			'musicPath'      : '/'.join((aprogpath, 'static', 'TEMP', 'MUSIC')),	
		}
		logging.info('Paths dict created')
		return prog_paths

	def _check_if_uname_already_in_db(self, auname, apword):
		try:
			ace = db.user_creds.find_one({'username': auname, 'password': apword})
			if ace['username'] != '': return True
		except TypeError: return False

	def insert_user(self, a_uname, a_pword, a_hash, txt_pword):
		if self._check_if_uname_already_in_db(a_uname, a_pword):
			print("The user %s with password %s already exist in the database" % (a_uname, txt_pword))
		else:
			db.user_creds.insert({'username': a_uname, 'password': a_pword, 'user_id': a_hash})
			print("The user   %s   with password   %s   has been created" % (a_uname, a_pword))

	def _remove_user(self, a_uname, a_pword):
		aid = db.user_creds.find_one({'username': a_uname, 'password': a_pword}, {'_id':1})
		db.user_creds.remove(aid['_id'])
		print("The user   %s   with password   %s   has been removed" % (a_uname, a_pword))

	def run_get_install_inputs(self, args):
		progpath = db.progpath.find_one({}, {'_id':0, 'progpath':1})
		progpath = progpath['progpath']
		
		RMDBI = self.DBI.drop_all_indexes()
		RMDB = self.DB.rm_all_dbs()
		
		httpaddr = self._check_server_addr(args.serv_addr)
		http1 = httpaddr.split('/', 3)
		http = ''.join([http1[0], '//', http1[2]])
		PATHS = self.create_paths_dict(progpath, http)		
		RM_OLD = self.RM._remove_all_old(PATHS)

		h = self.FUN.gen_hash(args.username, args.password)
		if args.username and args.password:
			users = self.insert_user(h[0], h[1], h[2], args.password)

		catname = self._check_cat_name(args.install_catalog_name)
		catdirpath = '/'.join((progpath, 'static', 'MUSIC', catname))
		os.mkdir(catdirpath)
		
		musicpathlist = self._check_media_path(args.media_path)
		CAT_META = []
		for mp in musicpathlist:
			catid = self._get_uuid()
			catpath = '/'.join((catdirpath, catid))
			try:
				os.symlink(mp, catpath)
			except FileExistsError: print('fuck')
			cat = (mp, catname, catid, catpath)
			CAT_META.append(cat)
		
		OPT = self.create_options_dict(args, CAT_META, catname)
		return OPT, PATHS