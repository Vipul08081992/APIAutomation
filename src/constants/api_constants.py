#Add constants here:

class APIConstants(object):
    #1. Base url
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    #2. Create booking url:
    @staticmethod
    def create_booking_url():
        return "https://restful-booker.herokuapp.com/booking"

    #3. Create token
    @staticmethod
    def create_token_url():
        return "https://restful-booker.herokuapp.com/auth"

    #4. Update- PUT, PATCH, DELETE with variable booking Id
    def get_update_delete_url(self,bookingId):
        return "https://restful-booker.herokuapp.com/booking/" + str(self.bookingId)
