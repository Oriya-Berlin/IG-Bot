from bot_functions import *
from DB_functions import *


#######################################################################################################
"""
    * login via another user (not one of the shooters client) -> 
    * iterate each shooter from shooters list (must get array as parameter) ->
    * open every shooter followers list ->
    * all followers list to array ->
    * insert every new follower to the DB if he does'nt exist.
"""


def update_shooter_followers_table(driver, username, password, shooters_list):

    login(driver, username, password)
    SLEEP(4)

    not_now_window(driver)
    SLEEP(3)

    for shooter in shooters_list:

        search(driver, shooter)
        SLEEP(3)

        find_user_in_search_result(driver, shooter)
        SLEEP(3)

        open_followers_list_in_current_page(driver)
        SLEEP(3)

        scroll_all_followers_list(driver, shooter)
        SLEEP(5)

        followers_list = all_followers_to_list(driver)
        print(len(followers_list))

        for follower in followers_list:
            insert_follower_to_DB(follower, shooter)


#######################################################################################################
"""
    * take an array of targets -> 
    * iterate each target followers list ->
    * filter users that's already exist in DB ->
    * follow and watch story ->
    * insert the new targets to the DB.
"""


def start_shooting(driver, username, password, shooter, targets_list):
    login(driver, username, password)
    SLEEP(8)

    not_now_window(driver)
    SLEEP(3)

    for target in targets_list:

        search(driver, target)
        SLEEP(3)

        find_user_in_search_result(driver, target)
        SLEEP(3)

        open_followers_list_in_current_page(driver)
        SLEEP(3)

        scroll_all_followers_list(driver, target)
        SLEEP(5)

        followers_list = all_followers_to_list(driver)
        print(len(followers_list))

        close_followers_list(driver)
        SLEEP(1)

        driver.refresh()
        SLEEP(3)

        for follower in followers_list:

            search(driver, follower)
            SLEEP(4)

            success = find_user_in_search_result(driver, follower)
            if success:   # need to test that

                SLEEP(3)
                follow_in_current_page(driver)
                SLEEP(2)

                watch_story(driver, follower)
                SLEEP(2)

                boolean = close_story(driver)
                SLEEP(1)

                if not is_he_in_my_targets(follower, shooter):
                    insert_target_to_DB(follower, shooter, boolean)

                SLEEP(1)
            else:
                clean_search_box(driver)


#######################################################################################################
"""
    * get an array of expired targets from DB -> 
    * search each expired target on instagram ->
    * unfollow him ->
    * change target status on DB.
"""


def unfollow_targets(driver, shooter, diff):  # need to test that
    expired_list = get_expired_targets(shooter, diff)

    for follower in expired_list:

        search(driver, follower)
        SLEEP(3)

        success_1 = find_user_in_search_result(driver, follower)
        SLEEP(3)

        if success_1:
            success_2 = unfollow_in_current_page(driver)
            SLEEP(2)
            if success_2:
                change_target_status(follower, shooter)
        else:
            clean_search_box(driver)

#######################################################################################################
"""
    * take an array of targets -> 
    * iterate each target followers list ->
    * filter users that's already exist in DB ->
    * follow and watch story ->
    * insert the new targets to the DB.
"""


def get_report_of_shooter():
    pass


#######################################################################################################

