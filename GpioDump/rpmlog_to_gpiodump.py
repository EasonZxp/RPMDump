#Sample code

import sys
import re
import os
import struct
import datetime
import array
import string
import bisect
import traceback
import gzip
import functools
import re

from optparse import OptionParser
from optparse import OptionGroup
#from print_out import *

# string table #
str_deepsleepenter="SLEEP_DEEP_SLEEP_ENTER_COMPLETE"
str_deepsleepexit="SLEEP_DEEP_SLEEP_EXIT_COMPLETE"
str_gpiodump="SLEEP_GPIO_DUMP"

out_file = None

def set_outfile(path) :
    global out_file
    out_file = open(path,"wb")

def print_out_str(string) :
    if out_file is None :
        print (string)
    else :
        out_file.write((string+"\n").encode('ascii','ignore'))

def gpioconfig(arg0,arg1) :
    # self.outline="gpio "+arg0 + "'s config is "
    # use 32 bit to save both cfg and inout, cfg << 16 | inout
    # HIHYS bit 26
    hihys = arg1 & 0x4000000
    # driver strength bit 24:22
    strength = (arg1 & 0x1c00000)>>22
    # func bit 21:18
    func = (arg1 & 0x3c0000)>>18
    # pull bit 17:16
    temp = ((arg1 & 0x30000)>>16)&0x1
    pull = ""
    if (((arg1 & 0x30000)>>16)&0x1) == 0:
        pull = "NO PULL"
    if (((arg1 & 0x30000)>>16)&0x1) == 0x1:
        pull = "PULL DOWN"
    if (((arg1 & 0x30000)>>16)&0x2) == 0x2:
        pull = "KEEPER"
    if (((arg1 & 0x30000)>>16)&0x3) == 0x3:
        pull = "PULL UP"

    # inout bit 1:0
    if (arg1 & 0x1) == 0x1:
        out = "input "
    else :
        out = "output"

    # OE bit 25
    oe = ""
    if (((arg1 & 0x2000000)>>25)&0x1) == 1:
        oe = "Enable "
        out = "OUTPUT"
        if (arg1 & 0x2) == 0x2:
            print_out_str ("gpio [{0:d}]        is func {1:x}     {2}       HIGH        {3}\n".format(arg0,func,out,pull))
        else:
            print_out_str ("gpio [{0:d}]        is func {1:x}     {2}       LOW     {3}\n".format(arg0,func,out,pull))
    else:
        oe = "Disable"
        out = "INPUT"
        print_out_str ("gpio [{0:d}]        is func {1:x}     {2}                    {3}\n".format(arg0,func,out,pull))


def qdssdump(filename) :
    if filename is not None:
        fd = open(filename,"rb")
        if not fd:
            print_out_str ("Could not open {0}".format(filename))

        for line in file.readlines(fd):
            if re.search(str_gpiodump,line) is not None:
                lpos = string.find(line,str_gpiodump)
                lpos = lpos + 17
                temp = line[lpos:lpos+10]
                arg0 = string.atol(temp,16)
                lpos = lpos + 11
                temp = line[lpos:lpos+10]
                arg1 = string.atol(temp,16)
                gpioconfig(arg0,arg1)
        print("done")




if __name__ == '__main__':
    usage = "usage: %prog [options to print]. Run with --help for more details"
    parser = OptionParser(usage)
    parser.add_option("-o", "--outdir", dest="outdir", help="Output directory")
    parser.add_option("-f", "--output-file", dest="outfile", help="Name of file to save output")
    parser.add_option("", "--stdout", action="store_true", dest="stdout", help="Dump to stdout instead of the file")
    parser.add_option("-l", "--log", dest="log", help="log filename")

    (options, args) = parser.parse_args()

    if options.outdir :
        if not os.path.exists(options.outdir) :
            print ("!!! Out directory does not exist. Create it first.")
            sys.exit(1)
    else :
        options.outdir = "."

    if options.outfile is None :
        # gpiodump is a very non-descriptive name and should be changed sometime in the future
        options.outfile = "gpiodump.txt"

    if not options.stdout :
        set_outfile(options.outdir+"/"+options.outfile)

    if options.log is None :
        print_out_str ("No log filename given. I can't proceed!")
        parser.print_usage()
        sys.exit(1)

    args = ""
    for arg in sys.argv:
      args = args + arg + " "

    print_out_str ("Arguments: {0}".format(args))


    if not os.path.exists(options.log) :
        print_out_str ("{0} does not exist. Cannot proceed without log file. Exiting...".format(options.log))
        sys.exit(1)
    else :
        print_out_str ("using log file {0}".format(options.log))

    qdssdump(options.log)

