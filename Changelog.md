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

## 15-09-01
* FrameworkExe-00-01-10: CXAOD-43: disable running on ggA (missing Xsection), daniel
* Tag FrameworkSub 12-8: Able to read 12-6 CxAODs. daniel
* CxAODTools, CxAODReader, CxAODReader\_VHbb: fix analysisType bug int/str in TriggerTool. CXAOD-40. david

## 15-09-02
* CxAODTools, CxAODMaker: modification in PU tool logic. CXAOD-54. jose
* CxAODTools, CxAODReader\_VHbb: add definition of trigger used for A-\>Zh, vbf and vbfa (matching too) analysis. david
* CxAODMaker: bugfix for MET in systematics. Takuya
* CxAODReader: adapt for the interface changes introduced by Revision: 692706; CXAOD-54. hannah
* CxAODMaker, CxAODTools: adding PDF info as props to eventinfo. CXAOD-82. ines

## 15-09-03
* FrameworkSub: updated cross section numbers 361106-361108, 361372-361443. ycguo
* CxAODMaker, CxAODTools, Add official BosonTag tool to FatJetHandler and switch for fatjet mass calibration. CXAOD-81. joe
* CxAODMaker: fix Higgs tagger corrected momentum. CXAOD-81. jose
* FrameworkSub: added back dijet and A-\>Zh. andy
* CxAODReader: added switches for applying lumi and PU weights; CXAOD-46. hannah

## 15-09-04
* CxAODMaker : Add official BosonTag tool to FatJetHandler and switch for fatjet mass calibration, jennis
* CxAODMaker : debug flag, benitezj
* CxAODMaker : fix Higgs tagger corrected momentum, benitezj
* CxAODReader : added switches for applying lumi and PU weights; CXAOD-46, hanar
* CxAODTools : Add boson substructure property for fatjets, jennis
* FrameworkExe : added switches for applying lumi and PU weights; CXAOD-46, hanar
* FrameworkSub : Added dijet and A-\>Zh, amehta

## 15-09-06
* CxAODMaker : Implement possible workaround for CutBookkkeepers bug. CXAOD-89, nmorange

## 15-09-07
* CxAODMaker, CxAODTools : add mu18\_mu8noL1 and mu24\_mu8noL1 triggers at Maker level to store on CxAODs, djamin
* CxAODMaker : CXAOD-45 updated TauHandler to run TauTruthMatchTool - needed for TauSmearingTool. Aparently this wont be neccessary when this gets run in the derivations. This fixes the problem stopping us moving to 2.3.25, haysjm
* FrameworkExe : CXAOD-45 added a flag to the default config file to turn on running of the TauTruthMatchingTool in the TauHandler - should be tru by default otherwise tool will fail on current derivations, haysjm
* FrameworkSub : added missing checkout of JetSubStructureMomentTools needed to match version of JetSubStructureutils, haysjm

## 15-09-08
* FrameworkSub : adding madgraph xs FrameworkSub in mydevbranch, cwang

## 15-09-09
* CxAODReader: do not write MVA job output stream if flag is off, fsforza
* CxAODMaker: Added switch to turn of Xbb tagging. Disable this automatically for non-standard fatjet collections. jennis

## 15-09-10
* CxAODMaker: Removed error messages from FatJetHandler for lack of muon collection if Xbb tagger disabled, jennis

## 15-09-11
* CxAODTools: added switch to remove tau from OR - default is to remove (avoids change inbehaviour) - but config option added to default config file to switch off taus in OR CXAOD-90. haysjm
* CxAODMaker: modified TauHandler to use new switch in TauAnalysisTools-00-01-09 to turn off truth match checking - this means we don't need to run truth matching - which wont work on our current derivations CXAOD-92 CXAOD-90. haysjm
* FrameworkExe: added switches to the default config file to not run TauTruthMatching and to remove taus from the overlap removal CXAOD-90 CXAOD-92. haysjm
* FrameworkSub: moved the release up to 2.3.25 and added checkout of TauAnalysisTools-00-01-09, CXAOD-92, CXAOD-90, CXAOD-45. haysjm

## 15-09-14
* CxAODMaker: Clean up code to turn of Xbb tag, jennis
* CxAODMaker: Add switch to turn off accessing TruthEvents, jennis
* FrameworkExe: pulled in GRL checker script from Tom CXAOD-48, haysjm
* FrameworkSub: bootstrap updated ready to make FrameworkSub tag CXAOD-55, haysjm

## 15-09-15
* CxAODMaker, CxAODMaker\_VHbb: pass derivation name from AnalysisBase to EventInfoHandler; access HLT\_Jet/Photon information only in case of HIGG5D1 and HIGG5D3 derivations;CXAOD-84, hanar
* FrameworkSub: removing pkg already in release, fsforza
* CxAODMaker, FrameworkSub: Bump to 2.3.26: electron efficiency SF (looseLH, mediumLH, tightLH) updated to v02. CXAOD-94. nmorange
* CxAODMaker: Hack 50ns GRL to include 50ns Run from Period D. Add Period D GRL. Add full 50ns ilumicalc file. CXAOD-64. nmorange
* FrameworkSub: Update data lists to full 50ns dataset with latest derivations available. CXAOD-65. nmorange
* CxAODReader\_VHbb: moved jet rescaling to function. hanar
* FrameworkExe: Use the updated ilumicalc files. CXAOD-64. nmorange
* CxAODReader\_VHbb: apply lepton sfs. hanar
* CxAODReader\_VHbb: replace MET cut, by HT/sqrt(MET) - need to follow up: how is the top CR defined then?. hanar

## 15-09-16
* CxAODMaker: Remove muon trigger SF bits, that are now done at Reader level. fsforza

## 15-09-17
* CxAODMaker: remove unused header. fsforza
* CxAODMaker: fix missing header file in Objecthandler.icc - possibly caused by upgrade to 2.3.26?. haysjm
* FrameworkSub: update tags to pull in filx to missing header in CxAODMaker. haysjm
* FrameworkSub: updated input files for MC - 50ns p2375 - includes Powheg and MadGraph V+jets samples p2411 CXAOD-65. haysjm
* FrameworkExe: bump the vtag. haysjm
* FrameworkSub: updated packages to final list for tag14. haysjm

## 15-09-18
* CxAODTools, FrameworkExe: added option (for the reader) to run with PU data SF variation. Default is 1.16. Option is commented in config file. fsforza
* FrameworkSub: add slides for histSvc. dbuesche
* FrameworkSub: remove duplicated sample lists. dbuesche
* CxAODMaker: retrieving metaData info for each file change and for each change input. This is safe for proof. fsforza
* FrameworkExe: fixing proof on the maker. fsforza

## 15-09-19
* FrameworkExe: update sample list names. dbuesche

## 15-09-20
* CxAODMaker: remove 1 compilation warning. fsforza
* CxAODTools: add LHValue property. fsforza
* CxAODMaker, CxAODTools: adding prescaled ele triggers for MJ study in Wenu. No additional space used in default CxAOD as triggers not in default triggerlist. fsforza

## 15-09-21
* CxAODMaker: Testing electron trigger SF; Adding 25/50 ns configs; Fixing systematic loop for electrons. fsforza
* CxAODTools: ele trigger SF at electron level. fsforza
* FrameworkExe: bugfix in sample list in copy script. dbuesche
* FrameworkExe: add switch for verbose mode. dbuesche
* FrameworkExe: add W/Z Madgraph and Powheg samples in copy script. dbuesche




