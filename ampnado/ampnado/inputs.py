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
import os, re, sys, uuid, configparser, hashlib, time
#from functions import Functions
from data import Data
from pymongo import MongoClient
client = MongoClient("mongodb://db:27017/ampnaodDB")
db = client.ampnadoDB

ALNEW_ERROR_MESSAGE = """
	Please only enter alpha numeric characters."""
MODE_ERROR_MESSAGE = """
	Please enter 'Install/Update/AddUser/RemoveUser'."""
MUSIC_PATH_ERROR_MESSAGE = """
	This path does not exist"""
SERVER_ADDR_ERROR_MESSAGE = """
	Enter a valid http address in the form of http://mysite.com/ampnado"""
#MODE_HELP = """
#Please select which mode to use (Install/Update/AddUser/RemoveUser). Install is used
#to initial setup AmpNado.  Update is used when adding new media to AmpNado. AddUser is used to
#add new users to AmpNado, and RemoveUser, removes users from AmpNado."""
#MEDIA_PATH_HELP = """
#	Path to the music collection, multiple paths may be entered
#	for example: '-m /home/fred/Music /home/fred/MyOtherMusicFolder'"""
#SERVER_ADDR_HELP = """
#	The Server Address. ex: http://192.168.1.100/ampnado"""
#SERVER_ADDR_PORT = """
#	The servers port number"""
#
#OFFSET_SIZE_HELP = """
#	Items per page to show, default is 15"""
#UNAME_HELP = """
#	Initial user username, 'Admin' is the default"""
#PWORD_HELP = """
#	Initial user password, 'ampnado' is the default"""
#ADD_UNAME_HELP = """
#	Add additional users, username, 'Admin' is the default"""
#ADD_PWORD_HELP = """
#	Add additional users, password, 'ampnado' is the default"""
#RM_UNAME_HELP = """
#	Remove user, username, 'Admin' is the default"""
#RM_PWORD_HELP = """
#	Remove user, password, 'ampnado' is the default"""

class GetInputs:
	
	def check_server_addr(self, a_server_addr):
		status = ""
		if a_server_addr is None: 			
			print(SERVER_ADDR_ERROR_MESSAGE)
			sys.exit()
		else:
			asp = a_server_addr.split('/')[0]
			if asp == 'http:':
				status = True
			else:
				status = False
		return status
	
	def check_media_path(self, a_path):
		status = None
		if a_path is None:
			print("Please enter a path to the music collection")
			sys.exit()
		else:
			if os.path.exists(a_path):
				status = True
			else:
				status = False
		return status

	def get_regex(self, a_name):
		un = re.match(r'^[\w]+$', a_name)
		try:
			if un.group(0): return True
		except AttributeError:
			print(ALNEW_ERROR_MESSAGE)
			return False
	
	def get_num_regex(self, a_input):
		nn = re.match(r'^[0-9]*$', str(a_input))
		try:
			if nn.group(0): return a_input
		except AttributeError:
			print("need error message here")

	def check_uname(self, a_uname):
		return self.get_regex(a_uname)

	def check_pword(self, a_pword):
		return self.get_regex(a_pword)
	
	def check_if_uname_already_in_db(self, auname, apword):
		try:
			ace = Data().fone_usercreds_user_pword(auname, apword)
			if ace['username'] != '':
				return True
			else:
				return False
		except TypeError:
			return False

	def hash_func(self, a_string):
		return str(hashlib.sha512(a_string.encode('utf-8')).hexdigest())

	def gen_hash(self, auname, apword):
		hash1 = self.hash_func(auname)
		hash2 = self.hash_func(apword)
		hash3 = self.hash_func(str(time.time()))
		hash4 = ''.join((hash1, hash2, hash3))
		hash5 = self.hash_func(hash4)
		return auname, hash2, hash5

	def insert_user(self, a_uname, a_pword, a_hash, txt_pword):
		if self.check_if_uname_already_in_db(a_uname, a_pword):
			print("The user %s with password %s already exist in the database" % (a_uname, txt_pword))
		else:
			Data().usercreds_insert_user_pword(a_uname, a_pword, a_hash)
			print("The user   %s   with password   %s   has been created" % (a_uname, a_pword))

	# def create_options_dict(self):
	# 	options_dict = {
	# 		"hostaddress" : os.environ["AMP_SERVER_ADDR"],
	# 		"musicpath" : os.environ["AMP_MEDIA_PATH"],
	# 		"offset"      : os.environ["AMP_OFFSET_SIZE"],
	# 		"port"        : os.environ["AMP_SERVER_PORT"],
	# 	}
	# 	return options_dict

	# def read_config(self, configpath):
	# 	# config = configparser.ConfigParser()
	# 	# config.read(configpath)
	# 	x = {
	# 		"server_addr" : os.environ["AMP_SERVER_ADDR"],
	# 		"server_port" : os.environ["AMP_SERVER_PORT"],
	# 		"media_path" : os.environ["AMP_MEDIA_PATH"],
	# 		"http_thumbnail_dir_path" : os.environ["AMP_HTTP_THUMBNAIL_DIR_PATH"],
	# 		"program_path" : os.environ["AMP_PROGRAM_PATH"],
	# 		"thumbnail_dir_path" : os.environ["AMP_THUMBNAIL_DIR_PATH"],
	# 		"no_art_pic_path": os.environ["AMP_NO_ART_PIC_PATH"],
	# 		"offset_size": os.environ["AMP_OFFSET_SIZE"],
	# 		"username": os.environ["AMP_USERNAME"],
	# 		"password": os.environ["AMP_PASSWORD"],
	# 		"configfile_path": None,
	# 		#"configfile_path": config["configfile-path"]["config_path"],
	# 	}
	# 	db.options.insert(x)
	# 	return x

	# def sanity_checks(self, conf):
	# 	status = 0
	# 	if not self.check_server_addr(os.environ["AMP_SERVER_ADDR"]):
	# 		status = 1
	# 		print("CHECK 1 HAS FAILED")
	# 	if not self.check_media_path(os.environ["AMP_MEDIA_PATH"]):
	# 		status = 1
	# 		print("CHECK 2 HAS FAILED")
	# 	if not self.check_uname(os.environ["AMP_USERNAME"]):
	# 		status = 1
	# 		print("CHECK 3 HAS FAILED")
	# 	if not self.check_pword(os.environ["AMP_PASSWORD"]):
	# 		status = 1
	# 		print("CHECK 4 HAS FAILED")
	# 	# if not self.check_if_uname_already_in_db(conf['username'], conf['password']):
	# 	# 	status = 1
	# 	# 	print("CHECK 5 HAS FAILED")
	# 	if status != 1:
	# 		h = self.gen_hash(os.environ["AMP_USERNAME"], os.environ["AMP_PASSWORD"])
	# 		self.insert_user(h[0], h[1], h[2], os.environ["AMP_PASSWORD"])
	# 		return self.create_options_dict()

	def remove_user(self, a_uname, a_pword):
		aid = Data().fone_usercreds_user_pword(a_uname, a_pword)
		Data().usercreds_remove_user_pword(aid['_id'])
		print("The user   %s   with password   %s   has been removed" % (a_uname, a_pword))
