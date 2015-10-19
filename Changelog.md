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

## 15-09-12

## 15-09-13

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
* Tag FrameworkSub 00-14-00. haysjm

## 15-09-18
* CxAODTools, FrameworkExe: added option (for the reader) to run with PU data SF variation. Default is 1.16. Option is commented in config file. fsforza
* FrameworkSub: add slides for histSvc. dbuesche
* FrameworkSub: remove duplicated sample lists. dbuesche
* CxAODMaker: retrieving metaData info for each file change and for each change input. This is safe for proof. fsforza
* FrameworkExe: fixing proof on the maker. fsforza

## 15-09-19
* FrameworkExe: update sample list names. dbuesche
* Tag FrameworkSub 00-14-01. haysjm

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
* CxAODMaker, FrameworkExe: switch for including (or not) taus in the MET calculation. agbet

## 15-09-22
* FrameworkSub: yields for 14-00 production, dbuesche
* FrameworkSub: new yields for Wlnu production in 2.3.26 and with all ele sys. Adding also one yield file for separate MJ production, needed for EWK subtraction. fsforza
* FrameworkExe: explicitily adding 50ns flag (off by default), fsforza
* FrameworkSub-00-14-01: update muon CP tools to 25ns recommendation, dbuesche
* FrameworkSub: add packages to met muon CP recommendation for 25ns, dbuesche
* FrameworkSub: change yields for those samples which excced AMI total number of events, thompson
* CxAODMaker: Update truth matching for tau hanlder so works for other generators, esp. sherpa. gwilliam

## 15-09-23
* FrameworkSub: add slides for CxAOD structure/reader. dbuesche
* CxAODTools, CxAODReader, CxAODReader\_VHbb: update trigger tool with lepton pTs and muon SF+sys. djamin
* CxAODMaker-00-01-13-branch: modified ObjectBaseHandler to add is50ns config switch and corresponding member variable m\_is50ns. Set to false by default. Then added code to use this in the ElectronHandler to use the correct Reco SF files and LHSelector config files for 25ns or 50ns running. haysjm

## 15-09-24
* Prepare for Tag FrameworkSub 14-01
* Tag 15-00, intermediate snapshot
* CxAODReader\_VHbb: b-tagging SF and fatjet safety checks. jhetherl
* FrameworkSub: Added 25ns MC and data lists. rroehrig
* CxAODMaker: updates according to CP group. agbet

## 15-09-25
* FrameworkSub: Update of 25ns MC lists. rroehrig

## 15-09-26
* CxAODReader\_VHbb: adding MVA tree for VBFHbb analyses, prose
* FrameworkSub: Some new samples available, nmorange
* CxAODMaker-00-01-13-branch: fixed typo in scale factor file name for 25ns running, haysjm
* FrameworkSub-00-14-01-branch: updated yield files from 14-00/14-01 production for 0lep 1lep and 2lep, haysjm
* FrameworkExe: Added GetXSection.py script to scripts directory to allow for the easy query of AMI with pyAMI API for the fixing/checking of the XSections file, meehan
* FrameworkSub: Updated xsections file to correct errors in formatting that would break the manner in which histograms are named in HistNameSvc and also added new diboson, single top, and monoW/Z file cross sections, meehan

## 15-09-27
* FrameworkSub: fix min-\>minus in W powheg samples, fsforza
* FrameworkSub: Remove duplications. Add DSIDs from Rev=3D691776. HVT DSIDs (301388 to 301396) are replaced by the Rev=3D691776. garabed
* FrameworkSub: Fix Xsec of DSID 361008 and filtereff of DSID 361503 (replace by Rev=3D693679). garabed

## 15-09-28
* FrameworkSub: Update of 25ns MC and Data lists, rroehrig
* FrameworkSub: Update of the Yields 0lep and 2lep selections for CxAOD production v14.1, arturos
* FrameworkSub: adding DM monoWZ signal mc samples to 50ns mc15\_13TeV list, arturos
* FrameworkSub: taking out samples 25ns into this file, sorry, arturos
* CxAODTools, CxAODMaker: add new VBF+photon triggers, lshi
* FrameworkSub: correct XS for Pythia8\_AU2CTEQ6L1\_ZH125\_nunubb, dsid 341101, cpandini
* CxAODMaker: write jet shape variables for Nominal only, dbuesche

## 15-09-29
* FrameworkSub: update SM VH cross-sections: include LHCHXS WG reference, fix sample names for gg-\>ZH samples (previously listed as qqZH), fix sample names for LO MC samples (previously reporting HNLO in the sample name), cpandini
* CxAODMaker, CxAODTools: added hlt jet triggers to CommonProperties.h, grkeren
* FrameworkSub: update to include yields of Zmumu\_Pw samples, arturos
* CxAODTools: added in dimuon matching props, amontalb

## 15-09-30
* FrameworkExe: adding missing ele SF sys, fsforza
* FrameworkSub: adding WJets Madgraph, miochoa

## 15-10-01
* FrameworkSub: fix ggA, ttbar and single top (yields files), thompson
* CxAODTools: fix TriggerTool to not have warnings for event with PU weight rdmRunNumber 0 when we want to set the MC RunNumber in muon trigger SF, djamin
* CxAODMaker: comment out unused m\_tauEfficiencyCorrections\_eveto, dbuesche
* CxAODTools: run OR tool even if applyOR=false to write hasSharedTrack flag, dbuesche
* CxAODTools, CxAODMaker: added trigger decoration for HLT\_j45\_bperf, grkeren

## 15-10-02
* CxAODMaker: remove ConeTruthLabelID from CxAOD for all jets, dbuesche
* CxAODReader: CXAOD-32: use HadronConeExclTruthLabelID instead of ConeTruthLabelID, dbuesche
* CxAODReader\_VHbb: CXAOD-32: consistently use TruthLabelID (which is a copy of HadronConeExclTruthLabelID), dbuesche
* CxAODMaker: CXAOD-101: set useAFII property (hard coded to false), fix compiler warnings, dbuesche
* CxAODMaker: CXAOD-100: set useAFII property (hard coded to false), dbuesche
* KinematicFit: Remove dependencies on obsolete run1 packages. Switch to mode where no corrections are applied to the jets before kin fit  is run, amehta
* CxAODMaker, CxAODMaker-00-01-13-branch, FrameworkExe-00-01-15-branch: Add GRL and ilumicalc files for 25ns running, nmorange
* CxAODTools: CXAOD-113: fix crash when running w/o taus, dbuesche
* FrameworkExe-00-01-15-branch: Update JES NP to 25ns, nmorange
* CxAODReader: CXAOD-78: add switch in HistSvc for histogram filling, dbuesche
* FrameworkExe: CXAOD-78: add writeHistograms=true, dbuesche
* CxAODMaker, CxAODTools: added number of constituents for track jets, benitezj
* FrameworkSub: Update of the 25ns list, rroehrig
* FrameworkSub-00-14-01-branch: Use latest and greatest Yields and XSection files, nmorange
* FrameworkSub-00-14-01-branch: Add of the 25ns lists, Data lists according to the latest GRL, MC must be updated, rroehrig
* CxAODTools: TriggerTool : access electron trigger SF and syst from Maker, djamin
* Weekly snapshot 15-01, haysjm

## 15-10-03
* CxAODReader\_VHbb: Baseline skeleton for Run2 HZvv, rriuppa

## 15-10-04

## 15-10-05
* FrameworkSub: Small update of MC list, rroehrig
* CxAODReader: PU tool needs to be initialized in any case, because trigger selection relies on it, hanar
* CxAODReader\_VHbb: removed unnecessary lines; added check on pointer validity, hanar

## 15-10-06
* CxAODTools: disabled execution of OR tool when 'applyOverlapRemoval' is set to false, grkeren
* CxAODTools, CxAODReader, CxAODReader\_VHbb: optional b-tagging weight syst, jhetherl
* FrameworkSub: Moving trunk to 2.3.30 configuration: version + extra-packages
* FrameworkExe-00-01-15-branch: Update Reader configuration for tag 14-02, nmorange
* FrameworkSub: Update of MC list: p2419, rroehrig
* CxAODTools, CxAODMaker: added more HLT mu-jet triggers, grkeren
* CxAODTools: make messaging level steerable from config, hanar
* FrameworkSub: Update of MC list, removed running samples, rroehrig
* FrameworkSub-00-14-01-branch: Final MC list, rroehrig
* Tag 14-02, 25ns production

## 15-10-07
* CxAODTools: initializing msglevel, hanar
* CxAODMaker-00-01-13-branch: Correct implementation of CutBookKeepers retrieval after the fix in derivations, nmorange
* Tag 14-03, with fixed CBC
* CxAODMaker-00-01-13-branch: Fix stupid bug. CXAOD-109, nmorange
* Tag 14-03, with bugfix for CBC
* CxAODMaker: Correct implementation of CutBookKeepers retrieval after the fix in derivations, ported from 14-01 branch. CXAOD-109, nmorange
* CxAODMaker: CXAOD-101: set property Preselection to 16 for ElectronPhotonShowerShapeFudgeTool, dbuesche

## 15-10-08
* FrameworkSub: yield files for v00-01-35 production. New MJ production with IBL cut and all triggers. NB: partially  buggy muons SF, fsforza
* CxAODMaker: fix of electron LH 25ns selection. Adding muon 50ns config loading if flag is set, fsforza
* FrameworkSub: fix name of pohweg samples, fsforza
* CxAODReader: check if m\_maxEvents is set, use m\_sampleAvailableEntries to scale weights when running on smaller stat MC, fsforza
* FrameworkExe: saving metaData info about NAvailableEntries, fsforza
* CxAODTools: CXAOD-54 Replace slow auxdecor with faster static AuxElement::Accessor, nmorange
* FrameworkExe: Update framework-run based on latest 25ns production branch, nmorange
* CxAODMaker: Tentative merging of LumiMetaData. Validation jobs running, fingers crossed. CXAOD-3, nmorange
* FrameworkExe: update default MC/data file to p2419/p2425 25ns, dbuesche
* FrameworkExe, CxAODMaker: CXAOD-53: remove 8 TeV switched, dbuesche
* CxAODMaker: Grab track jet links from parent fat jet, lkaplan
* FrameworkSub, FrameworkExe, CxAODMaker: Remove 8TeV lists, nmorange
* CxAODReader: moving histName sample initialization at ChangeInput stage. Same result but a bit faster, fsforza

## 15-10-09
* CxAODTools: modified requirement for applying OR tool from checking 'applyOverlapRemoval' to checking the validity of the pointers to electrons, muons and jets, to allow execution of tool in the mode where 'applyOverlapRemoval' is false but 'writeSharedTrack' is true, grkeren
* FrameworkSub: numbers consistent with mu-sf fixed production, fsforza
* CxAODMaker: add getter for EventInfo variations, dbuesche
* CxAODMaker: bug fix: retrieve variations also from event info for in event selector, dbuesche
* CxAODTools: CXAOD-119: add OverlapRemovalToolLargeR, dbuesche
* CxAODMaker, CxAODMaker\_VHbb, CxAODTools\_VHbb, CxAODReader, CxAODReader\_VHbb: CXAOD-50 add override keyword whenever possible, nmorange

## 15-10-10
* CxAODMaker\_VHbb: Replace deprecated getString by castString in  SampleHandler calls. Removes compilation warning, nmorange
* CxAODReader: PLEASE STOP PASSING/RETURNING STRINGS BY VALUE, nmorange

## 15-10-11
* CxAODMaker: CXAOD-118 First pass at improving maker performance. Low hanging fruits. 240s->140s for 1000 ttbar events. More details in JIRA, nmorange
* CxAODMaker: CXAOD-118 Second pass at improving maker performance. 140s->125s for 1000 ttbar events.  More details in JIRA, nmorange
* CxAODMaker: CXAOD-118 Third pass at improving maker performance. 125s->110s for 1000 ttbar events.  More details in JIRA, nmorange
* CxAODMaker: CXAOD-118 Fourth pass at improving maker performance. 110s->103s for 1000 ttbar events.  More details in JIRA, nmorange
* CxAODMaker: CXAOD-118 Calibrate only muons that pass MCP selections, nmorange

## 15-10-12
* CxAODMaker, CxAODTools: add run1-like electron trigger for 50ns+matching / access muon trig SF+syst stored CxAOD / no di-lep triggers and update lepton thresholds, djamin
* CxAODMaker: Write matchHLT variables only in Nominal. They are not calibration-dependent, nmorange
* CxAODMaker\_VHbb: Do not write lepton quality variables in weight systematics, nmorange

## 15-10-13
* CxAODMaker : update decorrelationModel to 1NP_v1 for EgammaCalibrationAndSmearingTool, lshi
* CxAODReader : Revert r699498 that introduced a bug for sample naming, nmorange
* CxAODTools : CXAOD-35 Better workaround in BTaggingTool. Speedup x2 on execute() in benchamrk 100000 ttbar events 0 lepton selection, nmorange
* FrameworkExe : add PH_EFF_Uncertainty for photon efficiency systematic, lshi

## 15-10-14
* CxAODMaker : Changed in default jesConfig 50ns to 25ns, abuzatu
* CxAODReader_VHbb : vvqq-specific features added, losterzo
* CxAODReader_VHbb : vvqq-specific features added, losterzo
* FrameworkSub : JetCalibTools-00-04-55 is recommended, but AnalysisBase 2.3.31 has JetCalibTools-00-04-52, abuzatu

## 15-10-15
* CxAODMaker : fixed random seed for MET systematics, tnobe

## 15-10-16
* CxAODMaker : Access and initialize MuonEfficiencyCorrections package + update arguments of writeEventVariables to compute muon trig SF/systs at Maker, djamin
* CxAODMaker : add new isolation working points for electron, lulu
* CxAODTools : Added back in the required macro to make the OverlapRegister properly persistent. Added TMVA as a preload package which should fix the strange problem of the thread local storad hang in the JetRegression code. CXAOD-52 CXAOD-122, haysjm
* CxAODTools : add new isolation working points for electron, lulu
* CxAODTools : update arguments of writeEventVariables to compute muon trig SF/systs at Maker + update TriggerTool : protect events with RdmRunNumber==0 and proper el trig SF computation in 2lep events, djamin
* CxAODTools_VHbb : update arguments of writeEventVariables to compute muon trig SF/systs at Maker + store muon trig SF/systs + add dependancy, djamin
* FrameworkExe : Add muon trig SF variations in Maker config, djamin
* FrameworkSub : use latest tag of MuonEfficiencyCorrections-03-01-17 to be able to handle events later than period D, for the moment these events have a SF of 1, not measured yet in official recommendations, djamin

## 15-10-17
* CxAODMaker : adjust outdated comment, dbuesche
* CxAODMaker : fix compiler warnings, dbuesche
* CxAODMaker : remove setting of CalibrationRelease property of MuonEfficiencyScaleFactors -> latest is used by default, dbuesche
* CxAODMaker : Set TriggerTool property of TrigMuonMatching as recommended. Has no effect(?), dbuesche
* CxAODTools : retrieve is50ns flag from config in TriggerTool, dbuesche

## 15-10-18

## 15-10-19
* CxAODReader : CXAOD-46: skip lumi weight computation if applyLumiWeight=false in config, dbuesche
