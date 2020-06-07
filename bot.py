from selenium import webdriver
from shooter_details import password, username, shooters_list
from bot_functions import *
from operations import *




path = 'https://www.instagram.com/'
driver = webdriver.Chrome('/home/berlin/PycharmProjects/IG_Bot/Driver/chromedriver')
driver.get(path)  # maybe that the problem !!!
SLEEP(3)


total_list = ['sapir.zisman', 'itsalexdaniel', 'roeyamos', 'morelleheller', 'mr.landsman', 'pazoshran',
     'result_academy', 'motivate.way', 'yuval_hass', 'iccm_college', 'barak_bit']




#collect_targets(driver, '', '', '', ['iccm_college'])

#start_shooting(driver, '', '', '')


#update_shooter_followers_table(driver, username, password, shooters_list)

login(driver, username, password)
SLEEP(3)

save_your_login_info_window(driver)
SLEEP(3)

not_now_window(driver)
SLEEP(3)

search(driver, 'aviel_dayan')
SLEEP(3)

find_user_in_search_result(driver, 'aviel_dayan')
SLEEP(3)


# for private pages 'following' number
print('PRIVATE')
elements = driver.find_elements_by_tag_name('span')
for element in elements:
     inner_text= element.get_attribute('innerHTML')
     try:
          exist = inner_text.endswith(' following')
          if exist:
               z = element.text
               print(z)
               print(inner_text)
               print(exist)
     except:
          pass

# for public pages 'following' number
print('PUBLIC')
