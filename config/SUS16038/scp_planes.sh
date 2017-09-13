#!/bin/bash

DIR="rjb3@lx01.hep.ph.ic.ac.uk:/home/hep/klo2/public_html/RA1/BTagFormula/FullFit/Log/20170713/Unblinding36fb2017_v14_" 
scp ./${DIR}${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root
MODEL="T2bb"
scp ./${DIR}${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root

DIR="rjb3@lx01.hep.ph.ic.ac.uk:/vols/build/cms/sdb15/public/Analysis/RA1/201708_Aug/10_SMS_limitPlane/" 
MODEL="T1tttt"
scp ./${DIR}/${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}/${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root
MODEL="T2tt"
scp ./${DIR}/${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}/${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root
MODEL="T2cc"
scp ./${DIR}/${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}/${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root
MODEL="T1qqqq"
scp ./${DIR}/${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}/${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root
MODEL="T2qq"
scp ./${DIR}/${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}/${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root

BASE="rjb3@lx01.hep.ph.ic.ac.uk:/vols/build/cms/bainbrid/output/v1.6.x_RB_170910_"
MODEL="T1qqqqLL"
scp ./${DIR}${MODEL}/gridOut_ul.root ${MODEL}_expected.root
scp ./${DIR}${MODEL}/gridOutObserved_ul.root ${MODEL}_observed.root
