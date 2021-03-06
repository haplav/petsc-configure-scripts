#!/usr/bin/python
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure
  configure_options = [
    '--download-c2html',
    '--download-ctetgen',
    '--download-f2cblaslapack',
    '--download-hdf5',
    '--download-metis',
    '--download-parmetis',
    '--download-ptscotch',
    '--download-zlib',
    '--with-64-bit-indices=1',
    '--with-cxx-dialect=C++11',
    '--with-fc=0',
    '--with-mpi-dir=/opt/mpich-3.2',
    '--with-precision=double',
    '--with-python=1',
    '--with-scalar-type=real',
    '--with-shared-libraries=1',
    '--with-valgrind-dir=/opt/valgrind/valgrind-3.13',
  ]
  configure.petsc_configure(configure_options)
