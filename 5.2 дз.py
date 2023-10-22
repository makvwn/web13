def restore_capitalization(text):
    result = ""
    capitalize_next = True

    for char in text:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char.lower()
        else:
            result += char
            if char in ".!?":
                capitalize_next = True

    return result

