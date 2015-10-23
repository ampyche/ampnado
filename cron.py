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
import logging
import amp.functions as fun

class AmpnadoCron():
	def __init__(self):
		FUN = fun.SetUp()
		self.FUN = FUN
		
	def main(self):
		logging.basicConfig(filename='/usr/share/ampnado/logs/cron.log', 
			format='%(asctime)s %(levelname)s:%(message)s', filemode='w', level=logging.INFO)
		logging.info('Cron job has started')
		self.FUN._create_random_art_db()
		logging.info('Cron job has completed')

if __name__ == "__main__":
	M = AmpnadoCron()
	M.main()