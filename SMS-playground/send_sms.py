
from twilio.rest import Client

account_sid = '[AccSID]'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12062032013',
    body='Thanks for your order! On a scale of 1-10 would you recommend [this program] to a friend? '
         'Reply with the number 1 to 10 to this message',
    to='[number]'
)

print(message.sid)
