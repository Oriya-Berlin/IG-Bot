import time


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