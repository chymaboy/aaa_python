def check(s):
    # return success or fail for string
    s = s.replace(' ', '')
    while len(s) > 0:
        if s == s.replace('[]', '').replace('()', '').replace('{}', ''):
            return 'fail'
        else:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
    return 'success'


if __name__ == '__main__':
    brackets = input('Input string of brackets\n')
    print(check(brackets))
