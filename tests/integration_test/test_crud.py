from src.helpers.api_requests_wrapper import post_data,get_data,patch_data,put_data,delete_data
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_hearder_json
from src.helpers.payload_manager import payload_create_booking,payload_create_token,payload_put_load
from src.helpers.common_verification import verify_status_code,verify_response_key_not_none
import pytest

class Test_complete_booking_process:

#Create Token
    @pytest.mark.positive
    @pytest.fixture()
    def test_create_token(self):
        response=post_data(url=APIConstants.create_token_url(),
        auth=None,headers=common_hearder_json(),
        payload=payload_create_token(),in_json=False)
        print(response.json())
        verify_response_key_not_none(["token"])
        verify_status_code(actual_code=response.status_code,expected_code=200)
        return response
#Create Booking
    @pytest.fixture()
    def test_create_booking(self):
        response = post_data(url=APIConstants.create_booking_url(), auth=None, headers=common_hearder_json(),
                             payload=payload_create_booking(), in_json=False)
        print(response.json())
        verify_response_key_not_none(response.json()["bookingid"])
        verify_status_code(actual_code=response.status_code, expected_code=200)
        return response.json()["bookingid"]


#Booking ids
    def test_get_all_booking(self):
        response =get_data(url=APIConstants.create_booking_url(),
                           auth=None,headers=common_hearder_json(),in_json=False)
        print(response.json())
        verify_status_code(actual_code=response.status_code, expected_code=200)
#Booking detail of specific id
    def test_get_booking_by_id(self,test_create_booking):

        response = get_data(url=APIConstants.get_update_delete_url(bookingId=test_create_booking),
                        auth=None,
                        headers=common_hearder_json(), in_json=False)
        print(response.json())
        verify_status_code(actual_code=response.status_code, expected_code=200)

    def test_complete_update(self,test_create_booking):
        url=APIConstants.get_update_delete_url(bookingId=test_create_booking)
        response=put_data(url=url,auth=None,headers=common_hearder_json(),payload=payload_put_load(),in_json=False)
        print(response.json())
        verify_status_code(actual_code=response.status_code, expected_code=200)
    def test_delete_booking(self,test_create_booking):
        url = APIConstants.get_update_delete_url(bookingId=test_create_booking)
        response = delete_data(url=url, auth=None, headers=common_hearder_json(), payload=None, in_json=False)
        print(response.text)
        verify_status_code(actual_code=response.status_code, expected_code=201)






