if __name__ == '__main__':
    u = str(input())

    for s in u:

        if s.isalnum():
            print('True')
            break
    else:
        print('False')

    for s in u:

        if (s.isalpha()):
            print('True')
            break
    else:
        print('False')

    for s in u:
        if (s.isnumeric()):
            print(s.isnumeric())
            break
    else:
        print('False')

    for s in u:

        if (s.islower()):
            print('True')
            break
    else:
        print('False')

    for s in u:

        if (s.isupper()):
            print('True')
            break
    else:
        print('False')

