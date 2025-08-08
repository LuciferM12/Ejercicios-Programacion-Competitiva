while True:
    try:
        inputUser = input()
        date = inputUser.split('/')
        if int(date[2]) >= 74:
            fourDigit = date[0] + '/' + date[1] + '/19' + date[2] 
        else:
            fourDigit = date[0] + '/' + date[1] + '/20' + date[2]
        print(fourDigit)
    except EOFError:
        break
    