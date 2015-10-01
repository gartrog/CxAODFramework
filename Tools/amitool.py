#! /usr/bin/env python
# following instructions from: http://ami.in2p3.fr/pyAMI/pyAMI5_atlas_api.html
import sys
import pyAMI.client
import pyAMI.atlas.api as AtlasAPI

def getParent(client,sample):
    dict = AtlasAPI.get_dataset_prov(client,sample)
    parent = dict['node'][1]['logicalDatasetName']
# get the immediate first parent - this should be an AOD for a DxAOD
    return parent


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print "amtool aods filename"
        exit()
    cmd = sys.argv[1]
    if cmd =='aods':
        client = pyAMI.client.Client('atlas')
        AtlasAPI.init()

        filename= sys.argv[2]
        with open(filename) as f:
            samplelist = f.readlines()
            
        with open('aods_'+filename,'w') as f:
            for sample in samplelist:
                print 'finding parent for sample:',sample.strip()
                parent = getParent(client,sample.strip())
                f.write(parent+'\n')
                
