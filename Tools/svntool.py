#! /usr/bin/env python
import pysvn
import time
from datetime import date

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
          'TupleReader',
          'FrameworkSub']

# get all log records between two pysvn.Revisions
def getLogRecordSVNRevision(client,package,rev1,rev2):
    results = {}
    results[package] = []
    logs = client.log(rpath+package+'/trunk',rev1,rev2)
    for log in logs:
        logRecord = ( log['author'] , date.fromtimestamp(log['date']),log['message'])
        results[package].append(logRecord)
    return results
              
# get all log records from the last n days
def getLogRecordSince(client,package,d):
    rev2 = pysvn.Revision( pysvn.opt_revision_kind.head )
    timestamp = time.time() - d*86400
    rev1 = pysvn.Revision( pysvn.opt_revision_kind.date, timestamp)
    return getLogRecordSVNRevision(client,package,rev1,rev2)
    
# get all log records for a given package between two revisions
def getLogRecordRevision(client,package,irev1,irev2):
    rev1 = pysvn.Revision( pysvn.opt_revision_kind.number, irev1)
    rev2 = pysvn.Revision( pysvn.opt_revision_kind.number, irev2)
    return getLogRecordSVNRevision(client,package,rev1,rev2)

# get all log records for a given package from the trunk since the last tag of the package
def getLogRecord(client,package):
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
            print '---> ',log['date'],date.fromtimestamp(log['date'])
            logRecord = ( log['author'], date.fromtimestamp(log['date']), log['message'])
            results[package].append(logRecord)
    return results

def getResultsRevision(client,irev1,irev2):
    results = {}
    for pack in packages:
        results.update(getLogRecordRevision(client,pack,irev1,irev2))
    return results

def getResultsSince(client,days):
    results = {}
    for pack in packages:
        results.update(getLogRecordSince(client,pack,days))
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
            print '    ','{0:10} : {1} : {2}'.format(log[0],log[1],log[2].rstrip('\n'))

def printResultsAlternate(results):
    for pack in packages:
        logs = results[pack]
        for log in logs:
            print '{0} : {1} : {2:10}, {3}'.format(log[1],pack,log[2].rstrip('\n'),log[0])
        
if __name__ == "__main__":
    client=pysvn.Client()
#    allResults = getAllResults(client)
#    allResults = getResultsRevision(client,688958,689715)
    allResults = getResultsSince(client,8)
#    printResults(allResults)
    printResultsAlternate(allResults)

    
