#!/bin/bash
if [ "$1" = "suppl" ]; then
    sed -i -- 's/PRELIMINARY\ /PRELIMINARY\ Supplementary/g' *.cfg
else 
    sed -i -- 's/PRELIMINARY\ Supplementary/PRELIMINARY\ /g' *.cfg
fi

