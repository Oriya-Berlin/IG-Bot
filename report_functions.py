from create_tables import *
import datetime


# dict format, sorted by dates (dates = keys)
def get_bot_successes_for_report(shooter):
    result = session.query(Followers).filter(Followers.follow_at_name == shooter,
                                             Followers.effected_by_bot == True).all()
    successes_dict = {}

    for res in result:
        date = str(res.date_of_success)

        if date not in successes_dict:
            successes_dict[date] = []

        successes_dict[date].append(res.follower_name)
    return successes_dict


# create txt file, print sorted data in text file
def print_report_to_txt_file(shooter, successes_dict):
    today = date_of_today()
    today = today.replace('/', '-')
    path = f"/home/berlin/Desktop/{shooter+' '+today}.txt"
    open(path, "x")  # create

    with open(path, 'w') as report:
        report.write(f' *** Report for user: {shooter} *** \n')
        generate_spaces_in_txt_file(report, 2)

        for key, values in successes_dict.items():

            report.write('-' * 45 + '\n')
            report.write(f' Followers from date: {key}.   Total: {len(values)} \n')
            report.write('-' * 45 + '\n')

            for value in values:
                report.write(f' {value} \n')

            generate_spaces_in_txt_file(report, 2)


# for clean code
def date_of_today():
    today = datetime.datetime.now()
    return today.strftime("%x")


# for clean code
def generate_spaces_in_txt_file(file_obj, number):
    for i in range(number):
        file_obj.write('\n')


#x = get_bot_successes_for_report('ben_liba')
#print_report_to_txt_file('ben_liba', x)
old = [1, 2, 3, 4, 5]
new = [5,6,7,8,9,0,3]
for i in old:
    if i in new:
        continue
    else:
        print(f'{i} NOT')
'''
def print_ordered_data(successes_dict, shooter):

    print(f' *** Report for user: {shooter} ***')
    generate_spaces(2)

    for key, values in successes_dict.items():

        print('-' * 45)
        print(f' Followers from date: {key}. Total: {len(values)}')
        print('-' * 45)

        for value in values:
            print(value)

        generate_spaces(2)

'''
