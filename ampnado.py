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
import amp.setup as su
import amp.get_inputs as gp
import amp.functions as fun
import amp.remove_old as rmOld
import amp.drop_db_indexes as dDBi
import amp.updatetags as ut

from pymongo import MongoClient
client = MongoClient()
db = client.ampnadoDB

import multiprocessing
cores = multiprocessing.cpu_count()

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
		GI = gp.GetInputs()
		FUN = fun.Functions()
		SU = su.Setup()
		RM = rmOld.RemoveOld()
		DBI = dDBi.DropDBIndexes()
		DB = dDBi.DropDBs()
		UT = ut.UpdateTagsDB()
		self.GI = GI
		self.SU = SU
		self.FUN = FUN
		self.RM = RM
		self.DBI = DBI
		self.DB = DB
		self.UT = UT
		
	def _get_uuid(self):
		return str(uuid.uuid4().hex)

	def _is_vid_in_db(self, apath):
		vdb = db.tags.find_one({'filename': apath})
		if vdb != None: return True
		else: return False

	def gettime(self, at): return (time.time() - at)
	
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
		parser_utils = subparsers.add_parser('Utils')
		parser_utils.add_argument("--add-user-name", help=ADD_UNAME_HELP)
		parser_utils.add_argument("--add-user-password", help=ADD_PWORD_HELP)
		parser_utils.add_argument("--remove-user-name", help=RM_UNAME_HELP)
		parser_utils.add_argument("--remove-user-password", help=RM_PWORD_HELP)
		parser_utils.add_argument("--update-tags", default='yes', help='help')
		args = parser.parse_args()
		return args

	def main(self):
		atime = time.time()
		logging.basicConfig(filename='/usr/share/ampnado/logs/setup.log', 
			format='%(asctime)s %(levelname)s:%(message)s', filemode='w', level=logging.INFO)
		ppath = os.path.dirname(os.path.abspath(__file__))
		progpath = {'progpath': ppath}
		db.progpath.insert(progpath)
		args = self._get_args(ppath)

		#this is for install
		try:
			if args.install_catalog_name and args.media_path and args.offset_size and args.username and args.password:
				gi = self.GI.run_get_install_inputs(args)
				print('Creating the DB')
				logging.info('Creating the DB')
				db.options.insert(gi[0])#OPT 
				print('this is   db.options.insert   time')
				print(self.gettime(atime))
				
				db.prog_paths.insert(gi[1])#PATHS
				print('this is   db.prog_paths.insert   time')
				print(self.gettime(atime))
				
				music = self.SU.run_setup(gi[0], gi[1], atime, cores)
		except AttributeError: pass

		try:
			if args.add_user_name and args.add_user_password:
				h = self.FUN.gen_hash(args.add_user_name, args.add_user_password)
				users = self.GI.insert_user(h[0], h[1], h[2], args.add_user_password)
		except AttributeError: pass
		#this is for removeuser
		try:
			if args.remove_user_name and args.remove_user_password:
				h = self.FUN.gen_hash(args.remove_user_name, args.remove_user_password)
				ruser = self.GI._remove_user(h[0], h[1])
		except AttributeError: pass
		
		try:
			L1 = ['yes', 'y', 'Y', 'Yes','YES']
			if args.update_tags in L1: self.UT.update_tags_main(cores)
			else: pass
		except AttributeError: pass

		ptime = time.time()
		t = ptime - atime
		print(t)
		logging.info(t)

if __name__ == "__main__":
	su = SetUp()
	sm = su.main()