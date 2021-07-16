def sequence(arg):
    string = arg
    if len(string) > 0:
        for i in range(1, len(string)):
            if '()' in string:
                answer = string.replace("()", "")
                string = answer
                if answer == '':
                    return True
            else:
                return False