#!/usr/bin/env python

## needed conda packages
# conda install  c-compiler cxx-compiler fortran-compiler  cmake cython eigen hdf5='*=mpi*' make metis mkl mpich numpy parmetis tetgen triangle yaml zlib
# conda update --all hdf5='*=mpi*'

import os

CONDA_PREFIX = os.getenv('CONDA_PREFIX')
CPPFLAGS = os.getenv('CPPFLAGS')
FFLAGS  = '-g -O0 -pipe -Wall -Wno-strict-aliasing -fstack-protector-strong'
CFLAGS = FFLAGS + ' -Wwrite-strings -Wno-unknown-pragmas -m64'
CXXFLAGS = CFLAGS + ' -fvisibility=hidden'
# Conda uses -Wl,-headerpad_max_install_names
# Conda uses -Wl,-dead_strip_dylibs but it doesn't work well with petsc4py because it does not add all dependencies to libpetsc.dylib
LDFLAGS = '-L%s/lib -Wl,-rpath,%s/lib' % (CONDA_PREFIX, CONDA_PREFIX)

configure_options = [
  'AR=' + os.getenv('AR'),
  'CPPFLAGS=' + CPPFLAGS,
  'CXXPPFLAGS=' + CPPFLAGS,
  'LDFLAGS=' + LDFLAGS,
  'RANLIB=' + os.getenv('RANLIB'),
  'CFLAGS=' + CFLAGS,
  'CXXFLAGS=' + CXXFLAGS,
  'FFLAGS=' + FFLAGS,
  '--download-chaco',
  '--download-ctetgen',
  '--download-exodusii',
  '--download-med',
  '--download-netcdf',
  '--download-pnetcdf',
  '--download-petsc4py',
  '--download-pragmatic',
  '--download-ptscotch',
  '--download-sowing',
  '--download-triangle',
  '--with-blaslapack-lib=-lmkl_intel_lp64 -lmkl_sequential -lmkl_core -lpthread -lm -ldl',
  '--with-cmake-dir=' + CONDA_PREFIX,
  '--with-debugging=1',
  '--with-eigen-dir=' + CONDA_PREFIX,
  '--with-hdf5-dir=' + CONDA_PREFIX,
  '--with-macos-firewall-rules',
  '--with-make-dir=' + CONDA_PREFIX,
  '--with-metis-dir=' + CONDA_PREFIX,
  '--with-mpi-dir=' + CONDA_PREFIX,
  '--with-parmetis-dir=' + CONDA_PREFIX,
  '--with-python-exec=%s/bin/python' % CONDA_PREFIX,
  '--with-scalar-type=real',
  '--with-shared-libraries=1',
  '--with-single-library=1',
  '--with-tetgen-dir=' + CONDA_PREFIX,
  #'--with-triangle-include=%s/include' % CONDA_PREFIX,
  #'--with-triangle-lib=-L%s/lib -ltri' % CONDA_PREFIX,
  '--with-x=0',
  '--with-yaml-dir=' + CONDA_PREFIX,
  '--with-zlib-dir=' + CONDA_PREFIX,
]

if __name__ == '__main__':
  import sys,os
  #import time
  #time.sleep(10)
  sys.path.insert(0,os.path.abspath('config'))
  import configure
  configure.petsc_configure(configure_options)
