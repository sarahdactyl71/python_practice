def reverse(self, x):
    reversed_string = str(x)[::-1]
    if '-' in reversed_string:
        a = reversed_string.strip('-')
        return -int(a)
    else:
        return int(reversed_string)