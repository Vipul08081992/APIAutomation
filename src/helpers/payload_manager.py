def payload_create_booking():
    payload={
        "firstname": "Atul",
        "lastname": "Singh",
        "totalprice": 111,
        "depositpaid":True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_token():
    payload={
        "username" : "admin",
        "password" : "password123"
    }
    return payload

def payload_put_load():
    payload={
            "firstname": "Pramod",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    return payload