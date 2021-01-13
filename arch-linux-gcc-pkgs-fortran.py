#!/usr/bin/python
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure
  configure_options = [
    '--download-c2html',
    '--download-chaco',
    '--download-ctetgen',
    '--download-eigen',
    '--download-exodusii',
    '--download-fblaslapack',
    '--download-hdf5',
    '--download-med',
    '--download-metis',
    '--download-mumps',
    '--download-netcdf',
    '--download-p4est',
    '--download-parmetis',
    '--download-pnetcdf',
    '--download-ptscotch',
    '--download-scalapack',
    '--download-suitesparse',
    '--download-superlu',
    '--download-superlu_dist',
    '--download-triangle',
    '--download-zlib',
    '--with-64-bit-indices=0',
    '--with-cxx-dialect=C++11',
    '--with-mpi-dir=/opt/mpich-3.2',
    '--with-precision=double',
    '--with-python=1',
    '--with-scalar-type=real',
    '--with-shared-libraries=1',
    '--with-valgrind-dir=/opt/valgrind/valgrind-3.13',
  ]
  configure.petsc_configure(configure_options)
