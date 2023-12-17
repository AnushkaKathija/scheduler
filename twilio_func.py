from twilio.rest import Client
account_sid='US0bed1f40ab950237ac2b3384ce6acf35' # Add your Twilio Acoounts SID'
auth_token='F9ZPFTW1DW4VNTRCK65TMSTM'
client= Client(account_sid, auth_token)
def send_rem(date,rem):
    message=client.messages.create 
    from_='whatsapp:+14155238886'
    body='*REMINDER* '+date+'\n' +rem,
    to='whatsapp:7676459198'

print(messages.sid)
