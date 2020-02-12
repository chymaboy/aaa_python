def check(string):
    # return success or index of wrong bracket
    string = string.replace(' ', '')
    match = {'(': ')', '{': '}', '[': ']'}
    opens_b = ['[', '(', '{']
    # list of pairs [bracket, index]
    opens = []
    for i, s in enumerate(string):
        # открывающая скобка
        if s in opens_b:
            # кладем в список
            opens.append([s, i])
        else:
            # есть открывающие скобки
            if len(opens) > 0:
                # совпадает с последней открывающей скобкой
                if s != match[opens.pop()[0]]:
                    return i + 1
            else:
                return i + 1
    if len(opens) == 0:
        return 'Success'
    else:
        return opens[0][1] + 1


if __name__ == '__main__':
    brackets = input('Input string of brackets\n')
    print(check(brackets))
