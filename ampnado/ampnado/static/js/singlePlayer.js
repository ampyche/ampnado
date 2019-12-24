
//This is the player controls for the artist, album, and songs page
function calcDuration(d) {
	var hr = Math.floor(d / 3600);
	var min = Math.floor((d - (hr * 3600))/60);
	var sec = Math.floor(d - (hr * 3600) - (min * 60));	
	if (min < 10) { min = "0" + min; };
	if (sec < 10) { sec = '0' + sec; };
	return [min, sec];
};

function singPlayer1(d) {
	console.log(d.soho);
	$('#introimg').attr('src', d.soho['AlbumArtHttpPath']);
	$('#playlistalbart').attr('src', d.soho['AlbumArtHttpPath']);
	$('#pictext').text(d.soho['Song']);
	$('#pictext2').text(d.soho['Album']);
	audio25 = $('#audio2');
	audio25.attr('src', d.soho['HttpMusicPath']);
	audio25.on('loadedmetadata', function () {
		var dur = audio25[0].duration;
		var cd = calcDuration(dur);
		var ftxt2 = d.soho['Song'] + " " + d.soho['Artist'];
		$('.footerSong').text(d.soho['Song']);
		$('.footerArtist').text(d.soho['Artist']);
		$('.PlayBtn').text("Play 00:00").css('background-color', 'grey').css('color', 'black');
		$('.StopBtn').text("Stop " + cd[0] + ':' + cd[1]).css('background-color', 'grey').css('color', 'black');
	});
};

$(document).on('click', '.playButton, .PlayBtn', function () {
	$('#audio1').attr('src', '');
	$('.duration, .current').css('background-color', 'green').css('color', 'white');
	$('.PlayBtn, .StopBtn').css('background-color', 'darkviolet').css('color', 'white');
//	$('.StopBtn').css('background-color', 'darkviolet').css('color', 'white');
	var audio2 = $('#audio2');
	audio2[0].play();
	dur = audio2[0].duration;
	caldur = calcDuration(dur);
	audio2.on('timeupdate', function () {
		var ct = audio2[0].currentTime;
		var cd = calcDuration(ct);
		$('.current').text(cd[0] + ':' + cd[1]);
		$('.PlayBtn').text("Play " + cd[0] + ':' + cd[1]);
	});
	audio2.on('ended', function () {
		$('.duration, .current').text("00:00").css('background-color', 'black').css("color", "white");
		$('.PlayBtn, .StopBtn').css('background-color', 'black').css("color", "white");
	});
})
.on('click', '.StopBtn, .stopButton', function () {
	$('#audio2').get(0).pause();
	$('.StopBtn').css('background-color', 'grey').css("color", "black");
	$('.PlayBtn').css('background-color', 'grey').css('color', 'black');
})
.on('click', '.rart1', function () {
	var sid = $(this).attr('data-songid');
	$('#popup1').popup('close');
	
	$.get('RandomAlbumPicPlaySong',
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
	
	$.get('RandomAlbumPicPlaySong',
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
	
	$.get('RandomAlbumPicPlaySong',
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

	$.get('RandomAlbumPicPlaySong',
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

	$.get('RandomAlbumPicPlaySong',
	{
		'sid' : sid
	},
	function (data) {
		singPlayer1(data);
	});
	rpwStart();
})
;