from array import *
import ROOT as rt

class sms():

    def __init__(self, modelname):
        self.lsp = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
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
        if modelname.find("T2qqOne") != -1: self.T2qqOne()
        elif modelname.find("T2qqDegen") != -1: self.T2qqDegen()
        elif modelname.find("T2qq") != -1: self.T2qq()
        if modelname.find("T2tb") != -1: self.T2tb()
        if modelname.find("T2bW-X05") != -1: self.T2bW_X05()
        if modelname.find("T1qqqqLLPrompt") != -1: self.T1qqqqLLPrompt()
        if modelname.find("T1qqqqLL0p001") != -1: self.T1qqqqLL0p001()
        if modelname.find("T1qqqqLL0p01") != -1: self.T1qqqqLL0p01()
        if modelname.find("T1qqqqLL0p1") != -1: self.T1qqqqLL0p1()
        if modelname.find("T1qqqqLL1") != -1: self.T1qqqqLL1()
        if modelname.find("T1qqqqLL10") != -1: self.T1qqqqLL10()
        if modelname.find("T1qqqqLL100") != -1: self.T1qqqqLL100()
        if modelname.find("T1qqqqLL1000") != -1: self.T1qqqqLL1000()
        if modelname.find("T1qqqqLL10000") != -1: self.T1qqqqLL10000()
        if modelname.find("T1qqqqLL100000") != -1: self.T1qqqqLL100000()
        if modelname.find("T1qqqqLLStable") != -1: self.T1qqqqLLStable()

    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        self.color = rt.kRed
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} "+self.lsp
        self.label2= ""
        self.label3= "#tilde{g} #rightarrow t #bar{t} "+self.lsp
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 2200.
        self.Ymin = 0.
        self.Ymax = 1900.
        self.Zmin = 0.001
        self.Zmax = 3.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
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
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} "+self.lsp
        self.label2= ""
        self.label3= "#tilde{g} #rightarrow q #bar{q} "+self.lsp
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600
        self.Xmax = 2200
        self.Ymin = 0
        self.Ymax = 1900
        self.Zmin = 0.001
        self.Zmax = 3.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
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
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} "+self.lsp
        self.label2= ""
        self.label3= "#tilde{g} #rightarrow b #bar{b} "+self.lsp
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 2300.
        self.Ymin = 0.
        self.Ymax = 2000.
        self.Zmin = 0.001
        self.Zmax = 3.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
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
        self.label= "pp #rightarrow #tilde{t}_{1} #bar{#tilde{t}_{1}}, #tilde{t}_{1} #rightarrow t^{(*)} "+self.lsp
        self.label2= ""
        self.label3= self.label
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 150.
        self.Xmax = 1200.
        self.Ymin = 0.
        self.Ymax = 800.
        self.Zmin = 0.001
        self.Zmax = 200.
        #self.Ndivisions = -1005
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{t}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = True
        self.blankTopCorr = True
        self.diagWOn = False
        # more specs on the text
        self.xTextTop = 0.48
        self.yTextTop = 0.60
        self.angleTextTop = 56

    def T2cc(self):
        # model name
        self.modelname = "T2cc"
        self.color = rt.kOrange+1
        # decay chain
        self.label= "pp #rightarrow #tilde{t}_{1} #bar{#tilde{t}_{1}}, #tilde{t}_{1} #rightarrow c "+self.lsp
        self.label2= ""
        self.label3= self.label
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 150.
        self.Xmax = 750.
        self.Ymin = 0.
        self.Ymax = 950.
        self.Zmin = 0.001#0.1
        self.Zmax = 200.#10.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{t}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = True
        # more specs on the text
        self.xTextW = 0.24
        self.yTextW = 0.25
        self.angleTextW = 35

    def T2bb(self):
        # model name
        self.modelname = "T2bb"
        self.color = rt.kBlue
        # decay chain 
        self.label= "pp #rightarrow #tilde{b}_{1} #bar{#tilde{b}_{1}}, #tilde{b}_{1} #rightarrow b "+self.lsp
        self.label2= ""
        self.label3= self.label
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1300.
        self.Ymin = 0.
        self.Ymax = 900.
        self.Zmin = 0.001
        self.Zmax = 200.#20.
        self.Ndivisions = -505
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{b}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False

    def T2qq(self):
        # model name
        self.modelname = "T2qq"
        self.color = rt.kGreen
        # decay chain
        self.label= "pp #rightarrow #tilde{q} #bar{#tilde{q}}, #tilde{q} #rightarrow q "+self.lsp
        self.label2= ""
        self.label3= self.label
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 300.
        self.Xmax = 1700.
        self.Ymin = 0.
        self.Ymax = 1300.
        self.Zmin = 0.001
        self.Zmax = 200.#10.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{q}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False
        self.textT2qqOne = True
        self.textT2qqEight = True

    def T2qqDegen(self):
        self.T2qq()
        self.modelname = "T2qqDegen"
        self.color = rt.kGreen+3
        tmp = " (#tilde{q}_{L} + #tilde{q}_{R}, #tilde{u}, #tilde{d}, #tilde{s}, #tilde{c})"
        self.label= "pp #rightarrow #tilde{q} #bar{#tilde{q}}, #tilde{q} #rightarrow q "+self.lsp+tmp
        self.label2= ""
        self.label3= self.label
        self.textT2qqOne = False
        self.textT2qqEight = True

    def T2qqOne(self):
        self.T2qq()
        self.modelname = "T2qqOne"
        self.color = rt.kGreen
        tmp = " (one light #tilde{q})"
        self.label= "pp #rightarrow #tilde{q} #bar{#tilde{q}}, #tilde{q} #rightarrow q "+self.lsp+tmp
        self.label2= ""
        self.label3= self.label
        self.textT2qqOne = True
        self.textT2qqEight = False

    def T1qqqqLL(self):
        self.modelname = "T1qqqqLL" # to be overwritten 
        self.color = rt.kGreen # to be overwritten 
        self.label = "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} "+self.lsp
        self.label2= ""
        self.label3 = "#tilde{g} #rightarrow q #bar{q} "+self.lsp
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600
        self.Xmax = 2200
        self.Ymin = 0
        self.Ymax = 1900
        self.Zmin = 0.001
        self.Zmax = 3.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+self.lsp+"}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagOn = False
        self.diagTopOn = False
        self.blankTopCorr = False
        self.diagWOn = False

    def ctau(self) : return True

    def T1qqqqLLPrompt(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLLPrompt"
        self.color = rt.kGreen+3
        self.label = "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} "+self.lsp
        self.label2 = "Prompt #tilde{g} decay"
        self.label3 = "#tilde{g} #rightarrow q #bar{q} "+self.lsp+" (Prompt decay)"

    def T1qqqqLL0p001(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL0p001"
        self.color = rt.kGreen+2
        self.label2 = "c#tau_{0} = 0.001 mm" if self.ctau() else "#tau_{0} = 3 #times 10^{-6} ns"
        self.label3 = self.label2

    def T1qqqqLL0p01(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL0p01"
        self.color = rt.kGreen+0
        self.label2 = "c#tau_{0} = 0.01 mm" if self.ctau() else "#tau_{0} = 3 #times 10^{-5} ns"
        self.label3 = self.label2

    def T1qqqqLL0p1(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL0p1"
        self.color = rt.kOrange
        self.label2 = "c#tau_{0} = 0.1 mm" if self.ctau() else "#tau_{0} = 3 #times 10^{-4} ns"
        self.label3 = self.label2

    def T1qqqqLL1(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL1"
        self.color = rt.kOrange+3
        self.label2 = "c#tau_{0} = 1 mm" if self.ctau() else "#tau_{0} = 3 #times 10^{-3} ns"
        self.label3 = self.label2

    def T1qqqqLL10(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL10"
        self.color = rt.kRed
        self.label2 = "c#tau_{0} = 10 mm" if self.ctau() else "#tau_{0} = 3 #times 10^{-2} ns"
        self.label3 = self.label2

    def T1qqqqLL100(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL100"
        self.color = rt.kBlue
        self.label2 = "c#tau_{0} = 100 mm" if self.ctau() else "#tau_{0} = 3 #times 10^{-1} ns"
        self.label3 = self.label2

    def T1qqqqLL1000(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL1000"
        self.color = rt.kCyan+1
        self.label2 = "c#tau_{0} = 1000 mm" if self.ctau() else "#tau_{0} = 3 #times 10^{0} ns"
        self.label3 = self.label2

    def T1qqqqLL10000(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL10000"
        self.color = rt.kMagenta
        self.label2 = "c#tau_{0} = 10#kern[0.05]{000 mm}" if self.ctau() else "#tau_{0} = 3 #times 10^{1} ns"
        self.label3 = self.label2

    def T1qqqqLL100000(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLL100000"
        self.color = rt.kGray
        self.label2 = "c#tau_{0} = 100#kern[0.05]{000 mm}" if self.ctau() else "#tau_{0} = 3 #times 10^{2} ns"
        self.label3 = self.label2

    def T1qqqqLLStable(self):
        self.T1qqqqLL()
        self.modelname = "T1qqqqLLStable"
        self.color = rt.kGray+2
        self.label = "pp #rightarrow #tilde{g} #tilde{g}"
        self.label2 = "Metastable #tilde{g}"
        self.label3 = "Metastable #tilde{g}"
