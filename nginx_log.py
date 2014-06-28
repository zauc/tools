#!/usr/bin/python

import string
import os
import re
from optparse import OptionParser

#config for log file
SEP="|"
user_ip_b=0
back_ip_b=1
c_time_b=2
back_code_b=3
n_time_b=4
req_url_b=5
user_code_b=6
data_size_b=7
all_size_b=8
req_ref_b=9
user_ag_b=10
back_time_b=11
u_time_b=12
user_time_b=13
host_name_b=14



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
#					(user_ip,back_ip,c_time,back_code,n_time,req_url,user_code,data_size,all_size,req_ref,user_ag,back_time,u_time,user_time,host_name) = each_line.split(SEP)
					user_ip = each_line.split(SEP)[user_ip_b]
					back_ip = each_line.split(SEP)[back_ip_b]
					c_time = each_line.split(SEP)[c_time_b]
					back_code = each_line.split(SEP)[back_code_b]
					n_time = each_line.split(SEP)[n_time_b]
					req_url = each_line.split(SEP)[req_url_b]
					user_code = each_line.split(SEP)[user_code_b]
					data_size = each_line.split(SEP)[data_size_b]
					all_size = each_line.split(SEP)[all_size_b]
					req_ref = each_line.split(SEP)[req_ref_b]
					user_ag = each_line.split(SEP)[user_ag_b]
					back_time = each_line.split(SEP)[back_time_b]
					u_time = each_line.split(SEP)[u_time_b]
					user_time = each_line.split(SEP)[user_time_b]
					host_name = each_line.split(SEP)[host_name_b]
					print user_ip 
					print host_name 
				except ValueError:
					print "Separation of the %s is error, please modify the separation to be %s" %(SF, SEP)
	except IOError as err:
		print ('File error: '+ str(err))


#def getMark():
#	BCD=options.BCD
#	
#
#
#def analysis():
	


if __name__ == "__main__":
	read_file(SF)
