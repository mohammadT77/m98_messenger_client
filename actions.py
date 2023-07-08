import requests
import api_requests as api


class UsernamePassword:
    CURRENT = None
    username: str
    password: str

    def __init__(self, username, password) -> None:
        self.username, self.password = username, password

def register():
    # TODO
    pass

def create_message():
    receiver_username = input("Enter receiver username: ")
    content = input("Enter message content: ")
    resp = api.create_new_message(UsernamePassword.CURRENT.username, UsernamePassword.CURRENT.password,
                           receiver_username, content)
    
    print("Response:",resp)
    # TODO: handler response

def inbox():
    resp = api.fetch_inbox(UsernamePassword.CURRENT.username, UsernamePassword.CURRENT.password)
    if resp.status_code == 200:
        messages_list = resp.json()['messages']
        for m in messages_list:
            print(m)
    else:
        print("Response error:", resp.status_code, resp)



def sentbox():
    # TODO
    pass


def logout():
    UsernamePassword.CURRENT = None
    exit()