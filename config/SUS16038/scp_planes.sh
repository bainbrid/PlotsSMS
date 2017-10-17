#!/bin/bash

OUTPUT="temp/"
HOST="rjb3@lx01.hep.ph.ic.ac.uk:"

DIR="/vols/build/cms/sdb15/public/Analysis/RA1/201710_Oct/11_SMSUpdate_36invfbGL_v1/planes/" 
MODEL="T1qqqq"
#scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root
MODEL="T1bbbb"
scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root
MODEL="T1tttt"
scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root
MODEL="T2qq"
scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root
MODEL="T2bb"
scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root
MODEL="T2tt"
scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root
MODEL="T2cc"
scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root

#/vols/build/cms/cl4010/RA1/AlphaStats/output/LL_171016_ctau*

DIR="/vols/build/cms/bainbrid/output/v1.6.x_RB_170910_"
MODEL="T1qqqqLL"
scp ${HOST}${DIR}${MODEL}/gridOut_ul.root ${OUTPUT}/${MODEL}_expected.root
scp ${HOST}${DIR}${MODEL}/gridOutObserved_ul.root ${OUTPUT}/${MODEL}_observed.root
