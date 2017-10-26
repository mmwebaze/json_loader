import requests, json, base64
import os

status = 200
selected_secrets = 1
#resource_folder = 'resources'
resource_folder = 'myfolders'

def load_secrets(secrets):
    return json.load(open(secrets, 'r'))

def post_payload(jsonPayload):
    credentials = load_secrets('secrets.json')
    baseUrl = credentials['credentials'][selected_secrets]['baseUrl']
    print('Running pay load : '+jsonPayload+' -> '+baseUrl )
    strlog = ('%s:%s' % (credentials['credentials'][selected_secrets]['username'], credentials['credentials'][selected_secrets]['password']))
    base64string = base64.b64encode(bytes(strlog, 'ascii'))
    headers = {"Authorization": "Basic %s" % base64string.decode('utf-8'), 'Accept' : 'application/json', "Content-Type": "application/json"}
    payLoad = json.load(open(resource_folder+'/'+jsonPayload, 'r'))
    #print(payLoad)
    baseFileName = base = os.path.basename(jsonPayload)
    dashboard = os.path.splitext(baseFileName)[0]
    url = baseUrl+dashboard
    req = requests.post(url, data=json.dumps(payLoad), headers=headers)

    if status == req.status_code:
        print(req.text)
    else:
        req = requests.put(url, data=json.dumps(payLoad), headers=headers)
        print(req.text)

def list_directory_files(path):
    dirs = os.listdir(path)
    for file in dirs:
        print('Posting Payload '+file)
        post_payload(file)

if __name__ == "__main__":
    cwd = os.getcwd()
    list_directory_files(cwd+'/'+resource_folder)
