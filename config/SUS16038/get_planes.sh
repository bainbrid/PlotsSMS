#!/bin/bash

INPUT="/Users/bainbrid/Repositories/PlotsSMS/config/SUS16038/temp/"

# Vanilla models
cp ${INPUT}T1bbbb/gridOut_ul.root T1bbbb_expected.root
cp ${INPUT}T1bbbb/gridOutObserved_ul.root T1bbbb_observed.root
cp ${INPUT}T2bb/gridOut_ul.root T2bb_expected.root
cp ${INPUT}T2bb/gridOutObserved_ul.root T2bb_observed.root
cp ${INPUT}T1tttt/gridOut_ul.root T1tttt_expected.root
cp ${INPUT}T1tttt/gridOutObserved_ul.root T1tttt_observed.root
cp ${INPUT}T2tt/gridOut_ul.root T2tt_expected.root
cp ${INPUT}T2tt/gridOutObserved_ul.root T2tt_observed.root
cp ${INPUT}T2cc/gridOut_ul.root T2cc_expected.root
cp ${INPUT}T2cc/gridOutObserved_ul.root T2cc_observed.root
cp ${INPUT}T1qqqq/gridOut_ul.root T1qqqq_expected.root
cp ${INPUT}T1qqqq/gridOutObserved_ul.root T1qqqq_observed.root
cp ${INPUT}T2qq/gridOut_ul.root T2qq_expected.root
cp ${INPUT}T2qq/gridOutObserved_ul.root T2qq_observed.root

# LL models
cp ${INPUT}T1qqqqLL/gridOutObserved_ul.root T1qqqqLL_observed.root
cp ${INPUT}T1qqqqLL/gridOut_ul.root T1qqqqLL_expected.root
