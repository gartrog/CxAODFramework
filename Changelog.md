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
* CxAODTester: add this new package, dbuesche
* CxAODMaker, CxAODTools: add a tau trigger in the EventInfoHandler, added bbtautau trigger list and a GRL file, agbet
* CxAODTools: fix compiler warnings by making sort\_pt a member of EventSelection, dbuesche
* CxAODMaker, CxAODTools: Add passTaggingReq for trackjets, garabed
* CxAODReader, FrameworkExe: CXAOD-120: add the possibility to create shallow copies of input containers, dbuesche

## 15-10-20
* CxAODReader\_VHbb: fix compiler warnings, dbuesche
* CxAODTools\_VHbb: remove deprecated comments, dbuesche
* FrameworkExe: add comment regarding shallow copies, dbuesche
* CxAODMaker: Add function to EventSelector to get selection back (needed e.g. for MMC), gwilliam
* CxAODMaker\_VHbb: fix compiler warning, dbuesche
* CxAODMaker, CxAODTools: remove photon EffSFError variables, lshi
* CxAODMaker, CxAODTools, CxAODReader, CxAODReader\_VHbb, FrameworkExe: CXAOD-119: add switch applyOverlapRemovalLargeR, dbuesche
* CxAODMaker-00-01-13-branch: Add new 25ns GRL with 1.4fb-1 of data, nmorange
* FrameworkExe-00-01-15-branch: Update framework-run.cfg to use latest 1.4fb-1 25ns GRL, nmorange
* FrameworkSub-00-14-01-branch: Add data lists for 2nd extention of 14-04 production: up to 1.4fb-1

## 15-10-21
* CxAODTools: Adapt to new interface of PU reweighting tool, nmorange
* FrameworkSub: Bump AnalysisBase release to 2.3.32, nmorange
* Tag 14-06 new tag with updated GRL for 1.4fb-1, haysjm
* FrameworkSub: Added additional cross sections, primarily for monoW, monoZ, and monoH samples as outlined in @CXAOD-133 issue, meehan
* CxAODTools, CxAODTools\_VHbb: re-adding simpler writeEventVariables initialization. Declared also as not-only virtual so different analyses can avoid the implementation, fsforza
* CxAODMaker, CxAODTools: Tau trigger matching variables, gwilliam
* Tag 15-02, intermediate tag, with 2.3.31, haysjm
* CxAODMaker, CxAODMaker\_VHbb: bugfix: proper initialization of TruthParticleHandler, dbuesche
* CxAODMaker: Adding protection against thinned electron variables needed by full hadronic bbtautau, carquin
* CxAODTools: Adding ditau trigger decorator, carquin

## 15-10-22
* CxAODTools: FIX: adding tool check; make PileupWeight a float hanar
* FrameworkSub: removed packages that are equal or outdated with respect to what is in the new release, hanar
* CxAODMaker: ilumicalc for 1.41fb-1, thompson
* CxAODTools: overwriting averageInteractionsPerCrossing only for data (if PU tool is used), hanar
* CxAODTools: changes for dijet\_JZxW normalization merged to the trunk, changqia
* CxAODTools: add PileupweightRecalc,averageInteractionsPerCrossingRecalc, compute if recomputePUWeight=true, dbuesche
* CxAODReader: use PileupweightRecalc if recomputePUWeight=true, dbuesche
* CxAODMaker: added latest grl (v69), grkeren

## 15-10-23
* FrameworkSub: Needed to add additional cross sections pertaining to @CxAOD-139, meehan

## 15-10-24
* CxAODMaker: adding isolation correction tool for photons, prose

## 15-10-25
* FrameworkSub: Add ttbar cross secions from twiki. WARNING: kfactor seem missing, contacted twiki resposible., dbuesche
* CxAODReader: CXAOD-135: apply cut on m(ttbar) for inclusive Powheg ttbar sample if apply PowhegTruthMttCut = true, default is false, dbuesche
* CxAODReader: CXAOD-135: more useful range for MttTruth histogram, dbuesche
* CxAODTools, CxAODReader: set Props::averageInteractionsPerCrossingRecalc also for MC (equal to Props::averageInteractionsPerCrossing); add comments and error message, hanar
* CxAODReader: FIX: did not actually retrieve corrected mu in data, since setEventWeight() (and applyPUWeight()) was only called for MC, hanar
* CxAODReader: CXAOD-135: possiblity to mix powheg ttbar inclusive sample with slices, set in config e.g. float usePowhegInclFraction = 0.25, dbuesche
* CxAODMaker: add IsolationCorrectionTool, lulu
* CxAODTools: fix mismatch of type for PileupWeight, lulu

## 15-10-26
* CxAODTools: BTaggingTool: set OldConeFlavourLabel to false -> use HadronConeExclTruthLabelID, dbuesche
* CxAODTools: add float sumOfWeightsProvider::getNEntries(int mc\_channel\_number), dbuesche
* CxAODReader: proper init of m\_maxEvents, use m\_sumOfWeightsProvider-\>getNEntries for scaling in case of m\_maxEvents>0 (old method gave bugged answers), dbuesche
* CxAODReader: add float AnalysisReader::computeBTagSFWeight(std::vector\<const xAOD::Jet*\> &signalJets), dbuesche
* CxAODTools: BTaggingTool: add Kenjis fix for tau track jet SFs (using non-default), dbuesche
* CorrsAndSysts: Run1 CorrsAndSysts package: minor changes introduced to interface it with the CxAODReader, cpandini
* CxAODMaker, CxAODTools: add HLT\_xe70 item, djamin

## 15-10-27
* CxAODTools: fix mismatch of type for PileupWeight, lulu
* CxAODReader: add getter methods, hanar
* CxAODMaker: fix for missing links, relevant to a new feature in the TauAnalysisTools, agbet
* FrameworkSub: Fix Wlnu yield files to account change in partial events running: Now only entries on ntuples are used.  NB: scaling is otherwise incorrect!, fsforza

## 15-10-28
* FrameworkSub: Updated JetSubStructureUtils-00-02-14 to JetSubStructureUtils-00-02-16, created last night, abuzatu
* CxAODReader\_VHbb: Added VH histos for 2lep, jabdalla
* CxAODTools: updated BTaggingTool, jhetherl
* FrameworkSub: added newest xAODBTaggingEfficiency, jhetherl
* FrameworkExe: added b-tagging syst options, jhetherl

## 15-10-29
* FrameworkSub: added CDI framework until next AnalysisBase, jhetherl
* CxAODReader: skip b-tag SF calculation for data, dbuesche
* CxAODTools, CxAODReader, CxAODReader\_VHbb: updated BTaggingTool systematic treatment, jhetherl
* CxAODTools: minor fix to MC/MC SF and removed spaces in b-tagging systematics names, jhetherl
* CxAODMaker, FrameworkExe: Adding PtReco, TruthWZ, reduce some mu/el info per Jet and FatJet, abuzatu
* CxAODTools: fix 0 random run numbers to get proper muon trigger SF + remove useless protections in TriggerTool, djamin
* CxAODTools: quick fix for b-tagging syst. names, jhetherl
* CxAODReader: add some debug output, dbuesche

## 15-10-30
* CxAODMaker: added ghost associated heavy flavour hadrons to fat/track jets (JIRA: CXAOD-140), grkeren
* CxAODReader: add some debug output, dbuesche
* CxAODTools: BTaggingTool: reduce printout in init, dbuesche
* CxAODTools: fix the random run number when it is greater than period D to avoid the numerous prints, djamin
* CxAODTools: CXAOD-147: splitting the removeOverlap method into setORInputLabels, getOROutputLabels and the actual removeOverlap, dbuesche
* CxAODTools: on-demand loading of b-tagging tools, jhetherl
* CxAODTools: small bug fix for BTaggingTool (msgLevel), jhetherl
* CxAODMaker: bugfix: muon-in-jet correction was crashing w/o electron-in-jet corr, dbuesche
* CxAODMaker: bugfix: use correct container name in JERTool init, dbuesche
* CxAODTools, CxAODReader: almost implemented b-tagging MC-to-MC corrections, jhetherl

## 15-10-31
* CxAODMaker: fixes for init/usage of JetSemileptonic, dbuesche
* CxAODMaker: CXAOD-137: implement jet energy unc tools in FatJetHandler, use AntiKt4 config for testing. Systematics are disabled, needs fix of CXAOD-134 first., dbuesche
* CxAODTools, CxAODReader, FrameworkExe: fixing lumi weight when running on a subset of events, dimicco
* CxAODMaker: CXAOD-134: fix selection for element links in FatJetHandler, CXAOD-137: enable jet systs for fat jets, dbuesche
* CxAODTools: fixing reading and position bug in sumOfWeightsProvider, dimicco
* CxAODReader: set sample and mc\_channel only once for each input file (plus at the start), fsforza
* CxAODReader: added methods in AnalysisReader so retrieve ghost associated heavy flavour labels (pt sorted), grkeren

## 15-11-01
* CxAODReader: use initializeChannel in the right place (but fix), fsforza
* CxAODTools: harmonize some printout, dbuesche
* FrameworkSub: update Wlnu MJ yield file to production 00-38 (with not-iso triggers) and with correct scaling if maxEvent, fsforza
* CxAODTools: BTaggingTool: fix init of CDI for tau SFs, dbuesche
* CxAODMaker: bugfix: use ROOTCOREBIN path in JetSemileptonic init, dbuesche
* CxAODTools: BTaggingTool: add flag for out of range warnings, dbuesche

## 15-11-02
* CxAODMaker: Made FatJetHandler::matchTruthJets virtual to allow overloading, jennis
* CxAODReader: make HistNameSvs::set\_sample() virtual, dbuesche
* FrameworkSub: update to CT14 predicitions cross sections for Wlnu and Zll samples for W,Z SM analysis, chiarad
* CorrsAndSysts: Fix compiler issues, amehta
* CxAODMaker: changed output container names for MET systematic variations, tnobe
* CxAODMaker\_VHbb: fix the jvt, cwang

## 15-11-03
* CxAODMaker: remove check on CoreFlags; CXAOD-150, hanar
* CxAODReader: Adding condor support and more configurability for Reader, sargyrop
* FrameworkExe: Add isMJ in data/framework-run.cfg, garabed
* CxAODMaker\_VHbb: Invert isolation if MJ, garabed
* CxAODMaker\_VHbb: passWHSignalElectronIso(electron) --> ElectronHandler\_VHbb::passWHSignalElectronIso(electron) and passWHSignalMuonIso(muon) --> MuonHandler\_VHbb::passWHSignalMuonIso(muon)
* CxAODTools\_VHbb: adding a new class for vvqq, cwang
* CxAODMaker: CXAOD-137: hack ObjectHandler.icc to rename fatJet systs, dbuesche
* CxAODTools: Removing PDF info properties, miochoa
* CxAODMaker: reimplementing PDF info on TruthEventHandler and removing it from EventInfoHandler, miochoa
* CxAODMaker: fixed problem with trying to access truth hadron flavour labels for data, grkeren
* CxAODMaker\_VHbb: registering handler for truthEvents, miochoa

## 15-11-04
* CxAODTools, CxAODReader: first draft of b-tagging MC-to-MC integration, jhetherl
* CxAODMaker: Changes for the regression in CxAODMaker: training/application separately for even and odd events and pt splitted (100 GeV), bug fix for the selection of tracks for regression, eschopf
* CxAODTools: Changes for regression in CxAODTools: extended the TMVA training and application tool to write/applicate separately for even and odd events, eschopf
* CxAODReader, CxAODReader\_VHbb: adding lepton charge to tree, hanar
* FrameworkExe: Changed config values for regression in framework-run.cfg: even and odd as well as pt splitted application is default; changed the used weightfiles and methods accordingly, eschopf
* CxAODReader: fixing the normalization problem, francav
* CxAODMaker: fixed crash caused by not initialised Props::passTauSelector and Props::forMETRebuild, agbet
* CxAODTools: made EventSelection::sort\_pt() public (was protected), grkeren
* CxAODReader: added method for retrieving label of leading ghost ass. heavy flav. hadron in AnalysisReader, added method to set 'm\_useEventFlav' in HistNameSvc, grkeren
* CxAODMaker: use IncompleteLumiBlocks if LumiBlocks not available, agbet
* CxAODTools, CxAODReader, CxAODReader\_VHbb, FrameworkExe, FrameworkSub: include interface to CorrsAndSysts, cpandini
* FrameworkExe: Add TruthEvents if PDF info exists in samples, nmorange
* FrameworkExe: Bump already verion in framework-run to 16, nmorange
* FrameworkExe: enable CxAOD merging, dbuesche
* CxAODMaker: Remove outdated GRL/ilumicalc, nmorange
* FrameworkSub: Add GRL and ilumicalc in FrameworkSub, nmorange
* FrameworkExe: removing un-used functions, fsforza
* FrameworkSub: Add prw file in FrameworkSub, nmorange
* FrameworkExe: Point all PU-related paths to new location in FrameworkSub, nmorange
* CxAODMaker: Remove PU-related files from CxAODMaker. Now use FrameworkSub, nmorange

## 15-11-05
* Tag 16-00
* FrameworkSub: update MC list\_sample\_grid.mc15\_13TeV\_25ns.HIGGXXX.txt to include ttbar syst , singletop syst and more llqq vvqq signal samples, smwang
* CxAODMaker: change where the forMETRebuild is set, so that it includes taus that have passed selection even when a dedicated handler is used., agbet
* FrameworkSub: remove rucio tag, update some Sherpa V+jet from p2411 tp p2419, fill previously missing V+jet samples, include more HVT samples for 0-lep, smwang
* FrameworkSub, FrameworkExe: Add new GRL/ilumicalc, nmorange
* FrameworkSub: Update data lists to latest GRL, nmorange
* CxAODMaker, CxAODMaker\_VHbb: Fixing bug when TruthWZ is not present for data, abuzatu
* CxAODReader\_VHbb: fix: protection for data in fill\_jetSelectedHistos, cpandini

## 15-11-06
* CxAODMaker: updating muon, electron, photon isolation variables, amontalb
* CxAODTools: tuple utilities, jhetherl
* CorrsAndSysts: Add in an Njet reweight option, ahmeta
* CxAODTools\_VHbb: updated jet cleaning; is it really necessary to redo it passSelection?; CXAOD-153, hanar

## 15-11-07
* FrameworkExe: turned on OverlapRegister in output, grkeren
* CxAODReader: updating the AnalysisReader to update the name of the sample and the mChannelNumber at each event, francav
* Tag 16-01

## 15-11-08
* CxAODTools: quick patch for BTaggingTool, jhetherl

## 15-11-09
* CxAODReader: add second getter method for eventFlavour, hanar
* CxAODTools, CxAODTools\_VHbb: introduce passJetCleaning method; CXAOD-153, hanar
* FrameworkSub: Remove duplications in list\_sample\_grid.mc15\_13TeV\_25ns.HIGG5D2.txt, garabed
* CorrsAndSysts: Don't exit if sample is unknown as now we have many unknow signal samples, ahmeta

## 15-11-10

* CxAODReader\_VHbb : add BDT weight file for vbfa analysis, lshi
* CxAODReader\_VHbb : add readMVA to vbfa analysis, merge with trunk, lshi
* CxAODReader\_VHbb : fixed long type for EasyTree, jhetherl
* CxAODReader\_VHbb : new EasyTree and Reader restructuring, jhetherl
* CxAODReader\_VHbb : svn update issues, jhetherl
* CxAODTools : added fast string comparison class for better map performance, jhetherl
* CxAODTools : fix a crash in initializing overlapRemovalToolVBFGamma when running on debug mode, lshi
* CxAODTools : store all possibles muon trigger SFs at Maker, djamin
* CxAODTools\_VHbb : store all possibles muon trigger SFs at Maker, djamin
* FrameworkExe : output job dataset name fixes : prune \_CT10 and store the first s-tag for MC, djamin
* FrameworkSub : add cross-section and yield for 341078 ZbbjjaQCD sample, lshi

## 15-11-11

* CxAODMaker : update on muon trigger SF : use loose lepton quality, djamin
* CxAODTools : update on lepton trigger SF : use loose lepton quality, djamin
* CxAODTools\_VHbb : adding track and fat jets to the selection result; CXAOD-156, hanar
* FrameworkSub : updated yields file, amontalb

## 15-11-12
* CxAODMaker : adding data15 lowest unprescaled trigger conditions, dimicco
* CxAODMaker : add some el/mu triggers and matching, djamin
* CxAODMaker : Fixing a bug when TruthWZ is not found in some events, abuzatu
* CxAODReader : adding  data15 lowest unprescaled trigger, dimicco
* CxAODReader : removing leftover debug line in setEventWeight, dimicco
* CxAODTools : adding data15 lowest unprescaled trigger conditions, dimicco
* CxAODTools : add some el/mu triggers and matching, djamin
* FrameworkExe : adding TriggerMenu flag in framework-read.cfg, dimicco
* FrameworkSub : update xsec and yield for ZGamma 341078, lshi
* FrameworkSub : update yields to fix position problem, lshi

## 15-11-13
* CxAODReader\_VHbb : update vbfa BDT weights, lshi
* FrameworkExe : Use latest GRL/ilumicalc, nmorange
* FrameworkSub : New final GRL, ilumicalc, and updated data lists. WARNING: one run still missing in derivtions ?, nmorange

## 15-11-14
* CxAODMaker : add again the histos*root, abuzatu
* CxAODMaker : Add PtReco from b Parton, besides TruthWZ; code reorganised, abuzatu
* CxAODMaker : delete temporarily the histos*root, abuzatu
* CxAODMaker : Fix a crash when applyJetSemileptonic=False; not save Regression state any more for FatJet; added PtReco when both muon and electron present, abuzatu
* CxAODMaker : Fix a crash when applyJetSemileptonic=False; not save Regression state any more for FatJet; added PtReco when both muon and electron present, abuzatu
* CxAODMaker : Fix a crash when applyJetSemileptonic=False; not save Regression state any more for FatJet; added PtReco when both muon and electron present, abuzatu
* CxAODMaker\_VHbb : Fix a crash when applyJetSemileptonic=False; not save Regression state any more for FatJet; added PtReco when both muon and electron present, abuzatu
* FrameworkExe : Add PtReco from b Parton, besides TruthWZ; code reorganised, abuzatu
* FrameworkExe : Revert to previous format; changed by mistake, abuzatu

## 15-11-15
* CxAODMaker : Replace PtReco histograms from vvbb of 16k events to llbb of 66k events, abuzatu

## 15-11-16
* CxAODMaker : update event cleaning cuts, tnobe
* CxAODReader : write cutflow from event selection in AnalysisReader::finalize(), dbuesche
* CxAODTools\_VHbb : Add more bins in PreselectionCutFlow histogram, sargyrop

## 15-11-17
* CxAODMaker : changed one of the tau triggers in the matching, agbet
* CxAODTools : changed one of the tau triggers in the matching, agbet
* FrameworkSub : update ttbar systs, amontalb

## 15-11-18
* CxAODMaker : update iso effSF; update iso working points, lulu
* CxAODMaker : updates to photon isolation WPs, prose
* CxAODMaker\_VHbb : update to vbf loose photon selection, prose
* CxAODReader\_VHbb : adding struct lepton; adding method setLeptonVariables; using both in fill\_2Lep, hanar
* CxAODReader\_VHbb : move HT computation to method, hanar
* CxAODTools : extra property isFixedCutTightCaloOnlyIso for new photon isolation WP, prose
* CxAODTools : update iso effSF; update iso working points, lulu
* FrameworkExe : final fix for s-tag in output dataset job name, djamin
* FrameworkSub : Added JetSubStructureUtils-00-02-17 and BoostedJetTaggers-00-00-12 to update FatJet CP, abuzatu
* FrameworkSub : fix broken yield for Wenu, fsforza
* FrameworkSub : Update of V+jets cross sections to 25ns values as explained in @CxAOD-160, thompson
* FrameworkSub : update release-trunk to 2.3.34, haysjm
* FrameworkSub : Xsections: add more mass points for A->ZH->llbb, dbuesche

## 15-11-19
* CxAODMaker : comment out isoCorr for the moment to avoid crash; debugging ..., lulu
* CxAODMaker : uncomment isolation correction, lulu
* CxAODReader : call copyConeTruthLabels also for track and fat jets;CXAOD-155;CXAOD-32, hanar
* CxAODReader\_VHbb : adding Jet struct, method to get corrected jets (default OneMuon), method to set jet variables; used in 2 lep analysis, hanar
* CxAODReader\_VHbb : move region definition in 2lep upstream; remove mBB cut in topemuCR; add missing if, hanar
* CxAODReader\_VHbb : removed deprecated MET cut, hanar
* CxAODReader\_VHbb : removed duplicated checks of truth label id; CXAOD-155, hanar
* CxAODReader\_VHbb : removed mBB cut in emu top CR, hanar
* CxAODReader\_VHbb : updated mLL cut in SR, rm cut in topCR; moved to method, hanar
* CxAODReader\_VHbb : wrapped up 2lep trigger selection, hanar
* CxAODTools : big changes in TriggerTool to make it working with tag14, tag16 and next CxAOD tag samples, djamin
* FrameworkExe : update the TriggerMenu strings in reader config, djamin
* FrameworkSub : I learn from Jose that JetSubStructureUtils-00-02-17 has a bug, so revert to JetSubStructureUtils-00-02-16, abuzatu
* FrameworkSub : Updated after a bug fix to JetSubStructureUtils-00-02-18, abuzatu

## 15-11-20
* CxAODMaker : Change of interface due to 2.3.35 and new MuonSelector:
* CxAODMaker : CXAOD-164: large jet resolution uncertainties: JER, JMS and D2R as custom methods, dbuesche
* CxAODMaker : update electron recoEffSF, idEffSF, isoEffSF, lulu
* CxAODMaker : Xbb variables, benitezj
* CxAODReader : add EL\_CHECK, hanar
* CxAODReader : no truth label on fat jets, don't call copyConeTruthLabels..., hanar
* CxAODReader\_VHbb : disentangle b-jet selection and pT cut on leading selected jet; get rid of isTruthTagged flag; CXAOD-166, hanar
* CxAODReader\_VHbb : require opposite charge for topemuCR, hanar
* CxAODTools : clean the data15 TriggerMenu, djamin
* CxAODTools : fix default TriggerMenu value to CxAODtag16, djamin
* CxAODTools : get rid of isTruthTagged flag, hanar
* CxAODTools : Xbb variables, benitezj
* FrameworkExe : clean the data15 TriggerMenu string in reader config, djamin
* FrameworkSub : Remove JetSubStructureUtils-00-02-18 as now we use AnalysisBase 2.3.35 which has it, abuzatu
* FrameworkSub : updated release tag to 2.3.35, haysjm

## 15-11-21
* CxAODMaker : update electron trigEffSF, lulu
* CxAODTools : add variables for electron effSF, lulu
* CxAODTools : update electron trigEffSF, lulu
* FrameworkSub : Added the 410006 DSID to the cross sections file and fixed naming conventions for the ttbar samples meant as variations for systematic uncertainty studies., meehan

## 15-11-22
* CxAODMaker : CXAOD-164: reduce FATJET\_JER smearing from 10% to 5%, dbuesche
* CxAODMaker : Instead of the muons from CxAOD, have my own muonEventSelector inside JetSemileptonic, to be able to move from loose to medium muons. Also add debug and msgLevel members., abuzatu
* CxAODTools\_VHbb : ugly patch to avoid verbose errors in muon trigger sf tool appearing in 2.3.35, fsforza
* FrameworkSub : update nominal production to 00-01-40 (also minor bkg). Update MJ to 00-01-42-MJ which should have all support triggers, fsforza

## 15-11-23
* CxAODMaker : adding TTVA SF and new isolation SF for muon WP, fsforza
* CxAODMaker : CXAOD-172: implement JetUncertaintiesTool for WZ and Hbb tagging. Hbb has WZ config for now (Hbb not available yet)., dbuesche
* CxAODReader : added jet author to b-tagging systs, jhetherl
* CxAODReader\_VHbb : added jet author to b-tagging systs, jhetherl
* CxAODReader\_VHbb : introduced inMbbWindow method; changed name of JetCorrTLV to getJetCorrTLV; in 2 lepton channel: changing order of cuts; add cutflow; minor clean-up, hanar
* CxAODReader\_VHbb : need to use tagcatIncl and tagcatExcl for now, hanar
* CxAODReader\_VHbb : removed return statement in 2 lepton trigger selection when dealing with syst - need to check with David Jamin, hanar
* CxAODReader\_VHbb : remove return in 2 lepton selection if there are more than 2 b-tagged jets, hanar
* CxAODTools : adding TTVA SF and new isolation SF for muon WP, fsforza
* FrameworkExe : adding TTVA SF sys, fsforza
* FrameworkSub : add JetUncertainties-00-09-31, dbuesche
* FrameworkSub : fix of MuonEfficiency crash on muons with negative pT, fsforza

## 15-11-24
* CxAODMaker : CXAOD-172: proper default settings for Hbb large JES, now adjustable via config file. Skip jets outside validity range to avoid errors., dbuesche
* CxAODMaker : fix match declaration done twice for mu20 trigger, djamin
* CxAODMaker : Introduced new PtReco using Bukin and Gauss fits. They use llbb, OneMu, Parton. Also not compute the PtReco for FatJet anymore, to save time. Also added the Regression training weights for SM., abuzatu
* CxAODMaker : store electron trigger MC eff, djamin
* CxAODMaker : update photon track iso variable from ptvarcone20 to ptcone20, lshi
* CxAODMaker\_VHbb : add isGoodOQ cut for photon, lshi
* CxAODReader\_VHbb : consistent hist naming, hanar
* CxAODReader\_VHbb : feed only selected fat jets to plotting, hanar
* CxAODReader\_VHbb : Implementing bit flag for cutflow and event categorization. Fully implemented only for the 2lep analysis for the moment. Minor changes to tagjet\_selection function and setJetVariables to allow the code to run with the above modifications. Optional print statement to check event weights, sargyrop
* CxAODReader\_VHbb : Removing mis-placed cut for 2lep analysis that affected cutflow results, sargyrop
* CxAODReader\_VHbb : switch order in cutflow, hanar
* CxAODReader\_VHbb : undo accidental commit, hanar
* CxAODTools : access electron trigger MC eff and use them in TriggerTool to deal properly the 2 el events trigger weight, djamin
* CxAODTools : modify electron trigger SF names accessed in TriggerTool to follow latest EOYE recommendations, djamin
* CxAODTools : remove period D protections for muon trigger SF, it is useless now as they have are computed for all data15, djamin
* CxAODTools\_VHbb : pkgs with fixs for muon-Trigger sf, fsforza
* CxAODTools\_VHbb : Updating leptonSF in 1 and 2lep selections to include TTVA, reco and iso SF, sargyrop
* FrameworkExe : run.cfg: add large jet uncertainties, dbuesche
* FrameworkExe : Switch to final GRL, nmorange
* FrameworkExe : Update vtag to 18, nmorange
* FrameworkSub : move to release 2.3.36, dbuesche
* FrameworkSub : pkgs with fixs for muon-Trigger sf and and, fsforza
* FrameworkSub : Removed BoostedJetTaggers, as actually we don't use it in CxAODFramework, abuzatu
* FrameworkSub : Update data lists to use full 2015 luminosity, nmorange
* FrameworkSub : Update GRL, ilumicalc, and add mc15b\_prw, nmorange
* FrameworkSub : updates to packages and release ready for tag18, haysjm
* FrameworkSub : update to JetUncertainties-00-09-32, dbuesche

## 15-11-25
* CxAODReader : better MC-to-MC index checks in b-tagging tool, jhetherl
* CxAODReader : improved b-tagging MC-to-MC index deduction, jhetherl
* CxAODReader\_VHbb : 2 lepton channel: reset histNameSvc description; remove return if less than 2 signal jets; fill histos only if event belongs to defined region; fill easy tree if there are at least 2 signal jets, hanar
* CxAODReader\_VHbb : 2 lepton: resolved mixup, compute\_jetSelectedQuantities doesn't belong to the histos, but the trees...histo filling relies on the jet selected quantities being stored in the easy tree, need to account for that, hanar
* CxAODReader\_VHbb : changed cut AtLeast1B, need to check if it is still correct, hanar
* CxAODReader\_VHbb : Change in 2lep selection: OS leptons for top CR only, sargyrop
* CxAODReader\_VHbb : move filling HVec and bbjVec (re-naming to be consistent) outside of compute\_jetSelectedQuantities in order to allow the building using corrected jets, hanar
* CxAODReader\_VHbb : some more re-ordering for better readability, hanar
* CxAODReader\_VHbb : some re-ordering for better readability, hanar
* CxAODReader\_VHbb : update 2lep call of tagjet\_selection, amontalb
* CxAODReader\_VHbb : update tagjet\_selection function - and its calls in 0lepton and 1lepton selections, cpandini
* CxAODTools : better MC-to-MC index checks in b-tagging tool, jhetherl
* CxAODTools : fixed MC-to-MC index safety check in b-tagging tool, jhetherl
* CxAODTools : improved b-tagging MC-to-MC index deduction, jhetherl
* FrameworkSub : Add MC lists for tag 18, nmorange
* FrameworkSub : Hopefully final update of V+jets cross sections.  The 25ns Pt>280 GeV samples are scaled by extra 1.1 to account for different ptV cross section. The 50ns/low pt values are also updated @CxAOD-160, thompson
* FrameworkSub : update Sherpa diboson k-factor to 0.91 following PMG's recommendations https://twiki.cern.ch/twiki/bin/view/AtlasProtected/DibosonTaskforce#Theoretical\_cross\_sections, cpandini

## 15-11-26
* CxAODMaker : adding HLT\_g120\_loose in trigger list, xulou
* CxAODReader : CXAOD-176: empty AnalysisReader::setObjectsForOR(), throw error on call, dbuesche
* CxAODReader : fixed BTaggingTool MC-to-MC index in data, jhetherl
* CxAODReader : make attaching of jet author to b-tag systs optional, dbuesche
* CxAODReader\_VHbb : 2 lep: adding histograms; clean-up existing ones, hanar
* CxAODReader\_VHbb : 2 lep: more wrapping up, hanar
* CxAODReader\_VHbb : adding whole bunch of quantities to easy tree, hanar
* CxAODReader\_VHbb : fixing compiler errors from previous commits - sorry, hanar
* CxAODReader\_VHbb : remove check, hanar
* CxAODReader\_VHbb : some more cleaning...also 0 and 2lep, hanar
* CxAODReader\_VHbb : some more cleaning..., hanar
* CxAODReader\_VHbb : use m\_physicsMeta to store information on number of (b)-jets; add nbJets to tree, hanar
* CxAODTools : apply HLT\_g120\_loose trigger in 0lep, xulou
* CxAODTools : apply photons to overlap removal, xulou
* CxAODTools : b-tagging temporary work-around, jhetherl

## 15-11-27
* CxAODMaker\_VHbb : Add in check in WHSignalMuon for tight quality and passing ID cuts, amontalb
* CxAODReader\_VHbb : bug fix: filling acutal mVH quantities, hanar
* CxAODReader\_VHbb : exclude cut on number of b-tagged jets from region definitions; add information on trigger selection to easy tree, hanar

## 15-11-28
* CxAODMaker : FatJets: move substructure calculation to decorateOriginParticle (-> fix D2 for JetUnc tool), do D2 smearing directly on D2 instead ECF2, dbuesche

## 15-11-29

## 15-11-30
* CxAODReader : added 0-lepton VH merged analysis options for naming, cmaiani
* CxAODReader\_VHbb : added AnalysisReader\_BoostedVHbb and MVATree\_BoostedVHbb classes for running 0-lepton VH merged analysis, cmaiani
* CxAODReader\_VHbb : Fix in fill\_2lepCutflow function, sargyrop
* CxAODReader\_VHbb : reorganised flags for boosted analysis, cmaiani
* FrameworkExe : addition of config flags and samples for VH boosted analysis, cmaiani
* FrameworkExe : fixing a typo in previous commit in hsg5frameworkReadCxAOD.cxx, cmaiani
* FrameworkSub : added new ggA signal cross-sections for VH boosted resonance search in 0lep channel, cmaiani
* FrameworkSub : removed mc15b sample that sneaked into mc15a lists, hanar

## 15-12-01
* CxAODReader\_VHbb : Adding merged analysis for the 2lep channel only. Merged analysis is not run by default, sargyrop

* CxAODMaker : CXAOD-172: add safety checks when calling the JetUncTool -> fix crash for unsupported collections, dbuesche
* CxAODReader\_VHbb : 2 lep: rm stuff needed for optimization, hanar
* CxAODTools : Updated TriggerTool: Enabled setting m\_compute\_muTrigSF from config, added initialization for all member fields, fixed compiler warning in TriggerTool (commented out unused parameter 'met' in getTriggerDecision()), grkeren
* FrameworkExe : hackyy scripts for yields, thompson
* FrameworkExe : Made GEDriver use nFilesPerJob and submitFlags from config., fmueller
* FrameworkExe : write out DxAOD in rather than out for yields calc, thompson

## 15-12-02
* CxAODReader\_VHbb : adding method to decide whether region should be blinded; apply blinding in 2lep, hanar
* CxAODReader\_VHbb : adding/removing comments, hanar
* CxAODReader\_VHbb : add n-jets histograms, hanar
* CxAODReader\_VHbb : store w/ and w/o PU weight applied as systematic variation, respectively, depending on default setting; write PU weight to tree, hanar
* CxAODReader\_VHbb : updated tree / histogram filling: cleaning-up, adding variables, using flat tree variables to fill histos, removed non-used argument from fill\_jetSelectedHistos; 2 lep: might crash for resolved+merged, hanar
* FrameworkExe : change the ouput name if testing DxAOD yields, thompson
* FrameworkExe : CT10 no longer in Sherpa V+jets name, thompson
* FrameworkExe : flag any datasets from the submission list not found, thompson
* FrameworkSub : updated packages for intermediate tag, haysjm

## 15-12-03
* CxAODReader\_VHbb : added new property for linking track jets to fat jets, jhetherl
* CxAODReader\_VHbb : add trigger cut for vbfa analysis in reader, lshi
* CxAODReader\_VHbb : applyCS() function update: treat njet>3 as njet=3 for CorrsAndSysts systematics, cpandini
* CxAODReader\_VHbb : clean old BDT weight file, lshi
* CxAODReader\_VHbb : Fixing el/mu cutflow for 2lep analysis, sargyrop
* CxAODReader\_VHbb : implement k-fold for vbfa analysis, lshi
* CxAODTools : added new property for linking track jets to fat jets, jhetherl
* CxAODTools : skip trigger matching for vbfa, as it always fails due to a trigger bug in 50 ns MC sample, lshi
* CxAODTools\_VHbb : clean trigger pre-selection, lshi
* FrameworkExe : update to copy PowHeg diboson, thompson

## 15-12-04
* CxAODMaker\_VHbb : Store muonQuality in CxAOD. Needed for implementing merged selection as done in VH resonance analyses, sargyrop
* CxAODReader : Changing HistNameSvc njet and ptv binning according to convention for fit inputs, sargyrop
* CxAODReader\_VHbb : 2lep: adding histos; moving to PtRecollbbOneMuPartonBukinNew in v18, hanar
* FrameworkExe : adapting to current trunk output; enable blinding of mBB and mVH for ggA500; merge regions, hanar
* FrameworkExe : removed reference to TupleBDT and updated to interface change in passing the config to the TupleMaker, haysjm
* FrameworkExe : some more powheg diboson, thompson
* FrameworkSub : The boosted Sherpa V+jets cross sections/k-factors are different, thompson

## 15-12-05

## 15-12-06

## 15-12-07
* CxAODReader\_VHbb : Restructuring and fixed of 2lep function to allow for a better integration of merged analysis with resolved one. Possibility to run either one standalone or combined based on ptV, sargyrop
* FrameworkSub : add missing ggA samples, thompson
* CxAODReader\_VHbb, FrameworkExe : make jet correction type stearable by config, hanar
* CxAODReader: CXAOD-128: add check for duplicated events in AnalysisReader, dbuesche
* CxAODMaker\_VHbb: add photon cleaning cut according to recommendation, lshi
* CxAODTools: add possibility to switch off large-R jet - small-R jet OR, hanar
* CxAODReader\_VHbb: Fix 2 lep: correct cuflow for merged; typo, hanar
* FrameworkExe: add options; set sensible defaults, hanar
* CxAODMaker: keep consistent information on number of vertices with at least 2 tracks; CXAOD-183, hanar
* CxAODTools: rm NVtx3Trks;  CXAOD-183, hanar
* CxAODReader\_VHbb: rm some commented code, hanar
* CxAODReader\_VHbb: adjust comments, hanar
* CxAODReader: Add HistFastSvc, nmorange
* CxAODReader\_VHbb: Add example regNaming class with VHRes naming conventions, nmorange
* CxAODTools: undo previous commit, need to keep NVtx3Trks a little longer; CXAOD-183, hanar
* CxAODReader, CxAODReader\_VHbb: fix to call only once the get random run number, djamin
* CxAODReader\_VHbb: Fixing fatJetCorrType was not read properly from the config file (stray character?). Also adding fix for 2Lep merged selection: exactly 2-btags in fat-jet, sargyrop
* CxAODReader\_VHbb: Fix for 2Lep analysis: exactly 2 b-jets (doing it correctly this time)
* CxAODReader\_VHbb: add photon isolation cut at Reader level, lshi
* CxAODReader\_VHbb: separating setJetVariables for small-R and fat jets; introduced setFatJetVariables, fat jet objects; cleaning of the 2 lep code accordingly, hanar
* FrameworkSub: adding diboson XSec for PwPy8EG, hanar
* FrameworkSub: correct WWlvlv xsec, hanar

## 15-12-08
* CxAODReader: streamlined setMCIndex call, jhetherl
* CxAODReader\_VHbb: got truth tagging technically to work for small-R calo and track jets; properties on non-tagged jets now also correctly set; can either call the b-tagging or the truth tagging methods, since properties can't be overwritten; currently truth tagging only correct for small-R jets and related quantities, still need to figure out how to do it in all places correctly for track / fat jets and related quantities; made tagStrategy a member, added it as argument to compute\_truthTagging - will be needed later on, hanar
* CxAODReader\_VHbb: make compute\_truthTagging return the truthTagWeight and decorate the event info outside instead; will allow the 2 lep to do it for small-R and fat jets in the same event, hanar
* CxAODTools: added tagger enum to BTaggingTool, jhetherl
* CxAODTools: cleanup truth tagging; move computing the truth tag weight to a separate method, hanar
* CxAODTools: fix usage of HLT\_g120\_loose in TriggerTool 0lep, djamin
* CxAODTools: optionally loop over b-tagging systematics and refactored loop, jhetherl
* CxAODTools: streamlined setMCIndex call, jhetherl
* CxAODTools\_VHbb: enabling cut on the number of tracks on the track jets; will lead to a crash on < v18 samples, hanar
* FrameworkExe: Add slash:    std::string sample\_dir(dataset\_dir+"/"+sample\_name);, abuzatu
* FrameworkExe: To allow eos files to be read also from an institution out of cern, one needs to setup before running first "source /afs/cern.ch/project/eos/installation/atlas/etc/setup.sh" and then "export EOS\_MGM\_URL=root://eosatlas.cern.ch", but also need to change in hsg5frameworkReadCxAOD.cxx from "root://eosatlas/" to "root://eosatlas.cern.ch:/", abuzatu
* FrameworkExe: adapt to new samples, separate nominal from others; needs testing, hanar
* FrameworkExe: add fix here, hanar
* FrameworkExe: default: do not apply tau OR, hanar
* FrameworkExe: move PwPy8EG\_A14\_ttbar from \_add to own directory, hanar
* FrameworkExe: undo previous commit, hanar
* FrameworkExe: undo previous commit, hanar
* FrameworkSub: add SM data 25ns derivations, fsforza
* FrameworkSub: adding 0 lepton yields files for v18 production, hanar
* FrameworkSub: adding 1 lepton yields files for v18 production, hanar
* FrameworkSub: adding 2 lepton yields files for v18 production, hanar
* FrameworkSub: different name for diboson powheg samples, hanar
* FrameworkSub: new yield files for Wlnu v46, fsforza

## 15-12-09
* CxAODMaker: Added ghost associated heavy flavour hadrons to output jets. Disabled by default, enable by putting in config file: bool storeGAHeavyFlavHadronsInJets = true, grkeren
* CxAODMaker: If electron track not found, variables are filled with 0s, also removing protection against isLooseLH missed variable in JetSemileptonic.cxx, carquin
* CxAODMaker: Revert commit which pulled too many things, nmorange
* CxAODMaker: remove m\_isoCorr\_tool-\>setProperty(Apply\_datadriven, false) to stop crashing, lshi
* CxAODReader\_VHbb: 2lep: also write data for PU syst variation, hanar
* CxAODReader\_VHbb: can't deal with zero PU weights...; can only switch off PU in config and store withPU as syst, hanar
* FrameworkExe: 2 lep: adding histograms; remove comments; add another tag cat; correct merged pTV label, hanar
* FrameworkExe: adapt to pTV binning; some cleanup, hanar
* FrameworkExe: default: don't do PU reweighting; 2 lep: store with PU reweighting as syst, hanar
* FrameworkExe: default: include taus in the OR, hanar
* FrameworkExe: small fix for Powheg diboson, thompson
* FrameworkSub: Addign XSections for 361601 (PwPy8\_WZlvll), 361603 (PwPy8\_ZZlll), 361604 (PwPy8\_ZZvvll). Cross-sections from PMG twiki, sargyrop
* FrameworkSub: Adding XSec for 361602 (PwPy\_WZlvvv) from PMG twiki, sargyrop
* FrameworkSub: Bump to 2.3.38, nmorange
* FrameworkSub: adding missing diboson Xsec; Xchecks welcome, hanar
* FrameworkSub: correct names, hanar

## 15-12-10
* CxAODReader: add VBF njet naming convention to HistNameSvc, lshi
* CxAODReader: optimized logic for looping over b-tagging systs, jhetherl
* CxAODReader\_VHbb: 2 lep: remove pTV binning; fix typo, hanar
* CxAODReader\_VHbb: use VBF njet naming convention from HistNameSvc, lshi
* CxAODTools: made MC channel crosscheck more robust in BTaggingTool, jhetherl
* FrameworkExe: FIX: did not actually merge the ptV bins, hanar
* FrameworkSub: add some missing monoHbb cross sections (from AMI), thompson
* FrameworkSub: update 4 datasets(rerun with 18-0d) which had low stats due to download problems, thompson

## 15-12-11
* CxAODMaker: Adding new jet regression weight files and removing old ones, eschopf
* CxAODMaker: Changing the regression to use the new target (truthpt/recopt). In addition the regression variables are written to the CxAOD - this can be disabled with the writeRegVars config value, eschopf
* CxAODTools: Adding the regression variables as properties, eschopf
* CxAODTools: add one flag to use or not the setORInputLables in the OR tool. Default to true, as in the previous code, fsforza
* FrameworkExe: FIX: filled 2jet twice; add debug output, hanar
* FrameworkExe: New configuration of the jet regression in framework-run.cfg using the new target (truept/recopt), eschopf
* FrameworkSub: cleaning pkg already in 2.3.38, fsforza

## 15-12-13
* CxAODReader\_VHbb: BUG FIX: compute ZH vec using fat jet in merged regime; thanks Yanhui, hanar
* CxAODReader\_VHbb: BUG FIX: topemuCR, correct cut on lep charge, hanar
* CxAODReader\_VHbb: fix formatting issue, hanar
* CxAODReader\_VHbb: fix previous commit, hanar
* CxAODReader\_VHbb: got to long int, match previous commit, hanar

## 15-12-14
* CxAODReader\_VHbb: add possibility to use alternative truth tagging method; default is the old version, hanar
* CxAODReader\_VHbb: increase hist ranges, hanar
* CxAODTools: add alternative truth tagging method; only validated for AllSignalJets strategy, hanar
* CxAODTools\_VHbb: update photon isolation cut, lshi
* FrameworkSub: Add documentation on HistFastSvc, nmorange

## 15-12-15
* CxAODReader\_VHbb: 2 lep: add alternative strategies for dealing resolved and boosted regime; from Spyros - thanks, hanar
* CxAODReader\_VHbb: 2 lep: adding CorrsAndSyst stuff; needs testing, hanar
* CxAODReader\_VHbb: 2 lep: retrieve taus from selection result; apply tau veto; add number of taus to tree, hanar
* CxAODReader\_VHbb: 2lep: adapt cutflow to tau veto, hanar
* CxAODReader\_VHbb: add tau veto to dilepton cuts, hanar
* FrameworkSub: updated MuonSelectorTool tag following latest recommendations, cmaiani

## 15-12-16
* CxAODReader\_VHbb: 2 lep: adapt cutflow hist to removing tighter selection on leptons in merged, hanar
* CxAODReader\_VHbb: 2 lep: add SFs to tree, hanar
* CxAODReader\_VHbb: 2 lep: add passedTauVeto to tree, hanar
* CxAODReader\_VHbb: 2 lep: finer binning, hanar
* CxAODReader\_VHbb: 2 lep: remove 2tag requirement from merged signal region def, hanar
* CxAODReader\_VHbb: 2 lep: remove tighter cuts on leptons in merged seleciton, hanar
* CxAODReader\_VHbb: add bjet energy correction to output tree, lshi
* CxAODReader\_VHbb: bug fix wrt previous commit in boosted analysis, cmaiani
* CxAODReader\_VHbb: fix       , hanar
* CxAODReader\_VHbb: implemented fasthistsvc option, from nicolas, cmaiani
* CxAODReader\_VHbb: make m\_csCorrections and m\_csVariations members, hanar
* CxAODReader\_VHbb: retrieve csVariations and csCorrections only once, hanar
* CxAODReader\_VHbb: rm couts  , hanar
* CxAODReader\_VHbb: small improvements: use status code as return; avoid string comparison, hanar
* CxAODReader\_VHbb: small ups to boosted code / cutflow def, cmaiani
* CxAODReader\_VHbb: use member, hanar
* CxAODTools: added method to sort taus according to pT, hanar
* CxAODTools: fix fix electron trig SF weight computation, djamin
* CxAODTools\_VHbb: add taus to selection result; basic selection and OR applied, hanar
* FrameworkSub: MJ yield for 00-01-47-MJ, fsforza

## 15-12-17
* CxAODReader: FIX: removed CorrsAndSyst variations from initializeVariations to avoid redundancy; CorrsAndSyst variations are treated as weight systematics, hanar
* CxAODReader: add possibility to store syst hists in one directoy; needs to be enabled in the config, hanar
* CxAODReader: only two pTV bins: smaller/greater 500 GeV, hanar
* CxAODReader: retrieve setting only once from config, hanar
* CxAODReader\_VHbb: Enlarge ranges of some histograms and enable ptv binning in 2lep analysis, sargyrop
* CxAODReader\_VHbb: Possibility to only store mbb and mVH histograms using doOnlyInputs flag - 2Lep analysis only, sargyrop
* FrameworkExe: mv also singletop schan syst samples to separate folder, hanar
* FrameworkSub: Addnew bbtautau XSs, gwilliam
* FrameworkSub: add bbtautau FrameworkSub package, nilic

## 15-12-18
* CxAODMaker: Allow to optionally apply MET, gwilliam
* CxAODMaker: added z0 significance for muons and electrons, fixed compiler warning in JetRegression.cxx, grkeren
* CxAODTools: added property for z0 significance, grkeren
* FrameworkExe: Cleaning up framework-read.cfg: change default luminosity to 3.21, moved doOnlyInputs to separate block to make it clear that it's not only for merged analysis, clean up driver options, better documentation of analysisStrategy option, sargyrop
* FrameworkSub: revert back to changes I accidently made, nilic
* FrameworkSub: revert back to changes, nilic
* FrameworkSub: revert changes, nilic
* FrameworkSub: revert to previous revision, nilic

## 15-12-19
* CxAODMaker: add photon isolation systematics, lshi
* CxAODTools: add photon track isolation scale factors, lshi
* FrameworkExe: update photon systematic list, lshi

## 15-12-21
* CxAODMaker: added property IsBjet to jets in JetHandler which is required when running with globally reduced set of JES uncertainties, 19 NPs, grkeren
* CxAODMaker: tau trigger SF implementation, agbet
* CxAODTools: tau trigger SF prop added, agbet

## 15-12-25
* CxAODReader\_VHbb: Bug fix: trackJetsInLeadFJ were not filled correctly in compute\_fatjetTags function, sargyrop
* CxAODReader\_VHbb: Change for 2lep merged cutflow - use fat-jet mass after corrections (instead of before corrections), sargyrop
* CxAODReader\_VHbb: Protection against missing EasyTree branches in fill\_jetSelectedHistos that were causing the Reader to crash, sargyrop

## 16-01-04
* FrameworkExe: fix the name of systematic PH\_Iso\_DDonoff, lshi

## 16-01-05
* CxAODMaker, CxAODTools: add photon MC Classifier info, lshi
* CxAODMaker, CxAODTools: add photon conversionType, lshi
* CxAODMaker, CxAODTools: add photon isEM value, lshi

## 16-01-07
* CxAODReader\_VHbb: Modify the arguments of getJetCorrTLV for better understanding in 0 lepton, ddelgove
* CxAODReader\_VHbb: Proper systematic variation for muon in jet in 0 lepton, ddelgove
* CxAODReader\_VHbb: update resolved 0 lepton selection, ddelgove
* CxAODTools: Fix in TriggerTool that affects top CR: restores previous behavior of the code, allowing subleading leptons in emu events to go down to 7 GeV., sargyrop
* FrameworkExe: add two options for 0 lepton selection, ddelgove

## 16-01-09
* CxAODReader: fixed b-tagging syst names with jet author, jhetherl
* FrameworkExe: Commented out due to crash at Maker run time string tauContainer             = TauJet, abuzatu

## 16-01-10
* CxAODReader: additional fix on b-tag sys naming;CXAOD-191, hanar
* CxAODReader\_VHbb: 2 lep: propagate jet corrections to jet syst variations, hanar

## 16-01-11
* CxAODMaker, CxAODTools: correct VBF+photon trigger name, lshi
* CxAODReader\_VHbb: correcting printout, hanar
* CxAODReader\_VHbb: 2 lep: add Z mass constraint to mumu channel, hanar
* FrameworkSub: Higgs WW->lvqq signal (commented), arturos

## 16-01-12
* CxAODReader\_VHbb: 2 lep: bug fix - use track jet author for btag syst in merged regime, hanar
* CxAODReader\_VHbb: fix compiler warning, hanar
* CxAODTools: small fix on truth tagging for Leading2SignalJets, hanar

## 16-01-13

## 16-01-14
* CxAODMaker: added protection: only copy hasSharedTrack flag if OR tool is run, hanar
* CxAODReader: added protection against missing container, hanar
* CxAODReader\_VHbb: added tau veto to the 0lep boosted code, not applied by default, cmaiani
* CxAODReader\_VHbb: Fix for 2lep merged analysis: calculate b-tag SF for merged region based on track-jets associated to leading fat-jet only, sargyrop

## 16-01-15
* CorrsAndSysts: New Run2 corrections for W, Z ttbar. Just for testing at the moment., amehta
* CorrsAndSysts: New Run2 corrections for W, Z ttbar. Just for testing at the moment., amehta
* CxAODMaker: Removed line in ElectronHandler which erased the first 4 characters of the trigger name for trigger matching since Trig::TrigEgammaMatchTool does not (as of 2.3.38) prepend 'HTL\_' to the trigger name passed to it, grkeren

## 16-01-16
* CxAODMaker: Using cluster->etaBE(2) instead of cluster->eta() to be in sync with AsgElectronEfficiencyCorrectionTool. Edge case encountered where the two values were on each side of 2.47, causing a seg. fault. in TElectronEfficiencyCorrectionTool::calculate(), grkeren

## 16-01-17

## 16-01-18
* CxAODReader: migrated EasyTree to common Reader, jhetherl
* CxAODReader\_VHbb: migrated EasyTree to common Reader, jhetherl
* CxAODTools: updated CDI file for b-tagging, jhetherl

## 16-01-19
* CxAODMaker: Compute SF starting from 7GeV for electrons, nmorange
* CxAODReader: fixed AZh boosted naming, cmaiani
* CxAODReader: New Muon Overlap Removal, sjiggins
* CxAODReader\_VHbb: 2 lep: change name of top CR to match limit input convention, hanar
* CxAODReader\_VHbb: added boosted AZh 0lep analysis to the \_VHbb code, cmaiani
* CxAODReader\_VHbb: adding new property; removing not used one; add new 2 lepton cut, hanar
* CxAODReader\_VHbb: adjusted compute\_fatjetTags to harmonized fat jet - track jet association: only use leading track jets to define the number of b-tags; 2 lep: allow fat jets with only one track jet; use new btag definition; add variables to tree, hanar
* CxAODTools: 1st fix for offline el quality for trig SF, djamin
* CxAODTools: New Muon Overlap Removal, sjiggins
* FrameworkExe: small updates related to A->Zh 0lep boosted analysis, cmaiani
* FrameworkSub: 2.3.40 not yet on cvmfs..., nmorange
* FrameworkSub: added W'->WH samples, cmaiani
* FrameworkSub: Bump AnalysisBase release to 2.3.40, nmorange
* FrameworkSub: ggA sample names adjusted to follow limit input conventions; renaming old ggA samples to be able to differentiate, hanar
* FrameworkSub: remove \_ from single top sample names to match limit input convention, also for syt samples, hanar
* FrameworkSub: renaming SM ZH samples to correctly match limit input convention also for vv, hanar
* FrameworkSub: renaming SM ZH samples to correctly match limit input convention, hanar
* FrameworkSub: renaming SM ZH samples to match limit input convention; removing DC14 samples, hanar
## 16-01-20
* CxAODMaker: added switch to turn off tau calibration and efficiency corrections but pass through taus to the output, haysjm
* CxAODMaker: Don't compute PtReco with Gauss fit any more, abuzatu
* CxAODMaker: fixed misplaced comma in TauHandler, haysjm
* CxAODMaker: Keep in CxAOD only OneMu, PtReco, Regression, remove AllMu, OneMuNu and AllMuNu, abuzatu
* CxAODMaker: Keep in CxAOD only XbbTagger, remove OneMu, AllMu, OneMuNu, AllMuNu, abuzatu
* CxAODReader: Correct MET binning for AZh 0 lepton resolved, ddelgove
* CxAODReader\_VHbb: Micro optimization (more readable) to getJetCorrTLV, nmorange
* CxAODReader\_VHbb: Propagate modification of hist name svc in 0 lepton resolved fill function, ddelgove
* CxAODReader\_VHbb: Reader optimization: don't fill C&S hists if variation is < 10^-6, nmorange
* FrameworkExe: turned the tau handler back on, added flag to turn off tau calibration and efficiency corrections to work-around problem of missing truth matching in the current derivations. This should go away when we switch to the next set of derivations... CXAOD-195, haysjm
* FrameworkSub: use latest AssociationUtils tag, nmorange

## 16-01-21
* CxAODMaker: updated configuration for TST MET systematics, tnobe
* CxAODReader\_VHbb: 2 lep: add medium quality to tree, hanar
* CxAODReader\_VHbb: Fix for 2lep analysis: add low mll cut for ttbar CR and remove tau veto, sargyrop
* CxAODReader\_VHbb: Fix for 2lep only: remove blinding at the level of fit inputs, sargyrop
* CxAODTools: prepare function in triggertool for MET trigger SF and systs, djamin
* FrameworkSub: Release 2.3.40 is finally available on cvmfs, nmorange

## 16-01-22
* CxAODReader: Add 23jet region in HistNameSvc, sargyrop
* CxAODReader\_VHbb: 2lep analysis: add fat-jet mass rescaling and fix event weight print-out for cutflow, sargyrop
* CxAODReader\_VHbb: 2lep analysis: add low, high and outer mBB control regions, sargyrop
* CxAODReader\_VHbb: 2lep analysis: allow to merge different mBB side-band regions into one using the doMergeCR flag, sargyrop
* CxAODReader\_VHbb: 2lep analysis: fix outer mbb definition - was not done correctly in my previous commit, sargyrop
* CxAODReader\_VHbb: 2lep analysis: make fat-jet mass rescaling steerable from config file. Default is to not apply rescaling., sargyrop
* CxAODReader\_VHbb: Add flag to allow merging the 2jet and 3jet regions. Default is to not merge, sargyrop
* CxAODReader\_VHbb: Change cut for 2lep analysis: move mBB window to 110-140 GeV, sargyrop
* CxAODReader\_VHbb: Changes for 2lep: rearrangement of code to allow for proper implementation of new resolved/merged combination strategies, sargyrop
* CxAODReader\_VHbb: Cleanup 2lep code, sargyrop
* CxAODReader\_VHbb: Cleanup: remove deprecated option m\_doMbbWindow; was not used anywhere in the code, sargyrop
* CxAODReader\_VHbb: Fixes to remove some of the compiler warnings, sargyrop
* CxAODReader\_VHbb: Update 2lep merged analysis cut: require both leptons above 25 GeV in all regions, sargyrop
* CxAODReader\_VHbb: Update 2lep merged analysis cut: use at least 2 track-jets associated to leading fat-jet in all regions, sargyrop
* CxAODReader\_VHbb: updated usage of CorrsAndSysts - example in fill\_0Lep(), cpandini
* FrameworkSub: MC15 samples for VH V->jj, H->mumu, amehta

## 16-01-23
* CxAODReader\_VHbb: Fix constructor inizialitation list: use bools to initialize bools not strings, sargyrop
* CxAODReader\_VHbb: Update 2lep cut: add opposite charge requirement for muons in resolved and merged analysis - all regions, sargyrop
* CxAODReader\_VHbb: Update cut for 2lep: move fat-jet mass window to 76-146 GeV, sargyrop
* CxAODReader\_VHbb: Updating 2lep cutflows to include OSLeptons cut, sargyrop

## 16-01-24
* CxAODReader\_VHbb: Fixes for 2lep analysis: remove tau veto from top CR and correctly fill OS leptons cut, sargyrop
* CxAODReader\_VHbb: Minor fixes for plotting for 2Lep analysis only, sargyrop

## 16-01-25
* CxAODReader\_VHbb: 2lep analysis: fix condition for applying m(mumu) rescaling, sargyrop
* FrameworkSub: adding some graviton samples, cwang

## 2016-01-26
* CxAODMaker: Fix compilation warning, nmorange
* CxAODMaker: add new vbf+photon triggers for trigger study, lshi
* CxAODMaker: add single photon triggers, lshi
* CxAODMaker: update to new v04 config files, lulu
* CxAODReader: removed tautau specific default in XSection, jhetherl
* CxAODReader: updates to boosted analysis, nilic
* CxAODReader\_VHbb: fixed EOYE recale on PU histos, cmaiani
* CxAODReader\_VHbb: remove AllMu, OneMuNu, AllMuNu and PtReco+Gauss from reader, lshi
* CxAODTools: add single photon triggers, lshi
* FrameworkExe: Start to add new validation script, nmorange
* FrameworkExe: add full list of csVariations recommended by Carlo, hanar
* FrameworkSub: Bump AnalysisBase to 2.3.41, nmorange
* FrameworkSub: updated yields file for di-lepton MC15b, jhetherl

## 2016-01-27
* CxAODMaker: IsBjet fix from bool to char, agbet
* CxAODMaker: remove HLT\_g20\_loose, HLT\_g25\_loose, lshi
* CxAODMaker: updated trigger list for bbtautau, agbet
* CxAODReader: Revert unwanted commit on AnalysisReader, nmorange
* CxAODReader: re-included track-jet TruthLabel copying, jhetherl
* CxAODTools: add MET trigger SF and syst, wangwe

## 2016-01-28
* CxAODMaker: Fixed bug in JetHandler where 'IsBjet' - truth label used by JES tool - was always set to true, grkeren
* CxAODMaker: Implemented Props::SumPtTrkPt500PV decoration for Variable Cone Overlap Removal, sjiggins
* CxAODReader: pointing to correct XSec and yields files for mc15b, amontalb
* CxAODReader\_VHbb: 0lepton selection update: (1) 110-140 mbb-window, (2) apply jet 4p correction on dijet H candidate for mbb-window cut and dijet-mass rescaling, cpandini
* CxAODReader\_VHbb: Fix in 2lep analysis: remove tau veto from resolved SR and mBBcr - temporary fix until we switch to new function (imminent), sargyrop
* CxAODTools: Implemented Variable Cone OR in OverlapRemoval.h(cxx), sjiggins
* FrameworkExe: adding flag for mc15b XSec and Yields files, amontalb
* FrameworkExe: config steering file: 0lepton MET correction set to false by default, AllSignalJets tagging strategy set to true by default, cpandini
* FrameworkSub: Added missing monoHbb samples, rroehrig
* FrameworkSub: Modified the monoHbb signal samples by changing the cross sections to all be identically 1.0 such that the fits are more stable without having to do scaling specific for each sample., meehan
* FrameworkSub: updating yields file, amontalb

## 16-01-29
* CxAODMaker: Minor changes related to CP check for photons, added IEGammaAmbiguityTool and isAmbiguity decoration for photons, jpasner
* CxAODMaker: Store OneMu once again, as in the end we use it and not XbbTagger, abuzatu
* CxAODReader\_VHbb: Add cut in 2lep analysis: |eta|<2.5 cut for muons in merged analysis. Also remove some old junk, sargyrop
* CxAODReader\_VHbb: Change 2lep cut: change m(fat-jet) cut to 75-145 GeV, sargyrop
* CxAODReader\_VHbb: Tidying up 2lep code: make cut definition cleaner and replace eventFlag checking with the more intuitive passSpecificCuts function, sargyrop
* CxAODTools: Adding isAmbiguous to common properties as decoration for IEGammaAmbiguityTool decision, jpasner
* CxAODTools: Implemented Variable Cone Overlap Removal with Props::OROutputLabel, sjiggins
* CxAODTools: variable cone OR - compiles, but not tested or even enabled, grkeren
* FrameworkExe: Move default sample and PU reweighting to MC15b in framewokr-run, nmorange
* FrameworkSub: prep for intermediate tag 19-01, haysjm
* FrameworkSub: typo in packages.txt, haysjm

## 16-01-30
* CxAODMaker: Storing jet variable Props::SumPtTrkPt500PV, abuzatu
* CxAODReader: adding virtual function executePreEvtSel() called before EventSelection, arnaez
* CxAODReader\_VHbb: 2 lep: adding switch using NVtx2Trks if available in inputs (new) otherwise NVtx3Trks (old); adding infos on track jets to tree, hanar
* CxAODReader\_VHbb: Updated at Nvtx NVtx3Trks to NVtx2Trks; crash otherwise, abuzatu
* CxAODTools: fixed bug in variable cone OR, grkeren
* FrameworkExe: correct settings for large jet OR, hanar

## 16-01-31
* CxAODReader\_VHbb: Updates in 2lep cutflow, sargyrop
* CxAODTools: Corrected VaribaleConeOverlapRemoval logic (minor), sjiggins
* CxAODTools: Implemented VariableConeOverlapRemoval added ORInputLabelCheck, sjiggins
* CxAODTools: Minor fix in sumOfWeightsProvider: use correct name of class in the Error messages (was printing out XSectionProvider before), sargyrop
* CxAODTools: fix in variable cone OR, grkeren

## 16-02-01
* CxAODMaker: Small fix for recording of TruthEvents, pottgen
* CxAODTools: VariableConeOverlapRemoval correction, sjiggins
* FrameworkExe: Improvement to script to draw CI plots, nmorange
* FrameworkSub: modified monoHbb cross sections to add missing DSD 304035, meehan
* FrameworkSub: updating yields, amontalb

## 16-02-02
* CxAODMaker : Added PtReco in Run I style (PtRecollbbOneMuTruthWZNoneOld), to evaluate the improvement with Run II style (PtRecollbbOneMuPartonBukinNew), abuzatu
* CxAODReader\_VHbb : 2 lep BUG fix: correctly fill third fat and track jet, hanar
* CxAODReader\_VHbb : 2 lep: correct usage of CorrsAndSyst, following Carlo's implementation in the 0 lepton channel, hanar
* CxAODReader\_VHbb : 2 lep: fixing compiling errors - thanks Wei for reporting, hanar
* CxAODTools : add a flag of met trigger SF, wangwe
* CxAODTools : VariableConeOverlapRemoval - logic statement correction for OROutputLabel initialisation, sjiggins
* FrameworkExe : add a flag of met trigger SF, wangwe
* FrameworkExe : Added applyVarOR = true to run and read config, abuzatu
* FrameworkSub : Bump to AnalysisBase 2.3.42, nmorange

## 16-02-03
* CxAODReader\_VHbb : 2 lep fix: use leading signal jets for dR and dPhi in CorrsAndSyst; changing format, hanar
* CxAODReader\_VHbb : Updating 2lep selection: mll window, sargyrop
* FrameworkExe : added flag deciding whether to put all systematics in one folder or not (needed to run fit), cmaiani
* FrameworkExe : moved the sys folder flag to a more suitable place, cmaiani
* FrameworkSub : Replacing yields file for 2lep with correct mc15a yields from 18-00 production (was overwritten with mc15b yields before), sargyrop

## 16-02-04
* CxAODReader\_VHbb : fixed b-tag syst for 0-lep boosted in VHbb, cmaiani
* CxAODReader\_VHbb : remove xsectionprovider re-instantiation in corrsandsysts initialization (not necessary), cpandini
* CxAODTools\_VHbb : Add track jets to VBFHbbEvtSelection result so that we can veto on soft-qcd activity, prose

## 16-02-05
* CxAODReader\_VHbb : 2Lep analysis: add splitting into 0 and 1+ additional b-tagged track-jets to merged selection, sargyrop
* CxAODReader\_VHbb : Fix for 2lep: Adding |eta|<2.5 cut for both muons in merged analysis, sargyrop
* CxAODReader\_VHbb : Fixing AnalysisReader\_VHbb::initializeSumOfWeights so that correct yields file is picked up when using mc15b, sargyrop
* CxAODTools\_VHbb : Change  0 lepton preselection to 140GeV for Moriond production, nmorange
* FrameworkSub : prep for tag 19-03, haysjm
* FrameworkSub : updating yields, amontalb
* FrameworkSub : updating yields, amontalb

## 16-02-06
CxAODReader\_VHbb : 2Lep: excluding some more histos with doReduceFillHistos option, sargyrop
CxAODReader\_VHbb : New feature for 2lep: doReduceFillHistos flag that allows to write out only a reduced set of histograms, sargyrop

## 16-02-07

## 16-02-08
* CxAODMaker : refixing the isBjet variable, agbet
* CxAODMaker : reverting isBjet type., agbet
* CxAODReader : FIX: only use mc15b yields file if the analysis type is 1 lepton, hanar
* CxAODReader\_VHbb : FIX: remove cout debug statement, hanar
* FrameworkExe : Add master continuous integration script, nmorange
* FrameworkExe : Add script to create webpages, nmorange

## 16-02-09
* CxAODReader : added protection: only retrieve random runnumber from PU tool if one wants to explicitely recompute the muon trigger SF; if so it is mandatory to also recompute the PU weight, hanar
* CxAODReader : revert FIX: don't use anaylsis type info here, breaks DB FW; implement FIX in VH reader, hanar
* CxAODReader\_VHbb : add initializeIsMC to override methods, hanar
* CxAODReader\_VHbb : Change in 2Lep: do not rescale mbb mass for emu events, sargyrop
* CxAODReader\_VHbb : fix       , hanar
* CxAODReader\_VHbb : FIX: override initializeIsMC; use only mc15b XSec if running 1 lep anaylsis, hanar
* CxAODReader\_VHbb : removing the cout affecting the boosted 0 lepton analysis, francav
* CxAODReader\_VHbb : removing the cout affecting the boosted 0 lepton analysis in Azh, francav
* FrameworkExe : Add log files in webpages, nmorange
* FrameworkExe : Prepare framework-run for tag, nmorange
* FrameworkSub : added WH\_lvqq samples for every available mass point in 0lep mc15a samples list, cmaiani
* FrameworkSub : added WH samples mc15a yields for 0lep channel, cmaiani
* FrameworkSub : Update packages tags, nmorange
* FrameworkSub : Upload of the MC lists for CxAOD production v20. To be used: list\_sample\_grid.mc15*\_only\_13TeV\_25ns\_HIGG*\_09feb16.txt, arturos

## 16-02-10
* CxAODReader\_VHbb : 2 lep bug fix: properly compute m\_physicsMeta.nAddBTrkJets; was previously number of fat jets -1, hanar
* CxAODReader\_VHbb : 2 lep bug fix: store actually number of b-tagged track jets in tree, hanar
* CxAODReader\_VHbb : fixed use of PUw tool for setting up the triggertool in the ^Clep boosted channel, cmaiani
* FrameworkExe : set the submit bool to true because often overlooked. Add data file lists back, thompson
* FrameworkSub : some of the VHmumu are mc15b, thompson

## 16-02-11
* CxAODReader : added function to get correct muon-in-jet correction for systematic variations of the jet, grkeren
* CxAODReader\_VHbb : 2Lep merged analysis: merge topaddbjetcr and noaddbjetsr in the merged analysis to keep things simple (based on Hannah's studies), sargyrop
* CxAODReader\_VHbb : fixed bug on FatJet sys in 0-lepton related to muon-in-jet correction, cmaiani
* CxAODTools : add in qcd isolation variables, amontalb
* FrameworkExe : put in comments on what fat jet OR variables are, amehta

## 16-02-12
* CxAODReader\_VHbb : New option in 2lep: doMergeJetBins: will only write out 2pjet bin. Replaces doMerge23Jets. Default value is false, sargyrop

## 16-02-13
* CorrsAndSysts : pT(ttbar) systematic included in CorrsAndSysts, cpandini
* CxAODReader\_VHbb : change to the CorrsAndSysts interface to correctly retrieve the pT(ttbar) systematic, cpandini
* FrameworkExe : add Z sherpa v22  and eos directory for prod20, thompson

## 16-02-14
* CxAODReader\_VHbb : fix in setup of random number in trigger tool, cmaiani
* CxAODReader\_VHbb : update to 0lepton selection, update 0lepton cutflow, cpandini
* FrameworkExe : default configuration for inputs 0Lepton (mc15a) - see here for list of modeling systematics CorrsAndSysts, cpandini
* FrameworkExe : updated list of experimental systematics in default config framework-read.cfg, cpandini

## 16-02-15
* CxAODReader\_VHbb : fix for yield file, cmaiani

## 16-02-16
* CxAODTools: fixed Sherpa sample MC/MC SF name in BTaggingTool, jhetherl
* FrameworkExe: added splitter macro used to prepare inputs for VH analysis, cmaiani
* FrameworkExe: improved input folder setup, cmaiani
* FrameworkExe: small fix split macro for mc15b samples, cmaiani

## 16-02-17
* CxAODTools: updated to new CDI version, jhetherl
* FrameworkExe: add low pt muon syst to list, assume v20 is now the default, hanar
* FrameworkExe: correct comments; set applyVarOR to true, hanar
* FrameworkExe: removed SysVVJetPDFAlphaPt (if needed apply directly in the fit - it's flat), cpandini
* FrameworkSub: add bbA(Zh) samples and Sherpa v2.2 Zee+Zmumu jets, thompson

## 16-02-18
*  CxAODReader: Changes in HistNameSvc to be able to assign flavor labels (bb, bc, bl etc) to Madgraph and Sherpa v2.2 samples, sargyrop
*  CxAODReader\_VHbb:  comment not used line - 0lepton selection, cpandini
*  CxAODReader\_VHbb:  fix tlorentzvector typo, cpandini
*  CxAODReader\_VHbb:  mVH definition in 0lepton with pT(dijet), cpandini
*  CxAODTools: changing error messages..., arnaez
*  FrameworkExe: Added script to merge XSection files based on MC15a/MC15b input., fmueller
*  FrameworkExe: Added script to sort CxAOD samples in MC15a/MC15b with different options (mv, cp, xrdcp, ln -s), fmueller
*  FrameworkSub: Adding xsec for 343500 (bbA220), sargyrop
*  FrameworkSub: Update Zvv k-factor 0.9376->0.9144, thompson
*  FrameworkSub: updating yields, amontalb

## 16-02-19
* CxAODReader\_VHbb: added plots needed for AZh inputs in boosted 0L analysis, cmaiani
* CxAODReader\_VHbb: fix for diboson systematic CSysVVJetScalePtST2, cpandini
* CxAODReader\_VHbb: variables for postfit plots 0lepton -resolved, cpandini
* CxAODTools\_VHbb: Fix bug in trackJetPreSelector for VBFHbbEvtSelection, prose
* FrameworkExe: adding bbA samples to prepare new inputs prod for AZh, fix of some missing default samples in the config file, cmaiani
* FrameworkExe: copy all V+jets Sherpa22 samples. Copy bbA fullsim to bbA\_fs, thompson
* FrameworkExe: update theory syst names, cpandini
* FrameworkSub: update yields, amontalb

## 16-02-20
* CxAODReader\_VHbb: 2Lep: additional distributions for postfit plots and reduced binning, sargyrop
* FrameworkSub: Replaced tag p2425 by 2436 for missing derivations., fmueller

## 16-02-22
* CxAODReader\_VHbb: 2Lep minor change: fill dPhiBB with absolute dPhiBB, sargyrop
* CxAODTools: made explicit ERROR messages for not finding MC/MC SF in BTaggingTool, jhetherl

## 16-02-23
* CxAODReader\_VHbb: remove trigger cut, lshi
* FrameworkExe: update vbfa sample naming conventions in Reader, lshi
* FrameworkExe: updating the Split Function to include the new ttbar systematics, francav
* FrameworkExe: updating the V+jets systematics, francav
* FrameworkSub: add yields for new vbfa mc15b samples, lshi
* FrameworkSub: recovering one run, fsforza
* FrameworkSub: update HIGG5D3 MC lists to include new 25ns vbfa samples, lshi
* FrameworkSub: update HIGG5D3 data lists to latest derivation, lshi
* FrameworkSub: update xsec for new vbfa mc15b samples, lshi

## 16-02-25
* CxAODMaker: changed private functions to protected, tnobe
* CxAODTools: patched Herwig++ MC/MC SF in BTaggingTool, jhetherl

## 16-02-26
* CxAODMaker: changes necessary for bbtautau analysis. Changes to allow MET calculation after selection, btagging in JetHandler, adding electron trigger SF,, updates to TauHandler and trigger list., agbet
* CxAODTools: adding props, custom OR for bbtautau and allowing flexibility in the event selection, agbet
* CxAODTools: finally fixed MC/MC SF indexing issue in BTaggingTool, jhetherl
* FrameworkSub: Add Sherpa v2.2 Znunu, thompson

## 16-02-28
* CxAODMaker: changed from copy to copyIfExists for isBJet in JetHandler since isBJet is not set in JetHandler, grkeren
* CxAODTools: added m\_applyHHbbtautauOR to initializer list with default value set to false, grkeren

## 16-02-29
* CxAODMaker, CxAODTools: add photon author and OQ, lshi
* FrameworkSub: adding bbA missing XS mA=380,460GeV, cpandini
* FrameworkSub: fix Sherpa v22 cross sections, k-factors etc., add Ztautau more updates likely, including W+jets, thompson

## 16-03-01
* CxAODMaker : Fixed bug on TruthWZ match to jet and fatJet; bool DR -> double DR, abuzatu
* CxAODTools : Adding matchHLT_tau80_medium1_tracktwo_L1TAU60 flag to common props, carquin

## 16-03-03
* CxAODMaker : check duplicates for systematics, fix memory leak problem in JIRA CxAOD-200, lshi
* CxAODReader : removing mc15b flag because v20 1lep now exists, amontalb
* CxAODTools : adding new analysis type for dilep ttbar b-tag calibration, miochoa

## 16-03-04
* CxAODReader_VHbb : removing mc15b flag because v20 1lep now exists, amontalb
* CxAODTools : debug bbtautau OR, agbet

## 16-03-07
* CxAODMaker : Added new PtReco estimation more stats and improved binning, abuzatu
* CxAODMaker : Remove old PtReco files used for Moriond, abuzatu
* CxAODMaker : Update new PtReco, abuzatu
* CxAODReader_VHbb : Appended getJetCorrTLV to be able to retrieve the Nominal as well, abuzatu
* FrameworkExe : fixes in namings of some samples, cmaiani

## 16-03-08
* CxAODMaker : Moved the JetRegression helpers JetRegressionVarHelper.h and JetRegressionVars_t.h from CxAODMaker/Root/ to CxAODMaker/CxAODMaker/ and adapted the includes in JetRegression.h accordingly, eschopf
* CxAODMaker : Updated Jet CP from JES_MC15Prerecommendation_April2015.config to JES_2015dataset_recommendation_Feb2016.config, abuzatu
* CxAODReader_VHbb : Fixed bug in mBBJ, not filled before because bbj instead of bbjVec, abuzatu
* CxAODTools : adapted PU rew tool to interface change in the underlying CP tool, grkeren
* CxAODTools : fix to variable cone OR concerning Tau-Jet OR, grkeren
* CxAODTools : fix to variable cone OR concerning Tau-Jet OR, grkeren
* FrameworkExe : fixed Split.py macro samples naming and missing signal masses, cmaiani
* FrameworkExe : Improved configuration of sample list in the reader., fmueller
* FrameworkSub : added JetSubStructureUtils-00-02-19 as not in AnalysisBase, abuzatu
* FrameworkSub : adding HH bbtautau hadhad graviton xsections, kgrimm
* FrameworkSub : Bump release to 2.3.46, nmorange

## 16-03-09
* FrameworkExe : fixes from v20 production, thompson
* FrameworkSub : Added cross section for ttbar allhad (mtt) and RS G->hh->bbbb., fmueller
* FrameworkSub : Add Sherpa v2.2 W+jets, thompson

## 16-03-10
* CxAODReader : added lower MET bin for 2lep CUT setup, cmaiani
* CxAODReader : prepared Vpt binning for SM Hbb analysis, cmaiani
* CxAODReader_VHbb : small changes for easy setup of SM Hbb analysis, cmaiani
* CxAODTools : updated BTaggingTool with recent CDI file, jhetherl
* FrameworkExe : small updates to setup for SM Hbb analysis, added links to current sps inputs, set PUreweighting to default, cmaiani

## 16-03-11
* CxAODReader : restore using mc15b yields file if flag is set to true in config; don't override initializeIsMC in VHbb reader anylonger
, hanar
* CxAODReader_VHbb : restore using mc15b yields file if flag is set to true in config; don't override initializeIsMC in VHbb reader anylonger, hanar
* FrameworkSub : added MC list for job sumbission, chiarad
* FrameworkSub : updated data VHF list with correct STDM4 derivation, chiarad

## 16-03-12
* FrameworkSub : corrected MC list STDM4 MC15b, chiarad
* FrameworkSub : p2436 for 3 runs missing in p2425, fsforza

## 16-03-14
* CxAODMaker : add some debug output in METHandler, dbuesche

## 16-03-15
* CxAODMaker_VHbb : updated JVT cut to follow latest recommendation, grkeren
* CxAODTools : fix truth tagging code for other strategies; not validated, hanar
* CxAODTools : fix truth tagging code for other strategies; not validated, hanar
* FrameworkSub : Added in addtional H->mumu cross sections and included gg->ZH in the qq->ZH as there will not be a dedicated sample, amehta
* FrameworkSub : fix duplicate for noosted Sherpa v2.2 Ztautau, thompson

## 16-03-17
* CxAODReader : fixed pTV binning for SM analysis in HistNameSvc, cmaiani
* FrameworkSub : updated yields VHF for new CxAOD production, chiarad

## 16-03-18
* CxAODReader_VHbb : added full cutflow histogram for 0-lep SM VHbb analysis, cmaiani
* CxAODReader_VHbb : adding plots for VHbb 0-lep Resolved analysis, small fix to 0-lep res cutflow, cmaiani

## 16-03-19
* FrameworkSub : updated yields because of Wlnu problem, chiarad

## 16-03-20
* FrameworkSub : updated VHF yileds for mc15b, chiarad

## 16-03-21
* CxAODMaker : add truth event, khramov
* CxAODReader_VHbb : 0-lep SM analysis: fixed muon-in-jet correction for 2LeadingSignal b-tag strategy, cmaiani

## 16-03-22
* FrameworkSub : Some Sherpa v22 W samples had old filter efficiencies and k-factor, thompson

## 16-03-23
* CxAODReader_VHbb : small fix to fill mBB with corrected value in 0-lep resolved, cmaiani

## 16-03-24
* CorrsAndSysts : EFT VpT reweighting for SM VH signals added as VpT corrections, cpandini
* CxAODMaker : adding JVT systematics, miochoa
* CxAODReader_VHbb : EFT VpT reweighting for SM VH signals added as VpT corrections in applyCS() function - CorrsAndSysts interface, cpandini
* CxAODReader_VHbb : vpt truth splitting for the SM signals in the 0 lept, changqia
* CxAODTools : adding new JVT decorators for jets, miochoa
* FrameworkExe : EFT VpT reweighting for SM VH signals added as VpT corrections in applyCS() function - CorrsAndSysts interface, cpandini
* FrameworkSub : updated VHF yields with missing WenuC file, chiarad

## 16-03-29
* CxAODMaker : Fixed heavy flavour ghosted-association (using parent, ungroommed jet), added ghost-associated higgs boson., fmueller

## 16-03-30
* CxAODTools : updated for FlatBEff in BTaggingTool, jhetherl

## 16-04-01
* FrameworkSub : updated SM VHF yields with missing 4 derivations, chiarad

## 16-04-04
* CxAODMaker : update tightLH to v10, with eff loss fix, lulu

## 16-04-05
* FrameworkSub : adding Alpgen STDM derivations for inclusive samples, fsforza

## 16-04-07
* CxAODReader_VHbb : Implementing mcPeriod string for switching between mc15a/b/c, sargyrop
* CxAODTools : Implementing mcPeriod string for switching between mc15a/b/c, sargyrop
* FrameworkExe : Implementing mcPeriod string for switching between mc15a/b/c, sargyrop
* FrameworkExe : updating Tuple calls, keeping as default as FALSE, arturos

## 16-04-08
* FrameworkExe : Adding mcPeriod to framework-run.cfg, sargyrop

## 16-04-10
* FrameworkExe : Re-introducing option to run over specific files in Reader executable, sargyrop

## 16-04-11
* CxAODMaker_VHbb : Updating VBF+photon signal photon selection: raise pT threshol to 26 GeV and require TightCaloOnlyIso, prose
* CxAODReader_VHbb : Added KinematicFit for 2 lepton, ckato
* CxAODReader_VHbb : add Run1 mva for 0lep, changqia
* CxAODTools : updated common properties for newly introduced variables in V+HF analysis: topoetcone30 and 40 for electron isolation, chiarad
* FrameworkSub : Added KinematicFit trunk, ckato

## 16-04-12
* CxAODMaker_VHbb : adding in topoetcone variables, amontalb
* CxAODReader_VHbb : KF monitor hist binning 1->5 GeV, ckato

## 16-04-13
* CxAODReader_VHbb : adding preliminary 0-lepton SM VH tmva training macro, cdelport
* CxAODReader_VHbb : Add MVA inputs for the 0 lepton channel, cdelport

## 16-04-14
* CxAODMaker : adding trigerSF e17 for LooseIso, agbet
* CxAODReader_VHbb : added an external function for some truth studies in 0-lep channel, cmaiani
* CxAODReader_VHbb : removed MPT cut from 2 tag in 0-lep, fixed the cutflow accordingly, cmaiani
* CxAODReader_VHbb : small fix to mpt change, cmaiani
* CxAODTools : add trigger SF e17 IsoLoose prop, agbet
* FrameworkSub : updating 0lepton yield files, cmaiani

## 16-04-18
* CxAODMaker : fix the EventNumber type, changqia
* CxAODReader : fix the EventNumber type, changqia
* CxAODReader_VHbb : fix the EventNumber type, changqia
* FrameworkExe : Implementing modelType flag (possible values for now AZh, HVT) to allow to change between different analyses in AnalysisReader_VHbb, sargyrop

## 16-04-19
* CxAODReader : Container for truthParticles added., cvittori
* CxAODTools : Container for truthParticles added., cvittori
* FrameworkSub : list of packages to svn co corrected, cvittori
* FrameworkSub : revert previous commit to generic setu, fsforza

	## 16-04-20
* FrameworkSub : Adding improved Sherpa diboson samples (mc15b), carquin
* FrameworkSub : add VV_improved, ckato

## 16-04-21
* CxAODReader : Major update of the 1-lepton code in AnalysisReader_VHbb., fmueller
* CxAODReader_VHbb : Major update of the 1-lepton code in AnalysisReader_VHbb., fmueller
* CxAODTools : add resolution property, ckato
* FrameworkExe : Binding call to AnalysisReader_BoostedVHbb with 0lep analysis - a more elegant fix should be made after the framework discussion, sargyrop
* FrameworkSub : Add Sherpa DY, gwilliam
* FrameworkSub : Erase 1 of 2 existing VV_improved afetr asking carquin. Ami says 361091 cross section is .024885, ckato

## 16-04-22
* CxAODMaker : add resolution variavle if doResolution=true in the config file, ckato

## 16-04-25
* CxAODMaker : copy systematics variations of pileup weight to output CxAOD, grkeren
* CxAODMaker : fixed compiler warnings for missing 'override's, grkeren
* CxAODMaker : fix names of MET systematics in OverlapRegister, grkeren
* CxAODReader_VHbb : Introducing modelType options in 2lep analysis with the possibility of switching between AZh and HVT analyses., sargyrop
* CxAODTools : Added new btagging strategy. cf. BTaggingTool::truth_tag_jets and the functions it calls, stchan
* CxAODTools : added pileup systematics and switch to set 'DefaultChannel', grkeren
* FrameworkSub : Bump to 2.3.48, nmorange

## 16-04-25
* CxAODMaker : copy systematics variations of pileup weight to output CxAOD, grkeren
* CxAODMaker : fixed compiler warnings for missing 'override's, grkeren
* CxAODMaker : fix names of MET systematics in OverlapRegister, grkeren
* CxAODReader_VHbb : Introducing modelType options in 2lep analysis with the possibility of switching between AZh and HVT analyses., sargyrop
* CxAODTools : Added new btagging strategy. cf. BTaggingTool::truth_tag_jets and the functions it calls, stchan
* CxAODTools : added pileup systematics and switch to set 'DefaultChannel', grkeren
* CxAODTools : fix for OverlapRgister dictionary generation pulled from devbranch, haysjm
* CxAODTools : Replaced BTagging::count with STL std::count; Note: for reader to run truth tagging must also be performed on track jets (uncomment e.g. l. 3082 in CxAODReader_VHbb/Root/AnalysisReader_VHbb.cxx, stchan
* FrameworkSub : Bump to 2.3.48, nmorange

## 16-04-26
* CxAODMaker : new default JES config files for fat jets, hanar
* CxAODMaker : Updating electron and muon trigger matching to new tool, amontalb
* CxAODReader_VHbb : new KF inetrface, ckato
* FrameworkExe : switched off PU systs until they are in working order, grkeren
* FrameworkExe : update JES config files and systematics for fat jets, hanar
* FrameworkSub : Add bbtautau 2HDM samples (lephad), gwilliam

## 16-04-27
* CxAODMaker : removing TrigEgammaMatchingTool and TrigMuonMatching dependencies, amontalb
* CxAODMaker : update photon trigger matching to new tool, lshi
* CxAODReader_VHbb : fixes to 0-lep plots filling for SM analysis, small changes in MVA tree, cmaiani
* CxAODTools : added check of return code when resetting systematics, grkeren
* CxAODTools : fixed printouts in PUReweightingTool, grkeren
* FrameworkExe : disabling doPUsysts again - will investigate further..., grkeren
* FrameworkExe : enabling PU systematics again, grkeren
* FrameworkExe : enabling pu systs after fixing pu tool, grkeren
* FrameworkExe : return to proper default, hanar

## 16-04-28
* CxAODMaker : Adding 'setAllObjectsFail()' to OverlapRemover.  This is used instead of 'removeOverlap()' for the vbf+photon analysis when there is no primary vertex, since the nominal overlap removal fails in these cases, prose
* CxAODMaker_VHbb : Adding isBTag decoration to isVBF(Signal)Jets, which is needed to give preference to b-tagged jets in the OR, prose
* CxAODReader : Adding 'get_analysisType()' to HistNameSvc.h which had been used in AnalysisReader_VHbb, but not yet implemented here, prose
* CxAODReader_VHbb : add HT soft calculation to analysisreader_vbfhbb, prose
* CxAODReader_VHbb : adding additional per-channel classes, to progressively replace the AnalysisReader_VHbb fill methods, cmaiani
* CxAODReader_VHbb : fix a typo for jet width for vbf+photon, lshi
* CxAODReader_VHbb : Removing printf debug statements from HT soft calculation for vbf + photon, prose
* CxAODReader_VHbb : updates to reader to support ht soft for vbf + photon, prose
* CxAODTools : Updating vbf+photon OR procedure to use the new OR recommendations and tool, prose
* FrameworkExe : adding additional per-channel classes, to progressively replace the AnalysisReader_VHbb fill methods, in the main function, cmaiani
* FrameworkExe : preparation for 2.4.X; xAOD access mode is set to _class to avoid crash, tnobe
* FrameworkExe : revise back to branch access. it is safe after p2613, tnobe
* FrameworkSub : Bump to 2.3.49, nmorange

## 16-04-29
* CxAODMaker_VHbb : update WHsignal lepton qualities, amontalb

## 16-04-30
* CxAODTools : Updated BTaggingTool truth tagging---untagged jets now get continuous b-tag weight (e.g. MV2c20J3 now possible with truth tagging), stchan

## 16-05-01
* CxAODReader_VHbb : new KF interface, ckato
* CxAODReader_VHbb : new KF interface, ckato
* CxAODReader_VHbb : new KF interface, ckato

## 16-05-03
* FrameworkSub : Added JetSubStructureMomentTools-00-01-26, as in AnalysisBase 2.3.49 we have -23, abuzatu
* FrameworkSub : Added JetUncertainties-00-09-40, as in AnalysisBase 2.3.49 we have -39, abuzatu

## 16-05-03
* CxAODMaker : adapted to change in interface of OverlapRegisterAccessor which includes adding fatjets, grkeren
* CxAODMaker : =add new MET defs, schae
* CxAODMaker : add TA mass and ElClusterEta, tnobe
* CxAODMaker : add TA mass and ElClusterEta, tnobe
* CxAODMaker : =fix MET crash for MC, schae
* CxAODMaker : for jet corrections store correction minus nominal, instead of the correction 4-vector, abuzatu
* CxAODMaker : increased msg level of calib tool to error to silence the tool when jets are not decorated with 'TrackSumMass', added checks to see if Track Assisted Mass variables exist before decoratingand copying them, grkeren
* CxAODReader : Reader to get jet energy corrections from difference with respect to Nominal, abuzatu
* CxAODReader : Reader to get jet energy corrections from difference with respect to Nominal, abuzatu
* CxAODReader_VHbb : Reader to get jet energy corrections from difference with respect to Nominal, abuzatu
* CxAODReader_VHbb : Reader to get jet energy corrections from difference with respect to Nominal, abuzatu
* CxAODTools : =add btag as an overlap option, schae
* CxAODTools : =add new MET defs, schae
* CxAODTools : add TA mass and ElClusterEta, tnobe
* CxAODTools : updated OverlapRegister to include fatjets - includes change of interface in OverlapRegisterAccessor, grkeren
* FrameworkExe : Reader to get jet energy corrections from difference with respect to Nominal, abuzatu
* FrameworkSub : Added JetSubStructureMomentTools-00-01-26, as in AnalysisBase 2.3.49 we have -23, abuzatu
* FrameworkSub : Added JetUncertainties-00-09-40, as in AnalysisBase 2.3.49 we have -39, abuzatu

## 16-05-04
* CxAODReader : Added OverlapRegister to Reader, can be switched on/off with 'bool useOverlapRegister = true/false' in config file, with default value being 'false' for now, still needs to be tested, grkeren
* CxAODTools : added 'const' in front of xAOD containers in OverlapRegisterAccessor to allow usage in Reader, grkeren
* CxAODTools : Add Props to store properties of Overlap Removed jet closest to tau for HHbbtt analysis, thsteven
* FrameworkSub : add temporary mc15c pile-up file done from mc15_13TeV.410022.Sherpa_CT10_ttbar_SingleLeptonP_MEPS_NLO.merge.DAOD_HIGG5D1.e3959_a766_a818_r7676_p2613, djamin

## 16-05-05
* CxAODMaker : reduced the trigger list, agbet
* CxAODTools : Add Props for MMC 4vect for HHbbtt analysis, thsteven

## 16-05-07
* CxAODMaker : Adding option to store low pt track jets via config item 'TrackJet::UseLowPt', prose

## 16-05-09
* CxAODTools : updated instructions for OverlapRegisterAccessor, grkeren

## 16-05-10
* CxAODMaker : added nr of truth jets in MC, abuzatu
* CxAODMaker : checked event cleaning - up to date, hanar
* CxAODMaker : =depricating the flag writeFlagForEleMuOR. Now set by applyNewToolOR, schae
* CxAODMaker_VHbb : added nr of truth jets in MC, abuzatu
* CxAODReader : added nr of truth jets in MC, abuzatu
* CxAODReader_VHbb : added nr of truth jets in MC, abuzatu
* CxAODTools : added nr of truth jets in MC, abuzatu
* CxAODTools : =add option applyNewToolOR to use the new overlap removal tool. defaulted to off, schae
* CxAODTools : =depricating the flag writeFlagForEleMuOR. Now set by applyNewToolOR, schae
* CxAODTools : update jet cleaning to latest recommendation, hanar
* CxAODTools_VHbb : added nr of truth jets in MC, abuzatu
* FrameworkExe : added nr of truth jets in MC, abuzatu
* FrameworkExe : =add flag for the new overlap removal. defaulted to off, schae
* FrameworkExe : =depricating the flag writeFlagForEleMuOR. Now set by applyNewToolOR, schae

## 16-05-11
* CxAODMaker : 30 GeV instead of 20 GeV for nr truth jets MC, abuzatu
* CxAODMaker : add 2016 MET triggers to Maker, wangwe
* CxAODMaker : add m_derivation20_7 flag to compute properly isMC and deal with bookkeeping, djamin
* CxAODMaker : =add met soft term, schae
* CxAODMaker : fix to duplicated fat jet systematics, grkeren
* CxAODMaker : =register the MJ MET definitions, schae
* CxAODMaker : Reverted back to 20 GeV, recommendation Paul Thompson., abuzatu
* CxAODMaker_VHbb : =register the MJ MET definitions, schae
* CxAODMaker_VHbb : updating WH signal lepton isolation definitions, amontalb
* CxAODReader_VHbb : 2LEP MAJOR CHANGE: move to per-channel class implementation, hanar
* CxAODReader_VHbb : 2lep: move methods to per-channel class, hanar
* CxAODReader_VHbb : fixed small bug introduced in 0lep code, cmaiani
* CxAODReader_VHbb : merged HVT and AZH/SM code for 0-lepton channel, cmaiani
* CxAODReader_VHbb : small fixes to work with HVT in new 0-lep code, cmaiani
* CxAODTools : add 2016 MET triggers to Maker, wangwe
* CxAODTools : fix truth tagging weight for Leading2SignalJets, zaidan
* CxAODTools_VHbb : fixing typo, amontalb
* CxAODTools_VHbb : update lepton SFs to new definitions and include switch for inverted isolation SFs, amontalb
* FrameworkExe : add mc15c pu file, djamin
* FrameworkExe : =add MET MJ defs. set off by default, schae
* FrameworkExe : =add met soft term, schae
* FrameworkExe : merged HVT and AZH/SM code for 0-lepton channel, boosted class is not used anymore, cmaiani
* FrameworkExe : set jetCorrectionOld to true to work with CxAOD-20 production; remove private path replace with eos; go to 2 lep and mc15b - working plus consistent, hanar
* FrameworkExe : use ttbar as test sample, hanar

## 16-05-12
* CxAODMaker : add 2016 lepton triggers 0.5-1.2, ckato
* CxAODMaker : add 2016 lepton triggers 0.5-1.2, ckato
* CxAODMaker : Add HLT_mu24_ivarloose_L1MU15 because mu24 without _L1MU15 was not in 20.7 ttbar 410022 p2613 HOGG2D4, ckato
* CxAODMaker : Add HLT_mu24_ivarloose_L1MU15 because mu24 without _L1MU15 was not in 20.7 ttbar 410022 p2613 HOGG2D4, ckato
* CxAODMaker : add more MET triggers for study, wangwe
* CxAODMaker : For data, do not compute and store nr TruthJets, abuzatu
* CxAODMaker : removing compilation warnings: inizialization order and using  ClassDefOverride, fsforza
* CxAODMaker : Storing nr TruthWZ for 20 and 30 GeV instead of only 20 GeV., abuzatu
* CxAODReader : =flags for MET recalculation & reading OR labels, schae
* CxAODReader : removing compilation warnings: using  ClassDefOverride, fsforza
* CxAODReader : truth selection, cvittori
* CxAODReader_VHbb : 1lep: fix small bug, hanar
* CxAODReader_VHbb : 2lep: move KF stuff to method; clean-up, hanar
* CxAODReader_VHbb : creating isSL property for jets; moving setting it to setJetVariables; some cleaning up, hanar
* CxAODReader_VHbb : revert previous change by Stephen J who is aware, hanar
* CxAODReader_VHbb : Version 0 SM VH & HVT Merge, sjiggins
* CxAODReader_VHbb : Version 0 SM VH & HVT Merge, sjiggins
* CxAODTools : add 2016 lepton triggers 0.5-1.2, ckato
* CxAODTools : Add HLT_mu24_ivarloose_L1MU15 because mu24 without _L1MU15 was not in 20.7 ttbar 410022 p2613 HOGG2D4, ckato
* CxAODTools : Adding variables for truth selection at dressed level and SelectionContainers for truth objects, cvittori
* CxAODTools : add more MET triggers for study, wangwe
* CxAODTools : =add tool for reader level MET changes, schae
* CxAODTools : created by mistake, alibrari
* CxAODTools : removing compilation warnings: inizialization order and using  ClassDefOverride, fsforza
* CxAODTools : removing contents of extra trunk, haysjm
* CxAODTools : Storing nr TruthWZ for 20 and 30 GeV instead of only 20 GeV., abuzatu
* CxAODTools : =turn writing share track flag off when reading it, schae
* FrameworkExe : 2lep: missing piece when moving to per-channel class, hanar
* FrameworkExe : Updated to GRL for 20.7, abuzatu
* FrameworkExe : Updated to GRL for 20.7, abuzatu
* FrameworkSub : 2015 GRL with 20.7, tnobe
* FrameworkSub : 2015 GRL with 20.7, tnobe
* FrameworkSub : update ilumicalc file, tnobe

## 16-05-13
* CxAODMaker : added 2016 triggers for matching, amontalb
* CxAODMaker : Added fat jet properties to store number of ghost-associated B- and prompt C-Hadrons, Taus and Higgs-Bosons for the ungroomed jet., fmueller
* CxAODMaker : adding 2016 single lepton triggers for matching, amontalb
* CxAODMaker : adding quality flags, fsforza
* CxAODMaker : add MV2c100 and MV2cl100 tagger, lulu
* CxAODMaker : add new VBF+photon triggers for data16 and mc15c, lshi
* CxAODMaker : exception to not write out MJ MET for systematics, amontalb
* CxAODMaker : fix compiler warning, hanar
* CxAODMaker : removing cut-based ele selector, fsforza
* CxAODMaker : removing dilepton triggers from matching list, amontalb
* CxAODMaker : removing electron triggers based on run1 cuts, amontalb
* CxAODMaker : Updated jesConfig to Moriond recommendation, abuzatu
* CxAODMaker_VHbb : adding back in mediumLH/tightLH props for electrons, amontalb
* CxAODMaker_VHbb : remove compiler warning: adding override, fsforza
* CxAODMaker_VHbb : removing LH props for electrons; present in handler, amontalb
* CxAODReader : added temporary fix in form of the method applyRtrkUncertFix() in AnalysisReader for bug in fat jet Rtrk uncertainties, grkeren
* CxAODReader : cleaning up HistNameSvc settings, hanar
* CxAODReader : =read met soft term, schae
* CxAODReader : small modification so that no changes for non-VH analyses are needed, hanar
* CxAODReader : upload HistNameSvc changes; CXAOD-221, hanar
* CxAODReader_VHbb : 0lep: adapt to HistNameSvc changes; CXAOD-221, hanar
* CxAODReader_VHbb : 0lep: adapt to HistNameSvc changes; CXAOD-221, hanar
* CxAODReader_VHbb : 2lep: adapt to HistNameSvc changes; CXAOD-221, hanar
* CxAODReader_VHbb : 2lep: some more cleaning on hist naming, hanar
* CxAODReader_VHbb : add MVA to model enum, hanar
* CxAODReader_VHbb : cleaned up 0lep code, removed unwanted warnings, cmaiani
* CxAODReader_VHbb : fixes for compiler warnings in AnalysisReader_VBFHbb, prose
* CxAODReader_VHbb : remove compiler warning: adding override, fsforza
* CxAODReader_VHbb : removed vvqq and lvqq code (1), cmaiani
* CxAODReader_VHbb : set other model types too; remove restriction of HVT analysis to merged regime, hanar
* CxAODReader_VHbb : small fixes related to 0lep, removing boosted 0lep class, cmaiani
* CxAODReader_VHbb : VBF: adapt to HistNameSvc changes; CXAOD-221, hanar
* CxAODTools : Added fat jet properties to store number of ghost-associated B- and prompt C-Hadrons, Taus and Higgs-Bosons for the ungroomed jet., fmueller
* CxAODTools : adding 2016 trigger matching props, amontalb
* CxAODTools : add MV2c100 and MV2cl100, lulu
* CxAODTools : add new VBF+photon triggers for data16 and mc15c, lshi
* CxAODTools : no need to set default channel number for PU rew anylonger; correct one gets picked up via mcPeriod; functionality still persists though, hanar
* CxAODTools : =read met soft term, schae
* CxAODTools : removed vvqq and lvqq code (3), cmaiani
* CxAODTools : removing dilepton triggers matching props, amontalb
* CxAODTools_VHbb : Commenting out unused passTrigger(Pre)Selection in VBFHbbEvtSelection to fix compiler warnings, prose
* CxAODTools_VHbb : removed vvqq and lvqq code (2), cmaiani
* CxAODTools_VHbb : tightening CxAOD event preselection: ask for at least 2 signal jets; CXAOD-232, hanar
* FrameworkExe : added diboson improved samples to list, added new namings to the HVT Split macro, cmaiani
* FrameworkExe : cleaned up config file, removing 0-lep outdated flags, cmaiani
* FrameworkExe : for running MJ template with inverted isolation, amontalb
* FrameworkExe : no need to set default channel number for PU rew anylonger; correct one gets picked up via mcPeriod; functionality still persists though, hanar
* FrameworkExe : turned on new OR by default in config, haysjm
* FrameworkExe : updated framework-run-MJ.cfg with changes also made to nominal config file, haysjm
* FrameworkExe : update JES uncertainty config, tnobe
* FrameworkSub : added diboson improved to mc15b 0lep yields file, cmaiani
* FrameworkSub : added missing KinematicFit from packages file, haysjm
* FrameworkSub : adding Alpgen V+HF slices, STDM derivations are now complete, fsforza
* FrameworkSub : adding the data, and resolving some double counting of samples, francav
* FrameworkSub : adding the list for 20.7 MC15c with the available samples, francav
* FrameworkSub : updated tag packages and release, haysjm

## 16-05-14
* CxAODMaker : Added debug statements for Regression derivation; warning in data 20.7 at least the correction factor from Regression is exactly 1, abuzatu
* CxAODMaker : Changed 4-vec of jet corrections to MeV from GeV, to be consistent with jet Nominal, but also to Muons, other objects, abuzatu
* CxAODMaker : It was a false alarm; b-jet energy corrections were in MeV; just we were storing the difference to Nominal, that is why they had small values; added more debug statements about these corrections, abuzatu
* CxAODMaker : pulling pv fix from devbranch - allows protection against missing PV, haysjm

## 16-05-15
* CxAODReader : Updating CxAODTools to enable AnalysisReader_Vhbb1lep.cxx, sjiggins
* CxAODReader_VHbb : Updating CxAODReader_VHbb to enable AnalysisReader_Vhbb1lep.cxx, sjiggins
* CxAODTools : Updating CxAODTools to enable AnalysisReader_Vhbb1lep.cxx, sjiggins
* CxAODTools_VHbb : Updating CxAODTools_VHbb to enable AnalysisReader_Vhbb1lep.cxx, sjiggins
* FrameworkExe : more config changes, haysjm
* FrameworkExe : updated config file with update to tag, haysjm
* FrameworkExe : updated default vtag, haysjm
* FrameworkExe : updated mcperiod to mc15c, haysjm
* FrameworkSub : fixed packages file for r20.1, haysjm
* FrameworkSub : fixed tag of ElectronEfficiencyCorrection, haysjm
* FrameworkSub : prep for tag v21-2, haysjm
* FrameworkSub : updated FrameworkExe tag, haysjm
* FrameworkSub : updated mcperiod in default config file, haysjm

## 16-05-16
* CxAODMaker : added TruthElectrons/Muons/Neutrinos Handlers for dressed truth-analysis, fsforza
* CxAODMaker : Removed the argument of applyJetRegression() since it is not needed anymore and caused a compiler warning, eschopf
* CxAODMaker : Removing old weight files of the jet regression, eschopf
* CxAODReader_VHbb : move the 1 lepton code to pre channel class, yama
* FrameworkExe : move the 1 lepton code to pre channel class, yama

## 16-05-17
* FrameworkSub : updated STDM4 MC list with missing sherpa 2.2 derivations, chiarad

## 16-05-17
* CorrsAndSysts : correct array sizes in CorrsAndSysts, haysjm
* CorrsAndSysts : fixed compiler warnings, haysjm
* CorrsAndSysts : missed an usused variable - now commented out, haysjm
* CxAODMaker : commented out code causing compiler warnings - will be needed in the future so not removed, haysjm
* CxAODReader_VHbb : added stephen truth tagging to 0-lep channel, cmaiani
* CxAODTools : fixed initializer ordering in TriggerTool to remove compiler warning, haysjm
* CxAODTools : update to BTaggingTool to bypass deprecated calls to getTaggerCutValueFromEfficiency, jhetherl
* FrameworkExe : added switch for stephen's truth tagging in 0-lep, cmaiani
* FrameworkExe : fixed warnings about deprecated use of scanDir and setMetaString, haysjm
* TupleMaker : fixed some incorrect includes and updated scanDir etc to remove compielr warnings, haysjm

## 16-05-18
* CxAODMaker : copyIfExists for NTruthWZJets20., agbet
* CxAODReader_VHbb : 2Lep: move regime decision to method, hanar
* CxAODReader_VHbb : added code to read xml in 0 lep, from Charles, cmaiani
* FrameworkSub : - added some XSec for the had-had parts, hfox

## 16-05-19
* CxAODMaker : Add ability to vary lower anti-tau BDT cut as a systematic, gwilliam
* CxAODMaker : Add TAU efficiencies to list of those for event info, gwilliam
* CxAODMaker : forgot to add truth handler getters in selection, fsforza
* CxAODReader_VHbb : Bug fix for 2lep: clear histogram description early in the code. Since the region is initialized to SR and the if statements are incomplete, this led to events being categorized as SR while they weren't passing the SR cuts, sargyrop
* CxAODTools : BDTCut syst, gwilliam
* FrameworkExe : Added Powheg Herwig++ Diboson samples for systematics, with PwHerwigppEGnloME, abuzatu
* FrameworkExe : add possibility to configure queue, hanar
* FrameworkExe : add queue setting for LSF driver; add mc15c PU file, hanar
* FrameworkExe : Arranged output in nice columns, abuzatu
* FrameworkSub : latest 2lep yields file, hanar
* FrameworkSub : latest 2lep yields file (mc15a), hanar

## 16-05-20
* CxAODReader_VHbb : 2Lep Reader: Update flavor labeling for fat-jets. Use heaviest flavor to categorize fat-jet when using only 1 flavor label (Zb,Zc,Zl). Previously the leading track-jet flavor was used. For the moment use this for HVT model, and use 2 labels for AZh model. Option to be reconsidered, sargyrop
* CxAODReader_VHbb : update vbf+photon BDT weight files: 15 vars, mc15b CxAOD April production, Reader21-01 + mjj>800 + passVBF18 + pTBB>100, lshi
* FrameworkExe : Added separated _improved for dibosons, for ex WW_improved, same WZ, and ZZ., abuzatu
* FrameworkExe : updated plotting macro for 0lep: adding sensitivity computation, correct reading of sys from one folder, blinding, ..., cmaiani
* FrameworkExe : Updated to 00-21-03 default values, abuzatu

## 16-05-23
* FrameworkExe : Switch to class access mode when running tuplemaker. Needed for systematics, thsteven
* TupleMaker : Fix loop over systematics in Tuplemaker to pass variations struct correctly, thsteven
* TupleMaker : Fix systematics for TupleMaker and add functionality to include event level selection, thsteven
* TupleMaker : Add missing files for TupleMaker, thsteven

## 16-05-24
* CxAODReader_VHbb : Update to AnalysisReader_VHbb1lep.cxx analysis code, sjiggins
* CxAODTools : Adding MET trigger for high ptW muon events for HVT (1lep is commented out), amontalb
* FrameworkExe : upload GRL for data16 and corresponding ilumicalc file, tnobe
* FrameworkSub : updated samples list mc15b VHF STDM4 with recommended diboson samples, chiarad
* FrameworkSub : upload GRL for data16 and corresponding ilumicalc file, tnobe

## 16-05-26
* CxAODReader : indent    , fsforza
* CxAODReader : MAJOR CHANGE: run ONLY NOMINAL if nominalOnly is set to true (until now b-tagging and CorrsAndSyst histos were still filled if vectors not disabled in config); make code abort if both nominalOnly and all syst options are set to false), hanar
* CxAODReader_VHbb : compute also truth tagging for fat jets even if not used; avoid code from crashing, hanar
* CxAODReader_VHbb : fix: proper commit, hanar
* CxAODReader_VHbb : MAJOR CHANGE: run ONLY NOMINAL if nominalOnly is set to true (until now b-tagging and CorrsAndSyst histos were still filled if vectors not disabled in config); make code abort if both nominalOnly and all syst options are set to false), hanar
* CxAODReader_VHbb : remove OS requirement in merged AZh analysis; resolved will follow soon, hanar
* CxAODTools : Updated truth tagging with systematics and ConfigStore callable options added--truth_tag_jets NO LONGER RETRUNS A WEIGHT; cf computeEventWeight_truthTag and Reader devbranches/stchan, stchan
* FrameworkExe : add flag to config to merge jet categories, hanar

## 16-05-27
* CxAODMaker : Fix issue with writeFlagForEleMuOR flag for VBFGamma OR, prose
* CxAODReader : Truth taggging SF handling implemented via ConfigStore, stchan
* CxAODReader_VHbb : BUG FIX: at least 2 track jets in lead fat jet for AZh, hanar
* CxAODReader_VHbb : Compilation with new truth tagging method resolved; note that compute_truthTagging for new method is DEPRECATED; use compute_TRF_tagging and new behavior of CxAODReader::computeBTagSFWeight instead, stchan
* CxAODReader_VHbb : Fixed bug for direct tagging case (compute_btagging() wasn't enabled in the 2lep example), stchan
* CxAODReader_VHbb : TEMPORARY FIX to remove compiler error..., hanar

## 16-05-29
* FrameworkSub : Updated to ICHEP recommendations JetCalibTools-00-04-66 and JetUncertainties-00-09-42, abuzatu

## 16-05-30
* CxAODMaker : update MET recommendtion, tnobe
* FrameworkExe : Changed default local test sample to be mc15c ttbar to work with the default settings, abuzatu
* FrameworkSub : add METUtilities-00-02-27 for the latest MET recommendation, tnobe
* FrameworkSub : SM Vbb yields with data,top, Z and dibosons, fsforza
* FrameworkSub : Update to JetUncertainties-00-09-43, new recommendation after a bug fix, abuzatu
* KinematicFit : shorter TF name, ckato
* KinematicFit : shorter TF name, ckato

## 16-05-31
* CorrsAndSysts : CorrsAndSysts now depends on PMGTools for Sherpa v2.2 reweight, thompson
* CxAODReader : include jat jets; CXAOD-252, hanar
* CxAODReader_VHbb : add setHiggsCandidate method (only used in 2 lep so far); 2 lep: move rescaling of muons here; should move setter method to 2 lep code, hanar
* CxAODReader_VHbb : comment out KF, ckato
* CxAODReader_VHbb : introduce two new structs: Higgs and VHCand; and setter method, hanar
* CxAODReader_VHbb : restructure and clean-up code, hanar
* FrameworkSub : CorrsAndSysts now depends on PMGTools for Sherpa v2.2 reweight, thompson
* FrameworkSub : updated VHF yields to reflect current VHF-00-09 production in svn - only files missing listed in https://indico.cern.ch/event/537606/contributions/2185350/attachments/1282290/1905585/VHF_Analysis_Meeting_Introduction_20160531.pdf, chiarad
* FrameworkSub : Update to AnalysisBase 2.4.9, abuzatu

## 16-06-01
* CorrsAndSysts : fix njet reweight, thompson
* CxAODMaker : Added number of ghost-matched (prompt) C-/B-Hadrons and Higgs-Bosons to TrackJets, analogous to FatJetHandler., fmueller
* CxAODMaker : Fixing problem with infinite loops in W+b samples in IsChild method., fmueller
* CxAODReader_VHbb : move checkMbbWindow to 2 lep code; could be used by all channels but isn't..., hanar
* CxAODReader_VHbb : move checkMllCut to 2 lep code, hanar
* CxAODTools : updated to new CDI file, jhetherl
* FrameworkSub : cross sections and k-factors for ALPGEN+Pythia6 samples, inclusive and massive-HF K-factors to NNLO calculated taking into account all the samples and the HFOR(DR>0.4) efficiency By Marco Lisboa Leite and Jose La Rosa Navarro, fsforza
* FrameworkSub : removed spourious line, fsforza
* FrameworkSub : updated yields of VHF analysis to reflect full VHF-00-09 production, chiarad

## 16-06-02
* CxAODReader : add possibility to have number of subjets as additional category; default is unchanged, hanar
* CxAODReader : update set_sample function to include shape2.2 w+jets sample, yama
* CxAODReader_VHbb : add possibility to receive HVT and AZh results in one go by addind additional subjet category; default is unchanged, hanar
* CxAODReader_VHbb : move DiLeptonCuts namespace to 2 lep code, hanar

## 16-06-03
* CxAODMaker : fix bug and picking the correct SF for control region., agbet
* CxAODMaker : Providing PileupReweightingTool for MuonEfficiencyScaleFactors as required in 2.4.9., fmueller
* CxAODReader_VHbb : change HVT flavour labelling: use 2 labels if 2 track jets available, 1 if 1, hanar
* CxAODReader_VHbb : implement mass-dependent cuts; usage optional, default old cuts, hanar
* CxAODReader_VHbb : move setLeptonVariables method to 2-lep class, hanar
* CxAODReader_VHbb : move to common method for jet 4-vector correction; CXAOD-218, hanar
* CxAODTools : =fix functionality for largeR jets to old prescription, schae
* CxAODTools : Providing PileupReweightingTool for MuonEfficiencyScaleFactors as required in 2.4.9., fmueller

## 16-06-05
* CxAODReader : BUG FIX: correct retrieval of corrected jet p4 for new correction method; thanks to Chikuma for spotting; CXAOD-251, hanar
* CxAODReader : revert accidental commit, hanar
* CxAODReader_VHbb : increase mVH range up to 6000; comment unweighted histos, hanar
* CxAODReader_VHbb : test      , yama
* CxAODReader_VHbb : update 1 lepton resolved code, yama
* CxAODReader_VHbb : update 1 lepton resolved code, yama
* CxAODReader_VHbb : update namespace OneLeptonResolvedCuts, yama
* CxAODReader_VHbb : update the function of fill_1lepResolvedCutFlow, yama
* CxAODReader_VHbb : update the function of fill_TLV, yama
* FrameworkExe : update 2016 GRL, tnobe
* FrameworkSub : update 2016 GRL, tnobe

## 16-06-06
* CxAODMaker : adding 2 trigger, fixing one bug, adding muon quality in output, dimicco
* CxAODMaker : add new mET triggers, tnobe
* CxAODMaker : removing isMC check to have all the decorations, fsforza
* CxAODReader : add getter method for pTV, hanar
* CxAODReader : add long long int and vector in, hanar
* CxAODReader_VHbb : run KF for 2 jet & jet_onemu pT > 1 GeV, ckato
* CxAODTools : addinglep-jet trigger flags in Properties, dimicco
* CxAODTools : add new mET triggers, tnobe
* FrameworkExe : bool doResolution = false # true for 2 lepton, ckato
* FrameworkExe : updated OverlapRemoval flags for 21-04 production prep., haysjm
* FrameworkSub : 2 lepton mc15c yields file, copied from eos, hanar
* FrameworkSub : updated bootstrap for 21-04, haysjm

## 16-06-06
* CxAODMaker : adding 2 trigger, fixing one bug, adding muon quality in output, dimicco
* CxAODMaker : add new mET triggers, tnobe
* CxAODMaker : removing isMC check to have all the decorations, fsforza
* CxAODReader : add getter method for pTV, hanar
* CxAODReader : add long long int and vector in, hanar
* CxAODTools : addinglep-jet trigger flags in Properties, dimicco
* CxAODTools : add new mET triggers, tnobe
* FrameworkExe : bool doResolution = false # true for 2 lepton, ckato
* FrameworkExe : updated OverlapRemoval flags for 21-04 production prep., haysjm
* FrameworkSub : 2 lepton mc15c yields file, copied from eos, hanar
* FrameworkSub : updated bootstrap for 21-04, haysjm

## 16-06-07
* CxAODMaker : add 5 new electron trigger, ckato
* CxAODMaker : HLT_mu20_iloose_L1MU15 was written twice, ckato
* CxAODMaker : sort lepton triggers, ckato
* CxAODMaker : update to release 20.7 electron IDs, lulu
* CxAODTools : add 5 new electron trigger, ckato
* FrameworkSub : Adding further graviton samples., fmueller

## 16-06-08
* CorrsAndSysts : eventType for inclusive W and Z added, losterzo
* CxAODMaker : Added number of ghost-matched (prompt) C-/B-Hadrons and Higgs-Bosons to small-R Jets, analogous to FatJetHandler., fmueller
* CxAODMaker : fixing == bug in trigger map assignment, dimicco
* CxAODMaker : fixing wrong commit due to additional files in previous one, dimicco
* CxAODMaker : mu trigger for 2016, agbet
* CxAODMaker : removing useless comments, dimicco
* CxAODMaker_VHbb : JVT hard coded replaced with Props::PassJvtMedium.get(jet), abuzatu
* CxAODReader_VHbb : fix bug in opt cuts, hanar
* CxAODReader_VHbb : fixed typo, abuzatu
* CxAODReader_VHbb : Harmonized config options to be more human readable---useNewTTMethod set to true will now actually invoke the new truth tagging method in AnalysisReader_VHbb::compute_TRF_tagging, stchan
* CxAODReader_VHbb : remove debug statement, hanar
* CxAODReader_VHbb : use same definition as in HistNameSvc, hanar
* CxAODTools : flag part fo the code that is only relevant to the new tools, agbet
* CxAODTools : JVT cuts update in the initialisation of the tool, abuzatu
* CxAODTools : JVT hard coded replaced with Props::PassJvtMedium.get(jet), abuzatu
* FrameworkExe : Added the exclusiveTruthTagging bool to framework-read.cfg for truth tagging, stchan
* FrameworkSub : Bump to 2.4.10, nmorange

## 16-06-09
* CxAODMaker : adding complete selection flags, it will make easier to use muons with |eta|>2.5, fsforza
* CxAODMaker : removing failure on missing id-track, fsforza
* CxAODReader_VHbb : added reading of Charles BDT, with latest xml files, for VHbb0lep, and implemented stephen's truth tagging in 0lep code, cmaiani
* CxAODReader_VHbb : bug fix: correct mll window cuts, hanar
* CxAODReader_VHbb : bug fix: used resolved instead of merged mVH, hanar
* CxAODReader_VHbb : store resolved and merged mBB and mVH separately, hanar
* FrameworkExe : corrected minor issue in reader config file, cmaiani
* FrameworkExe : small updates in reader config file, cmaiani
* FrameworkSub : Added SM signal and some bkg samples, abuzatu
* FrameworkSub : rm packages from list that are either now in the new release or are even outdated (METUtilities), hanar
* KinematicFit : read the same PtReco file from CxAOD 20-00 moriond production, ckato

## 16-06-10
* CxAODMaker : CP updates to photon handler configs, prose
* CxAODMaker : fixing bug, fsforza
* CxAODMaker_VHbb : Added check if JvtMedium exists, abuzatu
* CxAODMaker_VHbb : update to jet decoration for vbf+photon analysis, prose
* CxAODReader : bug fix: allow to run also on weight syst only..., hanar
* CxAODReader_VHbb : Updates to Reader for VBF+photon analysis, prose
* CxAODTools : Added check if JvtMedium exists, abuzatu
* FrameworkExe : Update to support new Reader for VBF+photon analysis, prose
* FrameworkSub : updating packages-trunk for recommended package tags not included in release, prose

## 16-06-11
* CxAODMaker : muon resolution is ready, ckato
* FrameworkExe : Added scripts keepOnlyGoodRuns.py and runKeepOnlyGoodRuns.sh to avoid running on bad data runs that give zero events selected anyway, abuzatu
* FrameworkExe : add the latest 2016 GRL (2.6fb-1), tnobe
* FrameworkExe : add the latest 2016 GRL (2.6fb-1), tnobe
* FrameworkExe : Commented out systematics as not needed for test runs, to be turned on for official ICHEP production, abuzatu
* FrameworkExe : list of sherpa2.2 V+jets samples, cpandini
* FrameworkExe : remove list of sherpa2.2 V+jets samples, cpandini
* FrameworkSub : add the latest 2016 GRL (2.6fb-1), tnobe
* FrameworkSub : Commented out bad data runs from data15 samples from 13May16 using script I introduced in FrameworkExe/scripts, abuzatu
* KinematicFit : fix eta phi, ckato
* KinematicFit : TF made from CxAOD 21-04, ckato

## 16-06-13
* CxAODReader_VHbb : 2Lep Reader: cut on Ntrackjets was accidentally changed with previous commit. Undoing accidental changes, sargyrop
* CxAODReader_VHbb : 2Lep Reader: turning optimizing cuts on by default, sargyrop
* CxAODReader_VHbb : getKF called if N(jets)=N(selected_jets), ckato
* CxAODReader_VHbb : move pTB145 cut to common cuts, hanar
* CxAODReader_VHbb : Reverted changes to VHbb1lep & event selection. Spliced all changes into trunk version, sjiggins
* FrameworkSub : tag first version of PMGTools, thompson

## 16-06-14
* FrameworkSub : Bump to 2.4.11, nmorange
* CxAODMaker : Add PtReco derived in mc15c 20.7 with ICHEP recommendations. Still keep the PtReco from the trunk, introduced after Moriond. Some checks still needed to choose which one to use for ICHEP., abuzatu
* CxAODMaker : Add PtReco files retrained in 20.7 to use for ICHEP (to be confirmed), abuzatu
* CxAODMaker : add RandomRunNumber, lulu
* CxAODMaker : Compute and store EMScaleEta for jets, used in PassJvtMedium, abuzatu
* CxAODMaker : Fixed typo, abuzatu
* CxAODMaker : update electron eff SF, lulu
* CxAODReader : implemented Sherpa 2.2 Njet reweighting in analysis reader, cmaiani
* CxAODReader_VHbb : removed mbb window cut from SM VH cutflow histo filling, cmaiani
* CxAODTools : Add EMScaleEta for jets, used in PassJvtMedium, abuzatu
* CxAODTools : add RandomRunNumber, lulu
* CxAODTools : Fixed typo at parantheses in if, abuzatu
* CxAODTools : for JVT if EMScaleEta is not stored as Prop, use incorrect but ok jet->eta(), abuzatu
* CxAODTools : Removed commented lines with 50 instead of 50 and 0.64 instead of 0.59, abuzatu
* CxAODTools : updated BTaggingTool with track-jet requirements, jhetherl
* CxAODTools : Update jet cleaning JVT requirement, abuzatu
* CxAODTools : Use EMScaleEta instead of jet eta in Jvt cut, abuzatu
* CxAODTools : When hard coded to recomputed Jvt cut, updated cuts from 50 GeV to 60 GeV and form 0.64 to 0.59, abuzatu
* FrameworkExe : add instructions for CxAOD-21-xx vs CxAOD-20-xx running - default is still CxAOD-20-xx, will be changed soon, hanar
* FrameworkExe : should be set to true for CxAOD-20-xx, hanar
* FrameworkSub : JetEtMiss experts confirm we can use JetSubstructure packages from AnalysisBase 2.4.11, abuzatu
* FrameworkSub : JetEtMiss group recommends JetUncertainties-00-09-46, not yet in AB 2.4.11, abuzatu

## 16-06-15
* CxAODMaker : For fat jets too Updated JES calibration and uncertainty configuration strings for 20.7 ICHEP recommendations, abuzatu
* CxAODMaker : switch to es2015PRE for calibration, lulu
* CxAODMaker : switch to es2016PRE for calibration, lulu
* CxAODMaker : Updated JES calibration and uncertainty configuration strings for 20.7 ICHEP recommendations, abuzatu
* CxAODMaker : update to ESModel for 2016, prose
* CxAODReader : Added NNLO reweighting to reader, abell
* CxAODReader_VHbb : Added NNLO reweighting to reader, abell
* CxAODReader_VHbb : changed name of BDT variable for 0lep analysis, for fit inputs compatibility, cmaiani
* CxAODReader_VHbb : harmonize HVT and AZh selection: 1+ track jets, hanar
* FrameworkSub : Added NNLO reweighting to reader - NNLOReweighter package needs to be checked out, abell
* FrameworkSub : Update to JetUncertainties-00-09-47, abuzatu

## 16-06-16
* CxAODMaker : comment old setting: better remove completely, hanar
* CxAODMaker : CXAOD-33: fix crash for MET maker debug output, enable it, dbuesche
* CxAODMaker : Readded PtReco after code checked it worked. We need to select the desired PtReco and set to store only that one for production, abuzatu
* CxAODMaker : resolve seg fault by reverting...need to be properly followed up, hanar
* CxAODMaker : temporary solution: write RandomRunNumber to original EventInfo so that it is accessible for the electron efficiency tool; CXAOD-263, hanar
* CxAODReader : Add Ghost Matching of TrackJets+FatJets, ahoenle
* CxAODReader_VHbb : Add Ghost Matching of TrackJets+FatJets, ahoenle
* CxAODReader_VHbb : modified the ordering of selected jets for the AllSigJets b-tagging strategy to match the twiki, cmaiani
* CxAODTools : remove property, not needed, hanar
* FrameworkExe : Add Ghost Matching of TrackJets+FatJets, ahoenle
* FrameworkExe : move to class access mode, hanar
* FrameworkSub : remove out-dated packages from packages-trunk to switch to the recommended ones in the release, lshi

## 16-06-17
* CxAODMaker : adding new electron matching triggers, amontalb
* CxAODMaker : a minor change to run data15+data16 with the same config file, tnobe
* CxAODMaker : =change to signal lepton MJ MET definition, schae
* CxAODMaker : fix: don't call tool twice just copy random runnumber to original container as needed by ele eff tool to avoid crash on data - should be removed once new ele eff tool is available, hanar
* CxAODMaker : set random runnumber only for MC, hanar
* CxAODMaker : Turn off PtReco trained after Moriond, remaining only 3 PtReco trained now, abuzatu
* CxAODMaker : update trigger matching dR for photon, lshi
* CxAODMaker : updating deltaR for electron trigger matching, amontalb
* CxAODMaker_VHbb : change electron cut for MJ study, nishijim
* CxAODMaker_VHbb : My update to CxAODMaker_VHbb in mydevbranch, nishijim
* CxAODMaker : write some jet properties not affected by systematics for nominal only -> -10% CxAOD size, dbuesche
* CxAODReader_VHbb : extra line to be sure b-tag tool is configured for the right jets in vbf+photon reader, prose
* CxAODReader_VHbb : Fix missing implementation of setevent_flavourGhost(), ahoenle
* CxAODReader_VHbb : latest updates to AnalysisReader_VBFHbb, prose
* CxAODReader_VHbb : Re-activate setevent_flavourGhost after successful checks., ahoenle
* CxAODReader_VHbb : Update to MVATree VBFHbb, prose
* CxAODReader_VHbb : update VBF+photon reader: merge with trigger study; update variables in MVATree to take the uncorrect b jet variables, lshi
* CxAODTools : adding electron matching props, amontalb
* CxAODTools : =add option for Scale factor calculation, schae
* CxAODTools : a minor change to calculate PU weight for 2015+2016 data, tnobe
* CxAODTools : making 1 lepton muon events trigger on MET trigger, amontalb
* CxAODTools : put property back, currently needed by ele eff tool...should be removed again soon once new tool available, hanar
* FrameworkExe : Fix missing implementation of setevent_flavourGhost(), ahoenle
* FrameworkExe : grid job can be submitted with phys-exotics role, tnobe
* FrameworkExe : updating MJ run config, amontalb
* FrameworkSub : adding the METUtilities-00-02-29 in the list of packeges, francav
* FrameworkSub : fix broken file, lulu

## 16-06-18
* CxAODMaker : added option for AF-II, tnobe
* CxAODMaker : Added some documentation of running multiple JES schemes in JetHandler class, zxi
* CxAODMaker : Added support for running multiple JES NP schemes in a single run; code still compatiable with the old config, zxi
* CxAODMaker : Only check duplicates bewteen begin of m_jesProvidersWZ and m_jesProviderHbb, zxi
* CxAODMaker : retrieve info on AFII vs full sim; use it in electron and jet handler; ToDo: double check grid running and switches in object handlers; CXAOD-243, hanar
* CxAODMaker_VHbb : retrieve info on AFII vs full sim; use it in electron and jet handler; ToDo: double check grid running and switches in object handlers; CXAOD-243, hanar
* CxAODTools : Fix compilation warning, nmorange
* FrameworkExe : Added support for running multiple JES NP schemes in a single run -- an example of config file, zxi
* FrameworkExe : Added support for running multiple JES NP schemes in a single run -- an example of config file, zxi
* FrameworkExe : deleted bad commit, zxi
* FrameworkExe : Make default test run an 1lep mc15c ttbar file, abuzatu
* FrameworkExe : Remove duplicate fat jet systs, nmorange
* FrameworkExe : reverted  , zxi
* FrameworkExe : Update config file with all systematics, nmorange
* FrameworkSub : Add Lists of datasets of 20.7.6.4 production, nmorange
* FrameworkSub : bump tag release to 2.4.11, haysjm
* FrameworkSub : updated packages.txt for v22 tag, haysjm

## 16-06-19
* CxAODMaker : Bugfix for JVT calculation, nmorange
* CxAODMaker : PassJvtMedium should now be copied again for every syst, nmorange
* FrameworkSub : Fixing typo in RS_G M2750 causing empty sample names., fmueller
* FrameworkSub : Uses new CxAODMaker tag, nmorange

## 16-06-20
* CxAODReader_VHbb : add MVA cutflow, ckato

## 16-06-21
* CxAODMaker : add single photon triggers to trigger list, lshi
* CxAODMaker_VHbb : Tentatively fix a Jet Cleaning bug, nmorange
* CxAODReader : Added jet author check for b-tag tool, stchan
* CxAODReader_VHbb : Cleaned up old truth tagging methods, stchan
* CxAODReader_VHbb : move namespace OneLeptonResolvedCuts to VHbb1Lep.h, yama
* CxAODTools : Cleaned up old truth tagging methods, stchan
* FrameworkExe : added script to merge truth and direct tagging samples, cmaiani
* FrameworkExe : updated merging script, cmaiani
* FrameworkSub : removing un-used and confusing mc15b files, fsforza
* FrameworkSub : Use new CxAODMaker_VHbb tag, nmorange

## 16-06-22
* CxAODReader : Recovered PtRecoParton and Regression at Reader level; stored also PtReco version 1, 2, 3 and Regression in the style of OneMu, KF already stored, to have the histograms all together, abuzatu
* CxAODReader_VHbb : 2Lep Reader: adding options for labeling fat-jets with 1 track-jet based on Andreas' studies. Default is TrackJetHybrid, sargyrop
* CxAODReader_VHbb : Recovered PtRecoParton and Regression at Reader level; stored also PtReco version 1, 2, 3 and Regression in the style of OneMu, KF already stored, to have the histograms all together, abuzatu
* CxAODReader_VHbb : Update for fat jet labeling baseline solution (TrackJetHybrid), ahoenle
* CxAODTools : Changed default behavior to return no tags if njets<nRequiredTTags, stchan
* CxAODTools : Second bugfix on Jvt+bad jets cleaning, nmorange
* CxAODTools : updated for 2D tagging testing, jhetherl
* FrameworkExe : Adding macro to make pie charts, sargyrop
* FrameworkExe : bool doResolution = true # true for 2 lepton, ckato
* FrameworkExe : updated for 2D tagging testing, jhetherl
* FrameworkSub : Add new lists of samples, nmorange
* FrameworkSub : dos2unix all list files, nmorange
* FrameworkSub : update HistSvc names for vbf+photon, prose
* FrameworkSub : Update packages list, nmorange
* FrameworkSub : Use new CxAODTools tag, nmorange

## 16-06-23
* CxAODReader : Adding variables needed by HH->bbtautau reader (hope they doesn't hurt...), carquin
* CxAODReader : Change in AnalysisReader.cxx to implement 2D cut for merged analysis, sargyrop
* CxAODReader : Modified getMuonInJetCorrTLV to retrieve correct Regression and PtReco also for systematics, yesterday I had corrected just for Nominal, reorganised code to be used for both nominal and systematic jet, abuzatu
* CxAODReader : Replaced assert(...) with Warning(...), abuzatu
* CxAODReader_VHbb : Add some missing instructions to use EasyTree, cdelport
* CxAODReader_VHbb : Change in AnalysisReader_VHbb.cxx to implement 2D cut for merged analysis. When 2D cut is used the analysis strategy is forced to be Merged., sargyrop
* CxAODReader_VHbb : move to common getMuonInJetCorrTLV method, hanar
* CxAODReader_VHbb : MVA part : Some cleaning + set the input variables in an extra function, cdelport
* CxAODReader_VHbb : Removed printout for debug, abuzatu
* CxAODReader_VHbb : Revert back from using mbb full range used in testing, abuzatu
* CxAODReader_VHbb : Three ptreco from 22-xx previously hard coded stored as the PtReco given by user, to be able to work also in 20-xx and 21-xx, abuzatu
* CxAODTools : Change in BTaggingTool to implement 2D cut for merged analysis. Is switched off by default, sargyrop
* FrameworkExe : Added clarifications and examples of b-jet energy corrections to be run in 20-xx, 21-xx, 22-xx, abuzatu
* FrameworkExe : It was decided to use PtRecollbbOneMuTruthWZNoneNewTrue, to be consistent with JetEtMiss group and be able to show public plots, as the performance of the different PtReco are very similar, abuzatu
* FrameworkExe : Reader config: add flag for using 2D b-tagging cuts, sargyrop

## 16-06-24
* CxAODReader : resolve some compiler warnings, hanar
* CxAODReader_VHbb : IF use2DbTagCut TRUE: make code crash if use2DbTagCut is enabled and another strategy than Merged is chosen; fix bug; silence errors from btagging tool for calo jets by disabling the call to the btagging tool, hanar
* CxAODReader_VHbb : Preparing some material for the parallel evaluation of several BDTs simultaneously, cdelport
* CxAODReader_VHbb : Updated pTW cut in resolved analysis PTW >150GeV now, sjiggins
* CxAODReader_VHbb : Update to VBF+photon reader, prose
* CxAODReader_VHbb : update vbf+photon BDT weights to 11 input vars and truth tagging 77%, lshi
* FrameworkExe : add plotting macro for vbf + photon, prose
* FrameworkExe : consistent settings; updated comment for 2DbTagCut, hanar
* FrameworkExe : some cleanup, sensible defaults, hanar
* FrameworkSub : Adding xAODBTaggingEfficiency to packages.txt and switching from using tag to using the trunk of said package, sargyrop
* FrameworkSub : Add xAODBTaggingEfficiency package to trunk packages, lkaplan

## 16-06-25
* CxAODReader_VHbb : 0lep reader: introduce doMergeModel flag to split events with 1 track-jet from events with at least 2 track-jets in the leading fat-jet, sargyrop
* CxAODReader_VHbb : 2Lep reader: Re-introducing doMergeModel, sargyrop

## 16-06-26
* CxAODMaker : add systematic variation MET_SoftTrk_ResoCorr, tnobe
* CxAODReader : Adding the tree for the overlap studies needed for the Higgs combination for SM and BSM, francav
* CxAODReader : Adding the tree for the overlap studies needed for the Higgs combination for SM and BSM, francav
* CxAODReader_VHbb : Adding the tree for the overlap studies needed for the Higgs combination for SM and BSM, francav
* CxAODReader_VHbb : Adding the tree for the overlap studies needed for the Higgs combination for SM and BSM, francav
* CxAODReader_VHbb : doResolution, ckato
* CxAODReader_VHbb : Updated plot creation as default & mBB rescaling fix, sjiggins
* FrameworkExe : added new samples (see the previous commit), tnobe
* FrameworkExe : add systematic variation MET_SoftTrk_ResoCorr, tnobe
* FrameworkExe : revert back the list of MET uncertainty, tnobe
* FrameworkSub : adding vbf + photon yields for mc15c, prose
* FrameworkSub : fill in cross section for HVT WW->lvqq, WZ->lvqq and RS G->WW->lvqq, lulu
* KinematicFit : TF made from CxAOD 22-01, ckato

## 16-06-27
* CxAODReader_VHbb : small updates to run 0lep SM VH code on mc15c BDT xml, cmaiani
* CxAODReader_VHbb : update VBF+photon reader: trigger part, lshi
* CxAODTools : Added/commented out example of how to do fixed fraction of events with 1tag, rest in 2tag, stchan
* FrameworkSub : Add new file lists as well on the trunk, nmorange
* KinematicFit : comment out truth pT(j) pdf before clean up, ckato
* KinematicFit : ICHEP PtReco when fit is not converged, ckato

## 16-06-28
* CxAODMaker : added electron trigger SF, correct tau SF new triggers, agbet
* CxAODTools : new props electron SF, agbet
* CxAODReader_VHbb : Adding new 0Lep-BDT xml files, cdelport
* CxAODReader_VHbb : up 0lep reader to properly read more than one xml, cmaiani
* CxAODReader_VHbb : update VBF+photon reader: add dEtaJJ reweighting, lshi
* CxAODTools : new CDI file in BTaggingTool, jhetherl
* CxAODTools : new props electron SF, agbet
* FrameworkExe : adding flags for 0-lep SM VH BDT reading, cdelport
* FrameworkSub : added latest muon-CP pkg, fsforza
* FrameworkSub : new CDI file uses Sherpa DSID not previously in XSections file - dummy entry for is now included, jhetherl

## 16-06-29
* CorrsAndSysts : CXAOD-272 add ttbar pTV syst from elisabeth, dbuesche
* CorrsAndSysts : CXAOD-272 merge from devbranch: remove Run 1 stuff, dbuesche
* CxAODReader : need to recompute random runnumber also if not recomputing muon trigger SFs; add some protections, hanar
* CxAODReader : =set jet pt cut, schae
* CxAODReader_VHbb : CXAOD-272 remove calls to Run 1 corrs and systs, dbuesche
* CxAODReader_VHbb : Remove three types of PtReco stored for private study; remain only GSC, OnMu, standard PtReco, Regression and KF, abuzatu
* CxAODReader_VHbb : Revert mbb bins from 2.5 to 502.5 from private study to 0 to 500 as before in trunk, abuzatu
* CxAODReader_VHbb : small updates for naming, cmaiani
* CxAODTools : el trigger is now present in MC, remove fix for new CxAODs, amontalb
* CxAODTools : Implementing whichData flag which allows to reweight to PU profile of 2015 and 2016 data separately. Default is to reweight to combined 2015+2016 PU profile, sargyrop
* CxAODTools : =jet ptcut setting, schae
* CxAODTools : trigger for 2016 data; note: no lepton trigger SFs; CXAOD-271, hanar
* FrameworkExe : Implementing whichData flag in reader config, sargyrop
* FrameworkExe : new TriggerMenu, hanar

## 16-06-30
* CxAODReader_VHbb : getKF if(2 jet & pT>1 GeV & resolution>0.001), ckato
* CxAODReader_VHbb : mBB monitor only in 2 lepton, ckato
* FrameworkExe : lumi for different years, hanar
* FrameworkExe : updated macro for merging truth and direct tagged samples, cmaiani
* FrameworkSub : 2 lepton yields for 22-01, hanar

## 16-07-01
* CorrsAndSysts : Minor fixes, nmorange
* CxAODMaker : use ConeExcl matched hadrons instead of ghost matched...need to clean-up code sometime; CXAOD-273, hanar
* FrameworkSub : change XSextion_13TeV.txt, nishijim
* FrameworkSub : change XSextion_13TeV.txt, nishijim
* FrameworkSub : correct 2 lepton yields file, hanar

## 16-07-02
* FrameworkExe : Update makePieCharts.C macro, sargyrop

## 16-07-03
* CxAODReader_VHbb : change mindPhi cut for nJets >= 4 to be in agreement with David D's recommendation for AZh/HVT; SMVH unchanged, hanar
* CxAODReader_VHbb : fill only mVH for AZh/HVT if only inputs; merge jet categories if doMergeJetBins set to true, hanar
* CxAODReader_VHbb : fixing a segfault issue in HVT/AZh reader for 0 lepton, francav
* CxAODReader_VHbb : use new topemucr definition = using SR mLL cut, hanar
* FrameworkSub : 0 lep yields file, hanar
* FrameworkSub : updated 2 lep yields file, hanar

## 16-07-04
* CxAODMaker : protection swtich fot the EMScale eta. default behavior as before., agbet
* CxAODMaker : Remove hadronic tau jets from counting of truth jets for Sherpa reweighting, abuzatu
* CxAODReader : add FakeFactor, nishijim
* CxAODReader_VHbb : add fakefactor method, nishijim
* CxAODTools : add FakeFactor, nishijim
* CxAODTools : Fixed inclusive truth tagging., stchan
* FrameworkExe : add 1lepton cofig, nishijim
* FrameworkExe : Update electron efficiency uncertainties, tnobe
* FrameworkSub : add fakefactor and mva xml, nishijim
* FrameworkSub : fix XSection_13TeV.txt, nishijim
* FrameworkSub : new TauAnalysisTools, agbet

## 16-07-05
* CxAODMaker : fix selection for METMJLoose, nishijim
* CxAODReader_VHbb : don't write PU histos if m_doOnlyInputs and if PU weight is applied, hanar
* CxAODTools : add xe100_mht trigger, add met trigger SFs for 2016, update SF for 2015 with 20.7, wangwe
* CxAODTools : Fix MET SF calculation in 1 muon channel, nmorange
* CxAODTools : removing forcing m_recomputePUWeight to true when running on  a single data period, dimicco
* FrameworkExe : fixing framework-run.cfg to properly handle 2015 and 2016 ilumiCalc files, dimicco
* FrameworkSub : add new fakefactor file, nishijim
* FrameworkSub : new ilumi calcs and GRL for 2015 and 2016 with GRL-v79 and 3.2+5.1 fb-1, fsforza

## 16-07-07
* CxAODMaker : added missing dep for Asg_MCUtil - pointed out by sekula, haysjm
* CxAODMaker : change of default: need to set storeGAParticlesInJets explicitely to true in config to write number of associated hadrons to CxAOD - current default caused issues for other analyses, hanar
* CxAODReader_VHbb : 3pjet was not for trunk, ckato
* CxAODReader_VHbb : use isTagged information in getKF, ckato
* CxAODTools : fix a bug in trigger decision, wangwe
* FrameworkExe : change: need to set storeGAParticlesInJets explicitely to true to write number of associated hadrons to CxAOD, hanar
* FrameworkExe : change setting: don't write number of hadrons associated to jets before we are sure it works on all samples; CXAOD-273, hanar
* FrameworkSub : adding HFOR testing tool, useful for possible Alpgen studies, fsforza
* FrameworkSub : bump to 2.4.13, haysjm

## 16-07-07
* CorrsAndSysts : CXAOD-281 merge from devbranch: add SysTTbarMBB, SysW/ZPtV/Mbb, dbuesche
* CxAODMaker : added JvtEfficiency uncertainty, tnobe
* CxAODMaker : rename JvtEfficiency uncertainties, hanar
* CxAODMaker : set CorrelationModel for elecEffSF tools explicitly as TOTAL since the default is now SIMPLIFIED, lulu
* CxAODReader_VHbb : 2Lep Reader: fix definition of mBB sidebands, sargyrop
* CxAODReader_VHbb : 2Lep Reader: re-introduce modelType to split between HVT and AZh. Fix sideband definition, sargyrop
* CxAODReader_VHbb : add usefull comment, hanar
* CxAODReader_VHbb : hack HVT CorrsAndSyst to make it work for Sherpa 2.2, hanar
* CxAODReader_VHbb : HVT CorrsAndSyst - needs to be further validated, hanar
* CxAODReader_VHbb : Moved V+Jet and TTbar HVT Merged Systematic CorrsAndSysts instantiation ton AnalysisReader_VHbb.cxx, sjiggins
* CxAODTools : Added Alpgen string to BTaggingTool::indexMCEfficiencyFrom*, tursom
* CxAODTools : PURewightingTool: call getRndNumber with true argument to comply with CP reccomendations, dimicco
* FrameworkExe : added JVT systematics and missing JET_SR1_JET_EtaIntercalibration_NonClosure, hanar
* FrameworkExe : Add Hbb fat jet systematics, before only WZ in previous production; to be discussed further if these are what we want, abuzatu
* FrameworkExe : updating to the last 2016 grl and ilumicalc 6.3 fb-1, dimicco
* FrameworkSub : Updated Alpgen V+jets sample names in data/XSections_13TeV.txt, tursom
* FrameworkSub : updating GRL and ilumicalc file to 2016 6.3 fb-1, dimicco
* FrameworkSub : updating to release 2.3.14, dimicco

## 16-07-08
* CorrsAndSysts : adding SysTTbarPTVMBB, nishijim
* CxAODMaker : 2016 bbtautau (hadhad) triggers and SFs, carquin
* CxAODMaker : implementing ICHEP_v2 recommendation from  Egamma in ElectronHandler, dimicco
* CxAODMaker_VHbb : change muon MJ selection, nishijim
* CxAODReader : adding jetRapidityCut, vcairo
* CxAODReader_VHbb : CorrsAndSyst for HVT, hanar
* CxAODTools : adding jetRapidityCut, vcairo
* CxAODTools : adding jetRapidityCut, vcairo
* CxAODTools : tau trigger SFs, carquin
* CxAODTools_VHbb : remove muon trigger SF computation for now; has to be done at reader level; CXAOD-283, hanar
* CxAODTools_VHbb : return code was missing in 1 lepton after trig muon sf comment out, ckato
* FrameworkExe : keep medium and strong schemes commented; removed outdated list of systematics, hanar
* FrameworkExe : remove weak and strong correlation schemes for WZ fat jet JES syst; remove Hbb JES syst identical to WZ ones, hanar
* FrameworkSub : Add datasets to produce, basewd on July 07 snapshot of derivations, nmorange
* FrameworkSub : Add Out/ directory, nmorange
* FrameworkSub : fix cx k-factor on the base of latest studies from Marco and Jose, fsforza
* FrameworkSub : prep for v24 tag, haysjm
* FrameworkSub : updated CxAODMaker_VHbb tag, haysjm
* FrameworkSub : updateed CxAODMaker tag, haysjm

## 16-07-09
* CxAODMaker : added filenames for temporary electron efficiency bugfixes, haysjm
* CxAODMaker : adding electron trigger, dimicco
* CxAODMaker : adding one more ele trigger to list, hanar
* CxAODMaker : try fixing the electorn triggers again, haysjm
* CxAODTools : adapt comment to previous commit, hanar
* CxAODTools : added trigger, hanar
* CxAODTools : adding pass and match electron trigger flags, dimicco
* CxAODTools : update for recomputing muon trigger SF for both 2015 and 2016 data; not sure backwards compatible; usage requires enabling in reader config; CXAOD-283, hanar
* FrameworkExe : updated names of EL_EFF_* uncertainties, tnobe
* FrameworkSub : updated CxAODMaker tag again - pull in electorn efficiency fix, haysjm
* FrameworkSub : updated cxaodtools_vhbb tag, haysjm
* FrameworkSub : updated tags for CxAODMaker and CxAODTools for update from hannah, haysjm
* FrameworkSub : updated tags for hopefully final tag for ichep, haysjm
* FrameworkSub : updatr cxaodtooks tag', haysjm

## 16-07-10
* CxAODMaker : fixed METMJTight, nishijim
* CxAODReader_VHbb : Updated basic input histogram to exclude only mVH & mBB when blinded, sjiggins
* CxAODReader_VHbb : Updated doMbbRescaling for merged analysis, sjiggins
* CxAODTools : fixing and restyling TriggerTool, use proper random run number extraction, dimicco
* CxAODTools : fix memory leak in MET trig SF computation, hanar
* FrameworkSub : fixed typo in packages file, haysjm
* FrameworkSub : tags for CxAODMaker and CxAODTools updated to pull in missing electron triggers, haysjm

## 16-07-11
* CxAODMaker : trigger effSF input file for looseLH isolLooseTrackOnly, lulu
* CxAODReader : protection no longer needed here, hanar
* CxAODReader_VHbb : fix getMuonInJetCorrTLV usage in merged regime, hanar
* CxAODTools : debugging Trigger Tool, dimicco
* CxAODTools : forcing the recomputation of the muon trigger SFs since no longer stored in CxAODs; CXAOD-283, hanar
* CxAODTools : putting back the set run number for TriggerSF also for data, it can help in spotting problems, dimicco
* FrameworkExe : setting sensible defaults (again), hanar
* FrameworkExe : update framework-run-MJ.cfg, nishijim
* FrameworkSub : add latest fackfactor root files, nishijim
* FrameworkSub : change muon fakefactor root file, nishijim
* FrameworkSub : Updated 2HDM bbtautau filter eff, gwilliam
* FrameworkSub : update data16 list files, yama
* FrameworkSub : updated packages list for 24-MJ, haysjm
* FrameworkSub : Updated RSG lh filter eff, gwilliam

## 16-07-12
* CxAODMaker : Fixing tau trigger systematics, carquin
