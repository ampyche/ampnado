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
function iArtist1P1Fun1(d0) {
	var art1 = "<div><img class='artistimgS' src='" + d0.getimgsonalb.thumbnail + "'></img>";
	var art2 = art1 + "</div><div class='art1divS'><ul class='artistSongULS' data-role='listview' ";
	var art3 = art2 + "data-inset='true' data-split-icon='gear'>";
	return art3
};
function iArtist1P1Fun2(d1) {
	var arttwo = "<li class='artSongLIS'><a href='#' class='artsongA1' ";
	var artthree = arttwo + "data-songid='" + d1[1] + "'>" + d1[0] + "</a><a ";
	var artfour = artthree + "href='#artistselectplpage' class='artToPlaylistBtn' ";
	var artfive = artfour + "data-song='" + d1[0] + "' data-songid='" + d1[1] + "' ";
	var art = artfive + "data-transition='slidefade'></a></li>";
	return art
};
function iArtist1P1Fun3(d2) {
	var artA = "<div class='artistPageDiv' data-role='collapsible'><h4>" + d2.artist + "</h4><div>";
	var artB = artA + "<form id='" + d2.artistid + "' class='artistForm'><div class='ui-field-contain'>";
	var artc = artB + "<select name='" + d2.artist + "' id='" + d2.artistid + "' class='artistselect'>";
	return artc	
};
function intitArtist1P1() {
	$.get('GetInitialArtistInfo', function (data) {
		$.each(data.ia, function ( key, val ) {
			if ( val.albums.length === 1 ) {
				var abc = "<div class='artistPageDivS' data-role='collapsible'><h4>" + val.artist + "</h4>";
				var selected = val.albums[0][1];
				$.get('GetImageSongsForAlbum',
					{
						'selected' : selected //this is albumid	
					},
					function (data) {
						var art3 = iArtist1P1Fun1(data);
						var liString = '';
						$.each(data.getimgsonalb.songs, function (kk, vv) {
							liString = liString + iArtist1P1Fun2(vv);
							return liString;
						})
						var result2 = abc + art3 + liString + "</ul></div>";
						$('#artistmain').append(result2);
				});
			} else {
				var artC = iArtist1P1Fun3(val);
				var a2 = '';
				var a3 = '';
				var aa1 = "<option class='artop0' value='Choose Album'>Choose Album</option>";
				$.each(val.albums, function (k, v) {
					var a1 = "<option class='artop1' value='" + v[1] + "'>" + v[0] + "</option>";
					a2 = a2 + a1;
					a3 = aa1 + a2;
					return a3
				})
				var result = artC + a3 + "</select></div></form></div>";
				$('#artistmain').append(result);
			}
		});
		$('.artistPageDivS, .artistPageDiv').collapsible().trigger('create');
		$.mobile.loading("hide");
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function initAlbum1P1Fun1(c0) {
	var alb1 = "<div class='albumDIV'><ul class='albumUL' data-role='listview' data-inset='true'>";
	var alb2 = alb1 + "<li class='albumLI'><a href='#' class='albumA1' data-artist='" + c0.artist + "' ";
	var alb3 = alb2 + "data-artistid='" + c0.artistid + "' data-album='" + c0.album + "' ";
	var alb4 = alb3 + "data-albumid='" + c0.albumid + "'><img id='" + c0.albumid + "' ";
	var alb5 = alb4 + "src='" + c0.thumbnail + "'><h3 id='albH3'>" + c0.album + "</h3>";
	var alb6 = alb5 + "<p>" + c0.artist + "</p><span class='ui-li-count'>" + c0.numsongs + "</span>";
	var alb7 = alb6 + "</a></li></ul></div><div class='albsongList'><ul id='albsongUL" + c0.albumid + "' ";
	var alb = alb7 + "class='albsongUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
	return alb
};
function initAlbum1P1Fun2(c1) {
	var albab = "<li class='albsongsLI'><a href='#' class='albsongsA' data-song='" + c1[0] + "' ";
	var albab1 = albab + "data-songid='" + c1[1] + "'>" + c1[0] + "</a><a href='#albumselectplpage' ";
	var albab2 = albab1 + "class='addToPlaylist' data-pageid='albums' data-song='" + c1[0] + "' ";
	var albab33 = albab2 + "data-songid='" + c1[1] + "' data-transition='slidefade'></a></li>";	
	return albab33
};
function initAlbum1P1() {
	$.get('GetInitialAlbumInfo', function (data) {
		$.each(data.ial, function (key, val) {		
			var alb8 = initAlbum1P1Fun1(val)
			var alba3 = '';
			$.each(val.songs, function (k, v) {
				$.each(v, function (ke, va) {
					var albab3 = initAlbum1P1Fun2(va);
					alba3 = alba3 + albab3;
					return alba3
				});
			});
			var result = alb8 + alba3 + "</ul></div>";
			$('#alblist').append(result);
			$('#albsongUL' + val.albumid).hide();
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function initSong1P1Fun1(e1) {
	var s1 = "<li class='songs_li'><a class='songname' href='#' data-songid='" + e1.songid + "'>";
	var s2 = s1 + "<h2>" + e1.song + "</h2><h6>" + e1.artist + "</h6></a><a href='#selectplpage' ";
	var s3 = s2 + "data-pageid='songs' data-song='" + e1.song + "' data-songid='" + e1.songid + "' ";
	var s = s3 + "class='addtoplaylist' data-transition='slidefade'></a></li>";
	return s
};
function initSong1P1() {
	$.get('GetInitialSongInfo', function (data) {
		$.each(data.ias, function ( key, val) {
			var s4 = initSong1P1Fun1(val);
			$("#songs_view").append(s4);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function initGetAllPlaylistsFun1(f0) {
	var pl1 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	var pl11 = pl1 + "ui-btn-icon-right' data-playlistid='" + f0[1] + "'>" + f0[0] + "</a></li>";
	return pl11
};
function initGetAllPlaylistsFun2(f1) {
	var pl3 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	var pl44 = pl3 + "ui-btn-icon-right'>" + f1 + "</a></li>";
	return pl44
};
function initGetAllPlaylistsFun3(f2) {
	var spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ui-icon-bullets ";
	var spl2 = spl1 + "ui-btn-icon-right ui-corner-all' data-textonly='false' data-textvisible='false' ";
	var spl33 = spl2 + "data-msgtext=''>" + f2 + "</a></li>";
	return spl33	
};
function initGetAllPlaylistsFun4(f3) {
	var albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg";
	var albspl2 = albspl1 + " ui-btn ui-btn-mini ui-icon-bullets ui-btn-icon-right ui-corner-all'";
	var albspl33 = albspl2 + " data-textonly='false' data-textvisible='false' data-msgtext=''>" + f3 + "</a></li>";
	return albspl33
};
function initGetAllPlaylistsFun5(f4) {
	var artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg";
	var artspl2 = artspl1 + " ui-btn ui-btn-mini ui-icon-bullets ui-btn-icon-right ui-corner-all'";
	var artspl33 = artspl2 + " data-textonly='false' data-textvisible='false' data-msgtext=''>" + f4 + "</a></li>";
	return artspl33
};
function initGetAllPlaylists() {
	$.get('GetAllPlaylists', function (data) {
		localStorage.setItem('playlists', JSON.stringify(data));
		var plone = '';
		var spl = '';
		var albspl='';
		var artspl='';
		$('#playPlaylistUL').empty();
		$.each(data, function (key, val) {
			if (val != "Please create a playlist") {
				$.each(val, function (k, v) {
					var pl2 = initGetAllPlaylistsFun1(v);
					plone = plone + pl2;
					return plone;
				})
			} else {
				var pl4 = initGetAllPlaylistsFun2(val);
				plone = plone + pl4;
				return plone;
			}
		})
		$.each(data, function (k, v) {
			var spl3 = initGetAllPlaylistsFun3(v);
			var albspl3 = initGetAllPlaylistsFun4(v);
			var artspl3 = initGetAllPlaylistsFun5(v);
			spl = spl + spl3
			albspl = albspl + albspl3;
			artspl = artspl + artspl3;
		})
		$('#playPlaylistUL').append(plone);
		$('#splUL').append(spl);
		$('#albsplUL').append(albspl);
		$('#artsplUL').append(artspl);
		$('#albsplUL, #splUL, #playPlaylistUL, #artsplUL').listview().trigger('refresh');
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function initAddOne(g1) {
	var one = g1 + 1;
	return one
};
function initGetArtistAlphaFun2(g2, g3) {
	var w1 = "<span id='artistOF" + g2 + "' "
	var w2 = w1 + "class='artOF show-page-loading-msg ui-btn ui-btn-mini ui-btn-inline ui-corner-all' ";
	var w33 = w2 + "data-textonly='false' data-textvisibility='false' data-msgtext=''>" + g3 + "</span>";
	return w33
};
function initGetArtistAlpha() {
	$.get('GetArtistAlpha', function (data) {
		$.each( data.artal, function (key, val) {
			var k = initAddOne(val);
			var w3 = initGetArtistAlphaFun2(k, val);
			$('#artistOFwrap').append(w3);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function initGetAlbumAlphaFun1(kk, cc) {
	var ww1 = "<span id='albumOF" + kk + "' ";
	var ww2 = ww1 + "class='albumOF show-page-loading-msg ui-btn ui-btn-mini ui-btn-inline ui-corner-all' ";
	var ww = ww2 + "data-textonly='false' data-textvisibility='false' data-msgtext=''>" + cc + "</span>";
	return ww
};
function initGetAlbumAlpha() {
	$.get('GetAlbumAlpha', function (data) {
		$.each(data.albal, function (ke, va) {
			var kk = initAddOne(ke);
			var ww3 = initGetAlbumAlphaFun1(kk, va);
			$('#albumOFwrap').append(ww3);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function initGetSongAlphaFun1(b) {
	var www1 = "<span id='songAlpaSpan' ";
	var www2 = www1 + "class='songOF show-page-loading-msg ui-btn ui-btn-mini ui-btn-inline ui-corner-all' ";
	var www333 = www2 + "data-textonly='false' data-textvisibility='false' data-msgtext=''>" + b + "</span>";
	return www333
};
function initGetSongAlpha() {
	$.get('GetSongAlpha', function (data) {
		$.each(data.songal, function (k2, vk) {
			var www3 = initGetSongAlphaFun1(vk);
			$('#songOFwrap').append(www3);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function initGetAllVideoFun1(a) {
	var v1 = "<div class='videolistViewDIV'>";
	var v2 = v1 + "<ul id='videolistViewUL' data-role='listview' data-split-icon='gear' data-inset='true'>";
	var v3 = v2 + "<li id='videolistViewLI'>";
	var v4 = v3 + "<a href='#vidplayer' id='videolistViewA' data-videoID='" + a.vid_id + "' ";
	var v5 = v4 + "data-vidAddr='" + a.vid_playpath + "'>";
	var v6 = v5 + "<img src='" + a.vid_poster_string + "'>" + a.vid_name;
	var vid = v6 + "</a></li></ul></div>";
	return vid
};
function initGetAllVideo() {
	$.get('GetAllVideo', function (data) {
		$.each(data.vlist, function (key, val) {
			var video = initGetAllVideoFun1(val);
			$('#vidDIV').append(video);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function calcDuration(d) {
	var hr = Math.floor(d / 3600);
	var min = Math.floor((d - (hr * 3600))/60);
	var sec = Math.floor(d - (hr * 3600) - (min * 60));	
	if (min < 10) { min = "0" + min; };
	if (sec < 10) { sec = '0' + sec; };
	return [min, sec];
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function blka(recm) {
	var ba1 = "<div class='ui-block-a' data-theme='a'>";
	var ba2 = ba1 + "<a href='#popup1' data-rel='popup' data-transition='pop'>";
	var ba3 = ba2 + "<img src='" + recm + "' class='PicGrid'>";
	var ba = ba3 + "</img></a></div>";
	return ba
};
function blkb(recm) {
	var bb1 = "<div class='ui-block-b' data-theme='a'>";
	var bb2 = bb1 + "<a href='#popup2' data-rel='popup' data-transition='pop'>";
	var bb3 = bb2 + "<img src='" + recm + "' class='PicGrid'>";
	var bb = bb3 + "</img></a></div>";
	return bb
};
function blkc(recm) {
	var bc1 = "<div class='ui-block-c' data-theme='a'>";
	var bc2 = bc1 + "<a href='#popup3' data-rel='popup' data-transition='pop'>";
	var bc3 = bc2 + "<img src='" + recm + "' class='PicGrid'>";
	var bc = bc3 + "</img></a></div>";
	return bc
};
function blkd(recm) {
	var bd1 = "<div class='ui-block-d' data-theme='a'>";
	var bd2 = bd1 + "<a href='#popup4' data-rel='popup' data-transition='pop'>";
	var bd3 = bd2 + "<img src='" + recm + "' class='PicGrid'>";
	var bd = bd3 + "</img></a></div>";
	return bd
};
function blke(recm) {
	var be1 = "<div class='ui-block-e' data-theme='a'>";
	var be2 = be1 + "<a href='#popup5' data-rel='popup' data-transition='pop'>";
	var be3 = be2 + "<img src='" + recm + "' class='PicGrid'>";
	var be = be3 + "</img></a></div>";
	return be
};
function creatPop1(recm) {
	var pu11 = "<ul id='pop1' data-role='listview' class='ui-content' data-insert='true'>"
	var pu12 = '';
	$.each(recm, function (key, val) {
		var s11 = "<li><a href='#' class='rart1' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu12 = pu12 + s11;
		return pu12
	})
	var pu111 = pu11 + pu12 + "</ul>";
	return pu111
};
function creatPop2(recm) {
	var pu21 = "<ul id='pop2' data-role='listview' class='ui-content' data-insert='true'>";
	var pu22 = '';
	$.each(recm, function (key, val) {
		var s22 = "<li><a href='#' class='rart2' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu22 = pu22 + s22;
		return pu22
	})
	var pu211 = pu21 + pu22 + "</ul>";
	return pu211
};
function creatPop3(recm) {
	var pu31 = "<ul id='pop3' data-role='listview' class='ui-content' data-insert='true'>";
	var pu32 = '';
	$.each(recm, function (key, val) {
		var s31 = "<li><a href='#' class='rart3' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu32 = pu32 + s31;
		return pu32
	})
	var pu311 = pu31 + pu32 + "</ul>";
	return pu311
};
function creatPop4(recm) {
	var pu41 = "<ul id='pop4' data-role='listview' class='ui-content' data-insert='true'>";
	var pu42 = '';
	$.each(recm, function (key, val) {
		var s41 = "<li><a href='#' class='rart4' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu42 = pu42 + s41
	})
	var pu411 = pu41 + pu42 + "</ul>";
	return pu411
};
function creatPop5(recm) {
	var pu51 = "<ul id='pop5' data-role='listview' class='ui-content' data-insert='true'>";	
	var pu52 = '';
	$.each(recm, function (key, val) {
		var s51 = "<li><a href='#' class='rart5' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu52 = pu52 + s51
	})
	var pu511 = pu51 + pu52 + "</ul>";
	return pu511
};

function initRandomPics() {
	$.get('RandomPics', function (data) {
		var result1 = blka(data.rsamp[0].thumbnail) + blkb(data.rsamp[1].thumbnail);
		var result2 = result1 + blkc(data.rsamp[2].thumbnail) + blkd(data.rsamp[3].thumbnail);
		var result = result2 + blke(data.rsamp[4].thumbnail);
		$('#popup1, #popup2, #popup3, #popup4, #popup5, #intropicGrid1').empty();
		$('#intropicGrid1').append(result);
		$('#popup1').append(creatPop1(data.rsamp[0].songs));
		$('#popup2').append(creatPop2(data.rsamp[1].songs));
		$('#popup3').append(creatPop3(data.rsamp[2].songs));
		$('#popup4').append(creatPop4(data.rsamp[3].songs));
		$('#popup5').append(creatPop5(data.rsamp[4].songs));
		$('#pop1, #pop2, #pop3, #pop4, #pop5').listview().trigger('refresh');
		$('#popup1, #popup2, #popup3, #popup4, #popup5').popup().trigger('create');
	});
};

function RandomPics() {
	$.get('RandomPics', function (data) {
		localStorage.setItem('nextimgset', JSON.stringify(data));
	});
};

function randomPicProcess() {
	var d = JSON.parse(localStorage.getItem('nextimgset'));
	var result1 = blka(d.rsamp[0].thumbnail) + blkb(d.rsamp[1].thumbnail);
	var result2 = result1 + blkc(d.rsamp[2].thumbnail) + blkd(d.rsamp[3].thumbnail);
	var result = result2 + blke(d.rsamp[4].thumbnail);
	$('#popup1, #popup2, #popup3, #popup4, #popup5, #intropicGrid1').empty();
	$('#intropicGrid1').append(result);
	$('#popup1').append(creatPop1(d.rsamp[0].songs));
	$('#popup2').append(creatPop2(d.rsamp[1].songs));
	$('#popup3').append(creatPop3(d.rsamp[2].songs));
	$('#popup4').append(creatPop4(d.rsamp[3].songs));
	$('#popup5').append(creatPop5(d.rsamp[4].songs));
	$('#pop1, #pop2, #pop3, #pop4, #pop5').listview().trigger('refresh');
	$('#popup1, #popup2, #popup3, #popup4, #popup5').popup().trigger('create');
};
///////////////////////////////////////////////////////////////////////////////
//////////////////////////// PLAYLIST PAGE STUFF //////////////////////////////
///////////////////////////////////////////////////////////////////////////////
//check a string for alpha-numeric characters only
function checkAlphaNums(anString) {
	var anRe = /^[\w]+$/;
	var anFound = anString.match(anRe);
	if (anFound != null){ 
		return true;
	} else {
		return false;
	}
};
//checks a sting for only numeric characters
function checkNums(numString) {
	var numRe = /^[0-9]*$/;
	var numFound = numString.match(numRe);
	if (numFound != null){
		return true;
	} else {
		return false;
	}
};
///////////////////////////////////////////////////////////////////////////////
//////////////////////////// END PLAYLIST PAGE STUFF //////////////////////////////
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
//////////////////////////// SETTINGS PAGE STUFF //////////////////////////
///////////////////////////////////////////////////////////////////////////////
function loadStats() {
	$('#statsTab').empty();
	$.get('GetStats', function ( data ) {
		var stattwo = "<tr><th>Total Artists</th><td>" + data.stats.total_artists + "</td></tr>";
		var statthree = "<tr><th>Total Albums</th><td>" + data.stats.total_albums + "</td></tr>";
		var statfour = "<tr><th>Total Songs</th><td>" + data.stats.total_songs + "</td></tr>";
		var statnine = "<tr><th>Total Videos</th><td>" + data.stats.total_videos + "</td></tr>";
		var statfive = "<tr><th>Music Lib Size</th><td>" + data.stats.total_music_size + "</td></tr>";
		var statseven = "<tr><th>Video Lib Size</th><td>" + data.stats.total_video_size + "</td></tr>";
		var stateight = "<tr><th>Total Disk Size</th><td>" + data.stats.total_disk_size + "</td></tr>";
		var stats = stattwo + statthree + statfour + statnine + statfive + statseven + stateight;
		$('#statsTab').append(stats);
	});
};
///////////////////////////////////////////////////////////////////////////////
//////////////////////////// END SETTINGS PAGE STUFF //////////////////////////
///////////////////////////////////////////////////////////////////////////////
var rpw;
function rpwStart() {
	rpw = setInterval(function () {RandomPics()}, 80000);
	rpw1 = setInterval(function () {randomPicProcess()}, 90000);
};
function rpwStop() {
	clearInterval(rpw);
	clearInterval(rpw1);
};
var initAmpyche = function () {
	initRandomPics();
	$('#audio2').show();
	//This hides the search boxes
	$('#controlGrid, #albSSD1, #albSSD2, #albListViewDIV2, #artForm, #SSD1, #SSD2, #songListViewDIV2').hide();
	RandomPics();
	rpwStart();
	intitArtist1P1();
	initAlbum1P1();
	initSong1P1();
	initGetAllPlaylists();
	initGetArtistAlpha();
	initGetAlbumAlpha();
	initGetSongAlpha();
	initGetAllVideo();
	loadStats();
};

$(window).load(initAmpyche)