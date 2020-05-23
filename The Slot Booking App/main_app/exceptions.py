# -*- coding: utf-8 -*-

class AppException(Exception):
    pass

class AuthenticationFailure(AppException):
    http_response_code = 401
    error_code = 1001
    message = "Username/Password are not provided or incorrect"


class EmailAlreadyRegistered(AppException):
    http_response_code = 406
    error_code = 1003
    message = "Email already registered. Use a different email"


class TimeSlotClash(AppException):
    http_response_code = 406
    error_code = 1004
    message = "TimeSlot not available"


class UnauthorizedAccess(AppException):
    http_response_code = 401
    error_code = 1005
    message = "unauthorized access"

class UnAcceptableEmail(AppException):
    http_response_code=406
    error_code =1006
    message ="email invalid"


class InvalidRequest(AppException):
    http_response_code=400
    error_code =1007
    message ="invalid request"

class DateTimeformatMisMatch(AppException):
    http_response_code=400
    error_code=1008
    message='the format of date and time should be %m-%d-%Y and %H:%M:%S respectively'


class SignUpParametersExpected(AppException):
    http_response_code=400
    error_code=1011
    message="signup parameters not fulfilled.Either (email/password/name) or (g/fb access token) not provided"
