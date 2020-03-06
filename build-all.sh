for s in `ls arch-*.py`; do
  echo "================================"
  echo $s
  ./$s && make
done
