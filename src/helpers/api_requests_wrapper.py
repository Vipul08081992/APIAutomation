#Make POST,GET,PUT,PATCH,DELETE
import json
import requests

# Http Requests - Generic Functions

#1. Get data:
def get_data(url,auth,headers,in_json):
    response=requests.get(url=url,auth=auth,headers=headers)
    if in_json is True:
        return response.json()
    return response

#2. Post data:
def post_data(url,auth,headers,payload,in_json):
    response = requests.post(url=url, auth=auth, headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

#3. Patch_data:
def patch_data(url,auth,headers,payload,in_json):
    response = requests.patch(url=url, auth=auth, headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

#4. Put data:

def put_data(url,auth,headers,payload,in_json):
    response = requests.put(url=url, auth=auth, headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

#5. Delete data

def delete_data(url,auth,headers,payload,in_json):
    response = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return response.json()
    return response