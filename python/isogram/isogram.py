def is_isogram(string):
    if len(string) == 0:
        return True
    else:
        for aChar in string.lower():
            if aChar.isalpha():
                if string.lower().count(aChar) != 1:
                    return False
        return True