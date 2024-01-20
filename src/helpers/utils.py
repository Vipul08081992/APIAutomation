#Common headers

def common_hearder_json():
    headers={
        "Content-Type": "application/json",
        "Accept":"application/json",
        "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers

def common_hearder_xml():
    headers={
        "Content-Type": "application/xml",
        "Accept":"application/xml",
        "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers

#Read data from Excel,csv,json,ymal - Keep the function in future
 