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
