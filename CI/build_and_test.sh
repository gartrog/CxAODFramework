#!/bin/bash

RESULTSDIR=/afs/cern.ch/work/n/nmorange/public/CI

TODAY=$(date +%y-%m-%d-%H-%M)
if [ -z $1 ]
then
  AGAINST=$(ls $RESULTSDIR | tail -n1)
else
  AGAINST=$1
fi
echo "Testing against $AGAINST"

cd /tmp/nmorange
mkdir CxAOD
cd CxAOD
svn co svn+ssh://svn.cern.ch/reps/atlasoff/PhysicsAnalysis/HiggsPhys/Run2/Hbb/CxAODFramework/FrameworkSub/trunk FrameworkSub
source FrameworkSub/bootstrap/setup-trunk.sh
rc build

