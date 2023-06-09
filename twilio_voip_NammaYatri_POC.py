import time
import requests
from twilio.rest import Client

# Twilio account credentials
account_sid = 'write_your_twilio_sid'
auth_token = 'write_your_twilio_auth_token'
client = Client(account_sid, auth_token)

# phone numbers
from_number = 'call_from_this_number_of_twilio'
to_number = 'call_this_number'

# make a call and record the audio
call = client.calls.create(
    twiml='<Response><Say>Hello, this is a test call.</Say></Response>',
    to=to_number,
    from_=from_number,
    record=True
)

# wait for the recording to be available
while len(call.recordings.list()) == 0:
    time.sleep(1)

# retrieve recording URL
recording_url = call.recordings.list()[0].uri

# download audio file
response = requests.get(recording_url)
with open('E:/twilio_voip/Recorded_twilio.m4a', 'wb') as f:
    f.write(response.content)

# print call SID to track the call
print(call.sid)