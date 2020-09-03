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
  '--download-cmake=1',
  '--download-f2cblaslapack=1',
  '--download-ctetgen=1',
  '--download-hdf5=1',
  '--download-mpich=1',
  '--download-mpich-device=ch3:nemesis', #for some reason runex174_2_elemental takes very long with ch3:p4
  '--download-metis=1',
  '--download-parmetis=1',
  '--download-ptscotch',
  '--download-libpng=1',
  '--download-libjpeg=1',
  '--with-macos-firewall-rules',
  '--with-zlib=1',
  ]

if __name__ == '__main__':
  import sys,os
  sys.path.insert(0,os.path.abspath('config'))
  import configure
  configure.petsc_configure(configure_options)
