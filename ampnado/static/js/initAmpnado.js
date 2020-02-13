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
const iArtist1P1Fun1 = (d0) => {
	let art1 = "<div><img class='artistimgS' src='" + d0.getimgsonalb.thumbnail + "'></img>";
	let art2 = art1 + "</div><div class='art1divS'><ul class='artistSongULS' data-role='listview' ";
	return art2 + "data-inset='true' data-split-icon='gear'>";
};

const iArtist1P1Fun2 = (d1) => {
	let arttwo = "<li class='artSongLIS'><a href='#' class='artsongA1' ";
	let artthree = arttwo + "data-songid='" + d1[1] + "'>" + d1[0] + "</a><a ";
	let artfour = artthree + "href='#artistselectplpage' class='artToPlaylistBtn' ";
	let artfive = artfour + "data-song='" + d1[0] + "' data-songid='" + d1[1] + "' ";
	return artfive + "data-transition='slidefade'></a></li>";
};

const iArtist1P1Fun3 = (d2) => {
	let artA = "<div class='artistPageDiv' data-role='collapsible'><h4>" + d2.Artist + "</h4><div>";
	let artB = artA + "<form id='" + d2.ArtistId + "' class='artistForm'><div class='ui-field-contain'>";
	let artc = artB + "<select name='" + d2.Artist + "' id='" + d2.ArtistId + "' class='artistselect'>";
	return artc	
};
const intitArtist1P1 = () => {
	$.get('InitialArtistInfo', (data) => {
		$.each(data.ia, ( key, val ) => {
			if ( val.Albums.length === 1 ) {
				let abc = "<div class='artistPageDivS' data-role='collapsible'><h4>" + val.Artist + "</h4>";
				let selected = val.Albums[0][1];
				$.get('ImageSongsForAlbum',
					{
						'selected' : selected //this is albumid	
					},
					(data) => {
						let art3 = iArtist1P1Fun1(data);
						let liString = '';
						$.each(data.getimgsonalb.songs, (kk, vv) => {
							return liString + iArtist1P1Fun2(vv);
						})
						let result2 = abc + art3 + liString + "</ul></div>";
						$('#artistmain').append(result2);
				});
			} else {
				let artC = iArtist1P1Fun3(val);
				let a2 = '';
				let a3 = '';
				let aa1 = "<option class='artop0' value='Choose Album'>Choose Album</option>";
				$.each(val.Albums, (k, v) => {
					let a1 = "<option class='artop1' value='" + v[1] + "'>" + v[0] + "</option>";
					a2 = a2 + a1;
					return aa1 + a2
				})
				let result = artC + a3 + "</select></div></form></div>";
				$('#artistmain').append(result);
			}
		});
		$('.artistPageDivS, .artistPageDiv').collapsible().trigger('create');
		$.mobile.loading("hide");
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const initAlbum1P1Fun1 = (c0) => {
	let alb1 = "<div class='albumDIV'><ul class='albumUL' data-role='listview' data-inset='true'>";
	let alb2 = alb1 + "<li class='albumLI'><a href='#' class='albumA1' data-artist='" + c0.Artist + "' ";
	let alb3 = alb2 + "data-artistid='" + c0.ArtistId + "' data-album='" + c0.Album + "' ";
	let alb4 = alb3 + "data-albumid='" + c0.AlbumId + "'><img id='" + c0.AlbumId + "' ";
	let alb5 = alb4 + "src='" + c0.AlbumArtHttpPath + "'><h3 id='albH3'>" + c0.Album + "</h3>";
	let alb6 = alb5 + "<p>" + c0.Artist + "</p><span class='ui-li-count'>" + c0.NumSongs + "</span>";
	let alb7 = alb6 + "</a></li></ul></div><div class='albsongList'><ul id='albsongUL" + c0.AlbumId + "' ";
	return alb7 + "class='albsongUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
};
const initAlbum1P1Fun2 = (c1) => {
	let albab = "<li class='albsongsLI'><a href='#' class='albsongsA' data-song='" + c1[0] + "' ";
	let albab1 = albab + "data-songid='" + c1[1] + "'>" + c1[0] + "</a><a href='#albumselectplpage' ";
	let albab2 = albab1 + "class='addToPlaylist' data-pageid='albums' data-song='" + c1[0] + "' ";
	return albab2 + "data-songid='" + c1[1] + "' data-transition='slidefade'></a></li>";
};
const initAlbum1P1 = () => {
	$.get('InitialAlbumInfo', (data) => {
		$.each(data.ial, (key, val) => {
			let alb8 = initAlbum1P1Fun1(val)
			let alba3 = '';
			$.each(val.Songs, (k, v) => {
				let albab3 = initAlbum1P1Fun2(v);
				return alba3 + albab3;
			});
			let result = alb8 + alba3 + "</ul></div>";
			$('#alblist').append(result);
			$('#albsongUL' + val.AlbumId).hide();
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const initSong1P1Fun1 = (e1) => {
	let s1 = "<li class='songs_li'><a class='songname' href='#' data-songid='" + e1.SongId + "'>";
	let s2 = s1 + "<h2>" + e1.Song + "</h2><h6>" + e1.Artist + "</h6></a><a href='#selectplpage' ";
	let s3 = s2 + "data-pageid='songs' data-song='" + e1.Song + "' data-songid='" + e1.SongId + "' ";
	return s3 + "class='addtoplaylist' data-transition='slidefade'></a></li>";
};
const initSong1P1 = () => {
	$.get('InitialSongInfo', (data) => {
		$.each(data.ias, ( key, val) => {
			let s4 = initSong1P1Fun1(val);
			$("#songs_view").append(s4);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const initGetAllPlaylistsFun1 = (f0) => {
	let pl1 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	return pl1 + "ui-btn-icon-right' data-playlistid='" + f0[1] + "'>" + f0[0] + "</a></li>";
};
const initGetAllPlaylistsFun2 = (f1) => {
	let pl3 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	return pl3 + "ui-btn-icon-right'>" + f1 + "</a></li>";
};
const initGetAllPlaylistsFun3 = (f2) => {
	let spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ui-icon-bullets ";
	let spl2 = spl1 + "ui-btn-icon-right ui-corner-all' data-textonly='false' data-textvisible='false' ";
	return spl2 + "data-msgtext=''>" + f2 + "</a></li>";
};
const initGetAllPlaylistsFun4 = (f3) => {
	let albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg";
	let albspl2 = albspl1 + " ui-btn ui-btn-mini ui-icon-bullets ui-btn-icon-right ui-corner-all'";
	return albspl2 + " data-textonly='false' data-textvisible='false' data-msgtext=''>" + f3 + "</a></li>";
};
const initGetAllPlaylistsFun5 = (f4) => {
	let artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg";
	let artspl2 = artspl1 + " ui-btn ui-btn-mini ui-icon-bullets ui-btn-icon-right ui-corner-all'";
	return artspl2 + " data-textonly='false' data-textvisible='false' data-msgtext=''>" + f4 + "</a></li>";
};
const initGetAllPlaylists = () => {
	$.get('AllPlaylists', (data) => {
		localStorage.setItem('playlists', JSON.stringify(data));
		let plone = '';
		let spl = '';
		let albspl='';
		let artspl='';
		$('#playPlaylistUL').empty();
		$.each(data, (key, val) => {
			if (val != "Please create a playlist") {
				$.each(val, (k, v) => {
					let pl2 = initGetAllPlaylistsFun1(v);
					return plone + pl2;
				})
			} else {
				let pl4 = initGetAllPlaylistsFun2(val);
				return plone + pl4;
			}
		})
		$.each(data, (k, v) => {
			let spl3 = initGetAllPlaylistsFun3(v);
			let albspl3 = initGetAllPlaylistsFun4(v);
			let artspl3 = initGetAllPlaylistsFun5(v);
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
const initAddOne = (g1) => {
	return g1 + 1
};
const initGetArtistAlphaFun2 = (g2, g3) => {
	let w1 = "<span id='artistOF" + g2 + "' "
	let w2 = w1 + "class='artOF show-page-loading-msg ui-btn ui-btn-mini ui-btn-inline ui-corner-all' ";
	return w2 + "data-textonly='false' data-textvisibility='false' data-msgtext=''>" + g3 + "</span>";
};
const initGetArtistAlpha = () => {
	$.get('ArtistAlpha', (data) => {
		$.each( data.artal, (key, val) => {
			let k = initAddOne(val);
			let w3 = initGetArtistAlphaFun2(k, val);
			$('#artistOFwrap').append(w3);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const initGetAlbumAlphaFun1 = (kk, cc) => {
	let ww1 = "<span id='albumOF" + kk + "' ";
	let ww2 = ww1 + "class='albumOF show-page-loading-msg ui-btn ui-btn-mini ui-btn-inline ui-corner-all' ";
	return ww2 + "data-textonly='false' data-textvisibility='false' data-msgtext=''>" + cc + "</span>";
};
const initGetAlbumAlpha = () => {
	$.get('AlbumAlpha', (data) => {
		$.each(data.albal, (ke, va) => {
			let kk = initAddOne(ke);
			let ww3 = initGetAlbumAlphaFun1(kk, va);
			$('#albumOFwrap').append(ww3);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const initGetSongAlphaFun1 = (b) => {
	let www1 = "<span id='songAlpaSpan' ";
	let www2 = www1 + "class='songOF show-page-loading-msg ui-btn ui-btn-mini ui-btn-inline ui-corner-all' ";
	return www2 + "data-textonly='false' data-textvisibility='false' data-msgtext=''>" + b + "</span>";
};
const initGetSongAlpha = () => {
	$.get('SongAlpha', (data) => {
		$.each(data.songal, (k2, vk) => {
			let www3 = initGetSongAlphaFun1(vk);
			$('#songOFwrap').append(www3);
		});
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
/*function initGetAllVideoFun1(a) {
	let v1 = "<div class='videolistViewDIV'>";
	let v2 = v1 + "<ul id='videolistViewUL' data-role='listview' data-split-icon='gear' data-inset='true'>";
	let v3 = v2 + "<li id='videolistViewLI'>";
	let v4 = v3 + "<a href='#vidplayer' id='videolistViewA' data-videoID='" + a.vid_id + "' ";
	let v5 = v4 + "data-vidAddr='" + a.httppath + "'>"; //a.vid_playpath + "'>";
	let v6 = v5 + "<img src='" + a.posterHttp + "'>" + a.vid_name;
	let vid = v6 + "</a></li></ul></div>";
	return vid
};
function initGetAllVideo() {
	$.get('AllVideo', (data) => {
		$.each(data.vlist, (key, val) => {
			let video = initGetAllVideoFun1(val);
			$('#vidDIV').append(video);
		});
	});
};*/
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////

/*
function calcDuration(d) {
	let hr = Math.floor(d / 3600);
	let min = Math.floor((d - (hr * 3600))/60);
	let sec = Math.floor(d - (hr * 3600) - (min * 60));	
	if (min < 10) { min = "0" + min; };
	if (sec < 10) { sec = '0' + sec; };
	return [min, sec];
};

*/
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const blka = (recm) => {
	let ba1 = "<div class='ui-block-a' data-theme='a'>";
	let ba2 = ba1 + "<a href='#popup1' data-rel='popup' data-transition='pop'>";
	let ba3 = ba2 + "<img src='" + recm + "' class='PicGrid'>";
	return ba3 + "</img></a></div>";
};
const blkb = (recm) => {
	let bb1 = "<div class='ui-block-b' data-theme='a'>";
	let bb2 = bb1 + "<a href='#popup2' data-rel='popup' data-transition='pop'>";
	let bb3 = bb2 + "<img src='" + recm + "' class='PicGrid'>";
	return bb3 + "</img></a></div>";
};
const blkc = (recm) => {
	let bc1 = "<div class='ui-block-c' data-theme='a'>";
	let bc2 = bc1 + "<a href='#popup3' data-rel='popup' data-transition='pop'>";
	let bc3 = bc2 + "<img src='" + recm + "' class='PicGrid'>";
	return bc3 + "</img></a></div>";
};
const blkd = (recm) => {
	let bd1 = "<div class='ui-block-d' data-theme='a'>";
	let bd2 = bd1 + "<a href='#popup4' data-rel='popup' data-transition='pop'>";
	let bd3 = bd2 + "<img src='" + recm + "' class='PicGrid'>";
	return bd3 + "</img></a></div>";
};
const blke = (recm) => {
	let be1 = "<div class='ui-block-e' data-theme='a'>";
	let be2 = be1 + "<a href='#popup5' data-rel='popup' data-transition='pop'>";
	let be3 = be2 + "<img src='" + recm + "' class='PicGrid'>";
	return be3 + "</img></a></div>";
};
const creatPop1 = (recm) => {
	let pu11 = "<ul id='pop1' data-role='listview' class='ui-content' data-insert='true'>"
	let pu12 = '';
	$.each(recm, (key, val) => {
		let s11 = "<li><a href='#' class='rart1' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		return pu12 + s11;
	})
	return pu11 + pu12 + "</ul>";
};
const creatPop2 = (recm) => {
	let pu21 = "<ul id='pop2' data-role='listview' class='ui-content' data-insert='true'>";
	let pu22 = '';
	$.each(recm, (key, val) => {
		let s22 = "<li><a href='#' class='rart2' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		return pu22 + s22;
	})
	return pu21 + pu22 + "</ul>"
};
const creatPop3 = (recm) => {
	let pu31 = "<ul id='pop3' data-role='listview' class='ui-content' data-insert='true'>";
	let pu32 = '';
	$.each(recm, (key, val) => {
		let s31 = "<li><a href='#' class='rart3' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		return pu32 + s31
	})
	return pu31 + pu32 + "</ul>"
};
const creatPop4 = (recm) => {
	let pu41 = "<ul id='pop4' data-role='listview' class='ui-content' data-insert='true'>";
	let pu42 = '';
	$.each(recm, (key, val) => {
		let s41 = "<li><a href='#' class='rart4' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu42 = pu42 + s41
	})
	return pu41 + pu42 + "</ul>"
};
const creatPop5 = (recm) => {
	let pu51 = "<ul id='pop5' data-role='listview' class='ui-content' data-insert='true'>";	
	let pu52 = '';
	$.each(recm, (key, val) => {
		let s51 = "<li><a href='#' class='rart5' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu52 = pu52 + s51
	})
	return pu51 + pu52 + "</ul>"
};

const initRandomPics = () => {
	$.get('RandomPics', (data) => {
		let result1 = blka(data.rsamp[0].thumbnail) + blkb(data.rsamp[1].thumbnail);
		let result2 = result1 + blkc(data.rsamp[2].thumbnail) + blkd(data.rsamp[3].thumbnail);
		let result = result2 + blke(data.rsamp[4].thumbnail);
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
const RandomPics = () => {
	$.get('RandomPics', (data) => {
		localStorage.setItem('nextimgset', JSON.stringify(data));
	});
};
const randomPicProcess = () => {
	let d = JSON.parse(localStorage.getItem('nextimgset'));
	let result1 = blka(d.rsamp[0].thumbnail) + blkb(d.rsamp[1].thumbnail);
	let result2 = result1 + blkc(d.rsamp[2].thumbnail) + blkd(d.rsamp[3].thumbnail);
	let result = result2 + blke(d.rsamp[4].thumbnail);
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
const checkAlphaNums = (anString) => {
	let anRe = /^[\w]+$/;
	let anFound = anString.match(anRe);
	if (anFound != null) { 
		return true;
	} else {
		return false;
	}
};
//checks a sting for only numeric characters
const checkNums = (numString) => {
	let numRe = /^[0-9]*$/;
	let numFound = numString.match(numRe);
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
const initLoadStats = () => {
	$('#statsTab').empty();
	$.get('Stats', ( data ) => {
		let stattwo = "<tr><th>Total Artists</th><td>" + data.stats.total_artists + "</td></tr>";
		let statthree = "<tr><th>Total Albums</th><td>" + data.stats.total_albums + "</td></tr>";
		let statfour = "<tr><th>Total Songs</th><td>" + data.stats.total_songs + "</td></tr>";
		let statnine = "<tr><th>Total Videos</th><td>" + data.stats.total_videos + "</td></tr>";
		let statfive = "<tr><th>Music Lib Size</th><td>" + data.stats.total_music_size + "</td></tr>";
		let statseven = "<tr><th>Video Lib Size</th><td>" + data.stats.total_video_size + "</td></tr>";
		let stateight = "<tr><th>Total Disk Size</th><td>" + data.stats.total_disk_size + "</td></tr>";
		let stats1 = stattwo + statthree + statfour + statnine + statfive + statseven + stateight;
		let stone = "<tr><th>Total MP3's</th><td>" + data.stats.total_mp3 + "</td></tr>";		
		let sttwo = "<tr><th>Total OGG's</th><td>" + data.stats.total_ogg + "</td></tr>";
		let stats = stats1 + stone + sttwo;	
		$('#statsTab').append(stats);
	});
};
///////////////////////////////////////////////////////////////////////////////
//////////////////////////// END SETTINGS PAGE STUFF //////////////////////////
///////////////////////////////////////////////////////////////////////////////
let rpw;
let rpw1;
const rpwStart = () => {
	rpw = setInterval(() => {RandomPics()}, 80000);
	rpw1 = setInterval(() => {randomPicProcess()}, 90000);
};
const rpwStop = () => {
	clearInterval(rpw);
	clearInterval(rpw1);
};
///////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////

//let initAmpnado = function () {
const initAmpnado = () => {
	initRandomPics();
	$('#audio2').show();
	//This hides the search boxes
//	$('.albsongUL').hide();
	$('#controlGrid, #albSSD1, #albSSD2, #albListViewDIV2, #artForm, #SSD1, #SSD2, #songListViewDIV2').hide();
	RandomPics();
	intitArtist1P1();
	initAlbum1P1();
	initSong1P1();
	initGetAllPlaylists();
	initGetArtistAlpha();
	initGetAlbumAlpha();
	initGetSongAlpha();
	initLoadStats();
};
$(window).load(initAmpnado)