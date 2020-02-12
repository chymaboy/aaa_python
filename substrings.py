def contain(x, s):
    r = [y for y in x if s in y]
    return r


if __name__ == '__main__':
    sub_string = input('Input substring\n')
    n = int(input('Input len of array\n'))
    first_string = []
    for i in range(n):
        first_string.append(input('Input string\n'))
    print(contain(first_string, sub_string))
