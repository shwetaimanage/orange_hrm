import json

def get_datastore():
    with open('users.json', 'r') as f:
        datastore = json.load(f)
    return datastore


def get_users(user_type):
    datastore = get_datastore()
    if user_type == 'admin':
        return datastore['users_to_login']['admin']
    elif user_type == 'normal_user':
        return datastore['users_to_login']['normal_user']

def get_url():
    datastore = get_datastore()
    return datastore["url"]


def users_to_add():
    datastore = get_datastore()
    return datastore['users_to_add']



