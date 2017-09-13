from array import *
import ROOT as rt

class sms():

    def __init__(self, modelname):
        if modelname.find("T1tttt") != -1: self.T1tttt()
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T1qqqq") != -1: self.T1qqqq()
        if modelname.find("T1ttbb") != -1: self.T1ttbb()
        if modelname.find("T5ttttDM175") != -1: self.T5ttttDM175()
        if modelname.find("T5tttt-degen") != -1: self.T5tttt_degen()
        if modelname.find("T5ttcc") != -1: self.T5ttcc()
        if modelname.find("T2tt") != -1: self.T2tt()
        if modelname.find("T2cc") != -1: self.T2cc()
        if modelname.find("T2mixed") != -1: self.T2mixed()
        if modelname.find("T2-4bd") != -1: self.T24bd()
        if modelname.find("T2bb") != -1: self.T2bb()
        if modelname.find("T2qq") != -1: self.T2qq()
        if modelname.find("T2qqDegen") != -1: self.T2qqDegen()
        if modelname.find("T2tb") != -1: self.T2tb()
        if modelname.find("T2bW-X05") != -1: self.T2bW_X05()
        if modelname.find("T1qqqqLL0p001") != -1: self.T1qqqqLL0p001()
        if modelname.find("T1qqqqLL0p01") != -1: self.T1qqqqLL0p01()
        if modelname.find("T1qqqqLL0p1") != -1: self.T1qqqqLL0p1()
        if modelname.find("T1qqqqLL1") != -1: self.T1qqqqLL1()
        if modelname.find("T1qqqqLL10") != -1: self.T1qqqqLL10()
        if modelname.find("T1qqqqLL100") != -1: self.T1qqqqLL100()
        if modelname.find("T1qqqqLL1000") != -1: self.T1qqqqLL1000()
        if modelname.find("T1qqqqLL10000") != -1: self.T1qqqqLL10000()
        if modelname.find("T1qqqqLL100000") != -1: self.T1qqqqLL100000()

    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        self.color = rt.kRed
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} "+lsp_s;
        self.label2= "";
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 2200.
        self.Ymin = 0.
        self.Ymax = 1900.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False
                
    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
        self.color = rt.kGreen+3
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} "+lsp_s;
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600
        self.Xmax = 2200
        self.Ymin = 0
        self.Ymax = 1900
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False

    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        self.color = rt.kBlue
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} "+lsp_s;
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2300.
        self.Ymin = 0.
        self.Ymax = 2000.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False

    def T2tt(self):
        # model name
        self.modelname = "T2tt"
        self.color = rt.kRed
        #self.color = rt.kCyan+2
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{t}_{1} #tilde{t}_{1}, #tilde{t}_{1} #rightarrow t^{(*)} #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 150.
        self.Xmax = 1200.
        self.Ymin = 0.
        self.Ymax = 800.
        self.Zmin = 0.001
        self.Zmax = 100.
        #self.Ndivisions = -1005
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{t}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = True
        self.diagTopOn = True
        self.blankTopCorr = True
        self.diagWOn = False
        # more specs on the text
        self.xTextTop = 0.38
        self.yTextTop = 0.50
        self.angleTextTop = 61

    def T2cc(self):
        # model name
        self.modelname = "T2cc"
        self.color = rt.kOrange+1
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{t}_{1} #tilde{t}_{1}, #tilde{t}_{1} #rightarrow c #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 250.
        self.Xmax = 800.
        self.Ymin = 175.
        self.Ymax = 950.
        self.Zmin = 0.1
        self.Zmax = 5.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{t}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = True
        # more specs on the text
        self.xTextW = 0.50
        self.yTextW = 0.38
        self.angleTextW = 33

    def T2bb(self):
        # model name
        self.modelname = "T2bb"
        self.color = rt.kBlue
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{b}_{1} #tilde{b}_{1}, #tilde{b}_{1} #rightarrow b #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1300.
        self.Ymin = 0.
        self.Ymax = 900.
        self.Zmin = 0.001
        self.Zmax = 20.
        self.Ndivisions = -505
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{b}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False

#    def T2qq(self):
#        # model name
#        self.modelname = "T2qq"
#        self.color = rt.kGreen+3
#        # decay chain
#        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
#        self.label= "pp #rightarrow #tilde{q}_{1} #tilde{q}_{1}, #tilde{q}_{1} #rightarrow q #tilde{#chi}^{0}_{1}";
#        self.label2= "";
#        # plot boundary. The top 1/4 of the y axis is taken by the legend
#        self.Xmin = 300.
#        self.Xmax = 1700.
#        self.Ymin = 0.
#        self.Ymax = 1300.
#        self.Zmin = 0.001
#        self.Zmax = 5.
#        # produce sparticle
#        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{q}}}} [GeV]"
#        # LSP
#        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
#        # turn off diagonal lines
#        self.diagOn = False
#        self.diagTopOn = False
#        self.blankTopCorr = False
#        self.diagWOn = False
#        self.textT2qqOne = True
#        self.textT2qqEight = True

    def T2qq(self):
        # model name
        self.modelname = "T2qq"
        self.color = rt.kGreen
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{q} #tilde{q}, #tilde{q} #rightarrow q #tilde{#chi}^{0}_{1} (#tilde{q} = #tilde{u}_{L})";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1700.
        self.Ymin = 0.
        self.Ymax = 1300.
        self.Zmin = 0.001
        self.Zmax = 5.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{q}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False
        self.textT2qqOne = True
        self.textT2qqEight = False

    def T2qqDegen(self):
        # model name
        self.modelname = "T2qqDegen"
        self.color = rt.kGreen+3
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{q} #tilde{q}, #tilde{q} #rightarrow q #tilde{#chi}^{0}_{1} (#tilde{q} = #tilde{Q})";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1700.
        self.Ymin = 0.
        self.Ymax = 1300.
        self.Zmin = 0.001
        self.Zmax = 5.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{q}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False
        self.textT2qqOne = False
        self.textT2qqEight = True

    def T1qqqqLL(self):
        self.modelname = "T1qqqqLL" # to be overwritten 
        self.color = rt.kGreen # to be overwritten 
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label = "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} "+lsp_s;
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600
        self.Xmax = 2100
        self.Ymin = 0
        self.Ymax = 1800
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m_{#tilde{g}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False

    def T1qqqqLL0p001(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL0p001"
        self.color = rt.kGreen+2
        self.label = "c#tau = 0.001 mm";

    def T1qqqqLL0p01(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL0p01"
        self.color = rt.kGreen+0
        self.label = "c#tau = 0.01 mm";

    def T1qqqqLL0p1(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL0p1"
        self.color = rt.kOrange
        self.label = "c#tau = 0.1 mm";

    def T1qqqqLL1(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL1"
        self.color = rt.kOrange+3
        self.label = "c#tau = 1 mm";

    def T1qqqqLL10(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL10"
        self.color = rt.kRed
        self.label = "c#tau = 1 cm";

    def T1qqqqLL100(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL100"
        self.color = rt.kBlue
        self.label = "c#tau = 10 cm";

    def T1qqqqLL1000(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL1000"
        self.color = rt.kCyan+1
        self.label = "c#tau = 1 m";

    def T1qqqqLL10000(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL10000"
        self.color = rt.kMagenta
        self.label = "c#tau = 10 m";

    def T1qqqqLL100000(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL100000"
        self.color = rt.kBlack
        self.label = "c#tau = 100 m";
