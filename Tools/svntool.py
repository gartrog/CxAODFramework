#! /usr/bin/env python
import sys
import pysvn
import time
from datetime import date

class Tag:
    def __init__(self,pack,tag,rev):
        self.pack = pack
        self.rev = rev
        numbers = tag.rsplit('-',3)
        tagpack=numbers[0]
        if tagpack != pack:
            print "package doesn't match the tag"
        self.low = int(numbers[3]);
        self.med = int(numbers[2]);
        self.high = int(numbers[1]);
        self.hash = self.low+1000*self.med+1000000*self.high

    def __lt__(self,other):
        if( self.high < other.high):
            return true
        if( self.high == other.high):
            if( self.med < other.med):
                return true
            if( self.med == other.med):
                if( self.low < other.log):
                    return true
        return false

    def __str__(self):
        return self.getTag()+' ( ' + str(self.rev) + ')'

    def __repr__(self):
        return self.getTag()+' ( ' + str(self.rev) + ')'

    def getTag(self):
        tagName="%s-%02d-%02d-%02d" % (self.pack,self.high,self.med,self.low)
        return tagName

    def getNextTag(self):
        tagName="%s-%02d-%02d-%02d" % (self.pack,self.high,self.med,self.low+1)
        return tagName

        
rpath='svn+ssh://svn.cern.ch/reps/atlasoff/PhysicsAnalysis/HiggsPhys/Run2/Hbb/CxAODFramework/'
packages=['CxAODMaker',
          'CxAODMaker_VHbb',
          'CxAODTools',
          'CxAODTools_VHbb',
          'CxAODReader',
          'CxAODReader_VHbb',
          'FrameworkExe',
          'FrameworkExe_VHbb',
#          'TupleMaker',
#          'TupleReader',
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

def getTagList(client,package):
    taglist=[]
    taglistRaw=client.list(rpath+package+'/tags',depth=pysvn.depth.immediates)
    for tagpath in taglistRaw:
        tag = tagpath[0].path.split('/')[-1]
        rev = tagpath[0].created_rev.number
        if tag != 'tags':
            taglist.append( Tag(package,tag,rev) )
    return taglist


# get all log records for a given package from the trunk since the last tag of the package
def getLogRecord(client,package):
    latestTag = ""
    latestRev =0 
    taglist = getTagList(client,package)
    for tag in taglist:
        if rev > latestRev:
            latestTag = tag.tag
            latestRev = tag.rev

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

def checkIfNeedNewTag(client,tag):
    url1=rpath+tag.pack+'/trunk'
    url2=rpath+tag.pack+'/tags/'+tag.getTag()
    rev1 = (client.info2(url1,recurse=False))[0][1]['last_changed_rev'].number
    rev2 = (client.info2(url2,recurse=False))[0][1]['last_changed_rev'].number
    print 'trunk=',rev1,'tag=',rev2
    if rev1 != rev2:
        return (rev1,rev2,True)
    return (rev1,rev2,False)
    

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

def makeNewTag(client,pack,doTag=False):
    if pack=='FrameworkSub':
        return None
    rev=-1
    taglist = getTagList(client,pack)
    # sort the tag list in reverse order
    taglist.sort(key=lambda x: x.hash, reverse=True)
    if len(taglist) < 1:
        print 'tag list for package:',pack,' is empty'
        print taglist
        return None
    else:
        currenttag = taglist[0]
        tagcheck = checkIfNeedNewTag(client,currenttag)
        if not tagcheck[2]:
            print 'tag not needed'
            return currenttag
        nextTag = currenttag.getNextTag()
        print currenttag.getTag(),nextTag, tagcheck
        urlsrc="%s/%s/trunk" % (rpath, pack)
        urldst="%s/%s/tags/%s" % (rpath,pack,nextTag)
        print '      ',urlsrc
        print '      ',urldst
        if doTag:
            client.callback_get_log_message = lambda : (True,"Prep for tag 14")
            newrev = client.copy(urlsrc,urldst)
            rev = newrev.number
    return Tag(pack,nextTag,rev)
            
        

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print "svntool log [days]"
        print "svntool checktags [package]"
        print "svntool maketags [package]"
        exit()

    client=pysvn.Client()
#    allResults = getAllResults(client)
#    allResults = getResultsRevision(client,688958,689715)
#    allResults = getResultsSince(client,8)
#    printResults(allResults)
#    printResultsAlternate(allResults)
    
    cmd = sys.argv[1]
    if cmd=="log":
        days=8
        if argc==3:
            days = int(sys.argv[2])
        allResults = getResultsSince(client,days)
        printResultsAlternate(allResults)
    if cmd=="checktags":
        if argc==3:
            pack=sys.argv[2]
            print makeNewTag(client,pack,False)
        else:
            for pack in packages:
                print makeNewTag(client,pack,False)
    if cmd=="maketags":
        if argc==3:
            pack=sys.argv[2]
            print makeNewTag(client,pack,True)
        else:
            for pack in packages:
                print makeNewTag(client,pack,True)
