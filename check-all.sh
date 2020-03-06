dir=$PWD
for s in `ls arch-*.py`; do
  echo "================================"
  arch=`echo "${s%.*}"`
  echo $arch
  make PETSC_DIR=$dir PETSC_ARCH=$arch check
done
