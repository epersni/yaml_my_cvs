#!/bin/bash
# Create 

RESUME_CONFIGS_PATH=./etc
RESULT_PATH=./out

for file in $RESUME_CONFIGS_PATH/*.yaml;
do
  TMP_DIR=$(mktemp -d)
  echo "Processing $file file..."
  NAME=$(echo $(basename $file) | cut -f 1 -d '.')
  TEX_FILE=${TMP_DIR}/${NAME}.tex
  ./yaml-to-latex.py $file > ${TEX_FILE}
  pdflatex -output-directory ${TMP_DIR} ${TEX_FILE} > /dev/null
  rm ${TEX_FILE}
  cp ${TMP_DIR}/${NAME}.pdf ${RESULT_PATH}/
  rm -rf ${TMP_DIR}
done
