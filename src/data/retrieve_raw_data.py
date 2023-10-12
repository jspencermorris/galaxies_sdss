import os.path
import csv
import json
import requests

'''
Galaxy Zoo Project
primary repository/documentation:  https://data.galaxyzoo.org/
secondary repository/documentation:  https://zenodo.org/record/3565489#.Y3vFKS-l0eY

manually downloaded files:
    Label Set ('Table 1')
        https://gz2hart.s3.amazonaws.com/gz2_hart16.csv.gz
    Image Set
        https://zenodo.org/record/3565489/files/gz2_filename_mapping.csv
        https://zenodo.org/record/3565489/files/images_gz2.zip
        https://zenodo.org/record/3565489/files/README.txt
        

'''

# define location where raw galaxy zoo 2 data is stored
raw_gz2_data_directory = '../../data/raw/gz2/'

# helper function return gz2 file
def save_gz2_data(url, filename):
    
    response = requests.get(url)
    data = csv.readaer(response)
    
    with open(os.path.join(raw_gz2_data_directory, filename), 'w') as f:
        writer = csv.writer(f)
        for line in response.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))
    
    return response



'''
Galaxy Zoo Enrichment Datasets
primary repository/documentation:  https://skyserver.sdss.org/dr16/en/home.aspx

tables incorporated in queries:
    zoo2MainPhotoz
    zoo2MainSpecz
    zooConfidence
    zooNoSpec
    zooSpec
    zooVotes
'''

# define the location where raw skyserver sdss data should be stored
raw_skysever_data_directory = '../../data/raw/skyserver_sdss/'

# helper function to query the sql database and return a file
def query_and_save_sdss_data(query, filename):
    
    query = query.replace(' ', '%20')
    file_format = 'json'
    host_url = 'http://skyserver.sdss.org/dr16/SkyServerWS/SearchTools/SqlSearch?cmd='
    
    response = requests.get(host_url+query+'&format='+file_format)
    data = response.json()
    
    #print(type(response))
    #print(type(data))
    
    with open(os.path.join(raw_skysever_data_directory, filename), 'w') as f:
        json.dump(data, f)
    
    #return response

# retrieve zoo2MainPhotoz
#query_zoo2MainPhotoz = 'select top 500000 dr8objid, dr7objid, ra, dec, total_classifications, total_voates, from zoo2MainPhotoz'
#query_and_save_sdss_data(query_zoo2MainPhotoz, 'zoo2MainPhotoz')

# retrieve zoo2MainSpecz
#query_zoo2MainSpecz = ''

# retrieve zooConfidence
#query_zooConfidence = ''

# retrieve zooNoSpec
#query_zooNoSpec = ''

# retrieve zooSpec
#query_zooSpec = ''

# retrieve zooVotes
query_zooVotes = '''select *
from DR16.zooVotes
into MyDB.zooVotes'''

# retrieve specObj
query_specObj = '''select top 1000000
  specObjID, bestObjID, targetObjID, instrument, ra, dec, z, 
  class, subClass, class_noqso, subClass_noqso, class_person,
  spectroFlux_u, spectroFlux_g, spectroFlux_r, spectroFlux_i, spectroFlux_z,
  spectroSynFlux_u, spectroSynFlux_g, spectroSynFlux_r, spectroSynFlux_i, spectroSynFlux_z,
  elodieObject, elodieSpType, elodieBV, elodieTEff, elodieLogG, elodieFeH, elodieZ
from DR16.specObj
into MyDB.specObj'''

# retrieve PhotoObj
query_PhotoObj = '''select top 1000000
  objID, type, clean, ra, dec, specObjID, u, g, r, i, z, nObserve, nDetect, nEdge, score
from DR16.PhotoObj
into MyDB.PhotoObjA'''