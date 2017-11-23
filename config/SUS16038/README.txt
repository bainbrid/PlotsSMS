Details:
- Plots found in SUS16038_171122/plots/
- Root files (not committed) in SUS16038_171112/root/ 
- Root files produced by Xian (22/11/17)
- T1qqqqLL 1E18 sample is not smoothed, all others are smoothed
- Based on AlphaStats branch: bainbrid:v1.6.x_RB_171125_T1qqqqLL

Paper plots:
- Produced with the head of this branch.

Supplementary plots:
- Need to add 'PRELIMINARY Supplementary' to each .cfg file
- e.g.: sed -i -- 's/PRELIMINARY\ Supplementary/PRELIMINARY\ /g' *.cfg
- To adjust location of CMS Supplementary and CoM/lumi labels for individual limit plots: 

diff --git a/python/CMS_lumi.py b/python/CMS_lumi.py
index 5393414..d795ae4 100644
--- a/python/CMS_lumi.py
+++ b/python/CMS_lumi.py
@@ -102,6 +102,7 @@ def CMS_lumi(pad,  iPeriod,  iPosX ):
     latex.SetTextSize(lumiTextSize*t)    
 
     latex.DrawLatex(1-r,1-t+lumiTextOffset*t,lumiText)
+    #latex.DrawLatex(1-r+0.06,1-t+lumiTextOffset*t,lumiText)
 
     if( outOfFrame ):
         latex.SetTextFont(cmsTextFont)
