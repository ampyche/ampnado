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

DS_USER_CREDS_PWORD = """
	c53d96b8aaa95e55a5d0d40cc1ea340f35e42d778cfbc0b39ea621e50362394e82b6e0112eb4e6303d371a6f
"""

DS_USER_CREDS_USERID = """
	85f2cf6f3c8a36c13678a9e159aef4ab6a26fa3f24eac2fa1360e260fe98107d1f9f950da40a4eb6ee6fbeb19
"""

DS_PP = {
	'httpmusicPath' : "http://192.168.1.115/Music", 'setupLog' : "/usr/share/ampnado/logs/setup.log",
	'musiccatPath' : "/usr/share/ampnado/static/MUSIC", 'musicPath' : "/usr/share/ampnado/static/TEMP/MUSIC",
	'programPath' : "/usr/share/ampnado", 'tempPath' : "/usr/share/ampnado/static/TEMP", 
	'httppath' : "http://192.168.1.115", 'isoPath' : "/usr/share/ampnado/static/TEMP/ISO",
}

DS_TAGS_ALL = [
	{
		'NoTagArt' : 1, 'song' : "Young Girl", 
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett",
		'songid' : "c2c96e01a93945f2a440b59db68013f3", 'track' : "01", 
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/01_-_Gary_Puckett_And_The_Union_Gap_-_Gary_Puckett_-_Young_Girl.mp3",
		'programPath' : "/usr/share/ampnado", 'artist' : "Gary Puckett And The Union Gap", 'catname' : "cat1", 'filesize' : 3773516, 
		'filetype' : ".mp3",	'album' : "Gary Puckett", 'largethumb_size' : 5855, 'smallthumb_size' : 2984, 
		'albumartPath' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/folder.jpg",
		'httpmusicpath' : "http://192.168.1.142/Music/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/01_-_Gary_Puckett_And_The_Union_Gap_-_Gary_Puckett_-_Young_Girl.mp3",
		'artistid' : "16243618e8f74436a28760c4b986fd81", 'albumid' : "c1dd0a3134e344a6b23493a55f83856f", 
		'sthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcp",
		'lthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC",
	},
	{
		'NoTagArt' : 1, 'song' : "Moonlight Shadow", 
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage",
		'songid' : "e544e219ff904a14a5470f76544f19ec", 'track' : "01", 'filename' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/01_-_Groove_Coverage_-_Groove_Coverage_-_MoonLight_Shadow.mp3",
		'programPath' : "/usr/share/ampnado", 'artist' : "Groove Coverage", 'catname' : "cat1", 'filesize' : 2640869, 
		'filetype' : ".mp3", 'album' : "Groove Coverage", 'albumartPath' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/folder.jpg",
		'httpmusicpath' : "http://192.168.1.142/Music/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/01_-_Groove_Coverage_-_Groove_Coverage_-_MoonLight_Shadow.mp3",
		'artistid' : "a3b08d94af6e41be821eb234526964aa", 'albumid' : "e703dd2b413947e99406fee1ba799c04", 
		'sthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQ",
		'lthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQg", 
		'largethumb_size' : 3283, 'smallthumb_size' : 2038,
	},
	{
		'NoTagArt' : 1, 'song' : "The Angel Song", 'songid' : "7ba4163b39ec467aa4a531b4930b8be1", 'track' : "01", 
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white",
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/01_-_Great_White_-_Great_White_-_The_Angel_Song.mp3",
		'programPath' : "/usr/share/ampnado", 'artist' : "Great White", 'catname' : "cat1", 'filesize' : 4552532, 
		'filetype' : ".mp3", 'album' : "Great White", 'albumartPath' : "/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/folder.jpg",
		'httpmusicpath' : "http://192.168.1.142/Music/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/01_-_Great_White_-_Great_White_-_The_Angel_Song.mp3",
		'artistid' : "ff312b038cde41f79ea15ab00b60f9d1", 'albumid' : "674b858949c84d7790753959b8c0ee1c", 
		'sthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBk",
		'lthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw", 
		'largethumb_size' : 13612, 'smallthumb_size' : 4050,
	},
	{
		'NoTagArt' : 1, 'song' : "Natural Born Bugie", 'songid' : "826ce048d8714d1f9a5648ee6b69410e", 'track' : "6",
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie",
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/06_-_Humble_Pie_-_Humble_Pie_-_Natural_Born_Bugie.mp3",
		'programPath' : "/usr/share/ampnado", 'artist' : "Humble Pie", 'catname' : "cat1", 'filesize' : 4337426, 
		'filetype' : ".mp3", 'album' : "Humble Pie", 'largethumb_size' : 5987, 'smallthumb_size' : 4176,
		'albumartPath' : "/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/folder.jpg",
		'httpmusicpath' : "http://192.168.1.142/Music/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/06_-_Humble_Pie_-_Humble_Pie_-_Natural_Born_Bugie.mp3",
		'artistid' : "28efd8e7756c4c2c894df13b1530e596", 'albumid' : "f86ab4716fe5409f95a6b746dd006083", 
		'sthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHR",
		'lthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRof", 
		
	},
	{
		'NoTagArt' : 1, 'song' : "Honky Tonk Women", 'songid' : "e54834feeef6449ca0ba7842a7e7257e", 'track' : "10", 
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie",
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/10_-_Humble_Pie_-_Humble_Pie_-_Honky_Tonk_Women.mp3", 
		'programPath' : "/usr/share/ampnado", 'artist' : "Humble Pie", 'catname' : "cat1", 'filesize' : 7117275, 
		'filetype' : ".mp3", 'album' : "Humble Pie", 'largethumb_size' : 5986, 'smallthumb_size' : 4176,
		'albumartPath' : "/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/folder.jpg",
		'httpmusicpath' : "http://192.168.1.142/Music/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/10_-_Humble_Pie_-_Humble_Pie_-_Honky_Tonk_Women.mp3",
		'artistid' : "28efd8e7756c4c2c894df13b1530e596", 'albumid' : "f86ab4716fe5409f95a6b746dd006083", 
		'sthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHR",
		'lthumbnail' : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRof", 
	},
]

DS_TAGS_ALL_RESULTS = {
	'filename': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/01_-_Gary_Puckett_And_The_Union_Gap_-_Gary_Puckett_-_Young_Girl.mp3', 
	'dirpath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett', 'programPath': '/usr/share/ampnado', 'song': 'Young Girl', 
	'albumartPath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/folder.jpg', 'filesize': 3773516, 'filetype': '.mp3', 
	'artist': 'Gary Puckett And The Union Gap', 'httpmusicpath': 'http://192.168.1.142/Music/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/01_-_Gary_Puckett_And_The_Union_Gap_-_Gary_Puckett_-_Young_Girl.mp3', 
	'smallthumb_size': 2984, 'artistid': '16243618e8f74436a28760c4b986fd81', 'catname': 'cat1', 'NoTagArt': 1, 'lthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC', 
	'albumid': 'c1dd0a3134e344a6b23493a55f83856f', 'sthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcp', 'track': '01', 'album': 'Gary Puckett', 
	'songid': 'c2c96e01a93945f2a440b59db68013f3', 'largethumb_size': 5855,
}

DS_TAGS_DISTINCT_ALBUMARTPATH_RESULT = [
	'/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/folder.jpg',
 	'/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/folder.jpg',
 	'/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/folder.jpg',
 	'/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/folder.jpg',
]

DS_TAGS_DISTINCT_ALBUMID = [
	'c1dd0a3134e344a6b23493a55f83856f', 'e703dd2b413947e99406fee1ba799c04', '674b858949c84d7790753959b8c0ee1c',
	'f86ab4716fe5409f95a6b746dd006083',
]

DS_TAGS_DISTINCT_ARTIST = [
	'Gary Puckett And The Union Gap', 'Groove Coverage', 'Great White', 'Humble Pie',
]

DS_TAGS_DISTINCT_ALBUM = ['Gary Puckett', 'Groove Coverage', 'Great White', 'Humble Pie']

DS_TAGS_DISTINCT_SONG = ['Young Girl', 'Moonlight Shadow', 'The Angel Song', 'Natural Born Bugie', 'Honky Tonk Women']

DS_TAGS_ALL_TAGS = [
	{
		'sthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcp', 
		'track': '01', 'artist': 'Gary Puckett And The Union Gap', 'filetype': '.mp3', 'albumid': 'c1dd0a3134e344a6b23493a55f83856f', 
		'lthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC', 
		'programPath': '/usr/share/ampnado', 'songid': 'c2c96e01a93945f2a440b59db68013f3', 
		'filename': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/01_-_Gary_Puckett_And_The_Union_Gap_-_Gary_Puckett_-_Young_Girl.mp3', 
		'album': 'Gary Puckett', 'song': 'Young Girl', 'filesize': 3773516, 'largethumb_size': 5855,
		'dirpath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett', 'catname': 'cat1', 'NoTagArt': 1, 
		'httpmusicpath': 'http://192.168.1.142/Music/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/01_-_Gary_Puckett_And_The_Union_Gap_-_Gary_Puckett_-_Young_Girl.mp3', 
		'smallthumb_size': 2984, 'artistid': '16243618e8f74436a28760c4b986fd81', 
		'albumartPath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/folder.jpg', 
		
	},
	{
		'filetype': '.mp3', 'track': '01', 'artist': 'Groove Coverage', 'sthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQ', 
		'albumid': 'e703dd2b413947e99406fee1ba799c04', 'lthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQg', 'programPath': '/usr/share/ampnado', 'songid': 'e544e219ff904a14a5470f76544f19ec', 
		'filename': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/01_-_Groove_Coverage_-_Groove_Coverage_-_MoonLight_Shadow.mp3', 'album': 'Groove Coverage', 
		'dirpath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage', 'catname': 'cat1', 'NoTagArt': 1, 
		'httpmusicpath': 'http://192.168.1.142/Music/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/01_-_Groove_Coverage_-_Groove_Coverage_-_MoonLight_Shadow.mp3', 'smallthumb_size': 2038, 
		'artistid': 'a3b08d94af6e41be821eb234526964aa', 'albumartPath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/folder.jpg', 
		'song': 'Moonlight Shadow', 'filesize': 2640869, 'largethumb_size': 3283,
	},
	{
		'filetype': '.mp3', 'track': '01', 'artist': 'Great White', 'sthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBk', 
		'albumid': '674b858949c84d7790753959b8c0ee1c', 'artistid': 'ff312b038cde41f79ea15ab00b60f9d1', 
		'lthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw', 'programPath': '/usr/share/ampnado', 'songid': '7ba4163b39ec467aa4a531b4930b8be1', 
		'filename': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/01_-_Great_White_-_Great_White_-_The_Angel_Song.mp3', 'album': 'Great White', 
		'dirpath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white', 'catname': 'cat1', 'NoTagArt': 1, 
		'httpmusicpath': 'http://192.168.1.142/Music/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/01_-_Great_White_-_Great_White_-_The_Angel_Song.mp3', 'smallthumb_size': 4050,
		'albumartPath': '/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/folder.jpg', 'song': 'The Angel Song', 'filesize': 4552532, 'largethumb_size': 13612,
	},
	{
		'filetype': '.mp3', 'track': '6', 'artist': 'Humble Pie', 
		'sthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHR', 'albumid': 'f86ab4716fe5409f95a6b746dd006083', 
		'lthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRof', 'programPath': '/usr/share/ampnado', 'songid': '826ce048d8714d1f9a5648ee6b69410e', 
		'filename': '/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/06_-_Humble_Pie_-_Humble_Pie_-_Natural_Born_Bugie.mp3', 
		'album': 'Humble Pie', 'largethumb_size': 5987,'smallthumb_size': 4176, 'artistid': '28efd8e7756c4c2c894df13b1530e596', 
		'dirpath': '/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie', 'catname': 'cat1', 'NoTagArt': 1, 
		'httpmusicpath': 'http://192.168.1.142/Music/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/06_-_Humble_Pie_-_Humble_Pie_-_Natural_Born_Bugie.mp3', 
		'albumartPath': '/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/folder.jpg', 'song': 'Natural Born Bugie', 'filesize': 4337426,
		
	},
	{
		'largethumb_size': 5987, 'filetype': '.mp3', 'track': '10', 'artist': 'Humble Pie', 
		'sthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHR', 'albumid': 'f86ab4716fe5409f95a6b746dd006083', 
		'lthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRof', 'programPath': '/usr/share/ampnado', 
		'songid': 'e54834feeef6449ca0ba7842a7e7257e', 'artistid': '28efd8e7756c4c2c894df13b1530e596',
		'filename': '/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/10_-_Humble_Pie_-_Humble_Pie_-_Honky_Tonk_Women.mp3', 
		'album': 'Humble Pie', 'filesize': 7117275, 'largethumb_size': 5986, 'smallthumb_size': 4176,
		'dirpath': '/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie', 'catname': 'cat1', 'NoTagArt': 1, 
		'httpmusicpath': 'http://192.168.1.142/Music/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/10_-_Humble_Pie_-_Humble_Pie_-_Honky_Tonk_Women.mp3', 
		'albumartPath': '/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/folder.jpg', 'song': 'Honky Tonk Women', 
		
	},
]

DS_TAGS_ALL_LTHUMB_SIZE = [
	{'largethumb_size': 5855}, {'largethumb_size': 3283}, {'largethumb_size': 13612}, 
	{'largethumb_size': 5987}, {'largethumb_size': 5986},
]

DS_TAGS_ALL_STHUMB_SIZE = 	[
	{'smallthumb_size': 2984}, {'smallthumb_size': 2038}, {'smallthumb_size': 4050}, 
	{'smallthumb_size': 4176}, {'smallthumb_size': 4176},
]

DS_TAGS_ALL_FILESIZE = [
	{'filesize': 3773516}, {'filesize': 2640869}, {'filesize': 4552532}, {'filesize': 4337426}, 
	{'filesize': 7117275},
]

DS_TAGS_ALL_SONG = [
	{'song': 'The Angel Song', 'songid': '7ba4163b39ec467aa4a531b4930b8be1'},
]

DS_TAGS_ALL_SONG_SONGID_ARTIST = [
	{'song': 'Young Girl', 'songid': 'c2c96e01a93945f2a440b59db68013f3', 'artist': 'Gary Puckett And The Union Gap'}, 
	{'song': 'Moonlight Shadow', 'songid': 'e544e219ff904a14a5470f76544f19ec', 'artist': 'Groove Coverage'}, 
	{'song': 'The Angel Song', 'songid': '7ba4163b39ec467aa4a531b4930b8be1', 'artist': 'Great White'}, 
	{'song': 'Natural Born Bugie', 'songid': '826ce048d8714d1f9a5648ee6b69410e', 'artist': 'Humble Pie'}, 
	{'song': 'Honky Tonk Women', 'songid': 'e54834feeef6449ca0ba7842a7e7257e', 'artist': 'Humble Pie'}
]

DS_TAGS_ALL_FILENAME_ARTIST_ALBUM_SONG = [
	('/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/gary.puckett/gary.puckett/01_-_Gary_Puckett_And_The_Union_Gap_-_Gary_Puckett_-_Young_Girl.mp3', 'Gary Puckett And The Union Gap', 'Gary Puckett', 'Young Girl'), 
	('/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/groove.coverage/groove.coverage/01_-_Groove_Coverage_-_Groove_Coverage_-_MoonLight_Shadow.mp3', 'Groove Coverage', 'Groove Coverage', 'Moonlight Shadow'), 
	('/usr/share/ampnado/static/MUSIC/cat1/254c8e8f3d6c4f458b5f9b436e1a1072/great.white/great.white/01_-_Great_White_-_Great_White_-_The_Angel_Song.mp3', 'Great White', 'Great White', 'The Angel Song'), 
	('/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/06_-_Humble_Pie_-_Humble_Pie_-_Natural_Born_Bugie.mp3', 'Humble Pie', 'Humble Pie', 'Natural Born Bugie'), 
	('/usr/share/ampnado/static/MUSIC/cat1/d50f82e775f440e6ae230949f1d86b14/humble.pie/humble.pie/10_-_Humble_Pie_-_Humble_Pie_-_Honky_Tonk_Women.mp3', 'Humble Pie', 'Humble Pie', 'Honky Tonk Women'),
]

DS_FONE_TAGS_ALBUMID = {
	'albumid': 'c1dd0a3134e344a6b23493a55f83856f', 'album': 'Gary Puckett', 
	'artistid': '16243618e8f74436a28760c4b986fd81', 'artist': 'Gary Puckett And The Union Gap', 
	'sthumbnail': 'data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcp',
}

DS_FONE_TAGS_ARTIST = {'artistid': '28efd8e7756c4c2c894df13b1530e596'}

DS_FONE_TAGS_ALBUM = {'albumid': 'e703dd2b413947e99406fee1ba799c04'}

DS_TAGS_AGGREGATE_ARTIST = [{'albumz': ['Humble Pie'], '_id': 'album'}]

DS_TAGS_AGGREGATE_ALBUMID = [{'_id': 'song', 'songz': ['Young Girl']}]

DS_TAGS_AGGREGATE_FILESIZE = 22421618

VIDEO_DEFAULT = [
	{
		'catname' : 'cat1', 'filesize' : 1328562128, 'vid_name' : "Avengers Grimm", 'vid_id' : "19e9049268184acea6087eaeb165ac88",
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video", 
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4", 
		'vid_playpath' : "Music/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4", 
		'vid_poster_string' : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD",
	},
	{
		'catname' : 'cat1', 'filesize' : 1713875628, 'vid_id' : "d0bde21c4ccf425faa1fb3a85aa697cd", 
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video", 
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Captain.America.The.First.Avenger.mp4", 
		'vid_name' : "Captain America The First Avenger", 
		'vid_playpath' : "Music/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Captain.America.The.First.Avenger.mp4", 
		'vid_poster_string' : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAACXBIWXMAAAsTA",
	},
	{
		'catname' : 'cat1', 'filesize' : 854881878, 'vid_id' : "68e78a6387aa4ab686334c191e146bef",
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/a6b7bf893c7f4598a3e4d18f71ca7bdb/Video", 
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/a6b7bf893c7f4598a3e4d18f71ca7bdb/Video/San.Andreas.2015.720p.BluRay.x264.YIFY.mp4", 
		'vid_name' : "San Andreas 2015 720p Bluray X264 Yify", 
		'vid_playpath' : "Music/cat1/a6b7bf893c7f4598a3e4d18f71ca7bdb/Video/San.Andreas.2015.720p.BluRay.x264.YIFY.mp4", 
		'vid_poster_string' : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAACXBIWXMAAAsTAAALEwEAmpwYA",
	},
	{
		'catname' : 'cat1', 'filesize' : 912696674, 'vid_id' : "63b8c90fc5884046b54c81e13d048bbf", 
		'dirpath' : "/usr/share/ampnado/static/MUSIC/cat1/a6b7bf893c7f4598a3e4d18f71ca7bdb/Video", 
		'filename' : "/usr/share/ampnado/static/MUSIC/cat1/a6b7bf893c7f4598a3e4d18f71ca7bdb/Video/Jurassic.World.2015.720p.BluRay.x264.YIFY.mp4", 
		'vid_name' : "Jurassic World 2015 720p Bluray X264 Yify", 
		'vid_playpath' : "Music/cat1/a6b7bf893c7f4598a3e4d18f71ca7bdb/Video/Jurassic.World.2015.720p.BluRay.x264.YIFY.mp4", 
		'vid_poster_string' : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAACXBIWXMAAAsTAAALEwEA",
	},
]

DS_VIDEO_DISTINCT_VID_NAME = ['Avengers Grimm', 'Captain America The First Avenger', 
	'San Andreas 2015 720p Bluray X264 Yify', 'Jurassic World 2015 720p Bluray X264 Yify',
]

DS_STATS_DEFAULT = {
	'total_albums' : 103, 'total_videos' : 0, 'total_songs' : 622, 'total_pic_size' : "10.29M",
	'total_video_size' : "0.00b", 'total_ogg' : 12, 'total_artists' : 59, 'total_mp3' : 618, 
	'total_music_size' : "3.62G", 'total_disk_size' : "3.63G",
}








ARTALPHA_DEFAULT = {"artalpha" : ["1", "2"]}

ALBALPHA_DEFAULT = {"albalpha" : ["1", "2", "3"]}

SONGALPHA_DEFAULT = {"songalpha" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}




VIEWSDB_DEFAULT = [
	{
		"thumbnail" : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgLDBkSEw", 
		"songs" : [ 
			[ [ "Something Wicked This Way Comes", "5c6b715d98a8478195b1a1724770358c" ] ],
		], 
		"album" : "Harry Potter", "albumid" : "94499fc273504efeb89f82fec498b56c", 
		"artistid" : "aa6ab32503744863975e52e06af43e42", "numsongs" : 1, "artist" : "Harry Potter",
		"page" : "1",
	},
	{
		"thumbnail" : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgAAhEBAx", 
		"songs" : [ 
			[ [ "Look Where We Are", "7a22496158514faa9657254ea77ca9df" ] ], 
			[ [ "The First of Me", "224d30b6b2ca4340b4367945e2eb9225" ] ], 
			[ [ "More than a Memory", "7119088d6f4e45928b5cb7ed1f6ebd15" ] ], 
			[ [ "Born to Lead", "1628d775f22043309d8cb1739add3f9d" ] ], 
			[ [ "Moving Forward", "dfa6f6b014684fbab10f907887d8dd15" ] ], 
			[ [ "The Rules", "fcb33f1777dc452092dba7454bc72b61" ] ], 
			[ [ "Don't Tell Me", "7fc8052a3eb14e4baa2c4a64c7195b2d" ] ], 
			[ [ "If I Were You", "2994b727a56945228e6ccbb7c9ea06a4" ] ], 
			[ [ "Inside of You", "0007c1ed231245be820a5f7aa20d80c5" ] ], 
			[ [ "Without a Fight", "5e796e8a36954f8bab8857290c11f60d" ] ], 
			[ [ "Say the Same", "5e3972351a294b46b9209ca2d9448dc0" ] ], 
			[ [ "Good Enough", "285ba3d245884cbe9f3116caee4bc47e" ] ], 
			[ [ "If Only", "5f21ea6e077f42038a3c87a2401d7bc0" ] ],
		], 
		"album" : "Every Man for Himself", "albumid" : "81243eb55c6841b8aab1cfbf71b22d76", 
		"artistid" : "1408ba9b774d4223b5f5f63ad7ab2d2c", "numsongs" : 13, "artist" : "Hoobastank", 
		"page" : "1"
	},
	{ 
		"thumbnail" : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBBkSE", 
		"songs" : [ 
			[ [ "You Make My Dreams Come True", "b69d0672329c422f9f39eab5130f68b1" ] ], 
			[ [ "Private Eyes", "21bd2a0fb28d4408bfb0567a00fe9f85" ] ], 
			[ [ "Shes Gone", "fb72d5b7558548fd9a396dbecee972f4" ] ], 
			[ [ "Maneater", "aac88b39c3fb42649fc872d62b6882b8" ] ], 
			[ [ "I'll Be Around", "7722c9c80b634733993346d2d9e03b73" ] ], 
			[ [ "Everytime You Go Away", "61f0ca5ccacf4af488fe48d475d4d3b2" ] ], 
			[ [ "Your Kiss Is on My List", "336e1063533d476eb7a9fab7ed56f004" ] ], 
			[ [ "Rich Girl", "a9e2877f5e8d4e3a9df4921e965194a3" ] ], 
			[ [ "Method of Modern Love", "7748aa36486940dd92c0b63802a49f9d" ] ], 
			[ [ "Out of Touch", "4d16989bc52b4831b20ccafa8fe5f5b8" ] ], 
			[ [ "Sara Smile", "bbb9034c906b4dac9d97ce40c85bb9ac" ] ], 
			[ [ "You Lost that Lovin Feeling", "e1cbbafa0ef143c8b8b5b355a2610ed5" ] ], 
			[ [ "Say It Isnt So", "dc152574f5ff4b7093ca1d1f5a261102" ] ],
		], 
		"album" : "Hall and Oates", "albumid" : "231f62e7df2d42a6a66613fe6a681775", 
		"artistid" : "5ed5a2bd573e441b9260f9240554932f", "numsongs" : 13, "artist" : "Hall And Oates", 
		"page" : "1",
	},
	{
		"thumbnail" : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQDBk", 
		"songs" : [ 
			[ [ "A Haunted House", "6df53d5f4fd24c6ca5982c87cb79fc8d" ] ],
		], 
		"album" : "Nightmarish Noise for Hallowee", "albumid" : "b205ba0015e74fe5b2c36b04d636b52e", 
		"artistid" : "00d62cb83db5405ba76c974c2fa8035a", "numsongs" : 1, "artist" : "Scary Sound Effects", 
		"page" : "1",
	},
	{
		"thumbnail" : "data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBLDBk", 
		"songs" : [ 
			[ [ "Hare Krishna Hare Ram", "d8f0f033b632413b9a6f9fc907d0cfda" ] ],
		], 
		"album" : "Bhool Bhulaiyaa", "albumid" : "3ac022aab18248848c5e3dac350857a2", 
		"artistid" : "451b18fbc3d6458e849fe8d365605c05", "numsongs" : 1, "artist" : "Bhool Bhulaiyaa", 
		"page" : "1",
	}
]





ARTISTVIEW_DEFAULT = [
	{
		"artistid" : "bda79e620ca44cf7a9528fd5f32859db", "artist" : "Forty Foot Echo", 
		"albums" : [ [ "Forty Foot Echo", "b70da3b08b9c4856855db2b863a3fca4" ] ], "page" : "1",
	},
	{
		"artistid" : "ba532eac90c34752a6c2d3e7c8cbb711", "artist" : "The Flaming Lips", "page" : "1",
		"albums" : [ 
			[ "The Dark Side of the Moon", "4933564edfe64f2fbdc803d6f974fa80" ], 
			[ "Yoshimi Battles the Pink Robots", "de2fe89faecf4c6c9b78c9cc5db3eb07" ],
		],
	},
	{
		"artistid" : "19e373fbfc784c4e8df7d37965186153", "artist" : "Faster Pussycat", 
		"albums" : [ [ "Faster Pussycat", "b494f0c268de42a4ba0f07406bba423b" ] ], "page" : "1",
	},
	{
		"artistid" : "d943dae862a24862bf04292ca61d884c", "artist" : "Hoobastank", "page" : "1",
		"albums" : [ 
			[ "The Reason", "20258558969e4f7a8382a3b7e3023d6f" ], 
			[ "Every Man for Himself", "390a13fbe44240dca99e88f098117943" ], 
			[ "Hoobastank", "5b1f136a195647f9b88ac2717d5f2e00" ],
		],
	},
	{
		"artistid" : "36e20aac998d45478552472aad1fb5b0", "artist" : "Flobots", 
		"albums" : [ [ "Fight with Tools", "c8b63804eff14a9d8aac319b6489d3ee" ] ], "page" : "1",
	},
]



VIEWSDB_ARTISTVIEW_INSERT = [
	('94499fc273504efeb89f82fec498b56c', '1'), 
	('81243eb55c6841b8aab1cfbf71b22d76', '1'), 
	('231f62e7df2d42a6a66613fe6a681775', '1'), 
	('b205ba0015e74fe5b2c36b04d636b52e', '1'), 
	('3ac022aab18248848c5e3dac350857a2', '1'),
]








RANDTHUMB_DEFAULT = [
	{
		"displayed" : "NOTSHOWN", 
		"chunk" : [
			"d5533d406f3e4f1cb600f2f03154eb21", 
			"e2b1da5cbaae48f4971500605e8e243f", 
			"4180b6430fb2443fa1de010fb11e8a4f", 
			"07d4cbe4bc25425b9a5959025f0f31fa", 
			"ffff5ce2aeb94571b979e1dc7f7aa05d",
		],
	},
	{
		"displayed" : "NOTSHOWN", 
		"chunk" : [
			"23db2fbec6c14261944aed2099e2da6a", 
			"a4769dff9c514ba882c51ffb3ace9c9d", 
			"f849310e40a14835ac9603dfbc5d0aea", 
			"988461d9df5f40eb882dfb60bd3b663b", 
			"881796dcd27b4aaea76ad81bf36cdf4a",
		],
	},
	{
		"displayed" : "NOTSHOWN", 
		"chunk" : [
			"1fef173c3e7c4b8f814917b881df8657", 
			"254a0ca0d84b4b89b39994ea18d6a450", 
			"eaa080a808a046f0abf933dfc0471635", 
			"109a2d52e69c4719bef0f16e4f6631cf", 
			"c8bc73ac535f43e68d0a8e5ebbc670a5",
		],
	},
	{
		"displayed" : "NOTSHOWN", 
		"chunk" : [
			"5c77a29c30cf4384bcf4340011c5f99a", 
			"97ed92d31e0d4ad4b5aef18d9ee0aeb6", 
			"c185dcd5246b45ecbf685c2b1a770eba", 
			"b9ae0c02a918470288f7613128aba64c", 
			"3d91ebf4240c4cf8a83791b50b060313",
		],
	},
	{
		"displayed" : "NOTSHOWN", 
		"chunk" : [
			"cd6f90fe736640a4963271981dc08356", 
			"22d7f34d7b4349658351f6ece4a82a56", 
			"b77e77bf4fbd467dbe588b766f6a47d6", 
			"2e5bceb6431842fda447c782d31fee53", 
			"685a293e463d44a3b4eea53c15c378eb",
		],
	},
]



