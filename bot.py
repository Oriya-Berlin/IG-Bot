from selenium import webdriver
from shooter_details import password, username, shooters_list
from bot_functions import *
from operations import *




path = 'https://www.instagram.com/'
driver = webdriver.Chrome('/home/berlin/PycharmProjects/IG_Bot/Driver/chromedriver')
driver.get(path)  # maybe that the problem !!!
SLEEP(3)


total_list = ['sapir.zisman', 'itsalexdaniel', 'roeyamos', 'morelleheller', 'mr.landsman', 'pazoshran',
     'result_academy', 'motivate.way', 'yuval_hass', 'iccm_college']

current_list = ['motivate.way', 'morelleheller']

update_shooter_followers_table(driver, username, password, shooters_list)

#if __name__ == "__main__":
#start_shooting(driver, username, password, shooter, current_list)


'''
login(driver, username, password)
SLEEP(4)

not_now_window(driver)
SLEEP(3)

search(driver, shooter)
SLEEP(3)

clean_search_box(driver)
'''
'''
login(driver, username, password)
SLEEP(4)

not_now_window(driver)
SLEEP(3)

search(driver, target)
SLEEP(3)

find_user_in_search_result(driver, target)
SLEEP(3)

open_followers_list_in_current_page(driver)
SLEEP(3)

close_followers_list(driver)
SLEEP(1)



x = watch_story(driver, target)
SLEEP(2)
print(x)
y = close_story(driver)
print(y)
'''

'''
x = ['cris_brokers', 'meshy_ezra', 'nyce_hyann', 'ana.pauladandrea']
for i in x:
    search(driver, i)
    SLEEP(3)

    find_user_in_search_result(driver, i)
    SLEEP(3)

    follow_in_current_page(driver)
    SLEEP(2)

    watch_story(driver, i)
    SLEEP(2)

    close_story(driver)
    SLEEP(1)
'''



#open_followers_list_in_current_page(driver)
#SLEEP(3)

#scroll_all_followers_list(driver, target)
#SLEEP(5)

#f_list = all_followers_to_list(driver)
#print(len(f_list))

#for i in f_list:
#    insert_follower_to_DB(i, target)




#is_followed(driver)

#unfollow_in_current_page(driver)


#print(is_followed(driver))
'''
follow_in_current_page(driver)
SLEEP(2)
driver.refresh()
SLEEP(3)
print(is_followed(driver))
SLEEP(1)
driver.quit()
'''

#watch_story(driver, target)




#is_followed(driver)

#unfollow_in_current_page(driver)


#print(is_followed(driver))
'''
follow_in_current_page(driver)
SLEEP(2)
driver.refresh()
SLEEP(3)
print(is_followed(driver))
SLEEP(1)
driver.quit()
'''

#watch_story(driver, target)

