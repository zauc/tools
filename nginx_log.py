#!/usr/bin/python

import string
import os
import re

from optparse import OptionParser


SEP="|"


parser = OptionParser()
parser.add_option("-n", "--last",  type="int", dest="LAST", help="select the line number to analyse")
parser.add_option("-l", "--limit", type="int", dest="LIMIT", help="show result number")
parser.add_option("-u", "--url", dest="URL", default=False, help="select request url to analyse")
parser.add_option("-i", "--ip", dest="UIP", default=False, help="select user ip to analyse")
parser.add_option("-r", "--reverse", default=False, help="show result by reversed")
parser.add_option("-R", "--refer", dest="REFER", default=False, help="select refer to analyse")
parser.add_option("-b", "--backend", dest="BIP", default=False, help="select backend ip address to analyse")
parser.add_option("-x", "--backendcode", dest="BCD", default=False, help="select backend http response code to analyse")
parser.add_option("-c", "--usercode", dest="UCD", default=False, help="select user http resonse code to analyse")
parser.add_option("-y", "--backendtime", dest="BTM", default=False, help="select backend time to analyse")
parser.add_option("-t", "--usertime", dest="UTM", default=False, help="select user time number to analyse")
parser.add_option("-f", "--filename", dest="DF", default=False, help="write the result to a file")
parser.add_option("-s", "--source", action="store", type="string", dest="SF", default=True, help="read the log from a file")
(options, args) = parser.parse_args()
SF = options.SF
DF = options.DF

def read_file(filename):
	try:
		with open(filename, 'r') as log_file:
#			print (filename)
			for each_line in log_file:
				try:
					(line, line_spoke) = each_line.split(SEP)
					print line
					print line_spoke
				except ValueError:
					print "Separation of the %s is error, please modify the separation to be %s" %(SF, SEP)
	except IOError as err:
		print ('File error: '+ str(err))



if __name__ == "__main__":
	read_file(SF)
