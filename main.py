# This is a sample Python script.
import requests
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def jprint(obj):
    text = json.dumps(obj,sort_keys=True, indent=4)
    print(text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    authentication = {
        'email':'makar.stozhyk@gmail.com',
        'password':'Mak0806199'
    }

    response = requests.post("https://api.onupkeep.com/api/v2/auth/",data=authentication)


    jprint(response.json())
    print('----------Token----------')
    api_token = response.json()['result'].get('sessionToken')


    headers = {'Session-Token': api_token}

    get_list_of_assets = requests.get('https://api.onupkeep.com/api/v2/assets',headers=headers)

    jprint(get_list_of_assets.json())



    # response = requests.get("http://api.open-notify.org/astros.json")
    # jprint(response.json())
    #
    # parameters = {
    #     "lat": 40.71,
    #     "lon": -74
    # }
    #
    # response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    #
    # jprint(response.json())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
