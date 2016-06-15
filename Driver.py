from EntryModel import EntryModel


def print_help():
    """Prints a list of commands."""
    print 'help : gives a list of commands'
    print 'exit : terminates app'
    print 'write [username]/[message] : writes a message as the username given'


def print_all_messages(messages):
    """Prints all messages currently stored in memory."""
    for message in messages:
        print message.to_string()


def create_initial_messages():
    """Creates initial data in memory. Used for testing."""
    test_message_a = EntryModel("Donald Trump", "Make America Great Again")
    test_message_b = EntryModel("Raymond Wu", "Sounds like a great idea!")
    return [test_message_a, test_message_b]


def guest_book_driver():
    """Main loop of project. """
    messages = create_initial_messages()
    print 'Welcome to mediocre guestbook app. Enter "help" for instructions.'
    while True:
        user_input = raw_input('Command: ')
        if user_input == "help":
            print_help()
        elif user_input == "exit":
            print 'Exiting guestbook app!'
            break
        elif user_input.startswith("write"):
            user_input = user_input[6:]  # take out the first 6 characters in user_input, gets rid of "write "
            username = user_input.split("/")[0]
            message = user_input.split("/")[1]
            new_message = EntryModel(username,message)
            messages.append(new_message)
        elif user_input == "show":
            print_all_messages(messages)
        else:
            print 'Invalid input. Enter "help" for instructions.'


if __name__ == "__main__":
    guest_book_driver()