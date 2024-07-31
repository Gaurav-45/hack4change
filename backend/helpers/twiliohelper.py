# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from dotenv import load_dotenv
load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


def makeCall(receiver_ph, voice_message):
    response = VoiceResponse()
    response.say(voice_message, language="hi-IN", voice="Polly.Aditi")

    call = client.calls.create(
        from_=os.getenv("TWILIO_NUMBER"),
        to=receiver_ph,
        twiml=str(response)
    )
    print("call made", call.sid)

def makeSMS(receiver_ph, text_message):
    # message = client.messages.create(
    #     from=os.getenv("TWILIO_NUMBER"),
    #     body=text_message,
    #     to=receiver_ph
    # )
    message = client.messages.create(from_=os.getenv("TWILIO_NUMBER"),
    body=text_message,
    to=receiver_ph
    )
    print("message send", message.sid)