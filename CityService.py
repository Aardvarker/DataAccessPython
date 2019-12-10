
class CityService:
    
    def SERVICE_NAME(self):
        return self.SERVICE_NAME
    def REQUESTED_DATETIME(self):
       return self.REQUESTED_DATETIME
    def STATUS_NOTES(self):
        return self.STATUS_NOTES
    def SERVICE_CODE(self):
        return self.SERVICE_CODE
    def ZIPCODE(self):
        return self.ZIPCODE
    def SERVICE_NOTICE(self):
        return self.SERVICE_NOTICE
    def UPDATED_DATETIME (self):
        return self.UPDATED_DATETIME
    def AGENCY_RESPONSIBLE (self):
        return self.AGENCY_RESPONSIBLE
    def STATUS (self):
        return self.STATUS
    def MEDIA_URL (self):
        return self.MEDIA_URL
    def DESCRIPTION (self):
        return self.DESCRIPTION
    def EXPECTED_DATETIME (self):
        return self.EXPECTED_DATETIME
    def ADDRESS (self):
        return self.ADDRESS
    def SERVICE_REQUEST_ID (self):
        return self.SERVICE_REQUEST_ID
    def LAT (self):
        return self.LAT
    def ADDRESS_ID (self):
        return self.ADDRESS_ID
    def LONG (self):
        return self.LONG
    
    
 

    def __init__(self,fill_list):
        self.SERVICE_NAME = fill_list[0]
        self.REQUESTED_DATETIME = fill_list[1]
        self.STATUS_NOTES = fill_list[2]
        self.SERVICE_CODE = fill_list[3]
        self.ZIPCODE = fill_list[4]
        self.SERVICE_NOTICE = fill_list[5]
        self.UPDATED_DATETIME = fill_list[6]
        self.AGENCY_RESPONSIBLE = fill_list[7]
        self.STATUS_NOTES = fill_list[8]
        self.MEDIA_URL = fill_list[9]
        self.DESCRIPTION= fill_list[10]
        self.EXPECTED_DATETIME = fill_list[11]
        self.ADDRESS = fill_list[12]
        self.SERVICE_REQUEST_ID = fill_list[13]
        self.LAT = fill_list[14]
        self.ADDRESS_ID = fill_list[15]
        self.LONG = fill_list[16]
        

