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
















///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
