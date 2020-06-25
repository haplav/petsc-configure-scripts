#!/usr/bin/env python

## needed conda packages
# conda install cython numpy hdf5 make mpich mkl c-compiler fortran-compiler valgrind yaml

import os
CONDA_ENV="/opt/miniconda3/envs/petsc"
configure_options = [
  'COPTFLAGS=-g -O',
  'FOPTFLAGS=-g -O',
  'CXXOPTFLAGS=-g -O',
  '--download-petsc4py',
  '--download-sowing',
  '--with-blaslapack-dir=' + CONDA_ENV,
  '--with-hdf5-dir=' + CONDA_ENV,
  '--with-make-dir=' + CONDA_ENV,
  '--with-mpi-dir=' + CONDA_ENV,
  '--with-python-exec=%s/bin/python' % CONDA_ENV,
  '--with-shared-libraries=1',
  '--with-valgrind-dir=' + CONDA_ENV,
  '--with-yaml-dir=' + CONDA_ENV,
  '--with-x=0',
]

if __name__ == '__main__':
  import sys,os
  sys.path.insert(0,os.path.abspath('config'))
  import configure
  configure.petsc_configure(configure_options)
