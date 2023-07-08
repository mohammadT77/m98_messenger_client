import requests

SERVER_BASE_URL = 'http://localhost:8000'

def get_user(username, password):
    return requests.get(
        SERVER_BASE_URL+'/user',
        headers={
            'USERNAME': username,
            'PASSWORD': password
        }
    )

def register(name, username, password):
    return requests.post(
        SERVER_BASE_URL+'/user',
        json={
            'name':name, 
            'username': username,
            'password':password
        }
    )

def change_name(id, name, username, password):
    # TODO: PATCH '/user'
    pass

def create_new_message(username, password, receiver_username, content):
    return requests.post(
        SERVER_BASE_URL+'/message',
        headers={
            'USERNAME': username,
            'PASSWORD': password,
        },
        json={
            'to_user': receiver_username,
            'content': content
        }
    )

def fetch_inbox(username, password):
    return requests.get(
        SERVER_BASE_URL+'/message/inbox',
        headers={
            'USERNAME': username,
            'PASSWORD': password,
        }
    )

def fetch_sentbox(username, password):
    return requests.get(
        SERVER_BASE_URL+'/message/sent',
        headers={
            'USERNAME': username,
            'PASSWORD': password,
        }
    )