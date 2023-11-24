#!/bin/bash

LineCount=0



while IFS='' read -r LinefromFile || [[ -n "${LinefromFile}" ]]; do



((LineCount++))



echo "Reading line $LineCount: ${LinefromFile}"



done < "$1"
