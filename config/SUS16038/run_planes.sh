mkdir plots/
cd ../..
python python/makeSMSplots.py config/SUS16038/T1qqqq_SUS16038.cfg T1qqqq
python python/makeSMSplots.py config/SUS16038/T1bbbb_SUS16038.cfg T1bbbb
python python/makeSMSplots.py config/SUS16038/T1tttt_SUS16038.cfg T1tttt
python python/makeSMSplots.py config/SUS16038/T2qq_SUS16038.cfg T2qq
python python/makeSMSplots.py config/SUS16038/T2bb_SUS16038.cfg T2bb
python python/makeSMSplots.py config/SUS16038/T2tt_SUS16038.cfg T2tt
python python/makeSMSplots.py config/SUS16038/T2cc_SUS16038.cfg T2cc
python python/makeSummarySMSplots.py
mv *.pdf config/SUS16038/plots/
cd -
