# Import an HTTP library 
import requests
import json 
from pprint import pprint
#entered_street = input("Enter Street:")

def DataAccess(entered_street,entered_date):
# Make the request 
   print("sending request")

   r = requests.get('https://www.stlouis-mo.gov/powernap/stlouis/api.cfm/requests.json?',
   params={'api_key':"MTU3MDIxNDg5NjMwNjAuODk1NDE4MzI4NDYx",
   'start_date':entered_date+" 00:00:00",'end_date': entered_date+" 00:00:00"}
   )
   output_list =[]
# The returned data 
   json_response = r.json()
   print("response received")
   length = len(json_response)
   print(length)
   print(json_response)
#print(length)
   for i in range(length):
      print("I IS:",i)
      resp = json_response[i]
      if (entered_street in resp['ADDRESS']):
         output_list.append(resp)
         
         
         
#print(length)
   return output_list