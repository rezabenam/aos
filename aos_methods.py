import sys
from selenium import webdriver # import selenium to the file
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
import time
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # <-- add this import for drop down lists
from selenium.webdriver.common.keys import Keys


print('---------------*%*----------------')
print('---------------*%*----------------')

s = Service(executable_path='/Users/reza/PycharmProjects/pythonProject/chromedriver')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'The testing was started at: {datetime.datetime.now()}')
    print('---------------*%*----------------')
    print(f'Chrome web browser  is opened')
    driver.implicitly_wait(30)
    # 2. Maximize the browser window.
    driver.maximize_window()
    time.sleep(.3)
    # 3. Navigate to web page URL - https://advantageonlineshopping.com/ (Links to an external site.)
    driver.get(locators.aos_url)
    time.sleep(2)
    # 4. Check URL and home page title are as expected.
    print(driver.current_url)
    print(driver.title)
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')
    else:
        print(f' Something is wrong. Check the URL of the web page!')
    print('---------------*%*----------------')

    print('1-Check that SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE texts are displayed')
def checkDisplayedItems():
    list = ['speakersTxt', 'laptopsTxt', 'miceTxt', 'headphonesTxt', 'tabletsTxt']
    time.sleep(2)
    for i in range(len(list)):
        assert driver.find_element(By.ID, list[i]).is_displayed()
        print(f'"{list[i]}" IS DISPLAYED.')
    print('SO IT IS CONFIRMED THAT ALL THE TEXT ARE DISPLAYED!----')
    time.sleep(0.2)
    print('---------------*%*----------------')

    print('2-Click by SPECIAL OFFER, POPULAR ITEMS and CONTACT US links at the top nav menu are clickable')
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    driver.implicitly_wait(30)
    assert driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').is_enabled()
    driver.implicitly_wait(30)
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    driver.implicitly_wait(30)
    assert driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').is_enabled()
    time.sleep(0.2)
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    driver.implicitly_wait(30)
    assert driver.find_element(By.LINK_TEXT, 'CONTACT US').is_enabled()
    print('CLCKABLE\'S TEXT AND ITEMS IN TE FIRST PAGE WERE VERIFIED---')
    print('---------------*%*----------------')

    print('3-Check main logo is displayed')
    driver.implicitly_wait(30)
    assert driver.find_element(By.XPATH, '//span[contains(.,"DEMO")]').is_displayed()
    print('MAIL LOGO WAS DISPLAYED---')
    print('---------------*%*----------------')

    #Check CONTACT US form is working properly
    print('4-Check CONTACT US form is working properly')
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'categoryListboxContactUs').click()
    driver.implicitly_wait(30)
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs' )).select_by_visible_text('Laptops')
    time.sleep(2)
    driver.find_element(By.NAME, 'categoryListboxContactUs').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'productListboxContactUs').click()
    time.sleep(2)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('HP Chromebook 14 G1(ES)')
    time.sleep(2)
    driver.find_element(By.NAME, 'productListboxContactUs').click()
    time.sleep(2)

    # driver.find_element(By.NAME, 'emailContactUs').click()
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.new_email)
    time.sleep(2)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.sentence)
    time.sleep(2)
    driver.find_element(By.ID, 'send_btnundefined').click()
    time.sleep(2)
    assert driver.find_element(By.XPATH , '//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()
    assert driver.find_element(By.XPATH , '//p[contains(.,"Thank you for contacting Advantage support.")]').is_enabled()
    print('TATYANA_QQ:does "is_enabled" means "is_clickable"?')
    assert driver.find_element(By.XPATH , '//a[contains(.," CONTINUE SHOPPING ")]').is_displayed()
    assert driver.find_element(By.XPATH , '//a[contains(.," CONTINUE SHOPPING ")]').is_enabled()
    time.sleep(2)
    driver.find_element(By.XPATH , '//a[contains(.," CONTINUE SHOPPING ")]').click()
    time.sleep(2)
    print('CONTACT US FORM WORKS PROPERLY!')

    print('---------------*%*----------------')


    # 5. Check bottom Social Media links are displayed and clickable.
    print('5. Check bottom Social Media links are displayed and clickable.')
    assert driver.find_element(By.NAME, 'follow_facebook').is_displayed
    time.sleep(0.5)
    assert driver.find_element(By.NAME, 'follow_facebook').is_enabled
    time.sleep(0.5)
    assert driver.find_element(By.NAME, 'follow_twitter').is_displayed
    time.sleep(0.5)
    assert driver.find_element(By.NAME, 'follow_twitter').is_enabled
    time.sleep(0.5)
    assert driver.find_element(By.NAME, 'follow_linkedin').is_displayed
    time.sleep(0.5)
    assert driver.find_element(By.NAME, 'follow_linkedin').is_enabled
    print('SOCIAL MEDIA LINNKS ARE SHOWN AND WORKS PROPERLY!')
    print('---------------*%*----------------')


def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        time.sleep(2)
        driver.close()
        driver.quit()


# Create New Account - using Faker library fake data
def create_new_user():
    driver.find_element(By.ID, 'menuUserLink').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT , 'CREATE NEW ACCOUNT').click()
    time.sleep(2)
    driver.find_element(By.NAME,'usernameRegisterPage').send_keys(locators.new_username)
    time.sleep(.3)
    driver.find_element(By.NAME,'emailRegisterPage').send_keys(locators.new_email)
    time.sleep(.3)
    driver.find_element(By.NAME,'passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.NAME,'confirm_passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(1)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    time.sleep(1)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    time.sleep(1)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    time.sleep(1)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    time.sleep(1)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    time.sleep(1)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    time.sleep(1)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.city)
    time.sleep(1)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
    time.sleep(1)
    x = driver.find_element(By.NAME, 'i_agree').is_selected()
    if x == False :
        driver.find_element(By.NAME, 'i_agree').click()
    else :
        print('there is a problem in registering')
        driver.close()
    time.sleep(2)
    driver.find_element(By.ID, 'register_btnundefined').click()
    time.sleep(1)
    print(f' the registered  username is  : "{locators.new_username}" and password is: "{locators.new_password}"')
    # logger('created')


# Logout
def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print('---------------*%*----------------')
    print(f'The {driver.current_url} was closed at: {datetime.datetime.now()}')
    # driver.close()
    # driver.quit()


# login
def log_in():
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')
    else:
        print(f' Something is wrong. Check the URL of the web page!')
    time.sleep(2)
    driver.find_element(By.ID, 'menuUser').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    driver.find_element(By.NAME,'password').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.ID,'sign_in_btnundefined').click()
    time.sleep(4)
    # CHECK-LOGIN
    x = driver.find_element(By.XPATH, f'//*[@id="menuUserLink"]/span[contains(.,"{locators.new_username}")]').is_displayed()
    print(x)
    if x == True:
        print(f' login was successful')
    else:
        print(f' THERE IS A PROBLEM- CAN YOU HELP ME PLEASE FIND IT??')


#logger
def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.new_email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


# setUp()
# checkDisplayedItems()
# create_new_user()
# log_out()
# log_in()
# logger('created')
# tearDown()

