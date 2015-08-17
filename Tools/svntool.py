#! /usr/bin/env python
import pysvn

rpath='svn+ssh://haysjm@svn.cern.ch/reps/atlasoff/PhysicsAnalysis/HiggsPhys/Run2/Hbb/CxAODFramework/'
packages=['CxAODMaker',
          'CxAODMaker_VHbb',
          'CxAODTools',
          'CxAODTools_VHbb',
          'CxAODReader',
          'CxAODReader_VHbb',
          'FrameworkExe',
          'FrameworkExe_VHbb',
          'TupleMaker',
          'TupleReader']

def getLogRecordRevision(client,package,irev1,irev2):
    results={}
    results[package] = []
    rev1 = pysvn.Revision( pysvn.opt_revision_kind.number, irev1)
    rev2 = pysvn.Revision( pysvn.opt_revision_kind.number, irev2)
    logs = client.log(rpath+package+'/trunk',rev1,rev2)
    for log in logs:
        logRecord = ( log['author'], log['date'], log['message'])
        results[package].append(logRecord)
    return results

def getLogRecord(client,package,rev2):
    taglist=[]
    taglistRaw=client.list(rpath+package+'/tags',depth=pysvn.depth.immediates)
    for tagpath in taglistRaw:
        tag = tagpath[0].path.split('/')[-1]
        rev = tagpath[0].created_rev.number
        if tag != 'tags':
            taglist.append( (tag,rev) )
            #print tag, rev
    latestTag = ""
    latestRev =0 
    for (tag,rev) in taglist:
        if rev > latestRev:
            latestTag = tag
            latestRev = rev

    results = {}
    results[package]=[]

    if latestTag != "":
        rev1 = pysvn.Revision( pysvn.opt_revision_kind.number, latestRev)
        rev2 = pysvn.Revision( pysvn.opt_revision_kind.head)
        print 'Getting logs for ',package,' from revision ',rev1,' until revision ',rev2
        logs = client.log(rpath+package+'/trunk',rev1,rev2)
        for log in logs:
            logRecord = ( log['author'], log['date'], log['message'])
            results[package].append(logRecord)
    return results

def getResultsRevision(client,irev1,irev2):
    results = {}
    for pack in packages:
        results.update(getLogRecordRevision(client,pack,irev1,irev2))
    return results

def getAllResults(client):
# build tag info for each package:
# 
    trunkinfolist = client.list(rpath,depth=pysvn.depth.empty)
    rev2 = trunkinfolist[0][0].created_rev
    results={}
    for pack in packages:
        results.update(getLogRecord(client,pack,rev2))
    
    return results

def printResults(results):
    for pack in packages:
        print pack
        logs = results[pack]
        for log in logs:
            print '    ','{0:10} : {1}'.format(log[0],log[2].rstrip('\n'))

if __name__ == "__main__":
    client=pysvn.Client()
#    allResults = getAllResults(client)
    allResults = getResultsRevision(client,678738,683752)
    printResults(allResults)

    
