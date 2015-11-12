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
import logging
from pymongo import MongoClient
from multiprocessing import Pool

client = MongoClient()
db = client.ampnadoDB
viewsdb = client.ampviewsDB

class AlbumView():
	def create_albumView_db(self, a):
		info = db.tags.find_one({'albumid':a}, {'album':1, 'albumid': 1, 'artist':1, 'artistid':1, 'sthumbnail':1, '_id':0})
		av = {}
		av['albumid'] = info['albumid']
		av['album'] = info['album']
		av['artist'] = info['artist']
		av['artistid'] = info['artistid']
		av['thumbnail'] = info['sthumbnail']
		boo = db.tags.aggregate([
			{'$match': {'albumid': a}},
			{'$group': {'_id': 'song', 'songz': {'$addToSet': '$song'}}},
			{'$project': {'songz' :1}}
			])
		doo = boo['result'][0]['songz']
		av['numsongs'] = len(doo)
		new_song_list = []
		for d in doo:
			sids = [(s['song'], s['songid']) for s in db.tags.find({'song':d}, {'song':1, 'songid':1, '_id':0})]
			new_song_list.append(sids)
		av['songs'] = new_song_list
		viewsdb.albumView.insert(av)
		return av
	
	def main(self, OFC):
		albid = db.tags.distinct('albumid')
		pool = Pool(processes=4)
		poogle = pool.map(self.create_albumView_db, albid)
		cleaned = [x for x in poogle if x != None]
		pool.close()
		pool.join()
		return cleaned




class ChunkIt():
	def chunks(self, l, n):
		if n < 1:
			n = 1
		return [l[i:i + n] for i in range(0, len(l), n)]		
	
	
	def _get_alphaoffset(self, chunks):		
		count = 0
		albidPlist = []
		albalphaoffsetlist = []
		for chu in chunks:
			count += 1
			for c in chu:
				albid_page = c['albumid'], str(count)
				albidPlist.append(albid_page)
			albalphaoffsetlist.append(str(count))
		viewsdb.albalpha.insert(dict(albalpha=albalphaoffsetlist))
		return albidPlist
			
			
			
			
	def _get_pages(self, c):
		viewsdb.albumView.update({'albumid': c[0]}, {'$set': {'page': c[1]}})
	
		

	def main(self, albv, OFC):
		chunks = self.chunks(albv, OFC)
		
		gaos = self._get_alphaoffset(chunks)
		
		
		pool = Pool(processes=4)
		voodoo = pool.map(self._get_pages, gaos)
		#print('this is voodoo')
#		print(voodoo)
#		cleaned = [x for x in voodoo if x != None]
		pool.close()
		pool.join()
		
		
		
		
#class AlbumView():
#	
#	def create_albumView_db(self, OFC):
#		count = 0
#		page = 1		
#		result = []
#		albalphaoffsetlist = []
#		for a in db.tags.distinct('albumid'):
#			info = db.tags.find_one({'albumid':a}, {'album':1, 'albumid': 1, 'artist':1, 'artistid':1, 'sthumbnail':1, '_id':0})
#			av = {}
#			av['albumid'] = info['albumid']
#			av['album'] = info['album']
#			av['artist'] = info['artist']
#			av['artistid'] = info['artistid']
#			av['thumbnail'] = info['sthumbnail']
#			boo = db.tags.aggregate([
#				{'$match': {'albumid': a}},
#				{'$group': {'_id': 'song', 'songz': {'$addToSet': '$song'}}},
#				{'$project': {'songz' :1}}
#				])
#			doo = boo['result'][0]['songz']
#			av['numsongs'] = len(doo)
#			
#			
#			
#			
#			new_song_list = []
#			for d in doo:
#				sids = [(s['song'], s['songid']) for s in db.tags.find({'song':d}, {'song':1, 'songid':1, '_id':0})]
#				new_song_list.append(sids)
#			av['songs'] = new_song_list
#			count += 1
#			if count == OFC:
#				page += 1
#				count = 0
#			av['page'] = page
#			albalphaoffsetlist.append(page)
#			result.append(av)
#		albalphaoffsetlist = list(set(albalphaoffsetlist))
#		viewsdb.albalpha.insert(dict(albalpha=albalphaoffsetlist))
#		viewsdb.albumView.insert(result)
#
#
#
##		else:
##			for a in db.tempTags.distinct('albumid'):
##				info = db.tempTags.find_one({'albumid':a}, {'album':1, 'albumid': 1, 'artist':1, 'artistid':1, 'sthumbnail':1, '_id':0})
##				av = {}
##				av['albumid'] = info['albumid']
#				av['album'] = info['album']
#				av['artist'] = info['artist']
#				av['artistid'] = info['artistid']
#				av['thumbnail'] = info['sthumbnail']
#				boo = db.tempTags.aggregate([
#					{'$match': {'albumid': a}},
#					{'$group': {'_id': 'song', 'songz': {'$addToSet': '$song'}}},
#					{'$project': {'songz' :1}}
#					])
#				doo = boo['result'][0]['songz']
#				av['numsongs'] = len(doo)
#				for d in doo:
#					sids = [(s['song'], s['songid']) for s in db.tempTags.find({'song':d}, {'song':1, 'songid':1, '_id':0})],
#				av['songs'] = sids
#				count += 1
#				if count == OFC:
#					page += 1
#					count = 0
#				av['page'] = page
#				albalphaoffsetlist.append(page)
#				result.append(av)
#			albalphaoffsetlist = list(set(albalphaoffsetlist))
#			viewsdb.albalpha.insert(dict(albalpha=albalphaoffsetlist))
#			viewsdb.tempalbumView.insert(result)