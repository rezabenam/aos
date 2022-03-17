from faker import Faker
fake = Faker(locale='en_CA')

#------------------ %&%-------------------------------

aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = ' Advantage Shopping'


# -------------------- data section ---------------------------------
new_username = fake.last_name()
new_password = fake.password()
new_email = fake.email()
print(new_username, new_password,new_email)
first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()
country = fake.current_country()
city = fake.city()[:10]
address = fake.address().replace("\n"," ")[:20]
province = fake.province()
postalcode = fake.postcode()
sentence = fake.sentence()[:100]

safepay_username = 'reza1'
safepay_password =  'Password1'


#------------------ %&%-------------------------------
print(new_username, new_password, new_email)


