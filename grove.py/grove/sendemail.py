# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import sendgrid
from sendgrid import SendGridAPIClient
import os

geo=os.popen("curl 'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?location=-96.751911,32.985675&f=json&langCode=EN' | jq '.'").read();

#from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import *
message = Mail(
   from_email='Pothole Reporter <hackutdaa@gmail.com>',
   to_emails=['sebastian.thomas.king@gmail.com','potpopo1234@gmail.com'],  #nicktindle@outlook.com
   subject='A pot hole has been dectected',
   html_content=geo)
try:
   api_key='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'
   sg = SendGridAPIClient(api_key)
   response = sg.send(message)
   print(response.status_code)
   print(response.body)
   print(response.headers)
except Exception as e:
   print("Error", e.message)
