mkdir plots/
cd ../..

python python/makeSMSplots.py config/SUS16038/T2tt_SUS16038_turd.cfg T2tt

# Vanilla SUSY 
#python python/makeSMSplots.py config/SUS16038/T1qqqq_SUS16038.cfg T1qqqq
#python python/makeSMSplots.py config/SUS16038/T1bbbb_SUS16038.cfg T1bbbb
#python python/makeSMSplots.py config/SUS16038/T1tttt_SUS16038.cfg T1tttt
#python python/makeSMSplots.py config/SUS16038/T2qq_SUS16038.cfg T2qq
#python python/makeSMSplots.py config/SUS16038/T2bb_SUS16038.cfg T2bb
#python python/makeSMSplots.py config/SUS16038/T2tt_SUS16038.cfg T2tt
#python python/makeSMSplots.py config/SUS16038/T2cc_SUS16038.cfg T2cc

# Split SUSY
#python python/makeSMSplots.py config/SUS16038/T1qqqqLLPrompt_SUS16038.cfg T1qqqqLLPrompt
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL0p001_SUS16038.cfg T1qqqqLL0p001
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL0p01_SUS16038.cfg T1qqqqLL0p01
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL0p1_SUS16038.cfg T1qqqqLL0p1
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL1_SUS16038.cfg T1qqqqLL1
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL10_SUS16038.cfg T1qqqqLL10
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL100_SUS16038.cfg T1qqqqLL100
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL1000_SUS16038.cfg T1qqqqLL1000
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL10000_SUS16038.cfg T1qqqqLL10000
#python python/makeSMSplots.py config/SUS16038/T1qqqqLL100000_SUS16038.cfg T1qqqqLL100000
#python python/makeSMSplots.py config/SUS16038/T1qqqqLLStable_SUS16038.cfg T1qqqqLLStable

# Summary plots
#python python/makeSummarySMSplots.py

mv *.pdf config/SUS16038/plots/
cd -
