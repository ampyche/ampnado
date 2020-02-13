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
///////////////////////////////////////////////////////////////////////////////
const oc_artOF1 = (xx) => {
	let soupArtOne = "<div><img class='artistimgS' src='" + xx + "'></img>";
	let soupArtTwo = soupArtOne + "</div><div class='art1divS'><ul class='artistSongULS' ";
	return soupArtTwo + "data-role='listview' data-inset='true' data-split-icon='gear'>";
};
const oc_artOF2 = (vv) => {
	let soupArt1 = "<li class='artSongLIS'><a href='#' class='artsongA1' ";
	let soupArt2 = soupArt1 + "data-songid='" + vv[1] + "'>" + vv[0] + "</a>";
	let soupArt3 = soupArt2 + "<a href='#artistselectplpage' class='artToPlaylistBtn' ";
	let soupArt4 = soupArt3 + "data-song='" + vv[0] + "' data-songid='" + vv[1] + "' ";
	return soupArt4 + "data-transition='slidefade'></a></li>";
};
const oc_artOF3 = (v) => {
	let a = "<div class='artistPageDiv' data-role='collapsible'><h4>" + v.Artist + "</h4><div>";
	let a11 = a + "<form id='" + v.ArtistId + "' class='artistForm'><div class='ui-field-contain'>";
	return a11 + "<select name='" + v.Artist + "' id='" + v.ArtistId + "' class='artistselect'>";
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const och_artistselect1 = (d) => {
	let aone = "<div id='songimglist'><img class='artistimg' src='" + d.getimgsonalb.thumbnail + "'></img>";
	let atwo = aone + "<div class='art1div'><ul id='artistSongUL' data-role='listview' data-inset='true' ";
	return atwo + "data-split-icon='gear'>";
};
const och_artistselect2 = (v1) => {
	let four = "<li class='artsongLI'><a href='#' class='artsongA1' ";
	let four1 = four + "data-songid='" + v1[1] + "'>" + v1[0] + "</a><a href='#artistselectplpage' ";
	let four2 = four1 + "class='artToPlaylistBtn' data-song='" + v1[0] + "' data-songid='" + v1[1] + "' ";
	return four2 + "data-transition='slidefade'></a></li>";	
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_albumOF1 = (va) => {
	let alb1 = "<div class='albumDIV'><ul class='albumUL' data-role='listview' data-inset='true'>";
	let alb2 = alb1 + "<li class='albumLI'><a href='#' class='albumA1' data-artist='" + va.Artist + "' ";
	let alb3 = alb2 + "data-artistid='" + va.ArtistId + "' data-album='" + va.Album + "' ";
	let alb4 = alb3 + "data-albumid='" + va.AlbumId + "'><img id='" + va.AlbumId + "' ";
	let alb5 = alb4 + "src='" + va.AlbumArtHttpPath + "'><h3 id='albH3'>" + va.Album + "</h3>";
	let alb6 = alb5 + "<p>" + va.Artist + "</p><span class='ui-li-count'>" + va.NumSongs + "</span>";
	let alb7 = alb6 + "</a></li></ul></div><div class='albsongList'><ul id='albsongUL" + va.AlbumId + "' ";
	return alb7 + "class='albsongUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
};
const oc_albumOF2 = (b) => {
	let albab = "<li class='albsongsLI'><a href='#' class='albsongsA' data-song='" + b[0] + "' ";
	let albab1 = albab + "data-songid='" + b[1] + "'>" + b[0] + "</a><a href='#albumselectplpage' ";
	let albab2 = albab1 + "class='addToPlaylist' data-pageid='albums' data-song='" + b[0] + "' ";
	return albab2 + "data-songid='" + b[1] + "' data-transition='slidefade'></a></li>";
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_addtoplaylist1 = (va) => {
	let pll1 = "<li class='playlistLi' data-playlistid='" + va[1] + "'><a href='#' class='plplay ui-btn ";
	let pll2 = pll1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	return pll2 + "data-playlistid='" + va[1] + "'>" + va[0] + "</a></li>";
};
const oc_addtoplaylist2 = (va) => {
	let spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + va[1] + "' ";
	return spl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + va[0] + "</a></li>";
};	
const oc_addtoplaylist3 = (va) => {
	let ablspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let ablspl2 = ablspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	let ablspl3 = ablspl2 + "data-playlistid='" + va[1] + "' data-textonly='false' data-textvisible='false' ";
	return ablspl3 + "data-msgtext=''>" + va[0] + "</a></li>";
};	
const oc_addtoplaylist4 = (va) => {
	let artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	let artspl3 = artspl2 + "data-playlistid='" + va[1] + "' data-textonly='false' data-textvisible='false' ";
	return artspl3 + "data-msgtext=''>" + va[0] + "</a></li>";
};
const oc_addtoplaylist5 = (p) => {
	let pll1 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	return pll1 + "ui-btn-icon-right'>" + p + "</a></li>";
};
const oc_addtoplaylist6 = (p) => {
	let spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	return spl2 + "data-textvisible='false' data-msgtext=''>" + p + "</a></li>";
};
const oc_addtoplaylist7 = (p) => {
	let albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	return albspl2 + "data-textvisible='false' data-msgtext=''>" + p + "</a></li>";
};
const oc_addtoplaylist8 = (p) => {
	let artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	return artspl2 + "data-textvisible='false' data-msgtext=''>" + p + "</a></li>";
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_artToPlaylistBtn1 = (v) => {
	let pll1 = "<li class='playlistLi' data-playlistid='" + v[1] + "'><a href='#' class='plplay ui-btn ";
	let pll2 = pll1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	return pll2 + "data-playlistid='" + v[1] + "'>" + v[0] + "</a></li>";
};
const oc_artToPlaylistBtn2 = (v) => {
	let spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	let spl3 = spl2 + "data-playlistid='" + v[1] + "' data-textonly='false' data-textvisible='false' ";
	return spl3 + "data-msgtext=''>" + v[0] + "</a></li>";
};
const oc_artToPlaylistBtn3 = (v) => {
	let albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	return albspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
};
const oc_artToPlaylistBtn4 = (v) => {
	let artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	return artspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
};		
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_addToPlaylist1 = (v) => {
	let pl1 = "<li class='playlistLi' data-playlistid='" + v[1] + "'><a href='#' class='plplay ui-btn ";
	let pl2 = pl1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	return pl2 + "data-playlistid='" + v[1] + "'>" + v[0] + "</a></li>";
};
const oc_addToPlaylist2 = (v) => {
	let spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	return spl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
};
const oc_addToPlaylist3 = (v) => {
	let albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	return albspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
};
const oc_addToPlaylist4 = (v) => {
	let artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	return artspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
};
const oc_addToPlaylist5 = (f) => {
	let p1 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	return p1 + "ui-btn-icon-right'>" + f + "</a></li>";
};
const oc_addToPlaylist6 = (f) => {
	let spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	return spl2 + "data-textvisible='false' data-msgtext=''>" + f + "</a></li>";
};
const oc_addToPlaylist7 = (f) => {
	let albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	return albspl2 + "data-textvisible='false' data-msgtext=''>" + f + "</a></li>";
};
const oc_addToPlaylist8 = (f) => {
	let artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	return artspl2 + "data-textvisible='false' data-msgtext=''>" + f + "</a></li>";
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_searchBut = (v) => {
	let s1 = "<li class='songs_li'><a class='songnameS' href='#' data-songid='" + v.songid + "' ";
	let s2 = s1 + "data-song='" + v.song + "'><h2>" + v.song + "</h2><h6>" + v.artist + "</h6></a>"
	let s3 = s2 + "<a href='#selectplpage' data-pageid='songs' data-songid='" + v.songid + "' ";
	return s3 + "data-song='" + v.song + "' class='addtoplaylist' data-transition='slidefade'></a></li>";
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_albsearchBut1 = (f) => {
	let alb1 = "<div class='albumDIV'><ul class='albumUL' data-role='listview' data-inset='true'>";
	let alb2 = alb1 + "<li class='albumLI'><a href='#' class='albumA1' data-artist='" + f.artist + "' ";
	let alb3 = alb2 + "data-artistid='" + f.artistid + "' data-album='" + f.album + "' ";
	let alb4 = alb3 + "data-albumid='" + f.albumid + "'><img id='" + f.albumid + "' src='" + f.thumbnail + "'>";
	let alb5 = alb4 + "<h3 id='albH3'>" + f.album + "</h3><p>" + f.artist + "</p>";
	let alb6 = alb5 + "<span class='ui-li-count'>" + f.numsongs + "</span></a></li></ul></div>";
	let alb7 = alb6 + "<div class='albsongList'><ul id='albsongUL" + f.albumid + "' class='albsongUL' ";
	return alb7 + "data-role='listview' data-inset='true' data-split-icon='gear'>";
};
const oc_albsearchBut2 = (v) => {
	let albab1 = "<li class='albsongsLI'><a href='#' class='albsongsA' data-song='" + v[0] + "' ";
	let albab2 = albab1 + "data-songid='" + v[1] + "'>" + v[0] + "</a><a href='#albumselectplpage' ";
	let albab3 = albab2 + "class='addToPlaylist' data-pageid='albums' data-song='" + v[0] + "' ";
	return albab3 + "data-songid='" + v[1] + "' data-transition='slidefade'></a></li>";
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_artsearchBut1 = (m) => {
	let a1 = "<div><img class='artistimgS' src='" + m + "'></img></div>";
	let a2 = a1 + "<div class='art1divS'><ul class='artistSongULS' data-role='listview' ";
	return a2 + "data-inset='true' data-split-icon='gear'>";
};
const oc_artsearchBut2 = (n) => {
	let art31 = "<li class='artSongLIS'><a href='#' class='artsongA1' ";
	let art32 = art31 + "data-songid='" + n[1] + "'>" + n[0] + "</a>";
	let art33 = art32 + "<a href='#artistselectplpage' class='artToPlaylistBtn' ";
	return art33 + "data-songid='" + n[1] + "' data-transition='slidefade'></a></li>";
};
const oc_artsearchBut3 = (n) => {
	let artA1 = "<div class='artistPageDivSearch' data-role='collapsible'><h4>" + n.artist + "</h4>";
	let artA2 = artA1 + "<div><form id='" + n.artistid + "' class='artistForm'><div ";
	let artA3 = artA2 + "class='ui-field-contain'><select ";
	return artA3 + "name='" + n.artist + "' id='" + n.artistid + "' class='artistselect'>";
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_homeBTN_fraz1 = (b) => {
	let b1 = "<div class='ui-block-a' data-theme='a'><a href='#popup1' data-rel='popup' data-transition='pop'>";
	let b2 = b1 + "<img src='" + b.rsamp[0].thumbnail + "' class='PicGrid'></img></a></div>";
	let b3 = b2 + "<div class='ui-block-b' data-theme='a'><a href='#popup2' data-rel='popup' data-transition='pop'>";
	let b4 = b3 + "<img src='" + b.rsamp[1].thumbnail + "' class='PicGrid'></img></a></div>";
	let b5 = b4 + "<div class='ui-block-c' data-theme='a'><a href='#popup3' data-rel='popup' data-transition='pop'>";
	let b6 = b5 + "<img src='" + b.rsamp[2].thumbnail + "' class='PicGrid'></img></a></div>";
	let b7 = b6 + "<div class='ui-block-d' data-theme='a'><a href='#popup4' data-rel='popup' data-transition='pop'>";
	let b8 = b7 + "<img src='" + b.rsamp[3].thumbnail + "' class='PicGrid'></img></a></div>";
	let b9 = b8 + "<div class='ui-block-e' data-theme='a'><a href='#popup5' data-rel='popup' data-transition='pop'>";
	return b9 + "<img src='" + b.rsamp[4].thumbnail + "' class='PicGrid'></img></a></div>";
};
const oc_homeBTN_fraz2 = (b) => {
	let pu11 = "<ul id='pop1' data-role='listview' class='ui-content' data-insert='true'>"
	let pu12 = '';
	$.each(b.rsamp[0].songs, (key, val) => {
		let s11 = "<li><a href='#' class='rart1' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		return pu12 + s11
	})
	let pu111 = pu11 + pu12 + "</ul>";
	$('#popup1').append(pu111);
	$('#pop1').listview().trigger('refresh');
	$('#popup1').popup().trigger('create');
};
const oc_homeBTN_fraz3 = (b) => {
	let pu21 = "<ul id='pop2' data-role='listview' class='ui-content' data-insert='true'>";
	let pu22 = '';
	$.each(b.rsamp[1].songs, (key, val) => {
		let s22 = "<li><a href='#' class='rart2' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		return pu22 + s22;
	})
	let pu211 = pu21 + pu22 + "</ul>";
	$('#popup2').append(pu211);
	$('#pop2').listview().trigger('refresh');
	$('#popup2').popup().trigger('create');
};
const oc_homeBTN_fraz4 = (b) => {
	let pu31 = "<ul id='pop3' data-role='listview' class='ui-content' data-insert='true'>";
	let pu32 = '';
	$.each(b.rsamp[2].songs, (key, val) => {
		let s31 = "<li><a href='#' class='rart3' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		return pu32 + s31;
	})
	let pu311 = pu31 + pu32 + "</ul>";
	$('#popup3').append(pu311);
	$('#pop3').listview().trigger('refresh');
	$('#popup3').popup().trigger('create');
};
const oc_homeBTN_fraz5 = (b) => {
	let pu41 = "<ul id='pop4' data-role='listview' class='ui-content' data-insert='true'>";
	let pu42 = '';
	$.each(b.rsamp[3].songs, (key, val) => {
		let s41 = "<li><a href='#' class='rart4' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu42 = pu42 + s41
	})
	let pu411 = pu41 + pu42 + "</ul>";
	$('#popup4').append(pu411);
	$('#pop4').listview().trigger('refresh');
	$('#popup4').popup().trigger('create');
};
const oc_homeBTN_fraz6 = (b) => {
	let pu51 = "<ul id='pop5' data-role='listview' class='ui-content' data-insert='true'>";	
	let pu52 = '';
	$.each(b.rsamp[4].songs, (key, val) => {
		let s51 = "<li><a href='#' class='rart5' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu52 = pu52 + s51
	})
	let pu511 = pu51 + pu52 + "</ul>";
	$('#popup5').append(pu511);
	$('#pop5').listview().trigger('refresh');
	$('#popup5').popup().trigger('create');
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////

/*
const singPlayer1(d) {
	console.log(d.soho);
	$('#introimg').attr('src', d.soho['AlbumArtHttpPath']);
	$('#playlistalbart').attr('src', d.soho['AlbumArtHttpPath']);
	$('#pictext').text(d.soho['Song']);
	$('#pictext2').text(d.soho['Album']);
	audio25 = $('#audio2');
	audio25.attr('src', d.soho['HttpMusicPath']);
	audio25.on('loadedmetadata', () => {
		var dur = audio25[0].duration;
		var cd = calcDuration(dur);
		$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
		$('#artistPlayBtn').text("Play 00:00").css('background-color', 'green').css("color", "white");
		$('#artistStopBtn').text("Stop " + cd[0] + ':' + cd[1]).css('background-color', 'purple');
	});
};

*/
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_butsub1 = (v) => {
	var npl1 = "<li class='playlistLi' data-playlistid='" + v.playlistid + "'><a href='#' ";
	var npl2 = npl1 + "class='plplay ui-btn ui-mini ui-icon-bullets ui-btn-icon-right' ";
	return npl2 + "data-playlistid='" + v.playlistid + "'>" + v.playlistname + "</a></li>"
};
const oc_butsub2 = (v) => {
	var npl21 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var npl22 = npl21 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var npl23 = npl22 + "data-playlistid='" + v.playlistid + "' data-textonly='false' ";
	return npl23 + "data-textvisible='false' data-msgtext=''>" + v.playlistname + "</a></li>"
};
const oc_butsub3 = (v) => {
	var npl31 = "<li><a href='#artists' class='artSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var npl32 = npl31 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var npl33 = npl32 + "data-playlistid='" + v.playlistid + "' data-textonly='false' data-textvisible='false' ";
	return npl33 + "data-msgtext=''>" + v.playlistname + "</a></li>"
};
const oc_butsub4 = (v) => {
	var npl41 = "<li><a href='#albumssongs' class='albSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var npl42 = npl41 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v.playlistid + "' ";
	return npl42 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v.playlistname + "</a></li>"
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
const oc_randomInput1 = (v) => {
	let p1 = "<li class='playlistLi' data-playlistid='" + v.playlistid + "'><a href='#' class='plplay ui-btn ";
	let p2 = p1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	return p2 + "data-playlistid='" + v.playlistid + "'>" + v.playlistname + "</a></li>"
};
const oc_randomInput2 = (v) => {
	let spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ui-icon-bullets ";
	let spl2 = spl1 + "ui-btn-icon-right ui-corner-all' data-playlistid='" + v.playlistid + "' ";
	return spl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v.playlistname + "</a></li>"
};
const oc_randomInput3 = (v) => {
	let alpl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let alpl2 = alpl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	let alpl3 = alpl2 + "data-playlistid='" + v.playlistid + "' data-textonly='false' data-textvisible='false' ";
	return alpl3 + "data-msgtext=''>" + v.playlistname + "</a></li>"
};	
const oc_randomInput4 = (v) => {
	let arpl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	let arpl2 = arpl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	let arpl3 = arpl2 + "data-playlistid='" + v.playlistid + "' data-textonly='false' data-textvisible='false' ";
	return arpl3 + "data-msgtext=''>" + v.playlistname + "</a></li>"
};

const albumSearchFunc = () => {
	$('.albumDIV, .albsongList').empty();
	$('#albsearch-basic').textinput({preventFocusZoom: true});
	albsearchVal = $("#albsearch-basic").val();
	$.get('AlbumSearch',
	{
		'albsearchval' : albsearchVal,
	},
	function(data) {
		$('#albListViewDIV2').empty();
		$.each(data.ysearch, ( ke, va) => {
			let alb8 = oc_albsearchBut1(va);
			let alba33 = '';
			$.each(va.songs, (k, v) => {
				$.each(v, (kk, vv) => {
					return alba33 + oc_albsearchBut2(vv);
				});
			});
			let result = alb8 + alba33 + "</ul></div>";
			$('#albListViewDIV2').append(result);
			$('.albumUL, .albsongUL').listview().trigger('refresh');
			$('.albsongUL').hide();
			$.mobile.loading("hide");
		});
	});
};
//This makes Artist soup
$(document).on('click', '.artOF', () => {
	let artass = $(this).text();
	$('#artistOFC').collapsible("collapse");
	$('#artistmain').empty();
	$.get('ArtistInfo', 
	{
		'selected': artass
	},
	(data) => {
		$.each(data.arts, ( key, val ) => {
			let alblength = val.Albums.length;
			let abc = "<div class='artistPageDivS' data-role='collapsible'><h4>" + val.Artist + "</h4>";
			let selected = val.Albums[0][1];
			if ( alblength === 1 ) {
				$.get('ImageSongsForAlbum', 
				{
					'selected' : selected
				}, 
				(data) => {
					let soupArtThree = oc_artOF1(data.getimgsonalb.thumbnail);
					let artSoupLI = '';
					$.each(data.getimgsonalb.songs, (kk, vv) =>{
						let soupArt5 = oc_artOF2(vv);
						return artSoupLI + soupArt5
					})
					var result2 = abc + soupArtThree + artSoupLI + "</ul></div>";
					$('#artistmain').append(result2);
					$('.artistPageDivS').collapsible().trigger('create');
				})
				
			} else {
				let a22 = oc_artOF3(val);
				let a2 = '';
				let a3 = '';
				let aa1 = "<option class='artop0' value='Choose Album'>Choose Album</option>";
				$.each(val.Albums, (k, v) => {
					let a1 = "<option class='artop1' value='" + v[1] + "'>" + v[0] + "</option>";
					a2 = a2 + a1;
					a3 = aa1 + a2;
					return a3
				})
				var result = a22 + a3 + "</select></div></form></div>";
				$('#artistmain').append(result);
				$('.artistPageDiv').collapsible().trigger('create');
			}
		});
		$.mobile.loading("hide");
	});
})
.on('click', 'a.songnameS', () => {
	let selected_song = $(this).attr('data-songid');
	let audio2 = $('#audio2');
	audio2.attr('src', '');
	$('.duration').text('00:00');
	var trancSS = localStorage.getItem('TransCode');
	$.get("PathArt",
	{
		"selected": selected_song, "transcode": trancSS,
	},
	function(data,status){
		audio2.attr('src', data.httpmusicpath);
		$('#introimg').attr('src', data.lthumbnail);
		$('#playlistalbart').attr('src', data.lthumbnail);
		$('#pictext').text(data.song);
		$('#pictext2').text(data.album);
		let boob = {'song': data.song, 'songid': data.songid};
		localStorage.setItem('songPageGetPathArt', JSON.stringify(data));
		localStorage.setItem("songPageSelected_SONG_SONGID", JSON.stringify(boob));
	});
	audio2.on('loadedmetadata', () => {
		var dur = audio2[0].duration;
		var cd = calcDuration(dur);
		$('.duration, .StopBtn').text("Stop " + cd[0] + ':' + cd[1]).css('background-color', 'purple');
		$('.PlayBtn').text("Play 00:00").css('background-color', 'green').css("color", "white");
	});	
})
//This get selected song from artist page and sends it to the player
.on('click', '.artsongA1', () => {
	var  audio24 = $('#audio2');
	let booty = {'song': $(this).text(), 'songid': $(this).attr('data-songid')}
	localStorage.setItem('artistPageSelected_SONG_SONGID', JSON.stringify(booty));
	$.get("PathArt",
	{
		"selected": booty.songid,
	},
	function(data) {
		audio24.attr('src', data.HttpMusicPath);
		$('#introimg').attr('src', data.AlbumArtHttpPath);
		$('#playlistalbart').attr('src', data.AlbumArtHttpPath);
		$('#pictext').text(data.Song);
		$('#pictext2').text(data.Album);
		localStorage.setItem('artistPageGetPathArt', JSON.stringify(data));
		audio24.on('loadedmetadata', () => {
			var dur = audio24[0].duration;
			var cd = calcDuration(dur);
//			$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
			$('.PlayBtn').text("Play 00:00").css('background-color', 'grey').css('color', 'black');
			$('.StopBtn').text("Stop " + cd[0] + ':' + cd[1]).css('background-color', 'grey').css('color', 'black');
			let ftxt = data.Song + " " + data.Artist;
			$('.footerSong').text(data.Song);
			$('.footerArtist').text(data.Artist);
			
		});
/*		audio24.on('ended', () => {
			$.get('ClearTemp',
			{
				'filetodelete': data.httpmusicpath,
			},
			(data) => {
				console.log(data.cleared);
			});
		});*/iArtist1P1Fun2
	});
})
//This fetches the selected album and displays albumart and
//song list for artist page
.on('change', '.artistselect', () => {
	$('.artistimg').remove(); //Clear albumart and songs list
	$('.art1div').empty();
	artistid = $(this).attr('id'); //This is the artistid of the selected album	
	selected = $(this).find(':selected').val(); //this is selected albumid
	$.get('ImageSongsForAlbum',
		{
			'selected' : selected //this is albumid	
		},
		(data) => {
			let athree = och_artistselect1(data);
			let artLIString = ''
			$.each(data.getimgsonalb.songs, (k, v) => {
				let four3 = och_artistselect2(v);
				artLIString = artLIString + four3;
				return artLIString
			})
			var result = athree + artLIString + "</ul></div></div>";
			$(result).insertAfter('#' + artistid);
			$('#artistSongUL').listview().trigger('refresh');
			$('.artistPageDiv').collapsible().trigger('create');
			$.mobile.loading("hide");
		}
	);
})
//This removes the image and songlist from the collapsible when it is collapsed
.on('collapsiblecollapse', '.artistPageDiv', () => {
	$('.artistimg').remove();
	$('.art1div').empty();
})
//This gets playlist selection and adds song to playlistdb for the artist page
.on('click', '.artistSelBtn', () => {
	let selectedPlayList = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
	localStorage.setItem('currentSelected_PLAYLIST_PLAYLISTID', JSON.stringify(selectedPlayList));
	var name = JSON.parse(localStorage.getItem("artistPageSelected_SONG_SONGID"));
	$.get('AddSongsToPlistDB', 
	{
		"songname" : name.song, "songid" : name.songid, "playlistid" : selectedPlayList.playlistid,	
	},
	function(data,status) {
		if ( status === 'success') {
			$.mobile.loading("hide");
		}
	});
})
//This hides and shows the albums page songs listview
.on('click', '.albumA1', () => {
	bebe = "#albsongUL" + $(this).attr('data-albumid');
	$(bebe).fadeToggle('fast');
})
.on('click', '.albumOF', () => {
	let albass = $(this).text();
	$('#albumOFC').collapsible("collapse");
	$('#alblist').empty();
	$.get('AlbumInfo', 
	{
		'selected': albass
	},
	(data) => {
		$.each(data.albs, ( key, val) => {
			let alb8 = oc_albumOF1(val);
			let alba33 = '';
			$.each(val.Songs, (ka, val) => {
				alba33 = alba33 + oc_albumOF2(val);
				return alba33
			});
			var result = alb8 + alba33 + "</ul></div>";
			$('#alblist').append(result);
			$('.albumUL, .albsongUL').listview().trigger('refresh');
			$('.albsongUL').hide();
			$.mobile.loading("hide");
		});
	});
})
//This get the selected song on the albums page and sends it to the player
.on('click', '.albsongsA', () => {
	var  audio23 = $('#audio2');
	audio23.attr('src', '');
	$('.duration').text('00:00');
	let selSong = $(this).attr('data-songid');
	$.get("PathArt",
	{
		"selected": selSong,
	},
	function(data){
		let foobar10 = {'song': data.Song, 'songid': selSong};
		audio23.attr('src', data.HttpMusicPath);
		$('#introimg').attr('src', data.AlbumArtHttpPath);
		$('#playlistalbart').attr('src', data.AlbumArtHttpPath);
		$('#pictext').text(data.Song);
		$('#pictext2').text(data.Album);
		localStorage.setItem('albumPageGetPathArt ', JSON.stringify(data));
		localStorage.setItem('albumPageSelected_SONG_SONGID', JSON.stringify(foobar10));
		audio23.on('loadedmetadata', () => {
			var dur = audio23[0].duration;
			var cd = calcDuration(dur);
			$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
			$('.PlayBtn').css('background-color', 'green').css("color", "white");
		});
/*		audio23.on('ended', () => {
			$.get('ClearTemp',
			{
				'filetodelete': data.httpmusicpath,
			},
			(data) => {
				console.log(data.cleared);
			});
		});*/
	});
	$('.albsongUL').hide();
})
//This adds the song and songid to localstorage 
.on('click', '.addToPlaylist', () => {
	let albssid = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')}	
	localStorage.setItem('albumPageSelected_SONG_SONGID', JSON.stringify(albssid));
})
//This gets the songs for the selected Alpha selecter
.on('click', '.songOF', () => {
	let ss = $(this).text();
	$('#songOFC').collapsible("collapse");
	$("#songs_view").empty();
	$.get('SongInfo',
	{
		'selected': ss
	},
	(data) => {
		$.each(data.song, ( key, val) => {
			let ss1 = "<li class='songs_li'><a class='songname' href='#' data-songid='" + val.SongId + "'>";
			let ss2 = ss1 + "<h2>" + val.Song + "</h2><h6>" + val.Artist + "</h6></a><a href='#selectplpage' ";
			let ss3 = ss2 + "data-song='" + val.Song + "' data-songid='" + val.SongId + "' class='addtoplaylist' ";
			let ss4 = ss3 + "data-transition='slidefade'></a></li>";
			$("#songs_view").append(ss4);
		});
		$('#songs_view').listview('refresh');
		$.mobile.loading("hide");
	});
})
//This gets the selected song from the first anchor 
//use data-song and data-songid they are set
//this should use songid instead of songname
.on('click', 'a.songname', () => {
	let audio2 = $('#audio2');
	audio2.attr('src', '');
	$('.duration').text('00:00');
	let selected_songid = $(this).attr('data-songid');

	$.get("PathArt",
	{
		"selected": selected_songid
	},
	function(data) {
		audio2.attr('src', data.HttpMusicPath);
		$('#introimg').attr('src', data.AlbumArtHttpPath);
		$('#playlistalbart').attr('src', data.AlbumArtHttpPath);
		$('#pictext').text(data.Song);
		$('#pictext2').text(data.Album);
		let booob = {'song': data.Song, 'songid': data.SongId};
		localStorage.setItem('songPageGetPathArt', JSON.stringify(data));
		localStorage.setItem("songPageSelected_SONG_SONGID", JSON.stringify(booob));
		audio2.on('loadedmetadata', () => {
			var dur = audio2[0].duration;
			var cd = calcDuration(dur);
			$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
		});
/*		audio2.on('ended', () => {
			$.get('ClearTemp',
			{
				'filetodelete': data.httpmusicpath,
			},
			(data) => {
				console.log(data.cleared);
			});
		});*/
	});	
})
//This sets the selectedSONG and selectedSONGid in the browser localstorage
//for the add to playlist button on the songs page.
.on('click', '.addtoplaylist', () => {
	let sname = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')}
	localStorage.setItem('songPageSelected_SONG_SONGID', JSON.stringify(sname));
	$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').empty();
	$.get("AllPlaylists",
	{
		"selected": sname.songid
	},
	function(data) {
		if ( data.plnames != 'Please create a playlist' ) {
			localStorage.setItem('playlists', JSON.stringify(data));
			$.each(data.plnames, (k, va) => {
				$('#playPlaylistUL').append(oc_addtoplaylist1(va));
				$('#splUL').append(oc_addtoplaylist2(va));
				$('#albsplUL').append(oc_addtoplaylist3(va));
				$('#artsplUL').append(oc_addtoplaylist4(va));	
			});
		} else {
			let pln = 'Please create a playlist';
			$('#playPlaylistUL').append(oc_addtoplaylist5(pln));
			$('#splUL').append(oc_addtoplaylist6(pln));
			$('#albsplUL').append(oc_addtoplaylist7(pln));
			$('#artsplUL').append(oc_addtoplaylist8(pln));
		}
	});
	$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').listview().trigger('refresh');
	$.mobile.loading("hide");
})
//This is the artists page
.on('click', '.artToPlaylistBtn', () => {
	let arr = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')};
	localStorage.setItem("artistPageSelected_SONG_SONGID", JSON.stringify(arr));
	$('#playPlaylistUL, #artsplUL, #albsplUL, #splUL').empty();
	$.get("AllPlaylists",
	{
		"selected": arr.songid
	},
	function(data) {
		$.each(data.plnames, (k, v) => {
			$('#playPlaylistUL').append(oc_artToPlaylistBtn1(v));
			$('#splUL').append(oc_artToPlaylistBtn2(v));
			$('#albsplUL').append(oc_artToPlaylistBtn3(v));
			$('#artsplUL').append(oc_artToPlaylistBtn4(v));
		});
		localStorage.setItem('playlists', JSON.stringify(data));
	});
	$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').listview().trigger('refresh');
	$.mobile.loading("hide");
})
//this is the albums page
.on('click', '.addToPlaylist', () => {
	let sname2 = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')};
	localStorage.setItem("albumPageSelected_SONG_SONGID", JSON.stringify(sname2));
	$.get("AllPlaylists",
	{
		"selected": sname2.songid
	},
	function(data) {
		localStorage.setItem('playlists', JSON.stringify(data));
		$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').empty();
		if ( data.plnames != 'Please create a playlist' ) {
			$.each(data.plnames, (k, v) => {
				$('#playPlaylistUL').append(oc_addToPlaylist1(v));
				$('#splUL').append(oc_addToPlaylist2(v));
				$('#albsplUL').append(oc_addToPlaylist3(v));
				$('#artsplUL').append(oc_addToPlaylist4(v));
			});
		} else {
			let plnln = 'Please create a playlist';
			$('#playPlaylistUL').append(oc_addToPlaylist5(plnln));
			$('#splUL').append(oc_addToPlaylist6(plnln));
			$('#albsplUL').append(oc_addToPlaylist7(v));
			$('#artsplUL').append(oc_addToPlaylist8(v));	
		}
		$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').listview().trigger('refresh');
	});
	$.mobile.loading("hide");
})
//This gets playlist selection and adds song to playlistdb for the albums page
.on('click', '.albumSelBtn', () => {
	let selectedPlaylist1 = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
	localStorage.setItem("currentSelected_PLAYLIST_PLAYLISTID", JSON.stringify(selectedPlaylist1));
	var name1 = JSON.parse(localStorage.getItem("albumPageSelected_SONG_SONGID"));
	$.get('AddSongsToPlistDB',
	{
		"songname" : name1.song, "songid" : name1.songid, "playlistid" : selectedPlaylist1.playlistid	
	},
	function(status) {
		if ( status === 'success') { 
			$.mobile.loading("hide");
		}
	});
})
//This gets playlist selection and adds song to playlist
.on('click', '.songSelBtn', () => {
	let selectedPlaylist2 = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
	localStorage.setItem("currentSelected_PLAYLIST_PLAYLISTID", JSON.stringify(selectedPlaylist2));
	var name2 = JSON.parse(localStorage.getItem('songPageSelected_SONG_SONGID'));
	$.get('AddSongsToPlistDB', 
	{
		"songname" : name2.song, "songid" : name2.songid, "playlistid" : selectedPlaylist2.playlistid,		
	},
	function(status) {
		if ( status === 'success') { 
			$.mobile.loading("hide");
		}		
	});
})




.on('click', '#searchBut', () => {
	searchVal = $('#search-basic').val();
	$.get('SongSearch',
	{
		'searchval' : searchVal,
	},
	function(data) {
		$('#songs_view, #songs_view2').empty();
		$.each(data.xsearch, ( k, v) => {
			let s4 = oc_searchBut(v);
			$("#songs_view2").append(s4);
		});
		$('#songs_view2').listview('refresh');
		$.mobile.loading("hide");
	});
})
.on('click', '#searchClear', () => {
	$('#search-basic').val('');
	$("#songs_view2").empty();
})
.on('click', '#SS', () => {
	$('#SSD1, #SSD2, #songListViewDIV2').fadeToggle('fast');
})






.on('keypress', (e) => {
	if (e.which == 13){
		let alb = $("#albsearch-basic").val()
		if (alb != '') {
			albumSearchFunc();
		}
	};
})








.on('click', '#albsearchBut', () => {
	albumSearchFunc();
})
.on('click', '#albsearchClear', () => {
	$('#albsearch-basic').val('');
	$('#albListViewDIV2').fadeToggle('fast').empty();
})
.on('click', '#albSS', () => {
	$('#albSSD1, #albSSD2, #albListViewDIV2').fadeToggle('fast');
})
.on('click', '#artsearchBut', () => {
	$('#artistmain').empty();
	artsearchval = $('#artsearch-basic').val();
	$.get('ArtistSearch',
	{
		"artsearchval" : artsearchval,
	},
	(data) => {
		$.each(data, ( key, val ) => {
			$.each(val, ( ke, va ) => {
				alblength = va.albums.length;
				if ( alblength === 1 ) {
					let abc = "<div class='artistPageDivS' data-role='collapsible'><h4>" + va.artist + "</h4>";
					let selected = va.albums[0][1]; //this is albumid
					$.get('ImageSongsForAlbum',
						{
							'selected' : selected	//this is albumid	
						},
						(data) => {
							let a3 = oc_artsearchBut1(data.getimgsonalb.thumbnail);							
							liString = '';
							$.each(data.getimgsonalb.songs, (kk, vv) => {
								let art34 = oc_artsearchBut2(vv);
								liString = liString + art34;
								return liString;
							})
							var result2 = abc + a3 + liString + "</ul></div>";
							$('#artSearchDIV').append(result2);
							$('.artistPageDivS').collapsible().trigger('create');	
					});
				} else {
					let artA4 = oc_artsearchBut3(va);
					let a2 = ''
					let aa1 = "<option class='artop0' value='Choose Album'>Choose Album</option>";
					$.each(va.albums, (k, v) => {
						let a1 = "<option class='artop1' value='" + v[1] + "'>" + v[0] + "</option>";
						a2 = a2 + a1;
						a3 = aa1 + a2;
						return a3
					})
					var result = artA4 + a3 + "</select></div></form></div>";
					$('#artSearchDIV').append(result);
					$('.artistPageDivSearch').collapsible().trigger('create');
				}
			});
		});
		$.mobile.loading("hide");
	});
})
.on('click', '#artSS', () => {
	$('#artForm').fadeToggle('fast');
})
.on('click', '#search-basic', () => {
	$('#search-basic').val('');
})
.on('click', '#artsearch-basic', () => {
	$('#artsearch-basic').val('');
})
.on('click', '#albsearch-basic', () => {
	$('#albsearch-basic').val('');
})
.on('click', '#artsearchClear', () => {
	$('#artsearch-basic').val('');
	$('#artSearchDIV').empty();
	$.mobile.loading("hide");
})
.on('click', '.homeBTN, .fraz', () => {
	rpwStop();
	$('#popup1, #popup2, #popup3, #popup4, #popup5, #intropicGrid1').empty();
	let boohoo = JSON.parse(localStorage.getItem('nextimgset'));
	var result = oc_homeBTN_fraz1(boohoo);
	$('#intropicGrid1').append(result);
	oc_homeBTN_fraz2(boohoo);
	oc_homeBTN_fraz3(boohoo);
	oc_homeBTN_fraz4(boohoo);
	oc_homeBTN_fraz5(boohoo);
	oc_homeBTN_fraz6(boohoo);
	RandomPics();
	rpwStart();		
})
.on('click', '#intropicGrid1', () => {
	rpwStop();
})
.on("click", ".hide-page-loading-msg", () => {
	$.mobile.loading("hide");
})
//This shows our spinner during ajax calls
.on('click', ".show-page-loading-msg", () => {
	var $this = $(this),
		theme = $this.jqmData("theme") ||
$.mobile.loader.prototype.options.theme,
		msgText = $this.jqmData('msgtext') ||
$.mobile.loader.prototype.options.text,
		textVisible = $this.jqmData("textvisible") ||
$.mobile.loader.prototype.options.textVisible,
		textonly = !!$this.jqmData('textonly');
		html = $this.jqmData("html") || "";
	$.mobile.loading("show", {
			text: msgText,
			textVisible: textVisible,
			theme: theme,
			textonly: textonly,
			html: html
	});
})
///////////////////////////////////////////////////////////////////////////////
//////////////////////////// PLAYLIST PAGE STUFF //////////////////////////////
///////////////////////////////////////////////////////////////////////////////
//$(document).on('click', '.playlistLi', () => {
.on('click', '.playlistLi', () => {
	$('#controlGrid').fadeToggle('fast');
	$('#playlistcollapsible').collapsible('collapse');
})
.on('click', '.plssel, .pldl', () => {
	$('#controlGrid').fadeToggle('fast');
})
.on('click', '#randomInput', () => {
	$('#addrandomplaylist').collapsible('collapse');
})
//This adds a new playlist to the db
.on('click', '#butsub', () => {
	$('#addnewplaylistDiv').collapsible('collapse');
	var text1 = $('input#text1').val();
	var checkAN = checkAlphaNums(text1);
	if (checkAN === true) {
		$.get('AddPlayListNameToDB',
		{
			"playlistname" : text1
		},
		function(data) {
			$('#playPlaylistUL, #artsplUL, #albsplUL, #splUL').empty();
			$.each(data.pnames, (k, v) => {
				let pln = {'playlist': v.playlistname, 'playlistid': v.playlistid};
				localStorage.setItem("currentSelected_PLAYLIST_PLAYLISTID", JSON.stringify(pln));
				$('#playPlaylistUL').append(oc_butsub1(v));
				$('#splUL').append(oc_butsub2(v));
				$('#artsplUL').append(oc_butsub3(v));
				$('#albsplUL').append(oc_butsub4(v));
				$('input#text1').val("");
				$('#playlistform').hide();
			});
			$('#playPlaylistUL, #artsplUL, #albsplUL, #splUL').listview('refresh');
			$.mobile.loading("hide");
		});
	} else {
		$.mobile.loading("hide");
	}
})
//Get current selected playlist
.on('click', '.plplay', () => {
	taz = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
	localStorage.setItem("currentSelected_PLAYLIST_PLAYLISTID", JSON.stringify(taz));
	$('#playlistcollapsible').collapsible('collapse');
	$('#audio1').show();
})
//delete a playlist
.on('click', '#playlistDeleteBtn1', () => {
	$('#playPlaylistUL').empty();
	let selpl = JSON.parse(localStorage.getItem("currentSelected_PLAYLIST_PLAYLISTID"));
	$.get('DeletePlaylistFromDB',
	{
		"playlistid" : selpl.playlistid
	},
	(data) => {
		localStorage.setItem('playlists', JSON.stringify(data));
		$.each(data.npl, (k, v) => {
			let pllone = "<li class='playlistLi' data-playlistid='" + v.playlistid + "'><a href='#' class='plplay ";
			let plltwo = pllone + "ui-btn ui-mini ui-icon-bullets ui-btn-icon-right' ";
			let pllthree = plltwo + "data-playlistid='" + v.playlistid + "'>" + v.playlistname + "</a></li>";
			$('#playPlaylistUL').append(pllthree);
		})
		$('#playPlaylistUL').listview('refresh');
		$.mobile.loading("hide");
	});
})
.on('click', '#playlistEditBtn1', () => {
	$("#pleditMain").empty();
	let pln33 = JSON.parse(localStorage.getItem("currentSelected_PLAYLIST_PLAYLISTID"));
	let blep = "<div id='pledith3'><h3>Edit: " + pln33.playlist + "</h3></div>";
	$.get('AllPlaylistSongsFromDB',
	{
		'playlistid' : pln33.playlistid
	},
	(data) => {
		let ple1 = "<div class='pleditLV'>";
		let ple = ple1 + "<ul class='editplUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
		let s3 = "";
		$.each(data.taz, (key, val) => {
			var lvLI1 = "<li><a href='#' class='lviewLi' data-sonID='" + val[1] + "'>" + val[0] + "</a>";
			var lvLI2 = lvLI1 + "<a href='#editpopup' data-sonID='" + val[1] + "' data-rel='popup' class='plpsongsA2  ";
			var lvLI3 = lvLI2 + "ui-btn' data-textonly='false' data-textvisible='false' data-msgtext=''></a></li>";
			s3 = s3 + lvLI3;
			return s3
		});
		editsongs1 = blep + ple + s3 + "</ul></div>";
		backB = "<div><a href='#playlists' data-rel='back' class='ui-btn ui-btn-mini ui-corner-all'>Back</a></div>"
		editsongs = editsongs1 + backB
		$('#pleditMain').append(editsongs);
		$('.editplUL').listview().trigger('refresh');
	});
	$.get('AllPlaylists', (data) => {
		localStorage.setItem('playlists', JSON.stringify(data));
	})
	$.mobile.loading("hide");
})
.on('click', '.lviewLi', () => {
	delsong = {'delsong': $(this).text(), 'delsongid': $(this).attr('data-sonID')};
	localStorage.setItem('editPageSelected_SONG_SONGID', JSON.stringify(delsong));
})
//This sets the values in the delete popup
.on('click', '.plpsongsA2', () => {
	let plsnid = {'dsongid': $(this).attr("data-sonID")};
	crock = localStorage.setItem("editPage_DELETE_SONGID", JSON.stringify(plsnid));
})
.on('click', '#editYesBtn' , () => {
	$('#pleditMain').empty();
	let snID = JSON.parse(localStorage.getItem("editPage_DELETE_SONGID"));
	let pln = JSON.parse(localStorage.getItem("currentSelected_PLAYLIST_PLAYLISTID"));
	let blep = "<div id='pledith3'><h3>Edit: " + pln.playlist + "</h3></div>";
	let ple1 = "<div class='pleditLV'>";
	let ple = ple1 + "<ul class='editplUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
	$.getJSON("DeleteSongFromPlaylist",
	{
		"playlistname" : pln.playlist, 'delsongid' : snID.dsongid
	},
	(data) => {
		let s3 = "";
		$.each(data, (key, valu) => {
			$.each(valu, (key, val) => {
				$.each(val, (k, v) => {
					var lvLI1 = "<li><a href='#' class='lviewLi' data-sonID='" + v.songid + "'>" + v.song + "</a>";
					var lvLI2 = lvLI1 + "<a href='#editpopup' data-sonID='" + v.sonID + "' data-rel='popup' ";
					var lvLI3 = lvLI2 + "class='plpsongsA2  ui-btn' data-textonly='false' data-textvisible='false' ";
					var lvLI4 = lvLI3 + "data-msgtext=''></a></li>";
					return s3 + lvLI4
				});
			});
		});
		editsongs = blep + ple + s3 + "</ul></div>";
		$('#pleditMain').append(editsongs);
		$('.editplUL').listview().trigger('refresh');
		$.mobile.loading("hide");
	});
})
//These sets the playlist page random playlist text inputs to blank when they are clicked on
.on('click', '#text2', () => {
	$('#text2').val('');
})
.on('click', '#text3', () => {
	$('#text3').val('');
})
//This adds a random playlist to the db
.on('click', '#randomInput', () => {
	var nan = "<p>Please only enter alpha numeric charcters.</p>";
	var noAlphaNum = nan + "<a href='#' class='ui-btn'>OK</a>";
	var nn = "<p>Please only enter numeric characters.</p>";
	var noNum = nn + "<a href='#' class='ui-btn'>OK</a>";
	var t2 = $('#text2').val();
	var t3 = $('#text3').val();
	var checkAN = checkAlphaNums(t2);
	if (checkAN === false) {
		$.mobile.loading("hide");
		$('#text2').text('');
		$('#text3').text('');
		$('#noAlphaNumPopup').popup('open');
	}
	var checkN = checkNums(t3);
	if (checkN === false) {
		$.mobile.loading("hide");
		$('#text2').text('');
		$('#text3').text('');
		$('#noNumPopup').popup('open');
	}
	if (checkAN === true && checkN === true) {
		$('#randomPLForm').hide();
		$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').empty();
		$.get('AddRandomPlaylist',
		{
			 'playlistname' : t2, 'playlistcount' : t3
		},
		(data) => {
			$.each(data.plists, (k, v) => {
				$('#playPlaylistUL').append(oc_randomInput1(v));
				$('#splUL').append(oc_randomInput2(v));
				$('#albsplUL').append(oc_randomInput3(v));
				$('#artsplUL').append(oc_randomInput4(v));
				$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').listview().trigger('refresh');
				if (t2 === v.playlistname) {
					var voo = {'playlist': v.playlistname, 'playlistid': v.playlistid};
					localStorage.setItem('currentSelected_PLAYLIST_PLAYLISTID', JSON.stringify(voo));
				}
			})
		})
		$.get('AllPlaylists', (data) => {
			localStorage.setItem('playlists', JSON.stringify(data));
		})
		
	}
	$.mobile.loading("hide");
})
.on('click', '#nanp', () => {
	$('#noAlphaNumPopup').popup('close');	
	$('#text2').text('');
	$('#text3').text('');
})
.on('click', '#nnp', () => {
	$('#noNumPopup').popup('close');
	$('#text2').text('');
	$('#text3').text('');
})
.on('click', '#playlistDownLoadBtn1', (e) => {
	e.preventDefault();
	let plid = JSON.parse(localStorage.getItem('currentSelected_PLAYLIST_PLAYLISTID'));
	$.get("Download",
	{
		"selectedplid": plid.playlistid
	},
	function(data) {
		window.location = data.zfile;
		$.mobile.loading("hide");
	});
})
//This pauses the Single Song Player when the playlist load button is clicked
//audio1 is the playlistplayer
.on('click', '#playlistLoadBtn1', () => {
/*	$('.playButton').hide();
	$('.stopButton').hide();*/
	$('#audio2').attr('src', '');
	$('.duration, .current').text("00:00").css('background-color', 'black');
})
.on('click', ".songname, .songnameS, .albsongsA, .artsongA1, .rart1, .rart2, .rart3, .rart4, .rart5", () => {
/*	$('.playButton').show();
	$('.stopButton').show();	*/
	$('#audio1').attr('src', '');
//	$('#audio1').hide();
})



;
///////////////////////////////////////////////////////////////////////////////
//////////////////////////// END PLAYLIST PAGE STUFF //////////////////////////////
///////////////////////////////////////////////////////////////////////////////