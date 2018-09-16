'''
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC6dde4f2c5dec01ff9c5c650567f2e811'
auth_token = '5f5708895de328cd555d6184a5e539b1'
client = Client(account_sid, auth_token)

call = client.calls.create(
    to='+17472558546',
    from_='+15052787618',
    url="https://demo.twilio.com/welcome/voice/",
)

print(call.sid)
'''
import os
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for

from twilio.twiml.voice_response import VoiceResponse, Say
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "AC6dde4f2c5dec01ff9c5c650567f2e811"
TWILIO_AUTH_TOKEN = "5f5708895de328cd555d6184a5e539b1"
TWILIO_CALLER_ID = "+15052787618"
TWILIO_APP_SID = "AP7c382977057944c9bcb2367679f8fabb"

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')


# Route for Click to Call demo page.
@app.route('/')
def index():
    return jsonify({'Hello': 'World!'})



# Voice Request URL
@app.route('/call', methods=['POST'])
def call():
    # Get phone number we need to call
    phone_number = '+17472558546'
    try:
        twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    except Exception as e:
        msg = 'Missing configuration variable: {0}'.format(e)
        return jsonify({'error': msg})

    try:
        twilio_client.calls.create(from_=TWILIO_CALLER_ID,
                                   to=phone_number,
                                   url='https://api.twilio.com/2010-04-01/Accounts/AC6dde4f2c5dec01ff9c5c650567f2e811/Calls')
        #my_response = VoiceResponse()
        #my_response.dial()
        #my_response.say("We've been notified of a call. Are you OK? Say Yes if you are. With other response, we will contact emergency medical services for immediate support.",
        #    voice='woman', language='en-US', loop = 3)

        #return str(my_response)

    except Exception as e:
        app.logger.error(e)
        return jsonify({'error': str(e)})


@app.route('/outbound', methods=['POST'])
def outbound():
    my_response = VoiceResponse()

    my_response.say("Thank you for contacting checking in. We have notified emergency medical services",
                 voice='alice')
    # Uncomment this code and replace the number with the number you want
    # your customers to call.
    return str(my_response)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    if port == 5000:
        debug = True
    app.run(host='0.0.0.0', port=port)


