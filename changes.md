## 2016-01-26
CxAODMaker: Fix compilation warning, nmorange
CxAODMaker: add new vbf+photon triggers for trigger study, lshi
CxAODMaker: add single photon triggers, lshi
CxAODMaker: update to new v04 config files, lulu
CxAODReader: removed tautau specific default in XSection, jhetherl
CxAODReader: updates to boosted analysis, nilic
CxAODReader\_VHbb: fixed EOYE recale on PU histos, cmaiani
CxAODReader\_VHbb: remove AllMu, OneMuNu, AllMuNu and PtReco+Gauss from reader, lshi
CxAODTools: add single photon triggers, lshi
FrameworkExe: Start to add new validation script, nmorange
FrameworkExe: add full list of csVariations recommended by Carlo, hanar
FrameworkSub: Bump AnalysisBase to 2.3.41, nmorange
FrameworkSub: updated yields file for di-lepton MC15b, jhetherl

## 2016-01-27
CxAODMaker: IsBjet fix from bool to char, agbet
CxAODMaker: remove HLT\_g20\_loose, HLT\_g25\_loose, lshi
CxAODMaker: updated trigger list for bbtautau, agbet
CxAODReader: Revert unwanted commit on AnalysisReader, nmorange
CxAODReader: re-included track-jet TruthLabel copying, jhetherl
CxAODTools: add MET trigger SF and syst, wangwe

## 2016-01-28
CxAODMaker: Fixed bug in JetHandler where 'IsBjet' - truth label used by JES tool - was always set to true, grkeren
CxAODMaker: Implemented Props::SumPtTrkPt500PV decoration for Variable Cone Overlap Removal, sjiggins
CxAODReader: pointing to correct XSec and yields files for mc15b, amontalb
CxAODReader\_VHbb: 0lepton selection update: (1) 110-140 mbb-window, (2) apply jet 4p correction on dijet H candidate for mbb-window cut and dijet-mass rescaling, cpandini
CxAODReader\_VHbb: Fix in 2lep analysis: remove tau veto from resolved SR and mBBcr - temporary fix until we switch to new function (imminent), sargyrop
CxAODTools: Implemented Variable Cone OR in OverlapRemoval.h(cxx) version 2, sjiggins
CxAODTools: Implemented Variable Cone OR in OverlapRemoval.h(cxx) version 3, sjiggins
CxAODTools: Implemented Variable Cone OR in OverlapRemoval.h(cxx), sjiggins
FrameworkExe: adding flag for mc15b XSec and Yields files, amontalb
FrameworkExe: config steering file: 0lepton MET correction set to false by default, AllSignalJets tagging strategy set to true by default, cpandini
FrameworkSub: Added missing monoHbb samples, rroehrig
FrameworkSub: Modified the monoHbb signal samples by changing the cross sections to all be identically 1.0 such that the fits are more stable without having to do scaling specific for each sample., meehan
FrameworkSub: updating yields file, amontalb
FrameworkSub: updating yields, amontalb

## 2016-01-29
CxAODMaker: Minor changes related to CP check for photons, added IEGammaAmbiguityTool and isAmbiguity decoration for photons, jpasner
CxAODMaker: Store OneMu once again, as in the end we use it and not XbbTagger, abuzatu
CxAODReader\_VHbb: Add cut in 2lep analysis: |eta|<2.5 cut for muons in merged analysis. Also remove some old junk, sargyrop
CxAODReader\_VHbb: Change 2lep cut: change m(fat-jet) cut to 75-145 GeV, sargyrop
CxAODReader\_VHbb: Tidying up 2lep code: make cut definition cleaner and replace eventFlag checking with the more intuitive passSpecificCuts function, sargyrop
CxAODTools: Adding isAmbiguous to common properties as decoration for IEGammaAmbiguityTool decision, jpasner
CxAODTools: Implemented Variable Cone Overlap Removal with Props::OROutputLabel, sjiggins
CxAODTools: variable cone OR - compiles, but not tested or even enabled, grkeren
FrameworkExe: Move default sample and PU reweighting to MC15b in framewokr-run, nmorange
FrameworkSub: prep for intermediate tag 19-01, haysjm
FrameworkSub: typo in packages.txt, haysjm

## 2016-01-30
CxAODMaker: Storing jet variable Props::SumPtTrkPt500PV, abuzatu
CxAODReader: adding virtual function executePreEvtSel() called before EventSelection, arnaez
CxAODReader\_VHbb: 2 lep: adding switch using NVtx2Trks if available in inputs (new) otherwise NVtx3Trks (old); adding infos on track jets to tree, hanar
CxAODReader\_VHbb: Updated at Nvtx NVtx3Trks to NVtx2Trks; crash otherwise, abuzatu
CxAODTools: fixed bug in variable cone OR, grkeren
FrameworkExe: correct settings for large jet OR, hanar

## 2016-01-31
CxAODReader\_VHbb: Updates in 2lep cutflow, sargyrop
CxAODTools: Corrected VaribaleConeOverlapRemoval logic (minor), sjiggins
CxAODTools: Implemented VariableConeOverlapRemoval added ORInputLabelCheck, sjiggins
CxAODTools: Minor fix in sumOfWeightsProvider: use correct name of class in the Error messages (was printing out XSectionProvider before), sargyrop
CxAODTools: fix in variable cone OR, grkeren

## 2016-02-01
CxAODMaker: Small fix for recording of TruthEvents, pottgen
CxAODTools: VariableConeOverlapRemoval correction, sjiggins
FrameworkExe: Improvement to script to draw CI plots, nmorange
FrameworkSub: modified monoHbb cross sections to add missing DSD 304035, meehan
FrameworkSub: updating yields, amontalb
FrameworkSub: updating yields, amontalb
