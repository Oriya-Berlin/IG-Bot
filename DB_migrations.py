"""
def splitit(date):
    date = date.split('-')
    return date

import json
with open('/home/berlin/Desktop/targets.json', 'r') as file:
    data = json.load(file)
    for dic in data:
        new_target = Targets()
        new_target.target_name = dic['target_name']
        new_target.shooter_name = dic['shooter_name']
        date = splitit(dic['target_followed_date'])
        new_target.target_followed_date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        new_target.story_watched = int(dic['story_watched'])
        new_target.is_following_canceled = False
        session.add(new_target)
        session.commit()
        session.close()

'''
x = datetime.datetime.strptime('30-01-12', '%d-%m-%y').date()
y = datetime.date(2012, 1, 30)
print(type(x))
print(type(y))
'''



"""
'''
import json
with open('/home/berlin/Desktop/followers.json', 'r') as file:
    data = json.load(file)
    for dic in data:
        new_follower = Followers()
        new_follower.follower_name = dic['follower_name']
        new_follower.follow_at_name = dic['follow_at_name']
        new_follower.effected_by_bot = bool(dic['effected_by_bot'])  #need to change to int()
        session.add(new_follower)
        session.commit()
        session.close()

'''