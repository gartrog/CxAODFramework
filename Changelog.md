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


