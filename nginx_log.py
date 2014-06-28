#!/usr/bin/python

import string
import os
import re



from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--last", help="select the line number to analyse")
parser.add_option("-l", "--limit", help="show result number")
parser.add_option("-u", "--url", default=False, help="select request url to analyse")
parser.add_option("-i", "--ip", default=False, help="select user ip to analyse")
parser.add_option("-r", "--reverse", default=False, help="show result by reversed")
parser.add_option("-R", "--refer", default=False, help="select refer to analyse")
parser.add_option("-b", "--backend", default=False, help="select backend ip address to analyse")
parser.add_option("-x", "--backendcode", default=False, help="select backend http response code to analyse")
parser.add_option("-c", "--usercode", default=False, help="select user http resonse code to analyse")
parser.add_option("-y", "--backendtime", default=False, help="select backend time to analyse")
parser.add_option("-t", "--usertime", default=False, help="select user time number to analyse")
parser.add_option("-f", "--filename", default=False, help="write the result to a file")
(options, args) = parser.parse_args()
