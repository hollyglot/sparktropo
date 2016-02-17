from httplib import HTTPConnection

# This script is also using the Tropo module, 'say'.
# Usually, you would import it:
#
# from tropo import say
#
# However, since this script is on Tropo's server,
# the 'tropo' module is automatically imported.

##
# Post message to the messages API on the heroku app
#
def send(message):
    conn = HTTPConnection('your_app.herokuapp.com')
    conn.request('POST', '/messages', body=message)

##
# Receive text and post it
#
def main():
    say("Processing your request...")
    message = currentCall.initialText
    send(message)
    say("Message posted!")

main()