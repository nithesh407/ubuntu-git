from twilio.rest import Client
account_sid = "account id"
auth_token = "provided by the account"
client = Client(account_sid, auth_token)
client.messages.create(from_="twilio account number", body="message", to="receiver number")

