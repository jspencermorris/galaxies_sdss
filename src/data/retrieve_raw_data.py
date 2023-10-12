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


# retrieve zoo + Spec + Photo
query_galaxySpecPhoto = '''select top 1000000
z.specobjid, z.objid as dr8objid, z.dr7objid, z.ra, z.dec, z.nvote_tot, z.nvote_std, z.nvote_mr1,
z.nvote_mr2, z.nvote_mon, z.p_el, z.p_cw, z.p_acw, z.p_edge, z.p_dk, z.p_mg, z.p_cs,
s.instrument, s.z as redshift, s.class as sdss_class_string, s.subClass as sdss_subclass_string, s.class_noqso,
s.subClass_noqso, s.spectroFlux_u, s.spectroFlux_g, s.spectroFlux_r, s.spectroFlux_i, s.spectroFlux_z,
s.spectroSynFlux_u, s.spectroSynFlux_g, s.spectroSynFlux_r, s.spectroSynFlux_i, s.spectroSynFlux_z,
s.elodieObject, s.elodieSpType, s.elodieBV, s.elodieTEff, s.elodieLogG, s.elodieFeH, s.elodieZ,
p.type as sdss_class_number, p.clean, p.u, p.g, p.r, p.i, p.z, p.nObserve, p.nDetect, p.nEdge, p.score
from DR16.PhotoObj as p
join DR16.SpecObj as s
on p.objid = s.bestobjid
join DR16.zooVotes as z
on p.objid = z.objid
into MyDB.galaxySpecPhoto'''


# retrieve 
query_otherSpecPhoto = '''select top 1000000
s.bestobjid as dr8objid, s.specObjID,
s.instrument, s.z as redshift, s.class as sdss_class_string, s.subClass as sdss_subclass_string, s.class_noqso,
s.subClass_noqso, s.spectroFlux_u, s.spectroFlux_g, s.spectroFlux_r, s.spectroFlux_i, s.spectroFlux_z,
s.spectroSynFlux_u, s.spectroSynFlux_g, s.spectroSynFlux_r, s.spectroSynFlux_i, s.spectroSynFlux_z,
s.elodieObject, s.elodieSpType, s.elodieBV, s.elodieTEff, s.elodieLogG, s.elodieFeH, s.elodieZ,
p.type as sdss_class_number, p.clean, p.u, p.g, p.r, p.i, p.z, p.nObserve, p.nDetect, p.nEdge, p.score
from DR16.SpecObj as s
join DR16.PhotoObj as p
on s.bestobjid = p.objid
where s.class <> "GALAXY"
into MyDB.otherSpecPhoto'''