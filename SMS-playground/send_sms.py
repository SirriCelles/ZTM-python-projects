
from twilio.rest import Client

account_sid = 'AC592825489a89fcd520ca601e7b3493b4'
auth_token = '3169bde7e7f956d18694d80ff2e6fe8c'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12062032013',
    body='Thanks for your order! On a scale of 1-10 would you recommend [this program] to a friend? '
         'Reply with the number 1 to 10 to this message',
    to='+237670756565'
)

print(message.sid)
