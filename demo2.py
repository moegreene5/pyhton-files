while True:
    text = input('>')
    if text == 'quit':
        break
    elif text == 'tired':
        continue
    else:
        print(text)
else:
    print('this loop is done!!')