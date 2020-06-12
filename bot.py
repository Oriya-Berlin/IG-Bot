from selenium import webdriver
from shooter_details import password, username, shooters_list
from bot_functions import *
from operations import *
from selenium.webdriver.common.keys import Keys



path = 'https://www.instagram.com/'
driver = webdriver.Chrome('/home/berlin/PycharmProjects/IG_Bot/Driver/chromedriver')
#driver = webdriver.Firefox('/home/berlin/PycharmProjects/IG_Bot/Driver/geckodriver')
driver.get(path)  # maybe that the problem !!!
SLEEP(3)


total_list = ['sapir.zisman', 'itsalexdaniel', 'roeyamos', 'morelleheller', 'mr.landsman', 'pazoshran',
     'result_academy', 'motivate.way', 'yuval_hass', 'iccm_college', 'barak_bit']




#collect_targets(driver, '', '', '', ['iccm_college'])

#start_shooting(driver, '', '', '')


#update_shooter_followers_table(driver, username, password, shooters_list)
#get_report_of_shooter('ben_liba')
"""
login(driver, '', '')
SLEEP(3)

save_your_login_info_window(driver)
SLEEP(5)  # need to add more time

not_now_window(driver)
SLEEP(3)
"""
#unfollow_targets(driver, 'ben_liba', 3)

"""
search(driver, 'ben_liba')
SLEEP(3)

find_user_in_search_result(driver, 'ben_liba')
SLEEP(3)

open_followers_list_in_current_page(driver)
SLEEP(5)
"""
"""
my_element = ''
elements = driver.find_elements_by_tag_name('div')
for element in elements:
    if element.get_attribute('role') == 'presentation':
        my_element = element
        print(type(my_element))
        break
"""
"""
my_element = driver.find_element_by_tag_name('html')
for i in range(20):
    print(type(my_element))
    #my_element.location_once_scrolled_into_view
    #my_element.send_keys(Keys.PAGE_DOWN)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    current = driver.current_window_handle()
    driver.
    SLEEP(2)
"""

"""
followers = driver.find_elements_by_tag_name('li')
loaded_till_now = len(followers)
total_followers = get_followers_number_on_PUBLIC_account(driver)  # maybe also with private
total_followers = int(total_followers)
print(total_followers)


while (loaded_till_now < total_followers):
    print(loaded_till_now)
    try:
        SLEEP(1)
        followers[loaded_till_now - 30].location_once_scrolled_into_view
        SLEEP(2.5)
        followers = driver.find_elements_by_tag_name('li')
        loaded_till_now = len(followers)
    except:
        print('NO')
        continue
"""

users = get_expired_targets('ben_liba', 3)
print(len(users))
"""
for user in users:
    driver.get(f'https://www.instagram.com/{user}/')
    SLEEP(4)
    driver.refresh()
    SLEEP(3)

    success_2 = unfollow_in_current_page(driver)
    SLEEP(2)
    if success_2:
         change_target_status(user, 'ben_liba')
    print(f'{user}   {success_2}')
"""
