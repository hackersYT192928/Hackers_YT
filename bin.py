#!/usr/bin/env python

from urllib2 import*
bin = raw_input('INGRESE BIN:')
api = "https://lookup.binlist.net/" + bin
consultar = urlopen(api).read()
print consultar