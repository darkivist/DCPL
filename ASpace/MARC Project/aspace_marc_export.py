import requests
import json
from os.path import join
import time
from datetime import datetime
import random
import os

start_time = datetime.now()

#enter aspace api endpoint and admin credentials
aspace_url = 'http://localhost:8089'
username = 'admin'
password = 'admin'

#enter pathway to directory where xml will be saved
marc_directory = '/Users/admin/desktop/marc'

if not os.path.exists(marc_directory):
    os.makedirs(marc_directory)

auth = requests.post(aspace_url + '/users/'+username+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session}
#change repo number accordingly
all_ids = requests.get(aspace_url+'/repositories/6/resources?all_ids=true', headers=headers).json()

def pad_id(resource_id):
    file_id = str(resource_id)
    while len(file_id) < 4:
        file_id = '0' + file_id
    return file_id

for resource_id in all_ids:
    file_id = pad_id(resource_id)
#change repo number accordingly
    marc = requests.get(aspace_url+'/repositories/6/resources/marc21/'+str(resource_id)+'.xml',headers=headers, stream=True)
    with open(join(marc_directory, file_id +'.xml'),'wb') as marc_out:
         for chunk in marc.iter_content(10240):
                marc_out.write(chunk)
    print "Wrote {0}".format(resource_id)

print "Done"

end_time = datetime.now()

print "Script start time:", start_time.strftime("%Y-%m-%d %H:%M:%S %p")
print "Script end time:", end_time.strftime("%Y-%m-%d %H:%M:%S %p")
print "Script running time:", end_time - start_time

exporter_stats = "Script start time: " + start_time.strftime("%Y-%m-%d %H:%M:%S %p") + "\n" + "Script end time: " +  end_time.strftime("%Y-%m-%d %H:%M:%S %p") + "\n" + "Script running time: " + str(end_time - start_time)
#enter pathway to directory where stats will be saved
stats_file = open('/Users/admin/desktop/marc/export_stats/export_stats.txt','w')
stats_file.write(exporter_stats)
stats_file.close()
