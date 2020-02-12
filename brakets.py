def check(s):
    s = s.replace(' ', '')
    while len(s) > 0:
        if s == s.replace('[]', '').replace('()', '').replace('{}', ''):
            return 'wrong'
        else:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
    return 'right'


if __name__ == '__main__':
    brackets = input('Input string of brackets\n')
    print(check(brackets))
