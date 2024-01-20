from src.helpers.api_requests_wrapper import post_data
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_hearder_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_status_code,verify_response_key_not_none
import pytest
class Test_create_booking:

#Test1: with valid payload
    @pytest.mark.positive
    def test_create_booking_1(self):
        #URL, Payload,Headers
        response=post_data(url=APIConstants.create_booking_url(),auth=None,headers=common_hearder_json(),payload=payload_create_booking(),in_json=False)
        print(response.json())
        verify_response_key_not_none(response.json()["bookingid"])
        verify_status_code(actual_code=response.status_code,expected_code=200)
        return response.json()["bookingid"]


#Test2: without payload
    @pytest.mark.negative
    def test_create_booking_2(self):
        #URL, Payload,Headers
        response=post_data(url=APIConstants.create_booking_url(),auth=None,headers=common_hearder_json(),payload={},in_json=False)
        print(response.text)
        verify_status_code(actual_code=response.status_code,expected_code=500)
