import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+916380795844")
print(geocoder.description_for_number(phone_number1, "en"))

