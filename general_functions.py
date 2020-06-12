import time
import datetime


# sleep function
def SLEEP(seconds):
    time.sleep(seconds)


# extract number from string and convert him
def extract_and_convert_number(string):
    string = string.split(' ')
    number = string[0].replace(',', '')

    if 'k' in number:
        number = number.replace('k', '')
        number = int(number) * 1000
        return number
    else:
        number = int(number)
        return number


# get url string and return only the name from the url
def clean_url(url):
    url = url.split('/')
    user_name = url[3]
    return user_name


# boolean, check the difference between current date, to the date we start to follow on some target
def check_date_diff(diff, bot_action_date):  # maybe we need to add 'shooter' and 'target' column as a parameters
    now = datetime.date.today()
    delta = (now - bot_action_date).days
    if delta == diff:
        return True
    return False


# calculate, convert and round the ratio value
def calculate_ratio(following_num, followers_num):

    if followers_num == 0:
        followers_num = 1
    if following_num == 0:
        following_num = 1

    following_num = float(following_num)
    followers_num = float(followers_num)
    ratio = float(following_num/followers_num)
    ratio = round(ratio, 5)
    return ratio

