import sys
import math
from inputFile import *
from smsPlotXSEC import *
from smsPlotCONT import *
from smsPlotBrazil import *

class ContPlotCollection():
    def __init__(self,modelNames,modelType,transpose=False,name = None):
        self.modelNames = modelNames
        lsp = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        label = "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} "+lsp
        modelTypeDict = {
            "gluino":"pp #rightarrow #tilde{g} #tilde{g}",
            "squark":"pp #rightarrow #tilde{q} #tilde{q}",
            "split":label
            }
        if modelType not in modelTypeDict:
            raise AttributeError, "Unsupported model type: "+modelType
        self.modelType = modelType
        self.label = modelTypeDict[modelType]
        self.labelOffset = 17.
        self.transpose = transpose
        self.name = name
        self.contPlotDict = {}

    def setContPlots(self,filenameTemplate):
        self.models = []
        for modelname in self.modelNames:
            makeHisto = True
            if modelname != self.modelNames[0]:
                makeHisto = False
            # read the config file
            fileIN = inputFile(filenameTemplate.format(modelname),transpose=self.transpose) #.replace("T2qqDegen","T2qq")
            contPlot = smsPlotCONT(modelname, fileIN.HISTOGRAM, fileIN.OBSERVED, fileIN.EXPECTED, fileIN.ENERGY, fileIN.LUMI, 
                    fileIN.PRELIMINARY, "CONT",makeHisto)
            self.contPlotDict[modelname] = contPlot
            if self.name == "natural" or self.name == "naturalWT1":
                if contPlot.model.modelname == "T1tttt":
                    contPlot.model.color = rt.kGray+1
            self.models.append(contPlot.model)
        self.getRanges()
        self.setStandard()

    def setStandard(self): 
        self.preliminary = self.contPlotDict[self.modelNames[0]].preliminary
        self.lumi = self.contPlotDict[self.modelNames[0]].lumi
        self.energy = self.contPlotDict[self.modelNames[0]].energy
        self.c = self.contPlotDict[self.modelNames[0]].c
        self.histo = self.contPlotDict[self.modelNames[0]].histo
        self.contPlotDict[self.modelNames[0]].emptyHistogramFromModel((self.Xmin,self.Xmax,self.Ymin,self.Ymax))
        self.uniqueModelList = []
        for model in self.models:
            if not any([model.modelname == x.modelname for x in self.uniqueModelList]):
                self.uniqueModelList.append(model)
        self.nmodels = 0
        if self.modelType == "split" : self.nmodels = (len(self.uniqueModelList)+1)/2
        else : self.nmodels = len(self.uniqueModelList)

    def getRanges(self):
        Xmin,Ymin,Xmax,Ymax = 1E7,1E7,-1,-1
        for contPlot in self.contPlotDict.itervalues():
            Xmin = min(contPlot.model.Xmin,Xmin)
            Ymin = min(contPlot.model.Ymin,Ymin)
            Xmax = max(contPlot.model.Xmax,Xmax)
            Ymax = max(contPlot.model.Ymax,Ymax)
        self.Xmin = Xmin
        self.Ymin = Ymin
        self.Xmax = Xmax
        self.Ymax = Ymax
        print self.name
        if self.name == "gluino":
            self.Xmin = 600
            self.Xmax = 2300
            self.Ymin = 0
            self.Ymax = 2000
        elif self.name == "squark":
            self.Xmin = 0
            self.Xmax = 1500
            self.Ymin = 0
            self.Ymax = 1300
        elif self.name == "split":
            self.Xmin = 600
            self.Xmax = 2000
            self.Ymin = 0
            self.Ymax = 2200
        if self.transpose:
            if self.name == "gluino":
                self.Xmin = 600
                self.Xmax = 2300
                self.Ymin = 0
                self.Ymax = 3400
            elif self.name == "squark":
                self.Xmin = 0
                self.Xmax = 1500
                self.Ymin = 0
                self.Ymax = 2600
            elif self.name == "squarkZoom":
                self.Xmin = 0
                self.Xmax = 1000
                self.Ymin = 0
                self.Ymax = 800
            elif self.name == "split":
                self.Xmin = 600
                self.Xmax = 2000
                self.Ymin = 0
                self.Ymax = 3200

    def DrawLegend(self):
        LObsList = []
        LExpList = []
        textObsList = []
        xRange = self.Xmax-self.Xmin
        yRange = self.Ymax-self.Ymin
        seenT2qq = False
        iM = 0

        for iM,model in enumerate(self.uniqueModelList):
            yoffset = -(yRange/self.labelOffset)*int(iM%self.nmodels)
            xoffset = int(iM/self.nmodels)*0.5*xRange

            LObs = rt.TGraph(2)
            LObs.SetName("LObs")
            LObs.SetTitle("LObs")
            LObs.SetLineColor(model.color)
            LObs.SetLineStyle(1)
            LObs.SetLineWidth(4)
            LObs.SetMarkerStyle(20)
            LObs.SetPoint(0,self.Xmin+3*xRange/100+xoffset, self.Ymax-1.35*yRange/10+yoffset)
            LObs.SetPoint(1,self.Xmin+10*xRange/100+xoffset, self.Ymax-1.35*yRange/10+yoffset)
            if model.label2 != "":
                textObs = rt.TLatex(self.Xmin+11*xRange/100+xoffset, 
                                    self.Ymax-1.50*yRange/10+yoffset, 
                                    model.label+"  ("+model.label2+")")
            else:
                textObs = rt.TLatex(self.Xmin+11*xRange/100+xoffset, 
                                    self.Ymax-1.50*yRange/10+yoffset, 
                                    model.label)
            textObs.SetTextFont(42)
            textObs.SetTextSize(0.030)
            textObs.Draw()
            textObsList.append(textObs)

            LExp = rt.TGraph(2)
            LExp.SetName("LObsP")
            LExp.SetTitle("LObsP")
            LExp.SetLineColor(model.color)
            LExp.SetLineStyle(7)
            LExp.SetLineWidth(4)
            LExp.SetMarkerStyle(20)
            LExp.SetPoint(0,self.Xmin+3*xRange/100+xoffset, self.Ymax-1.20*yRange/10+yoffset)
            LExp.SetPoint(1,self.Xmin+10*xRange/100+xoffset, self.Ymax-1.20*yRange/10+yoffset)

            LObs.Draw("LSAME")
            LExp.Draw("LSAME")

            LObsList.append(LObs)
            LExpList.append(LExp)

        yoffset = -(-1.6)*(yRange/self.labelOffset)
        LObs= rt.TGraph(2)
        LObs.SetName("LObs")
        LObs.SetTitle("LObs")
        LObs.SetLineColor(rt.kBlack)
        LObs.SetLineStyle(7)
        LObs.SetLineWidth(4)
        LObs.SetMarkerStyle(20)
        LObs.SetPoint(0,self.Xmin+74*xRange/100+xoffset, self.Ymax-1.35*yRange/10+yoffset)
        LObs.SetPoint(1,self.Xmin+81*xRange/100+xoffset, self.Ymax-1.35*yRange/10+yoffset)

        #textObs = rt.TLatex(0.15,0.90, "Expected")
        textObs = rt.TLatex(self.Xmin+82*xRange/100+xoffset, self.Ymax-1.50*yRange/10+yoffset, "Expected")
        textObs.SetTextFont(42)
        textObs.SetTextSize(0.030)
        textObs.Draw()
        textObsList.append(textObs)

        yoffset = -(-0.8)*(yRange/self.labelOffset)
        LExp= rt.TGraph(2)
        LExp.SetName("LExp")
        LExp.SetTitle("LExp")
        LExp.SetLineColor(rt.kBlack)
        LExp.SetLineStyle(1)
        LExp.SetLineWidth(4)
        LExp.SetMarkerStyle(20)
        LExp.SetPoint(0,self.Xmin+74*xRange/100+xoffset, self.Ymax-1.35*yRange/10+yoffset)
        LExp.SetPoint(1,self.Xmin+81*xRange/100+xoffset, self.Ymax-1.35*yRange/10+yoffset)
        textObs = rt.TLatex(self.Xmin+82*xRange/100+xoffset, self.Ymax-1.50*yRange/10+yoffset, "Observed")
        textObs.SetTextFont(42)
        textObs.SetTextSize(0.030)
        textObs.Draw()
        textObsList.append(textObs)

        LObs.Draw("LSAME")
        LExp.Draw("LSAME")
        LObsList.append(LObs)
        LExpList.append(LExp)

        self.c.LObsList = LObsList
        self.c.LExpList = LExpList
        self.c.textObsList = textObsList

    def DrawText(self):
        #redraw axes
        self.contPlotDict[self.modelNames[0]].c.RedrawAxis()
        # white background
        graphWhite = rt.TGraph(5)
        graphWhite.SetName("white")
        graphWhite.SetTitle("white")
        graphWhite.SetFillColor(rt.kWhite)
        graphWhite.SetFillStyle(1001)
        graphWhite.SetLineColor(rt.kBlack)
        graphWhite.SetLineStyle(1)
        graphWhite.SetLineWidth(2)
        graphWhite.SetPoint(0,self.Xmin, self.Ymax)
        graphWhite.SetPoint(1,self.Xmax, self.Ymax)
        graphWhite.SetPoint(2,self.Xmax, self.Ymax*(1-(min(self.nmodels,len(self.uniqueModelList))+0.5)/self.labelOffset-0.8/9))
        graphWhite.SetPoint(3,self.Xmin, self.Ymax*(1-(min(self.nmodels,len(self.uniqueModelList))+0.5)/self.labelOffset-0.8/9))
        graphWhite.SetPoint(4,self.Xmin, self.Ymax)
        graphWhite.Draw("FSAME")
        graphWhite.Draw("LSAME")
        self.c.graphWhite = graphWhite
       	CMS_lumi.writeExtraText = 0
	CMS_lumi.extraText = "Supplementary"#self.preliminary
        print self.preliminary
	CMS_lumi.lumi_13TeV = self.lumi+" fb^{-1}"

	CMS_lumi.lumi_sqrtS = self.energy+" TeV"  
	iPos=0
	CMS_lumi.CMS_lumi(self.c,4, iPos)
        # CMS LABEL
        textCMS = rt.TLatex(0.27,0.96,"  %s " %(self.preliminary))
        textCMS.SetNDC()
        textCMS.SetTextAlign(13)
        textCMS.SetTextFont(52)
        textCMS.SetTextSize(0.038)
        textCMS.Draw()
        self.c.textCMS = textCMS
        # MODEL LABEL
        textModelLabel= rt.TLatex(0.18,0.90,"%s   NLO+NLL exclusion" %self.label)
        textModelLabel.SetNDC()
        textModelLabel.SetTextAlign(13)
        textModelLabel.SetTextFont(42)
        textModelLabel.SetTextSize(0.035)
        textModelLabel.Draw()
        self.c.textModelLabel = textModelLabel

        # LABEL MWtop
        if any([x.diagWOn for x in self.models]):
            xT = 0.58
            yT = 0.56
            angleT = 50.
            if self.transpose:
                if "Zoom" in self.name:
                    xT = 0.87
                    yT = 0.25
                    angleT = 0
                else:
                    xT = 0.82
                    yT = 0.19
                    angleT = 0
            textMW = rt.TLatex(xT,yT,"#Deltam_{1}")
            textMW.SetNDC()
            textMW.SetTextAlign(13)
            textMW.SetTextFont(42)
            textMW.SetTextSize(0.024)
            textMW.SetTextAngle(angleT)
            textMW.Draw()
            self.c.textMW = textMW
            xT = 0.19
            yT = 0.58
            textMWop2 = rt.TLatex(xT,yT,"#Deltam_{1} #equiv m#kern[0.2]{_{ #tilde{t}}} - m_{#chi^{0}_{1}} = m_{W}")
            textMWop2.SetNDC()
            textMWop2.SetTextAlign(13)
            textMWop2.SetTextFont(42)
            textMWop2.SetTextSize(0.024)
            textMWop2.Draw()
            self.c.textMWop2 = textMWop2

        # MTOP LABEL
        if any([x.diagTopOn for x in self.models]):
            xT = 0.63
            yT = 0.56
            angleT = 50.
            if self.transpose:
                if "Zoom" in self.name:
                    xT = 0.87
                    yT = 0.34
                    angleT = 0
                else:
                    xT = 0.82
                    yT = 0.218
                    angleT = 0
            textMTop = rt.TLatex(xT,yT,"#Deltam_{2}")
            textMTop.SetNDC()
            textMTop.SetTextAlign(13)
            textMTop.SetTextFont(42)
            textMTop.SetTextSize(0.024)
            textMTop.SetTextAngle(angleT)
            textMTop.Draw()
            self.c.textMTop = textMTop

            xT = 0.19
            yT = 0.54
            textMTop2 = rt.TLatex(xT,yT,"#Deltam_{2} #equiv m#kern[0.2]{_{ #tilde{t}}} - m_{#chi^{0}_{1}} = m_{ t}")
            textMTop2.SetNDC()
            textMTop2.SetTextAlign(13)
            textMTop2.SetTextFont(42)
            textMTop2.SetTextSize(0.024)
            textMTop2.Draw()
            self.c.textMTop2 = textMTop2

    def DrawDiagonalMTop(self):
        if self.transpose:
            xs = array("d",[self.Xmin,self.Xmax])
            ys = array("d",[175,175])
            diagonal = rt.TGraph(2, xs, ys)
        else:
            xs = array("d",[self.Xmin,(self.Xmax-self.Xmin)/2+self.Xmin,self.Xmax])
            ys = array("d",[x - 175. for x in xs])
            diagonal = rt.TGraph(3, xs, ys)
        diagonal.SetName("diagonal")
        diagonal.SetFillColor(rt.kGray)
        diagonal.SetLineColor(rt.kBlack)
        diagonal.SetLineStyle(2)
        #diagonal.Draw("FSAME")
        diagonal.Draw("LSAME")
        self.c.topDiagonal = diagonal

    def DrawTransposeLine(self):
        if self.transpose:
            xs = array("d",[self.Xmin,self.Xmax])
            ys = array("d",[x for x in xs])
            diagonal = rt.TGraph(2, xs, ys)
        diagonal.SetName("transpose")
        diagonal.SetFillColor(rt.kGray)
        diagonal.SetLineColor(rt.kBlack)
        diagonal.SetLineStyle(2)
        #diagonal.Draw("FSAME")
        diagonal.Draw("LSAME")
        self.c.transposeLine = diagonal

    def DrawDiagonalMW(self):
        if self.transpose:
            xs = array("d",[self.Xmin,self.Xmax])
            ys = array("d",[80.4,80.4])
            diagonal = rt.TGraph(2, xs, ys)
        else:
            xs = array("d",[self.Xmin,(self.Xmax-self.Xmin)/2+self.Xmin,self.Xmax])
            ys = array("d",[x - 80.4 for x in xs])
            diagonal = rt.TGraph(3, xs, ys)
        diagonal.SetName("diagonal")
        diagonal.SetFillColor(rt.kWhite)
        diagonal.SetLineColor(rt.kBlack)
        diagonal.SetLineStyle(2)
        #diagonal.Draw("FSAME")
        diagonal.Draw("LSAME")
        self.c.wDiagonal = diagonal

    def DrawDiagonal(self):
        if self.transpose:
            return 
        else:
            xs = array("d",[self.Xmin,(self.Xmax-self.Xmin)/2+self.Xmin,self.Xmax])
            ys = array("d",[x for x in xs])
            diagonal = rt.TGraph(3, xs, ys)
        diagonal.SetName("diagonal")
        diagonal.SetFillColor(rt.kGray)
        diagonal.SetLineColor(rt.kBlack)
        diagonal.SetLineStyle(2)
        #diagonal.Draw("FSAME")
        diagonal.Draw("LSAME")
        self.c.diagonal = diagonal

    def DrawTopCorrPoly(self):
        if self.transpose:
            xs = array("d",[self.Xmin,self.Xmin,275.,275.])
            ys = array("d",[150.,200.,200,150])
        else:
            xs = array("d",[150.+self.Ymin,200.+self.Ymin,287.5,262.5])
            ys = array("d",[self.Ymin,self.Ymin,87.5,112.5])
        trap = rt.TPolyLine(4,xs,ys)
        trap.SetFillColor(rt.kGray)
        trap.SetLineColor(0)
        trap.Draw("FSAME")
        self.c.topCorr = trap

    def Draw(self):
        self.contPlotDict[self.modelNames[0]].Draw(simple=True)
        blankList = [model.modelname.replace("_","-") for model in self.models if model.blankTopCorr]
        remainderList = [model.modelname.replace("_","-") for model in self.models if not model.blankTopCorr]
        if len(blankList) != 0:
            for modelName in blankList:
                self.contPlotDict[modelName].DrawLinesSimple()
            self.DrawTopCorrPoly()
        for modelName in remainderList:
            self.contPlotDict[modelName].DrawLinesSimple()

        self.c.SetLeftMargin(0.16)
        self.c.SetRightMargin(0.05)
        self.contPlotDict[self.modelNames[0]].emptyHisto.GetYaxis().SetTitleOffset(1.5)
        if self.transpose:
            self.contPlotDict[self.modelNames[0]].emptyHisto.GetYaxis().SetTitle(self.contPlotDict[self.modelNames[0]].emptyHisto.GetXaxis().GetTitle().replace(" [GeV]","") + " - " + self.contPlotDict[self.modelNames[0]].emptyHisto.GetYaxis().GetTitle())
        if any([model.diagOn for model in self.models]):
            self.DrawDiagonal()
        if any([model.diagTopOn for model in self.models]):
            self.DrawDiagonalMTop()
        if any([model.diagWOn for model in self.models]):
            self.DrawDiagonalMW()
        if self.transpose:
            self.DrawTransposeLine()

        self.DrawText()
        self.DrawLegend()

    def Save(self,name):
        self.contPlotDict[self.modelNames[0]].Save(name)

def makeSummary(outputname,filenameTemplate,modelNames,modelType,transpose):
    contPlotCollection = ContPlotCollection(modelNames,modelType,name= outputname,transpose=transpose)
    contPlotCollection.setContPlots(filenameTemplate)
    contPlotCollection.Draw()
    contPlotCollection.Save("{0}SUMMARY{1}".format(outputname,{True:"_transpose",False:""}[transpose]))

if __name__ == '__main__':
    # read input arguments
    transpose = False
    filenameTemplate = "./config/SUS16038/{0}_SUS16038.cfg"
    gluinoModelNames = ["T1qqqq","T1bbbb","T1tttt"]
    squarkModelNames = ["T2qqOne","T2qqDegen","T2bb","T2tt","T2cc"]
    splitModelNames = [
        "T1qqqqLL0p001",
        "T1qqqqLL0p01",
        "T1qqqqLL0p1",
        "T1qqqqLL1",
        "T1qqqqLL10",
       "T1qqqqLL100",
        "T1qqqqLL1000",
        "T1qqqqLL10000",
        #"T1qqqqLL100000",
        ]

    makeSummary("squark",filenameTemplate,squarkModelNames,"squark",transpose=False)
    makeSummary("gluino",filenameTemplate,gluinoModelNames,"gluino",transpose=False)
    makeSummary("split",filenameTemplate,splitModelNames,"split",transpose=False)

    makeSummary("squark",filenameTemplate,squarkModelNames,"squark",transpose=True)
    makeSummary("gluino",filenameTemplate,gluinoModelNames,"gluino",transpose=True)
    makeSummary("split",filenameTemplate,splitModelNames,"split",transpose=True)

    makeSummary("squarkZoom",filenameTemplate,squarkModelNames,"squark",transpose=True)
