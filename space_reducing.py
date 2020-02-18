def space_reduce(string: str) -> str:
    # replace multiple space for single
    return ' '.join(string.split())


if __name__ == '__main__':
    space_string = input('Input string\n')
    print(space_reduce(space_string))
