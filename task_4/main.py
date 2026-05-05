from handlers import parse_input, COMMANDS


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        handler = COMMANDS.get(command)

        if handler:
            print(handler(args, contacts))
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()