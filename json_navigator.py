import json


def reading_json(file):
    '''
    str -> dict
    Function reads json file
    and returns dictionary
    '''
    with open(file, mode='r', encoding='utf-8') as rd:
        json_read = json.load(rd)

    return json_read


def json_navigation(json_read):
    '''
    Function navigates user in
    json dictionary
    '''
    step_set = set()

    for step in json_read:
        step_set.add(step)
    navigate = input('Enter one of the list words to go to the next '
                     'json step or enter 0 to go to the first stage '
                     'enter 1 to exit: \n' + str(step_set) + '\n')
    if navigate == '1':
        return quit()

    elif navigate == '0':
        return json_navigation(reading_json(file='json_api.json'))

    elif navigate not in step_set:
        print('You entered the wrong word! Try again')
        return json_navigation(json_read)

    elif navigate in step_set:
        if type(json_read[navigate]) == dict:
            print(str(json_read[navigate]) + ' - this is the result')
            return json_navigation(json_read[navigate])
        else:
            print(str(json_read[navigate]) + ' - this is the final result')
            stay = input('Enter 1 to quit or 0 to go to the first stage of json: ')
            if stay == '1':
                quit()
            elif stay == '0':
                return json_navigation(reading_json(file='json_api.json'))
            else:
                print('You entered the wrong word! Try again')
                return json_navigation(json_read)


if __name__ == '__main__':
    print(json_navigation(reading_json('json_api.json')))
