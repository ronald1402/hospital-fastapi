import enum


class MessageType(enum.Enum):
    SUCCESS = ["000", "SUCCESS", "Service run successfully"]
    INVALID_PARAM = ["001", "INVALID_PARAM", "Parameter is blank or invalid"]
    USER_NOT_EXIST = ["002", "USER_NOT_EXIST", "User not found or unregistered before"]
    USER_EXISTED = ["003", "USER_EXISTED", "User has registered before"]
    EMAIL_NOT_VALID = ["004", "EMAIL_NOT_VALID", "Email not valid"]
    AUTHENTICATION_FAILED = ["005", "AUTHENTICATION_FAILED", "Authentication not valid"]
    DB_FAIL_CONNECT = ["006", "DB_FAIL_CONNECT", "Connection to DB failed"]

    def getMessageDetail(errorType):
      errorDetail =  {
            "messageCode":errorType.value[0],
            "messageName": errorType.value[1],
            "messageDetail": errorType.value[2]
                      }
      return errorDetail
