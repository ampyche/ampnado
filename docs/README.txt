Ampnado is very dependent on mp3 tags.  Please insure that the mp3
files are tagged correctly, there are several mp3 taggers such as
picard, and eyeD3.

Install the following softwares:
	pymongo
	PIL
	mutagen or mutagenx
	tornado
	mongodb
	
To enable text search in versions of mongodb where textsearch is not enabled do:

	mongod --setParameter textSearchEnabled=true

	or via mongo shell

	db.adminCommand({setParameter:true, textSearchEnabled:true})


To setup AmpNado use the setup script in /usr/share/ampnado:

	usage: ampnado_setup.py [-h] [-c CAT_NAME] [-o OFFSET_SIZE] [-P PWORD]
	                        [-U UNAME]
	                        MusicPath ServerAddr
	
	Setup AmpNado
	
	positional arguments:
	  MusicPath             Path to the Music Collection
	  ServerAddr            The Server Address
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -c CAT_NAME, --cat-name CAT_NAME
	                        Catalog Name or Music collection name, default is
	                        current date
	  -o OFFSET_SIZE, --offset-size OFFSET_SIZE
	                        Items per page to show, default is 15
	  -P PWORD, --pword PWORD
	                        Initial user password, 'ampnado' is the default
	  -U UNAME, --uname UNAME
                        Initial user username, 'admin' is the default

	Example:
		python3 ampnado_setup.py /path/to/music/collection http://192.168.1.001/ampnado -o 40 -U Rodger -P rabbit
 

To add additional music after the initial setup script has been run, use the
add_music.py script:

	usage: add_music.py [-h] MusicPath CatalogName

	Add New Music To AmpNado

	positional arguments:
		MusicPath    Path to the Music Collection
  		CatalogName  Catalog Name or Music collection name, default is current date

	optional arguments:
  		-h, --help   show this help message and exit

	Example:
		python2 add_music.py /path/to/music/collection Cat2


To add additional users, use the add_user.py script:

	usage: add_user.py [-h] UserName PassWord

	Add Users to AmpNado

	positional arguments:
		UserName    New User Name
		PassWord    New User Password

	optional arguments:
		-h, --help  show this help message and exit

	Example:
		python3 add_user.py myusername mypassword
 
To drop all databases using mongo shell use the following commands from a 
terminal:

	mongo
	use ampnadoDB
	db.dropDatabase()