# SLOT BOOKING
#
## Api Authentication


## There are two types of auth tokens-
    * authentication token
        * type basic auth 
            * require authorization id token
            * require authorization password token
        * its for managing one's meetings and timeslots

#
    * Slot Booking authorization token
        * type basic auth
            * requires meeting id token
            * requires meeting password token
        * it can be get in response by hitting the calender link provided by the user from his signup signin response

        * this is required for anyone to book meeting or see available time slots on some calendly user calender.
#
### After Logging  in User wants to
    * create,delete time slots
    * create or delete meetings on their own time slots
     use basic auth type of authentication with 
     - id from authorization id token
     -password from authorization password token
     which can be retrieved from the user signin
    
### When a user wants to book a meeting slots,he/she can book with the help of their logging token id
    
    # that person needs to have meeting id token and meeting password token for basic auth authorization which the  registered user can provide for the person using the api http://{url}/calender?calender_id={token}.
#

#
#
