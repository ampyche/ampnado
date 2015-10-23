/*
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
*/

jQuery(function ($) {
	$('#playlistLoadBtn, #playlistLoadBtn1').on('click', function () {
		plname = JSON.parse(localStorage.getItem("currentSelected_PLAYLIST_PLAYLISTID"));
		$.get("CreatePlayerPlaylist",
		{
			"playlistid": plname.playlistid
		},
		function (data) {
			$.each(data, function (key, val) {
				$.mobile.loading("hide");
				tracks = val;
				var supportsAudio = !!document.createElement('audio').canPlayType;
				if(supportsAudio) {	
					index = 0,
					playing = false;
					mediaPath = '/Music',
					extension = '',
					trackCount = tracks.length,
					audio = $('#audio1').bind('play', function () {
						playing = true;
					}).bind('pause', function () {
						playing = false;
					}).bind('ended', function () {
						if ((index +1) < trackCount) {
							index++;
							loadTrack(index);
							audio.play();
						} else {
							audio.pause();
							index = 0;
							loadTrack(index);
						}
					}).get(0),
					btnPrev = $('.plprevButton').click(function () {
						if((index - 1) > -1) {
							index--;
							loadTrack(index);
							if(playing) {
								audio.play();
							}
						} else {
							audio.pause();
							index = 0;
							loadTrack(index);
						} 
					}),
					btnNext = $('.plnextButton').click(function () {
						if((index + 1) < trackCount) {
							index++;
							loadTrack(index);
							if(playing) {
								audio.play();
							}
						} else {
							audio.pause();
							index = 0;
							loadTrack(index);
						}
					}),
					loadTrack = function (id) {
						art = tracks[id].thumbnail;
						$('#playlistalbart').attr('src', art);
						$('.fraz').attr('src', art);
						$('#pictext').text(tracks[id].name);
						$('#pictext2').text(tracks[id].album);
						index = id;
						audio.src = mediaPath + tracks[id].file + extension;
					},
					playTrack = function (id) {
						loadTrack(id);
						audio.play();
					};
					if(audio.canPlayType('audio/ogg')) {
						extension = '.ogg';
					}
					if(audio.canPlayType('audio/mp3')) {
						extension = '.mp3';
					}
					loadTrack(index);
				}
			});
		});
	});
});
