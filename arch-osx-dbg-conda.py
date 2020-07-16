#!/usr/bin/env python

## needed conda packages
# conda install cython numpy hdf5 make mpich mkl c-compiler fortran-compiler valgrind yaml

import os

CONDA_PREFIX = os.getenv('CONDA_PREFIX')
CPPFLAGS = os.getenv('CPPFLAGS')
FFLAGS  = '-g -O0 -pipe -Wall -Wno-strict-aliasing -fstack-protector-strong'
CFLAGS = FFLAGS + ' -Wwrite-strings -Wno-unknown-pragmas'
CXXFLAGS = CFLAGS + ' -fvisibility=hidden'

configure_options = [
  'AR=' + os.getenv('AR'),
  'CPPFLAGS=' + CPPFLAGS,
  'CXXPPFLAGS=' + CPPFLAGS,
  'LDFLAGS=-Wl,-headerpad_max_install_names -Wl,-dead_strip_dylibs -Wl,-rpath,%s/lib -L%s/lib' % (CONDA_PREFIX, CONDA_PREFIX),
  'RANLIB=' + os.getenv('RANLIB'),
  'CFLAGS=' + CFLAGS,
  'CXXFLAGS=' + CXXFLAGS,
  'FFLAGS=' + FFLAGS,
  #'--download-petsc4py',
  '--download-sowing',
  '--with-blaslapack-dir=' + CONDA_PREFIX,
  '--with-debugging=1',
  '--with-hdf5-dir=' + CONDA_PREFIX,
  '--with-make-dir=' + CONDA_PREFIX,
  '--with-mpi-dir=' + CONDA_PREFIX,
  '--with-python-dir=' + CONDA_PREFIX,
  '--with-python-exec=%s/bin/python' % CONDA_PREFIX,
  '--with-shared-libraries=1',
  '--with-single-library=1',
  '--with-valgrind-dir=' + CONDA_PREFIX,
  '--with-yaml-dir=' + CONDA_PREFIX,
  '--with-x=0',
]

if __name__ == '__main__':
  import sys,os
  sys.path.insert(0,os.path.abspath('config'))
  import configure
  configure.petsc_configure(configure_options)
