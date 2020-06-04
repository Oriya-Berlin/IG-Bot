from bot_functions import *
from DB_functions import *
from report_functions import *


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

    save_your_login_info_window(driver)
    SLEEP(3)

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

        updated_followers_list = all_followers_to_list(driver)
        print(len(updated_followers_list))

        for follower in updated_followers_list:
            insert_follower_to_DB(follower, shooter)

        # ----------------------------------------- need to test that
        old_followers_list = get_all_followers_from_DB(shooter)

        for old_follower in old_followers_list:
            if old_follower in updated_followers_list:
                continue
            else:
                delete_follower_from_Followers_table(old_follower, shooter)


#######################################################################################################
"""
    * take an array of targets -> 
    * iterate each target followers list ->
    * filter users that's already exist in DB ->
    * follow and watch story ->
    * insert the new targets to the DB.
"""


def start_shooting(driver, username, password, shooter):  # need to test that
    login(driver, username, password)
    SLEEP(8)

    save_your_login_info_window(driver)
    SLEEP(3)

    not_now_window(driver)
    SLEEP(3)
#
    """
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
        """
#
    targets_list = get_targets_from_OnHold_table(shooter)
    for target in targets_list:

        search(driver, target)
        SLEEP(4)

        success = find_user_in_search_result(driver, target)
        if success:   # need to test that

            SLEEP(3)
            follow_in_current_page(driver)
            SLEEP(2)

            watch_story(driver, target)
            SLEEP(2)

            boolean = close_story(driver)
            SLEEP(1)

            if not is_he_in_my_targets(target, shooter):
                insert_target_to_Targets_table(target, shooter, boolean)
                delete_target_from_OnHold_table(target, shooter)
            else:
                delete_target_from_OnHold_table(target, shooter)

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
    * grab all bot successes from Followers table -> 
    * push them into ordered dict ->
    * print them to new txt file.
"""


def get_report_of_shooter(shooter):
    successes_dict = get_bot_successes_for_report(shooter)
    print_report_to_txt_file(shooter, successes_dict)


#######################################################################################################
"""
    * take a list of arsenals (users with mass of followers or with potential followers) -> 
    * iterate every arsenal and grab all his followers ->
    * insert every follower to 'OnHold' table under the specific shooter.
"""


def collect_targets(driver, username, password, shooter, arsenal_targets_list):  # need to test & look at that again

    login(driver, username, password)
    SLEEP(8)

    save_your_login_info_window(driver)
    SLEEP(3)
    
    not_now_window(driver)
    SLEEP(3)

    for arsenal in arsenal_targets_list:

        search(driver, arsenal)
        SLEEP(3)

        find_user_in_search_result(driver, arsenal)
        SLEEP(3)

        open_followers_list_in_current_page(driver)
        SLEEP(3)

        scroll_all_followers_list(driver, arsenal)
        SLEEP(5)

        followers_list = all_followers_to_list(driver)
        print(len(followers_list))

        for follower in followers_list:
            insert_target_to_OnHold_table(follower, arsenal, shooter)

        close_followers_list(driver)
        SLEEP(1)

        driver.refresh()
        SLEEP(3)


#######################################################################################################
"""
    * take a list of arsenals (users with mass of followers or with potential followers) -> 
    * iterate every arsenal and grab all his followers ->
    * insert every follower to 'OnHold' table under the specific shooter.
"""


def many_shooters_operation():
    pass


#######################################################################################################
