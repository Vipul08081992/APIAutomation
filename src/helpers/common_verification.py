# HTTPS Status Verification:

def verify_status_code(actual_code,expected_code):
    assert actual_code == expected_code,"Status code is not as expected i.e is" + expected_code

def verify_key_not_null(key):
    assert key != 0,"Key is not null" +key
    assert key >0, "Key is not zero"

def verify_response_key_not_none(key):
    assert key is not None

def verify_response_time():
    pass

