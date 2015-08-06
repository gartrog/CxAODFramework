# TODO list to create a new tag

## List of new functionalities we want to have
  - have they people actively working on them
  - when are they expected to be ready
  - track progress to make sure they are ready on time

## Update what we have
  - are we at the latest AnalysisBase tag ?
  - do we follow latest muon recommendations ?
    + ID and trigger efficiencies and systematics
    + scale/resolution and systematics
    + check that values in default config file are correct
  - do we follow latest electron recommendations ?
    + ID and trigger efficiencies and systematics
    + scale/resolution and systematics
    + check that values in default config file are correct
  - do we follow latest photon recommendations ?
    + ID and trigger efficiencies and systematics
    + scale/resolution and systematics
    + check that values in default config file are correct
  - do we follow latest tau recommendations ?
    + ID and trigger efficiencies and systematics
    + scale/resolution and systematics
    + check that values in default config file are correct
  - do we follow latest jets recommendations ?
    + scale/resolution and systematics
    + cleaning
    + check that values in default config file are correct
  - do we follow latest MET recommendations ?
    + rebuilding
    + systematics
    + check that values in default config file are correct
  - do we follow latest data prep recommendations ?
    + GRL
    + pile-up reweighting
    + check that values in default config file are correct

## FREEZE NOW. no more changes allowed

## Deal with bugs
  - are there known bugs in OUR code ?
    + if yes, check that there are people fixing them
    + are they critical for the next tag ?
  - are we suffering from upstream bugs/issues ?
    + to what extent are we affected ? Maybe we don't care
    + can we work around ourselves, temporarily ?
    + when are the fixes expected ?

## Prepare submission
  - prepare the list of data datasets
  - prepare the list of MC datasets
  - if several p-tags are being used, make sure they are compatible, and
    that the code can run on all

## Test
  - always use the default config file (which is going to be used for production)
  - test locally on MC and data. Maybe test 0, 1, and 2 lepton selections ?
  - quick grid test on 1 file of MC and data ?
  - if crashes/bugs, yell at people until it is fixed

## TAG

## Submission
  - find the necessary people to run on all derivations, data and MC
  - launch
