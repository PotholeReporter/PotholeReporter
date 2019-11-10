import twilio
from twilio.rest import Client
import os

geo=os.popen("echo -n `curl 'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?location=-96.751911,32.985675&f=json&langCode=EN' -s | jq '.address.Match_addr'`").read();

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC458d3cd4cbdae013a326c661bcdded49'
auth_token = '282d3ddfbb0268fd2fa87ec46213c624'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='The pothole at {} has been reported to the government.'.format(geo),
         from_='+15184123454',
         media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
         to='+18179664080'
     )

print(message.sid)
