from menu import generate_menu_from_dict, get_input
import api_requests as api
import actions
from actions import UsernamePassword

menu_route = {
    'name': 'M98 Messenger Client',
    'description': 'A CLI (menu) Client for m98_messenger server',
    'children': [
        {
            'name': 'Create new message',
            'action': actions.create_message
        },
        {
            'name': 'Inbox',
            'action': actions.inbox
        },
        {
            'name': 'Sent',
            'action': actions.sentbox
        },
        {
            'name': 'Logout',
            'action': actions.logout
        }
    ]
}

root_menu = generate_menu_from_dict(menu_route)


if __name__ == '__main__':
    username = get_input("Username: ")
    password = get_input("Password: ")

    # Try to get user from server to validate username and password
    get_user_response = api.get_user(username, password)
    if get_user_response.status_code == 200:
        print("Welcome", get_user_response.json().get('name',''))
        UsernamePassword.CURRENT = UsernamePassword(username, password)

    elif get_user_response.status_code == 403:
        # User not found
        print("Invalid username and password")
        if get_input("Do you want to register? (Y/n)", target_type=lambda ans:ans.lower()=='y'):
            actions.register()
        else:
            exit()
    else:
        print("Server error:", get_user_response.status_code)
        exit()


    root_menu()

    