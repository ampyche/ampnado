Ampnado is very dependent on mp3 tags.  Please insure that the mp3
files are tagged correctly, there are several mp3 taggers such as
picard, and eyeD3.

As of this writing the only hardware that I have tested Ampnado on 
is the Raspberry Pi2 Model B

On the Raspberry Pi it toke approx. 328.19 seconds to process 3895 mp3's
and 4 videos thats approx. 34.05G of media processed.

You will need to utilize a modern Web Browser to take advantage of the
html5 features in Ampnado.  

Currently I recommend to use Python3, however when PyPy3 comes out
I will be testing it to see if it will give Ampnado a bit of a speed
boost on the server side.

I have only tested Ampnado on Debian and Ubuntu, it should run on
just about any favor of linux that is running Python3.  I very rarely have a
reason to use Windows so Ampnado has not been tested on that platform.

Install the Python3 versions of the following software packages:
	pymongo
	PIL
	mutagen or mutagenx
	tornado
	
	mongodb
	FFmpeg
	
To enable text search in versions of mongodb where textsearch is not enabled by default do:

	Start the server with:

	mongod --setParameter textSearchEnabled=true

	or via mongo shell

	db.adminCommand({setParameter:true, textSearchEnabled:true})


To setup AmpNado use the setup script in /usr/share/ampnado/ampnado_setup.py:
	To show the Ampnado's Help message do:
		python3 ampnado_setup.py --help
		
		Example Install command:
		
		python3 ampnado_setup.py Install 
			-s http://192.168.1.100/ampnado 
			-m /home/fred/Music 
			-c Cat1 
			-o 40 
			-u fred 
			-p 123fred123

		Example of adding a new user:
		
		python3 ampnado_setup.py Utils
			--add-user-name Betty
			--add-user-password 456betty456


To drop all databases using mongo shell use the following commands from a 
terminal:

	mongo
	use ampnadoDB
	db.dropDatabase()
	use ampviewsDB
	db.dropDatabase()