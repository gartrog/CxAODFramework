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
* CxAODMaker Update FatJet calibration to EtaJET\_JMS jennis

## 15-08-18
* CxAODMaker adding isolation selection tool to photon handler, and other small changes -- support for additional triggers, latest config files, etc. prose
* CxAODTools skip duplicated mc\_channel\_number, remove deprecated DerivEffProvider, Daniel
* CxAODTools update to vbf+gamma OR tool and addition of common properties for photon isolation prose
* CxAODReader  CXAOD-41: use applySherpaTruthPtCut config flag, default is false, Daniel
* CxAODReader  adding sample names for VBF+gamma analysis for HistNameSvc, prose
* CxAODReader\_VHbb  minor changes to AnalysisReader\_VBFHbb -- different histogram binning, MV2c20 cut, debug info, prose
* FrameworkExe  add sample HZZllqq,  CXAOD-41: add applySherpaTruthPtCut flag, Daniel
* FrameworkExe adding the HZZvvqq sample string, arturo
* FrameworkExe support for additional vbf+gamma samples, prose

## 15-08-19
* CxAODTools fixed typo in HLT\_mu24\_iloose\_L1MU15 trigger, amontalb
* CxAODTools Update made to the XSectionProvider to allow for the XSection\_13TeV.txt and XSection\_8TeV.txt files to be read in properly and contain the additional information that sets the sample name associated to a given DSID.   (performed for @CxAOD-19), meehan
* CxAODReader Update made to AnalysisReader and HistNameSvc to simplify the manner in which the sample name is determined.  It is no longer hardcoded into the HistNameSvc and therefore, when new samples are added, one need not update this file.  Instead, the sample name is now set by using the map generated in the XSectionProvider tool, which has been modified as well, to allow for another member of the struct containing the sample name.  (performed for @CxAOD-19), meehan
* CXAODReader\_VHbb added missing protection, hannah

## 15-08-20
* CxAODMaker shallow copies of input containers recorded in EventLoop's TStore, resolves JIRA ticket CXAOD-38, Kristian
* CxAODReader remove some debug output, add counter for selected events, print at end of job, Daniel
* FrameworkExe Update of the samples to copy in SVN, more names have been added to the list too, Arturo

## 15-08-21
* CxAODReader\_VHbb, proper init, Hannah

## 15-08-22

## 15-08-23

## 15-08-24
* CxAODTools, CxAODReader, CxAODReader\_VHbb, FrameworkExe, new b-tagging tool, jhetherl
* CxAODReader\_VHbb : put m\_doTruthTagging flag back, hanar

## 15-08-25
* CxAODMaker, CxAODTools : Add Jet Shape related paramters to the CxAOD and minor modification in type of return of get\_indexPV() function, okumura
* CxAODReader : init m\_triggerTool with nullptr on job creation, dbuesche
* CxAODReader : put trigger decision access at reader level, djamin
* CxAODReader : skip initialization of m\_bTagTool if config invalid (prevent crash), safely delete m\_bTagTool and m\_overlapRemoval, dbuesche
* CxAODReader\_VHbb : Update from Yasu - for VBF inclusive analysis, add a new function declaration and implementation, and add lines to swithc type to "VBFIncl" in nitializeSelection function, okumura
* CxAODTools\_VHbb : add VBF inclusive analysis selector reproducing the Run1 analysis pre-selection so far, okumura

## 15-08-26
* CxAODTools : Added OverlapRegister and related files. First part of [CERN-JIRA](CXAOD-52), grkeren
* CxAODMaker : Added OverlapRegister to CxAODMaker - turned off by default. Second part of [CERN-JIRA](CXAOD-52). Next is implementing it in CxAODReader., grkeren
* CxAODReader : add info output for finalize methods, dbuesche
* CxAODReader : removed m\_mcChannel retrieval in initializeIsMC (); ensure consistent usage throughout the code; CXAOD-51, hanar
* CxAODTools : proper CLIDs, adjusted print-out, grkeren
* FrameworkExe : remove duplicated comment, dbuesche
* FrameworkExe : update default sample (previous was removed), add TrackJet::AddPreselJets=true, dbuesche

## 15-08-27
* CxAODMaker : copyIfExists ConeTruthLabelID and HadronConeExclTruthLabelID for truth jets, dbuesche
* CxAODMaker : replace using PileupReweightingTool by wrapper PUReweightingTool; CXAOD-54, hanar
* CxAODMaker : Update to photon efficiency correction config files, prose
* CxAODMaker\_VHbb : Remove VBF0phEvtSelection and add VBFInclEvtSelection, prose
* CxAODReader : delete m\_triggerTool, hanar
* CxAODReader : introduced setEventWeight method, where MC gen weight, lumi weight and PU weight are derived and multplied; getLumiWeight(double& weight) was renamed and cleaned-up; applyPUWeight() was introduced where the PU weight is either retrieved from the input CxAOD or retrieved from the PUReweightingTool depending on the config settings; the execute() method was restructured and cleaned-up, in order to avoid retrieving the eventInfo several times and to decorate it with the lumi and PU weight for each systematic variation; CXAOD-46, hanar
* CxAODReader\_VHbb : changes to vbf0ph analysis reader, and update vbf analyses names for consistent analysis selection between reader and maker, prose
* CxAODTools : condensed the code for OverlapRegisterAccessor, grkeren
* CxAODTools : fix 2lep TriggerTool for matching bug and put xe80 by default for 0lep, djamin
* CxAODTools : introduced setEventWeight method, where MC gen weight, lumi weight and PU weight are derived and multplied; getLumiWeight(double& weight) was renamed and cleaned-up; applyPUWeight() was introduced where the PU weight is either retrieved from the input CxAOD or retrieved from the PUReweightingTool depending on the config settings; the execute() method was restructured and cleaned-up, in order to avoid retrieving the eventInfo several times and to decorate it with the lumi and PU weight for each systematic variation; CXAOD-46, hanar
* CxAODTools : Use isWHSignalElectrons in VBF+gamma OR, prose
* CxAODTools\_VHbb : Updating VBFHbb\*EvtSelection to a common preSelection so that vbf and vbf+gamma can share CxAODs, prose
* CxAODTools : wrapper for PU reweighting; CXAOD-54, hanar
* FrameworkExe : enable PU retrieval in config; CXAOD-46, hanar

## 15-08-28
* CxAODMaker : add electron isolation effSF; CXAOD-37, lulu
* CxAODMaker : CXAOD-58: add efficiency scale factors for Tight working point, dbuesche
* CxAODMaker : CXAOD-58 bugfix: write correct looseIsoSF, dbuesche
* CxAODMaker : CXAOD-58: user proper xAOD::Muon::Quality enum for MuonSelectionTool (no change in behaviour), dbuesche
* CxAODMaker : removed deprecated debugging output; added debug output; CXAOD-63, hanar
* CxAODReader : CXAOD-40: temporarily disable trigger tool initialization, dbuesche
* CxAODReader\_VHbb : CXAOD-40: temporarily enable trigger tool initialization in CxAODReader\_VHbb, dbuesche
* CxAODTools : add electron isolation effSF, lulu
* CxAODTools : rm \_\_MAKECINT\_\_, hanar
* FrameworkExe : added two additional, recommended systematics affecting METTrack, hanar

## 15-08-31
* CxAODMaker : Higgs tagger, benitezj
* CxAODTools : adding deletes..., hanar
* CxAODTools : Higgs tagger, benitezj
* CxAODTools : use m\_msgLevel; reduce messaging, hanar
