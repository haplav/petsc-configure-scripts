#!/usr/bin/env python

# brew install openblas lapack hdf5 metis mpich zlib
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure
  P='/usr/local'
  configure_options = [
    # petsc should have separate --with-lapack-* and --with-blas-* options
    '--with-blaslapack-include=[%s/opt/openblas/include,%s/opt/lapack/include]' % (P,P), 
    '--with-blaslapack-lib=-L%s/opt/lapack/lib -llapack -L%s/opt/openblas/lib -lopenblas' % (P,P), 
    '--with-debugging',
    '--with-hdf5',
    '--with-macos-firewall-rules',
    '--with-metis',
    '--with-mpi-dir=/usr/local',
    '--with-zlib',
    'COPTFLAGS=-g -O0',
    'CXXOPTFLAGS=-g -O0',
    'FOPTFLAGS=-g -O0',
    'LDFLAGS=-Wl,-rpath,%s/lib -L%s/lib' % (P,P), 
  ]
  configure.petsc_configure(configure_options)
