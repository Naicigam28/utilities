import requests
import json
import csv
from tqdm import tqdm
access = "TOKEN GOES HERE"
payload={}


url = f'''https://graph.microsoft.com/v1.0/applications'''
    

headers = {
    'Authorization':'Bearer '+ access
}

response = requests.request("GET", url, headers=headers, data=payload,timeout=10)
data=json.loads(response.text)
if(data.get('error')!=None or data.get('error') !='None'):
    print(data)
    groups=data['value']
    hasNext=True
    while (hasNext):
        response = requests.request("GET", data['@odata.nextLink'], headers=headers, data=payload)
        data=json.loads(response.text)
        for group in data['value']:
            groups.append(group)

        if(data.get('@odata.nextLink')==None or data.get('@odata.nextLink')=='None'):
            print("Done!")
            hasNext=False


    file = open('./apps1.csv', 'w', newline ='')
    with file: 
        # identifying header   
        header = groups[0].keys() 
        writer = csv.DictWriter(file, fieldnames = header)

        for group in tqdm(groups):
            writer.writerow(group)
            #print(f'''{group['id']}\t{group['displayName']}''')
    
        

else:
    print(data['error']['message'])