from .decorators import input_error

def handle_hello(args, contacts):
    return "How can I help you?"


@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return "This contact already exists."
    
    if phone in contacts.values():
        return "This phone number already exists."
    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        raise KeyError
    
    if phone in contacts.values() and contacts[name] != phone:
        return "This phone number already exists."

    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]

    return contacts[name]

@input_error
def show_all(args, contacts):
    if not contacts:
        return "No contacts found."

    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)

@input_error
def delete_contact(args, contacts):
    name = args[0]

    del contacts[name] 
    return "Contact deleted."

COMMANDS = {
    "hello": handle_hello,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "delete": delete_contact,
} 