
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
