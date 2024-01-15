from src.helpers.api_requests_wrapper import post_data,get_data,patch_data,put_data,delete_data
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_hearder_json
from src.helpers.payload_manager import payload_create_booking,payload_create_token
from src.helpers.common_verification import verify_status_code,verify_response_key_not_none
import pytest

class Test_complete_booking_process:

#Create Token
    @pytest.mark.positive
    def test_create_token(self):
        response=post_data(url=APIConstants.create_token_url(),
        auth=None,headers=common_hearder_json(),
        payload=payload_create_token(),in_json=False)
        print(response.json())
        verify_response_key_not_none(["token"])
        verify_status_code(actual_code=response.status_code,expected_code=200)
        return response
#Create Booking
    def test_create_booking(self):
        response = post_data(url=APIConstants.create_booking_url(),
                             auth=None, headers=common_hearder_json(),
                             payload=payload_create_booking(), in_json=False)
        print(response.json())
        verify_response_key_not_none(response.json()["bookingid"])
        verify_status_code(actual_code=response.status_code, expected_code=200)
        return response.json()["bookingid"]

#Booking ids
    def test_get_all_booking(self):
        response =get_data(url=APIConstants().create_booking_url(),
                           auth=None,headers=common_hearder_json(),in_json=False)
        print(response.json())
        verify_response_key_not_none(response.json()["bookingid"])
        verify_status_code(actual_code=response.status_code, expected_code=200)
#Booking detail of specific id
    def test_get_booking_by_id(self):

        response = get_data(url=APIConstants().get_update_delete_url(bookingId=self.test_create_booking()),
                        auth=None,
                        headers=common_hearder_json(), in_json=False)
        print(response.json())
        verify_status_code(actual_code=response.status_code, expected_code=200)

#Update partial details
    def test_partial_update(self):
        token=self.test_create_token
        patch_url = APIConstants.create_booking_url() + "/" +str(self.test_create_booking().json()["bookingid"])
        response=patch_data(url=patch_url, auth, headers, payload, in_json):
    def test_complete_update(self):
        pass
    def test_delete_booking(self):
        pass



    def test_create_booking_1(self):
        #URL, Payload,Headers
        response=post_data(url=APIConstants.create_booking_url(),auth=None,headers=common_hearder_json(),payload=payload_create_booking(),in_json=False)
        print(response.json())
        verify_response_key_not_none(response.json()["bookingid"])
        verify_status_code(actual_code=response.status_code,expected_code=200)
        booking_id=response.json()["bookingid"]
        print(booking_id)

