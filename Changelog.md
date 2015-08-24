# Global changelog for the full CxAODFramework -- VHbb variant

## 15-08-04

* CxAODReader: Changes to HistSvc for filling weight systematics, proposed by Andy, merged by Daniel
* Tag FrameworkSub 12-3, with tags of CxAODReader and CxAODReader\_VHbb. Last ones compatible with DC14
* CxAODReader: change in constructor of MVATree, to allow trees with systematics. Paul Mullen
* FrameworkExe: container names of framework-read.cfg updated to rel20 ; rel19 names removed. Daniel

## 15-08-05

* CxAODReader/CxAODReader\_VHbb/CxAODTools/FrameworkExe: new BTagging tool, final rel20 one. Jeff
* FrameworkExe: CXAOD-8, fixed name of JER systematic. Daniel
* FrameworkExe: correct name in testCxAODVariations. Daniel

## 15-08-06

* FrameworkExe: use of a few command-line arguments in hsg5framework. Jon
* CxAODMaker: emulation of the VBF+photon trigger. Liaoshan
* CxAODMaker/FrameworkExe: CXAOD-13, fix bug with MET systematics. Nicolas
* CxAODReader: Add function to fill cutflow hists with/without weights in one go. Sam

## 15-08-07

* FrameworkSub: Update the lists of samples in In/ with generic lists that should be updated. CXAOD-17. Daniel
* Tag FrameworkSub 12-4: like 12-2, with updated samples list, for new and complete production with DxAOD. Daniel
* CxAODMaker: CXAOD-20: more truth information, well targetted at our processes. Daniel

## 15-08-08

* CxAODReader: Fix bugs with new b-tagging on data. Daniel
* CxAODReader: Some cleanups. Daniel

## 15-08-10

* FrameworkSub: CXAOD-21: Bump to 2.3.23. Bugfixes in xAODRootAccess. No change in CP tools. Daniel
* FrameworkSub: bugfixes in sample names in In/ files. Daniel
* CxAODMaker: re-enable writing of event count histogram to CxAOD file. Daniel

## 15-08-11

* CxAODReader: Add possibility to call automatic yield file generation from reader executable. CXAOD-22. Daniel
* Tag FrameworkSub 12-5: same as 12-4, with fixed dataset names in In/. Daniel
* CxAODMaker\_VHbb/FrameworkExe: dump in CxAOD only fat jets that pass some preselection. CXAOD-23. Nicolas
* CxAODTool/CxAODMaker: add LumiMetaDataTool to propagate LB information on data. CXAOD-3. Nicolas
* CxAODMaker: Fix crashes in 2 lepton production due to nullptr in JetRegressionVars. CXAOD-28 CXAOD-29. Jon
* CxAODReader/CxAODReader\_VHbb: some cleanups. Daniel
* Tag FrameworkSub 12-6: same as 12-5, with fix for crashed in 2 lepton production applied. Daniel
* CxAODReader/FrameworkExe: CXAOD-31: enable failure on unchecked status codes by default in the Reader. Daniel

## 15-08-12

* CxAODReader: fixes on btagging. CXAOD-18, CXAOD-34. Hannah
* CxAODMaker: Update PU. CXAOD-16. Daniel
* CxAODTools/CxAODMaker: Small changes to taus in OR. Agni

## 15-08-13

* CxAODMaker/FrameworkSub: Update data and GRL up to period C5. CXAOD-25. Daniel
* FrameworkExe/CxAODReader: Use xAOD branch access when reading NominalOnly. CXAOD-35. Daniel

## 15-08-14

* Make PRW file configurable from cfg file. CXAOD-36. Lulu

## 15-08-15

## 15-08-16
* CxAODReader fix compiler warning. Daniel

## 15-08-17
* CxAODMaker Update FatJet calibration to EtaJET_JMS jennis

## 15-08-18
* CxAODMaker adding isolation selection tool to photon handler, and other small changes -- support for additional triggers, latest config files, etc. prose
* CxAODTools skip duplicated mc_channel_number, remove deprecated DerivEffProvider, Daniel
* CxAODTools update to vbf+gamma OR tool and addition of common properties for photon isolation prose
* CxAODReader  CXAOD-41: use applySherpaTruthPtCut config flag, default is false, Daniel
* CxAODReader  adding sample names for VBF+gamma analysis for HistNameSvc, prose
* CxAODReader_VHbb  minor changes to AnalysisReader_VBFHbb -- different histogram binning, MV2c20 cut, debug info, prose
* FrameworkExe  add sample HZZllqq,  CXAOD-41: add applySherpaTruthPtCut flag, Daniel
* FrameworkExe adding the HZZvvqq sample string, arturo
* FrameworkExe support for additional vbf+gamma samples, prose

## 15-08-19
* CxAODTools fixed typo in HLT_mu24_iloose_L1MU15 trigger, amontalb
* CxAODTools Update made to the XSectionProvider to allow for the XSection_13TeV.txt and XSection_8TeV.txt files to be read in properly and contain the additional information that sets the sample name associated to a given DSID.   (performed for @CxAOD-19), meehan
* CxAODReader Update made to AnalysisReader and HistNameSvc to simplify the manner in which the sample name is determined.  It is no longer hardcoded into the HistNameSvc and therefore, when new samples are added, one need not update this file.  Instead, the sample name is now set by using the map generated in the XSectionProvider tool, which has been modified as well, to allow for another member of the struct containing the sample name.  (performed for @CxAOD-19), meehan
* CXAODReader_VHbb added missing protection, hannah

## 15-08-20
* CxAODMaker shallow copies of input containers recorded in EventLoop's TStore, resolves JIRA ticket CXAOD-38, Kristian
* CxAODReader remove some debug output, add counter for selected events, print at end of job, Daniel
* FrameworkExe Update of the samples to copy in SVN, more names have been added to the list too, Arturo

## 15-08-21  
* CxAODReader_VHbb, proper init, Hannah

## 15-08-22

## 15-08-23

## 15-08-24
* CxAODTools, CxAODReader, CxAODReader_VHbb, FrameworkExe, new b-tagging tool, jhetherl
* CxAODReader_VHbb put m_doTruthTagging flag back, Hannah
