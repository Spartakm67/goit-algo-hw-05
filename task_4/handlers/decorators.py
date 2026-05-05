def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Give me name and phone please."

        except IndexError:
            return "Enter the required arguments."

        except KeyError:
            return "Contact not found."

    return inner