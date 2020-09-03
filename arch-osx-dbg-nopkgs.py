#!/usr/bin/env python

import os

configure_options = [
  '--with-cc=clang',
  '--with-cxx=clang++',
  #'--with-fc=gfortran', # https://brew.sh/
  '--with-fc=0',
  'COPTFLAGS=-g -O',
  'FOPTFLAGS=-g -O',
  'CXXOPTFLAGS=-g -O',
  '--download-make=1',
  '--download-f2cblaslapack=1',
  '--download-mpich=1',
  '--download-mpich-device=ch3:nemesis', #for some reason runex174_2_elemental takes very long with ch3:p4
  '--with-macos-firewall-rules',
  ]

if __name__ == '__main__':
  import sys,os
  sys.path.insert(0,os.path.abspath('config'))
  import configure
  configure.petsc_configure(configure_options)
