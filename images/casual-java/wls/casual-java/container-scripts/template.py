#!/usr/bin/env python
import os

in_filename = os.environ['TEMPLATE_IN']
out_filename = os.environ['TEMPLATE_OUT']
casual_version = os.environ['CASUAL_VERSION']

f_in = open(in_filename,'r')
f_out = open(out_filename,'w')

lines = f_in.readlines()

for line in lines:
    line_out = line.replace('CASUAL_VERSION', casual_version)
    f_out.write(line_out)

print('Template {0} parsed and file {1} created'.format(in_filename,out_filename))

