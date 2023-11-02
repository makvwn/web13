def palindrom(string: str) -> bool:
    string = string.replace(" ", "")
    count = 0
    string_len = len(string)
    for i in range(string_len):
        if string[i] == string[string_len - i - 1]:
            count += 1
    if count == string_len:
        return True 
    return False

 