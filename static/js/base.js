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
function oc_artOF1(xx) {
	var soupArtOne = "<div><img class='artistimgS' src='" + xx + "'></img>";
	var soupArtTwo = soupArtOne + "</div><div class='art1divS'><ul class='artistSongULS' ";
	var soupArtThree1 = soupArtTwo + "data-role='listview' data-inset='true' data-split-icon='gear'>";
	return soupArtThree1			
};
function oc_artOF2(vv) {
	var soupArt1 = "<li class='artSongLIS'><a href='#' class='artsongA1' ";
	var soupArt2 = soupArt1 + "data-songid='" + vv[1] + "'>" + vv[0] + "</a>";
	var soupArt3 = soupArt2 + "<a href='#artistselectplpage' class='artToPlaylistBtn' ";
	var soupArt4 = soupArt3 + "data-song='" + vv[0] + "' data-songid='" + vv[1] + "' ";
	var soupArt51 = soupArt4 + "data-transition='slidefade'></a></li>";
	return soupArt51			
};
function oc_artOF3(v) {
	var a = "<div class='artistPageDiv' data-role='collapsible'><h4>" + v.artist + "</h4><div>";
	var a11 = a + "<form id='" + v.artistid + "' class='artistForm'><div class='ui-field-contain'>";
	var a222 = a11 + "<select name='" + v.artist + "' id='" + v.artistid + "' class='artistselect'>";
	return a222	
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function och_artistselect1(d) {
	var aone = "<div id='songimglist'><img class='artistimg' src='" + d.getimgsonalb.thumbnail + "'></img>";
	var atwo = aone + "<div class='art1div'><ul id='artistSongUL' data-role='listview' data-inset='true' ";
	var athree1 = atwo + "data-split-icon='gear'>";
	return athree1	
};
function och_artistselect2(v1) {
	var four = "<li class='artsongLI'><a href='#' class='artsongA1' ";
	var four1 = four + "data-songid='" + v1[1] + "'>" + v1[0] + "</a><a href='#artistselectplpage' ";
	var four2 = four1 + "class='artToPlaylistBtn' data-song='" + v1[0] + "' data-songid='" + v1[1] + "' ";
	var four31 = four2 + "data-transition='slidefade'></a></li>";
	return four31		
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_albumOF1(va) {
	var alb1 = "<div class='albumDIV'><ul class='albumUL' data-role='listview' data-inset='true'>";
	var alb2 = alb1 + "<li class='albumLI'><a href='#' class='albumA1' data-artist='" + va.artist + "' ";
	var alb3 = alb2 + "data-artistid='" + va.artistid + "' data-album='" + va.album + "' ";
	var alb4 = alb3 + "data-albumid='" + va.albumid + "'><img id='" + va.albumid + "' ";
	var alb5 = alb4 + "src='" + va.thumbnail + "'><h3 id='albH3'>" + va.album + "</h3>";
	var alb6 = alb5 + "<p>" + va.artist + "</p><span class='ui-li-count'>" + va.numsongs + "</span>";
	var alb7 = alb6 + "</a></li></ul></div><div class='albsongList'><ul id='albsongUL" + va.albumid + "' ";
	var alb81 = alb7 + "class='albsongUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
	return alb81
};
function oc_albumOF2(b) {
	var albab = "<li class='albsongsLI'><a href='#' class='albsongsA' data-song='" + b[0] + "' ";
	var albab1 = albab + "data-songid='" + b[1] + "'>" + b[0] + "</a><a href='#albumselectplpage' ";
	var albab2 = albab1 + "class='addToPlaylist' data-pageid='albums' data-song='" + b[0] + "' ";
	var albab31 = albab2 + "data-songid='" + b[1] + "' data-transition='slidefade'></a></li>";
	return albab31			
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_addtoplaylist1(va) {
	var pll1 = "<li class='playlistLi' data-playlistid='" + va[1] + "'><a href='#' class='plplay ui-btn ";
	var pll2 = pll1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	var pll31 = pll2 + "data-playlistid='" + va[1] + "'>" + va[0] + "</a></li>";
	return pll31
};
function oc_addtoplaylist2(va) {
	var spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + va[1] + "' ";
	var spl31 = spl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + va[0] + "</a></li>";
	return spl31
};	
function oc_addtoplaylist3(va) {	
	var ablspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var ablspl2 = ablspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var ablspl3 = ablspl2 + "data-playlistid='" + va[1] + "' data-textonly='false' data-textvisible='false' ";
	var ablspl41 = ablspl3 + "data-msgtext=''>" + va[0] + "</a></li>";
	return ablspl41
};	
function oc_addtoplaylist4(va) {	
	var artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var artspl3 = artspl2 + "data-playlistid='" + va[1] + "' data-textonly='false' data-textvisible='false' ";
	var artspl41 = artspl3 + "data-msgtext=''>" + va[0] + "</a></li>";
	return artspl41
};
function oc_addtoplaylist5(p) {	
	var pll1 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	var pll21 = pll1 + "ui-btn-icon-right'>" + p + "</a></li>";
	return pll21
};
function oc_addtoplaylist6(p) {	
	var spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	var spl31 = spl2 + "data-textvisible='false' data-msgtext=''>" + p + "</a></li>";
	return spl31	
};
function oc_addtoplaylist7(p) {	
	var albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	var albspl31 = albspl2 + "data-textvisible='false' data-msgtext=''>" + p + "</a></li>";
	return albspl31		
};
function oc_addtoplaylist8(p) {	
	var artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	var artspl31 = artspl2 + "data-textvisible='false' data-msgtext=''>" + p + "</a></li>";
	return artspl31		
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_artToPlaylistBtn1(v) {
	var pll1 = "<li class='playlistLi' data-playlistid='" + v[1] + "'><a href='#' class='plplay ui-btn ";
	var pll2 = pll1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	var pll31 = pll2 + "data-playlistid='" + v[1] + "'>" + v[0] + "</a></li>";
	return pll31
};
function oc_artToPlaylistBtn2(v) {
	var spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var spl3 = spl2 + "data-playlistid='" + v[1] + "' data-textonly='false' data-textvisible='false' ";
	var spl41 = spl3 + "data-msgtext=''>" + v[0] + "</a></li>";
	return spl41
};
function oc_artToPlaylistBtn3(v) {
	var albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	var albspl31 = albspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
	return albspl31	
};
function oc_artToPlaylistBtn4(v) {
	var artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	var artspl31 = artspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
	return artspl31
};		
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_addToPlaylist1(v) {
	var pl1 = "<li class='playlistLi' data-playlistid='" + v[1] + "'><a href='#' class='plplay ui-btn ";
	var pl2 = pl1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	var pl31 = pl2 + "data-playlistid='" + v[1] + "'>" + v[0] + "</a></li>";
	return pl31
};
function oc_addToPlaylist2(v) {
	var spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	var spl31 = spl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
	return spl31
};
function oc_addToPlaylist3(v) {
	var albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	var albspl31 = albspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
	return albspl31
};
function oc_addToPlaylist4(v) {
	var artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v[1] + "' ";
	var artspl31 = artspl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v[0] + "</a></li>";
	return artspl31
};
function oc_addToPlaylist5(f) {
	var p1 = "<li class='playlistLi'><a href='#' class='plplay ui-btn ui-mini ui-icon-bullets ";
	var p22 = p1 + "ui-btn-icon-right'>" + f + "</a></li>";
	return p22
};
function oc_addToPlaylist6(f) {
	var spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var spl2 = spl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	var spl32 = spl2 + "data-textvisible='false' data-msgtext=''>" + f + "</a></li>";
	return spl32
};
function oc_addToPlaylist7(f) {
	var albspl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var albspl2 = albspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	var albspl33 = albspl2 + "data-textvisible='false' data-msgtext=''>" + f + "</a></li>";
	return albspl33
};
function oc_addToPlaylist8(f) {
	var artspl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var artspl2 = artspl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-textonly='false' ";
	var artspl33 = artspl2 + "data-textvisible='false' data-msgtext=''>" + f + "</a></li>";
	return artspl33	
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_searchBut(v) {
	var s1 = "<li class='songs_li'><a class='songnameS' href='#' data-songid='" + v.songid + "' ";
	var s2 = s1 + "data-song='" + v.song + "'><h2>" + v.song + "</h2><h6>" + v.artist + "</h6></a>"
	var s3 = s2 + "<a href='#selectplpage' data-pageid='songs' data-songid='" + v.songid + "' ";
	var s41 = s3 + "data-song='" + v.song + "' class='addtoplaylist' data-transition='slidefade'></a></li>";
	return s41		
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_albsearchBut1(f) {
	var alb1 = "<div class='albumDIV'><ul class='albumUL' data-role='listview' data-inset='true'>";
	var alb2 = alb1 + "<li class='albumLI'><a href='#' class='albumA1' data-artist='" + f.artist + "' ";
	var alb3 = alb2 + "data-artistid='" + f.artistid + "' data-album='" + f.album + "' ";
	var alb4 = alb3 + "data-albumid='" + f.albumid + "'><img id='" + f.albumid + "' src='" + f.thumbnail + "'>";
	var alb5 = alb4 + "<h3 id='albH3'>" + f.album + "</h3><p>" + f.artist + "</p>";
	var alb6 = alb5 + "<span class='ui-li-count'>" + f.numsongs + "</span></a></li></ul></div>";
	var alb7 = alb6 + "<div class='albsongList'><ul id='albsongUL" + f.albumid + "' class='albsongUL' ";
	var alb81 = alb7 + "data-role='listview' data-inset='true' data-split-icon='gear'>";
	return alb81
};
function oc_albsearchBut2(v) {
	var albab1 = "<li class='albsongsLI'><a href='#' class='albsongsA' data-song='" + v[0] + "' ";
	var albab2 = albab1 + "data-songid='" + v[1] + "'>" + v[0] + "</a><a href='#albumselectplpage' ";
	var albab3 = albab2 + "class='addToPlaylist' data-pageid='albums' data-song='" + v[0] + "' ";
	var albab44 = albab3 + "data-songid='" + v[1] + "' data-transition='slidefade'></a></li>";
	return albab44
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_artsearchBut1(m) {
	var a1 = "<div><img class='artistimgS' src='" + m + "'></img></div>";
	var a2 = a1 + "<div class='art1divS'><ul class='artistSongULS' data-role='listview' ";
	var a37 = a2 + "data-inset='true' data-split-icon='gear'>";
	return a37
};
function oc_artsearchBut2(n) {
	var art31 = "<li class='artSongLIS'><a href='#' class='artsongA1' ";
	var art32 = art31 + "data-songid='" + n[1] + "'>" + n[0] + "</a>";
	var art33 = art32 + "<a href='#artistselectplpage' class='artToPlaylistBtn' ";
	var art342 = art33 + "data-songid='" + n[1] + "' data-transition='slidefade'></a></li>";
	return art342
};
function oc_artsearchBut3(n) {
	var artA1 = "<div class='artistPageDivSearch' data-role='collapsible'><h4>" + n.artist + "</h4>";
	var artA2 = artA1 + "<div><form id='" + n.artistid + "' class='artistForm'><div ";
	var artA3 = artA2 + "class='ui-field-contain'><select ";
	var artA46 = artA3 + "name='" + n.artist + "' id='" + n.artistid + "' class='artistselect'>";
	return artA46
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_homeBTN_fraz1(b) {
	var b1 = "<div class='ui-block-a' data-theme='a'><a href='#popup1' data-rel='popup' data-transition='pop'>";
	var b2 = b1 + "<img src='" + b.rsamp[0].thumbnail + "' class='PicGrid'></img></a></div>";
	var b3 = b2 + "<div class='ui-block-b' data-theme='a'><a href='#popup2' data-rel='popup' data-transition='pop'>";
	var b4 = b3 + "<img src='" + b.rsamp[1].thumbnail + "' class='PicGrid'></img></a></div>";
	var b5 = b4 + "<div class='ui-block-c' data-theme='a'><a href='#popup3' data-rel='popup' data-transition='pop'>";
	var b6 = b5 + "<img src='" + b.rsamp[2].thumbnail + "' class='PicGrid'></img></a></div>";
	var b7 = b6 + "<div class='ui-block-d' data-theme='a'><a href='#popup4' data-rel='popup' data-transition='pop'>";
	var b8 = b7 + "<img src='" + b.rsamp[3].thumbnail + "' class='PicGrid'></img></a></div>";
	var b9 = b8 + "<div class='ui-block-e' data-theme='a'><a href='#popup5' data-rel='popup' data-transition='pop'>";
	var result12 = b9 + "<img src='" + b.rsamp[4].thumbnail + "' class='PicGrid'></img></a></div>";
	return result12
};
function oc_homeBTN_fraz2(b) {
	var pu11 = "<ul id='pop1' data-role='listview' class='ui-content' data-insert='true'>"
	var pu12 = '';
	$.each(b.rsamp[0].songs, function (key, val) {
		var s11 = "<li><a href='#' class='rart1' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu12 = pu12 + s11;
		return pu12
	})
	var pu111 = pu11 + pu12 + "</ul>";
	$('#popup1').append(pu111);
	$('#pop1').listview().trigger('refresh');
	$('#popup1').popup().trigger('create');
};
function oc_homeBTN_fraz3(b) {
	var pu21 = "<ul id='pop2' data-role='listview' class='ui-content' data-insert='true'>";
	var pu22 = '';
	$.each(b.rsamp[1].songs, function (key, val) {
		var s22 = "<li><a href='#' class='rart2' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu22 = pu22 + s22;
		return pu22
	})
	var pu211 = pu21 + pu22 + "</ul>";
	$('#popup2').append(pu211);
	$('#pop2').listview().trigger('refresh');
	$('#popup2').popup().trigger('create');
};
function oc_homeBTN_fraz4(b) {
	var pu31 = "<ul id='pop3' data-role='listview' class='ui-content' data-insert='true'>";
	var pu32 = '';
	$.each(b.rsamp[2].songs, function (key, val) {	
		var s31 = "<li><a href='#' class='rart3' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu32 = pu32 + s31;
		return pu32
	})
	var pu311 = pu31 + pu32 + "</ul>";
	$('#popup3').append(pu311);
	$('#pop3').listview().trigger('refresh');
	$('#popup3').popup().trigger('create');
};
function oc_homeBTN_fraz5(b) {
	var pu41 = "<ul id='pop4' data-role='listview' class='ui-content' data-insert='true'>";
	var pu42 = '';
	$.each(b.rsamp[3].songs, function (key, val) {	
		var s41 = "<li><a href='#' class='rart4' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu42 = pu42 + s41
	})
	var pu411 = pu41 + pu42 + "</ul>";
	$('#popup4').append(pu411);
	$('#pop4').listview().trigger('refresh');
	$('#popup4').popup().trigger('create');
};
function oc_homeBTN_fraz6(b) {
	var pu51 = "<ul id='pop5' data-role='listview' class='ui-content' data-insert='true'>";	
	var pu52 = '';
	$.each(b.rsamp[4].songs, function (key, val) {
		var s51 = "<li><a href='#' class='rart5' data-songid='" + val[1] + "'>" + val[0] + "</a></li>";
		pu52 = pu52 + s51
	})
	var pu511 = pu51 + pu52 + "</ul>";
	$('#popup5').append(pu511);
	$('#pop5').listview().trigger('refresh');
	$('#popup5').popup().trigger('create');
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function singPlayer1(d) {
	$('#introimg').attr('src', d.soho[1]);
	$('#playlistalbart').attr('src', d.soho[1]);
	$('#pictext').text(d.soho[2]);
	$('#pictext2').text(d.soho[3]);
	audio2 = $('#audio2');
	audio2.attr('src', d.soho[0]);
	audio2.on('loadedmetadata', function () {
		var dur = audio2[0].duration;
		var cd = calcDuration(dur);
		$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
	});
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_butsub1(v) {
	var npl1 = "<li class='playlistLi' data-playlistid='" + v.playlistid + "'><a href='#' ";
	var npl2 = npl1 + "class='plplay ui-btn ui-mini ui-icon-bullets ui-btn-icon-right' ";
	var npl31 = npl2 + "data-playlistid='" + v.playlistid + "'>" + v.playlistname + "</a></li>"
	return npl31
};
function oc_butsub2(v) {
	var npl21 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var npl22 = npl21 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var npl23 = npl22 + "data-playlistid='" + v.playlistid + "' data-textonly='false' ";
	var npl242 = npl23 + "data-textvisible='false' data-msgtext=''>" + v.playlistname + "</a></li>";
	return npl242
};
function oc_butsub3(v) {
	var npl31 = "<li><a href='#artists' class='artSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var npl32 = npl31 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var npl33 = npl32 + "data-playlistid='" + v.playlistid + "' data-textonly='false' data-textvisible='false' ";
	var npl344 = npl33 + "data-msgtext=''>" + v.playlistname + "</a></li>";
	return npl344
};
function oc_butsub4(v) {
	var npl41 = "<li><a href='#albumssongs' class='albSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var npl42 = npl41 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' data-playlistid='" + v.playlistid + "' ";
	var npl437 = npl42 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v.playlistname + "</a></li>";
	return npl437
};
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
function oc_randomInput1(v) {
	var p1 = "<li class='playlistLi' data-playlistid='" + v.playlistid + "'><a href='#' class='plplay ui-btn ";
	var p2 = p1 + "ui-mini ui-icon-bullets ui-btn-icon-right' ";
	var p36 = p2 + "data-playlistid='" + v.playlistid + "'>" + v.playlistname + "</a></li>";
	return p36
};
function oc_randomInput2(v) {
	var spl1 = "<li><a href='#songs' class='songSelBtn show-page-loading-msg ui-btn ui-btn-mini ui-icon-bullets ";
	var spl2 = spl1 + "ui-btn-icon-right ui-corner-all' data-playlistid='" + v.playlistid + "' ";
	var spl35 = spl2 + "data-textonly='false' data-textvisible='false' data-msgtext=''>" + v.playlistname + "</a></li>";
	return spl35
};
function oc_randomInput3(v) {
	var alpl1 = "<li><a href='#albums' class='albumSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var alpl2 = alpl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var alpl3 = alpl2 + "data-playlistid='" + v.playlistid + "' data-textonly='false' data-textvisible='false' ";
	var alpl43 = alpl3 + "data-msgtext=''>" + v.playlistname + "</a></li>";
	return alpl43
};	
function oc_randomInput4(v) {	
	var arpl1 = "<li><a href='#artists' class='artistSelBtn show-page-loading-msg ui-btn ui-btn-mini ";
	var arpl2 = arpl1 + "ui-icon-bullets ui-btn-icon-right ui-corner-all' ";
	var arpl3 = arpl2 + "data-playlistid='" + v.playlistid + "' data-textonly='false' data-textvisible='false' ";
	var arpl49 = arpl3 + "data-msgtext=''>" + v.playlistname + "</a></li>";
	return arpl49
};

//This makes Artist soup
$(document).on('click', '.artOF', function () {
	var artass = $(this).text();
	$('#artistOFC').collapsible("collapse");
	$('#artistmain').empty();
	$.get('GetArtistInfo', 
	{
		'selected': artass
	},
	function (data) {
		$.each(data.arts, function ( key, val ) {
			var alblength = val.albums.length;
			var abc = "<div class='artistPageDivS' data-role='collapsible'><h4>" + val.artist + "</h4>";
			var selected = val.albums[0][1];
			if ( alblength === 1 ) {
				$.get('GetImageSongsForAlbum', 
				{
					'selected' : selected
				}, 
				function (data) {
					var soupArtThree = oc_artOF1(data.getimgsonalb.thumbnail);
					var artSoupLI = '';
					$.each(data.getimgsonalb.songs, function (kk, vv) {
						var soupArt5 = oc_artOF2(vv);
						artSoupLI = artSoupLI + soupArt5;
						return artSoupLI;
					})
					var result2 = abc + soupArtThree + artSoupLI + "</ul></div>";
					$('#artistmain').append(result2);
					$('.artistPageDivS').collapsible().trigger('create');
				})
				
			} else {
				var a22 = oc_artOF3(val);
				var a2 = '';
				var a3 = '';
				var aa1 = "<option class='artop0' value='Choose Album'>Choose Album</option>";
				$.each(val.albums, function (k, v) {
					var a1 = "<option class='artop1' value='" + v[1] + "'>" + v[0] + "</option>";
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
//This get selected song from artist page and sends it to the player
.on('click', '.artsongA1', function () {
	var booty = {'song': $(this).text(), 'songid': $(this).attr('data-songid')}
	localStorage.setItem('artistPageSelected_SONG_SONGID', JSON.stringify(booty));
	$.get("GetPathArt",
	{
		"selected": booty.songid
	},
	function(data) {
		$('#audio2').attr('src', data.httpmusicpath);
		$('#introimg').attr('src', data.albumart);
		$('#playlistalbart').attr('src', data.albumart);
		$('#pictext').text(data.song);
		$('#pictext2').text(data.album);
		localStorage.setItem('artistPageGetPathArt', JSON.stringify(data));
	});
	var  audio22 = $('#audio2');
	audio22.on('loadedmetadata', function () {
		var dur = audio22[0].duration;
		var cd = calcDuration(dur);
		$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
	});
})
//This fetches the selected album and displays albumart and
//song list for artist page
.on('change', '.artistselect', function () {
	$('.artistimg').remove(); //Clear albumart and songs list
	$('.art1div').empty();
	artistid = $(this).attr('id'); //This is the artistid of the selected album	
	selected = $(this).find(':selected').val(); //this is selected albumid
	$.get('GetImageSongsForAlbum',
		{
			'selected' : selected //this is albumid	
		},
		function (data) {
			var athree = och_artistselect1(data);
			var artLIString = ''
			$.each(data.getimgsonalb.songs, function (k, v) {
				var four3 = och_artistselect2(v);
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
.on('collapsiblecollapse', '.artistPageDiv', function () {
	$('.artistimg').remove();
	$('.art1div').empty();
})
//This gets playlist selection and adds song to playlistdb for the artist page
.on('click', '.artistSelBtn', function () {
	var selectedPlayList = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
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
.on('click', '.albumA1', function () {
	bebe = "#albsongUL" + $(this).attr('data-albumid');
	$(bebe).fadeToggle('fast');
})
.on('click', '.albumOF', function () {
	var albass = $(this).text();
	$('#albumOFC').collapsible("collapse");
	$('#alblist').empty();
	$.get('GetAlbumInfo', 
	{
		'selected': albass
	},
	function (data) {
		$.each(data.albs, function ( key, val) {
			var alb8 = oc_albumOF1(val);
			var alba33 = '';
			$.each(val.songs, function (ka, val) {
				$.each(val, function (kk, vv) {
					$.each(vv, function (k, v) {
						alba33 = alba33 + oc_albumOF2(v);
						return alba33
					});
				});
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
.on('click', '.albsongsA', function () {
	var selSong = $(this).attr('data-songid');
	$.get("GetPathArt",
	{
		"selected": selSong
	},
	function(data){
		var foobar10 = {'song': data.song, 'songid': selSong};
		$('#audio2').attr('src', data.httpmusicpath);
		$('#introimg').attr('src', data.albumart);
		$('#playlistalbart').attr('src', data.albumart);
		$('#pictext').text(data.song);
		$('#pictext2').text(data.album);
		localStorage.setItem('albumPageGetPathArt ', JSON.stringify(data));
		localStorage.setItem('albumPageSelected_SONG_SONGID', JSON.stringify(foobar10));
	});
	var  audio23 = $('#audio2');
	audio23.on('loadedmetadata', function () {
		var dur = audio23[0].duration;
		var cd = calcDuration(dur);
		$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
	});
	$('.albsongUL').hide();
})
//This adds the song and songid to localstorage 
.on('click', '.addToPlaylist', function () {
	var albssid = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')}	
	localStorage.setItem('albumPageSelected_SONG_SONGID', JSON.stringify(albssid));
})
//This gets the songs for the selected Alpha selecter
.on('click', '.songOF', function () {
	var ss = $(this).text();
	$('#songOFC').collapsible("collapse");
	$("#songs_view").empty();
	$.get('GetSongInfo',
	{
		'selected': ss
	},
	function (data) {
		$.each(data.song, function ( key, val) {
			var ss1 = "<li class='songs_li'><a class='songname' href='#' data-songid='" + val.songid + "'>";
			var ss2 = ss1 + "<h2>" + val.song + "</h2><h6>" + val.artist + "</h6></a><a href='#selectplpage' ";
			var ss3 = ss2 + "data-song='" + val.song + "' data-songid='" + val.songid + "' class='addtoplaylist' ";
			var ss4 = ss3 + "data-transition='slidefade'></a></li>";
			$("#songs_view").append(ss4);
		});
		$('#songs_view').listview('refresh');
		$.mobile.loading("hide");
	});
})
//This gets the selected song from the first anchor 
//use data-song and data-songid they are set
//this should use songid instead of songname
.on('click', 'a.songname', function () {
	var selected_songid = $(this).attr('data-songid');
	var audio2 = $('#audio2');
	audio2.attr('src', '');
	$('.duration').text('OO:00');
	$.get("GetPathArt",
	{
		"selected": selected_songid
	},
	function(data) {
		audio2.attr('src', data.httpmusicpath);
		$('#introimg').attr('src', data.albumart);
		$('#playlistalbart').attr('src', data.albumart);
		$('#pictext').text(data.song);
		$('#pictext2').text(data.album);
		var booob = {'song': data.song, 'songid': data.songid};
		localStorage.setItem('songPageGetPathArt', JSON.stringify(data));
		localStorage.setItem("songPageSelected_SONG_SONGID", JSON.stringify(booob));
	});
	audio2.on('loadedmetadata', function () {
		var dur = audio2[0].duration;
		var cd = calcDuration(dur);
		$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
	});	
})
//This sets the selectedSONG and selectedSONGid in the browser localstorage
//for the add to playlist button on the songs page.
.on('click', '.addtoplaylist', function () {
	var sname = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')}
	localStorage.setItem('songPageSelected_SONG_SONGID', JSON.stringify(sname));
	$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').empty();
	$.get("GetAllPlaylists",
	{
		"selected": sname.songid
	},
	function(data) {
		if ( data.plnames != 'Please create a playlist' ) {
			localStorage.setItem('playlists', JSON.stringify(data));
			$.each(data.plnames, function (k, va) {
				$('#playPlaylistUL').append(oc_addtoplaylist1(va));
				$('#splUL').append(oc_addtoplaylist2(va));
				$('#albsplUL').append(oc_addtoplaylist3(va));
				$('#artsplUL').append(oc_addtoplaylist4(va));	
			});
		} else {
			var pln = 'Please create a playlist';
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
.on('click', '.artToPlaylistBtn', function () {
	var arr = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')};
	localStorage.setItem("artistPageSelected_SONG_SONGID", JSON.stringify(arr));
	$('#playPlaylistUL, #artsplUL, #albsplUL, #splUL').empty();
	$.get("GetAllPlaylists",
	{
		"selected": arr.songid
	},
	function(data) {
		$.each(data.plnames, function (k, v) {
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
.on('click', '.addToPlaylist', function () {
	var sname2 = {'song': $(this).attr('data-song'), 'songid': $(this).attr('data-songid')};
	localStorage.setItem("albumPageSelected_SONG_SONGID", JSON.stringify(sname2));
	$.get("GetAllPlaylists",
	{
		"selected": sname2.songid
	},
	function(data) {
		localStorage.setItem('playlists', JSON.stringify(data));
		$('#playPlaylistUL, #splUL, #albsplUL, #artsplUL').empty();
		if ( data.plnames != 'Please create a playlist' ) {
			$.each(data.plnames, function (k, v) {
				$('#playPlaylistUL').append(oc_addToPlaylist1(v));
				$('#splUL').append(oc_addToPlaylist2(v));
				$('#albsplUL').append(oc_addToPlaylist3(v));
				$('#artsplUL').append(oc_addToPlaylist4(v));
			});
		} else {
			var plnln = 'Please create a playlist';
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
.on('click', '.albumSelBtn', function () {
	var selectedPlaylist1 = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
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
.on('click', '.songSelBtn', function () {
	var selectedPlaylist2 = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
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
//This is the player controls for the artist, album, and songs page
.on('click', '.stopButton', function () {	
	$(".duration, .current").css('background-color', 'firebrick');
	$('#audio2').get(0).pause();
})
.on('click', '.playButton', function () {
	$('#audio1').attr('src', '');
	$('.duration, .current').css('background-color', 'purple');
	var audio2 = $('#audio2');
	audio2[0].play();
	audio2.on('timeupdate', function () {
		var ct = audio2[0].currentTime;
		var cd = calcDuration(ct);
		$('.current').text(cd[0] + ':' + cd[1]);
	});
	audio2.on('ended', function () {
		$('.duration, .current').text("00:00").css('background-color', 'black');
	});
})
.on('click', '#searchBut', function () {
	searchVal = $('#search-basic').val();
	$.get('SongSearch',
	{
		'searchval' : searchVal,
	},
	function(data) {
		$('#songs_view, #songs_view2').empty();
		$.each(data.xsearch, function ( k, v) {
			var s4 = oc_searchBut(v);
			$("#songs_view2").append(s4);
		});
		$('#songs_view2').listview('refresh');
		$.mobile.loading("hide");
	});
})
.on('click', 'a.songnameS', function () {
	var selected_song = $(this).attr('data-songid');
	var audio2 = $('#audio2');
	audio2.attr('src', '');
	$('.duration').text('OO:00');
	$.get("GetPathArt",
	{
		"selected": selected_song
	},
	function(data,status){
		audio2.attr('src', data.httpmusicpath);
		$('#introimg').attr('src', data.albumart);
		$('#playlistalbart').attr('src', data.albumart);
		$('#pictext').text(data.song);
		$('#pictext2').text(data.album);
		var boob = {'song': data.song, 'songid': data.songid};
		localStorage.setItem('songPageGetPathArt', JSON.stringify(data));
		localStorage.setItem("songPageSelected_SONG_SONGID", JSON.stringify(boob));
	});
	audio2.on('loadedmetadata', function () {
		var dur = audio2[0].duration;
		var cd = calcDuration(dur);
		$('.duration').text(cd[0] + ':' + cd[1]).css('background-color', 'purple');
	});	
})
.on('click', '#searchClear', function () {
	$('#search-basic').val('');
	$("#songs_view2").empty();
})
.on('click', '#SS', function () {
	$('#SSD1, #SSD2, #songListViewDIV2').fadeToggle('fast');
})
.on('click', '#albsearchBut', function () {
	$('.albumDIV, .albsongList').empty();
	$('#albsearch-basic').textinput({preventFocusZoom: true});
	albsearchVal = $("#albsearch-basic").val();
	$.get('AlbumSearch',
	{
		'albsearchval' : albsearchVal,
	},
	function(data) {
		$('#albListViewDIV2').empty();
		$.each(data.ysearch, function ( ke, va) {
			var alb8 = oc_albsearchBut1(va);
			var alba33 = '';
			$.each(va.songs, function (k, v) {
				$.each(v, function (kk, vv) {
					console.log('this is albumsearchBut vv[0]');
					console.log(vv[0]);
					var albab4 = oc_albsearchBut2(vv);
					alba33 = alba33 + albab4;
					return alba33
				});
			});
			var result = alb8 + alba33 + "</ul></div>";
			$('#albListViewDIV2').append(result);
			$('.albumUL, .albsongUL').listview().trigger('refresh');
			$('.albsongUL').hide();
			$.mobile.loading("hide");
		});
	});
})
.on('click', '#albsearchClear', function () {
	$('#albsearch-basic').val('');
	$('#albListViewDIV2').fadeToggle('fast').empty();
})
.on('click', '#albSS', function () {
	$('#albSSD1, #albSSD2, #albListViewDIV2').fadeToggle('fast');
})
.on('click', '#artsearchBut', function () {
	$('#artistmain').empty();
	artsearchval = $('#artsearch-basic').val();
	$.get('ArtistSearch',
	{
		"artsearchval" : artsearchval,
	},
	function (data) {
		$.each(data, function ( key, val ) {		
			$.each(val, function ( ke, va ) {
				alblength = va.albums.length;
				if ( alblength === 1 ) {
					var abc = "<div class='artistPageDivS' data-role='collapsible'><h4>" + va.artist + "</h4>";
					var selected = va.albums[0][1]; //this is albumid
					$.get('GetImageSongsForAlbum',
						{
							'selected' : selected	//this is albumid	
						},
						function (data) {
							var a3 = oc_artsearchBut1(data.getimgsonalb.thumbnail);							
							liString = '';
							$.each(data.getimgsonalb.songs, function (kk, vv) {
								var art34 = oc_artsearchBut2(vv);
								liString = liString + art34;
								return liString;
							})
							var result2 = abc + a3 + liString + "</ul></div>";
							$('#artSearchDIV').append(result2);
							$('.artistPageDivS').collapsible().trigger('create');	
					});
				} else {
					var artA4 = oc_artsearchBut3(va);
					var a2 = ''
					var aa1 = "<option class='artop0' value='Choose Album'>Choose Album</option>";
					$.each(va.albums, function (k, v) {
						var a1 = "<option class='artop1' value='" + v[1] + "'>" + v[0] + "</option>";
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
.on('click', '#artSS', function () {
	$('#artForm').fadeToggle('fast');
})
.on('click', '#search-basic', function () {
	$('#search-basic').val('');
})
.on('click', '#artsearch-basic', function () {
	$('#artsearch-basic').val('');
})
.on('click', '#albsearch-basic', function () {
	$('#albsearch-basic').val('');
})
.on('click', '#artsearchClear', function () {
	$('#artsearch-basic').val('');
	$('#artSearchDIV').empty();
	$.mobile.loading("hide");
})
.on('click', '#videolistViewA', function () {
	$('#audio1').attr('src', '');
	$('#audio2').attr('src', '');
	var vAddr = $(this).attr('data-vidAddr');
	var vId = $(this).attr('data-videoID');
	$('#vid100').attr('src', vAddr);
})
.on('click', '#vartists, #valbums, #vsongs, #vplaylists, #vvideos', function () {
	$('#vid100').attr('src', '');
})
.on('click', '#vidH3', function () {
	$('#vid1DIV').fadeToggle('fast');
	$('#vid1').attr('src', '');
})
.on('click', '.homeBTN, .fraz', function () {
	rpwStop();
	$('#popup1, #popup2, #popup3, #popup4, #popup5, #intropicGrid1').empty();
	var boohoo = JSON.parse(localStorage.getItem('nextimgset'));
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
.on('click', '.rart1', function () {
	var sid = $(this).attr('data-songid');
	$('#popup1').popup('close');
	$.get('RamdomAlbumPicPlaySong',
	{
		'sid' : sid
	},
	function (data) {
		singPlayer1(data);
	});
	rpwStart();
})
.on('click', '.rart2', function () {
	var sid = $(this).attr('data-songid');
	$('#popup2').popup('close');
	$.get('RamdomAlbumPicPlaySong',
	{
		'sid' : sid
	},
	function (data) {
		singPlayer1(data);
	});
	rpwStart();
})
.on('click', '.rart3', function () {
	var sid = $(this).attr('data-songid');
	$('#popup3').popup('close');
	$.get('RamdomAlbumPicPlaySong',
	{
		'sid' : sid
	},
	function (data) {
		singPlayer1(data);
	});
	rpwStart();
})
.on('click', '.rart4', function () {
	var sid = $(this).attr('data-songid');
	$('#popup4').popup('close');
	$.get('RamdomAlbumPicPlaySong',
	{
		'sid' : sid
	},
	function (data) {
		singPlayer1(data);
	});
	rpwStart();
})
.on('click', '.rart5', function () {
	var sid = $(this).attr('data-songid');
	$('#popup5').popup('close');
	$.get('RamdomAlbumPicPlaySong',
	{
		'sid' : sid
	},
	function (data) {
		singPlayer1(data);
	});
	rpwStart();
})
.on('click', '#intropicGrid1', function () {
	rpwStop();
})
.on("click", ".hide-page-loading-msg", function () {
	$.mobile.loading("hide");
})
//This shows our spinner during ajax calls
.on('click', ".show-page-loading-msg", function () {
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
//$(document).on('click', '.playlistLi', function () {
.on('click', '.playlistLi', function () {
	$('#controlGrid').fadeToggle('fast');
	$('#playlistcollapsible').collapsible('collapse');
})
.on('click', '.plssel, .pldl', function () {
	$('#controlGrid').fadeToggle('fast');
})
.on('click', '#randomInput', function () {
	$('#addrandomplaylist').collapsible('collapse');
})
//This adds a new playlist to the db
.on('click', '#butsub', function () {
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
			$.each(data.pnames, function (k, v) {
				var pln = {'playlist': v.playlistname, 'playlistid': v.playlistid};
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
		console.log("need a popup to handle non alpha numeric characters errror");
		$.mobile.loading("hide");
	}
})
//Get current selected playlist
.on('click', '.plplay', function () {
	taz = {'playlist': $(this).text(), 'playlistid': $(this).attr('data-playlistid')};
	localStorage.setItem("currentSelected_PLAYLIST_PLAYLISTID", JSON.stringify(taz));
	$('#playlistcollapsible').collapsible('collapse');
	$('#audio1').show();
})
//delete a playlist
.on('click', '#playlistDeleteBtn1', function () {
	$('#playPlaylistUL').empty();
	var selpl = JSON.parse(localStorage.getItem("currentSelected_PLAYLIST_PLAYLISTID"));
	$.get('DeletePlaylistFromDB',
	{
		"playlistid" : selpl.playlistid
	},
	function (data) {
		localStorage.setItem('playlists', JSON.stringify(data));
		$.each(data.npl, function (k, v) {
			var pllone = "<li class='playlistLi' data-playlistid='" + v.playlistid + "'><a href='#' class='plplay ";
			var plltwo = pllone + "ui-btn ui-mini ui-icon-bullets ui-btn-icon-right' ";
			var pllthree = plltwo + "data-playlistid='" + v.playlistid + "'>" + v.playlistname + "</a></li>";
			$('#playPlaylistUL').append(pllthree);
		})
		$('#playPlaylistUL').listview('refresh');
		$.mobile.loading("hide");
	});
})
.on('click', '#playlistEditBtn1', function () {
	$("#pleditMain").empty();
	var pln33 = JSON.parse(localStorage.getItem("currentSelected_PLAYLIST_PLAYLISTID"));
	var blep = "<div id='pledith3'><h3>Edit: " + pln33.playlist + "</h3></div>";
	$.get('GetAllPlaylistSongsFromDB',
	{
		'playlistid' : pln33.playlistid
	},
	function (data) {
		var ple1 = "<div class='pleditLV'>";
		var ple = ple1 + "<ul class='editplUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
		var s3 = "";
		$.each(data.taz, function (key, val) {
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
	$.get('GetAllPlaylists', function (data) {
		localStorage.setItem('playlists', JSON.stringify(data));
	})
	$.mobile.loading("hide");
})
.on('click', '.lviewLi', function () {
	delsong = {'delsong': $(this).text(), 'delsongid': $(this).attr('data-sonID')};
	localStorage.setItem('editPageSelected_SONG_SONGID', JSON.stringify(delsong));
})
//This sets the values in the delete popup
.on('click', '.plpsongsA2', function () {
	var plsnid = {'dsongid': $(this).attr("data-sonID")};
	crock = localStorage.setItem("editPage_DELETE_SONGID", JSON.stringify(plsnid));
})
.on('click', '#editYesBtn' , function () {
	$('#pleditMain').empty();
	var snID = JSON.parse(localStorage.getItem("editPage_DELETE_SONGID"));
	var pln = JSON.parse(localStorage.getItem("currentSelected_PLAYLIST_PLAYLISTID"));
	var blep = "<div id='pledith3'><h3>Edit: " + pln.playlist + "</h3></div>";
	var ple1 = "<div class='pleditLV'>";
	var ple = ple1 + "<ul class='editplUL' data-role='listview' data-inset='true' data-split-icon='gear'>";
	$.getJSON("DeleteSongFromPlaylist",
	{
		"playlistname" : pln.playlist, 'delsongid' : snID.dsongid
	},
	function (data) {
		var s3 = "";
		$.each(data, function (key, valu) {
			$.each(valu, function (key, val) {
				$.each(val, function (k, v) {
					var lvLI1 = "<li><a href='#' class='lviewLi' data-sonID='" + v.songid + "'>" + v.song + "</a>";
					var lvLI2 = lvLI1 + "<a href='#editpopup' data-sonID='" + v.sonID + "' data-rel='popup' ";
					var lvLI3 = lvLI2 + "class='plpsongsA2  ui-btn' data-textonly='false' data-textvisible='false' ";
					var lvLI4 = lvLI3 + "data-msgtext=''></a></li>";
					s3 = s3 + lvLI4;
					return s3
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
.on('click', '#text2', function () {
	$('#text2').val('');
})
.on('click', '#text3', function () {
	$('#text3').val('');
})
//This adds a random playlist to the db
.on('click', '#randomInput', function () {
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
		function (data) {
			$.each(data.plists, function (k, v) {
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
		$.get('GetAllPlaylists', function (data) {
			localStorage.setItem('playlists', JSON.stringify(data));
		})
		
	}
	$.mobile.loading("hide");
})
.on('click', '#nanp', function () {
	$('#noAlphaNumPopup').popup('close');	
	$('#text2').text('');
	$('#text3').text('');
})
.on('click', '#nnp', function () {
	$('#noNumPopup').popup('close');
	$('#text2').text('');
	$('#text3').text('');
})
.on('click', '#playlistDownLoadBtn1', function (e) {
	e.preventDefault();
	var plid = JSON.parse(localStorage.getItem('currentSelected_PLAYLIST_PLAYLISTID'));
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
.on('click', '#playlistLoadBtn1', function () {
	$('.playButton').hide();
	$('.stopButton').hide();
	$('#audio2').attr('src', '');
	$('.duration, .current').text("00:00").css('background-color', 'black');
})
.on('click', ".songname, .songnameS, .albsongsA, .artsongA1, .rart1, .rart2, .rart3, .rart4, .rart5", function () {
	$('.playButton').show();
	$('.stopButton').show();	
	$('#audio1').attr('src', '');
	$('#audio1').hide();
})
.on('click', ".navPls, .navVid", function () {
	if ($('#audio2')[0].duration > 0 && !$('#audio2')[0].paused) {
		$('.playButton, .stopButton').show();
		$('#audio1').hide();
	} else {
		$('.playButton, .stopButton').hide();
		$('#audio1').show();
	}
})
.on('click', ".navArt, .navAlb, .navSong, .navVid", function () {
	if ($('#audio1')[0].duration > 0 && !$('#audio1')[0].paused) {
		$('.playButton, .stopButton').hide();
		$('#audio1').show();
	} else {
		$('.playButton, .stopButton').show();
		$('#audio1').hide();
	}
});
///////////////////////////////////////////////////////////////////////////////
//////////////////////////// END PLAYLIST PAGE STUFF //////////////////////////////
///////////////////////////////////////////////////////////////////////////////