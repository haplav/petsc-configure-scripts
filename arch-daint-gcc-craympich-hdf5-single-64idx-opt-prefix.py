#!/usr/bin/python
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure

  PREFIX_DIR = os.getenv('PROJECT') + '/petsc-prefix'
  PE = os.getenv('PE_ENV').lower()
  HDF5_DIR = os.getenv('HDF5_DIR')
  LIBSCI_DIR = os.getenv('CRAY_LIBSCI_PREFIX_DIR')

  configure_options = [
    '--download-metis',
    '--download-parmetis',
    '--download-ptscotch',
    '--known-64-bit-blas-indices=0',
    '--known-mpi-c-double-complex=1',
    '--known-mpi-int64_t=1',
    '--known-mpi-long-double=1',
    '--with-64-bit-indices',
    '--with-batch=1',
    #'--with-blaslapack-lib=-L%s/lib -lsci_%s_mpi' % (LIBSCI_DIR, PE),
    '--with-blaslapack-lib=',
    '--with-cc=cc',
    '--with-cxx=CC',
    '--with-debugging=0',
    '--with-etags=0',
    '--with-fc=ftn',
    '--with-fortran-bindings=0',
    '--with-hdf5-dir=' + HDF5_DIR,
    '--with-make-np=4',
    '--with-mpi-include=',
    '--with-mpi-lib=',
    '--with-precision=single',
    '--with-scalar-type=real',
    '--with-shared-libraries=0',
    '--with-sowing=0',
    '--with-ssl=0',
    '--with-x=0',
    '--with-zlib-include=',
    '--with-zlib-lib=-L/usr/lib64 -lz',
    'COPTFLAGS=-O3 -march=native',
    'CXXOPTFLAGS=-O3 -march=native',
    'FOPTFLAGS=-O3 -march=native',
    '--prefix=' + PREFIX_DIR,
  ]
  configure.petsc_configure(configure_options)
