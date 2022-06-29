email = input('Введите почтовый адрес: ')
if "@" not in email:
    print("It isn't email adress")
else:
    email = email.split('@')
    if email[1] == 'gmail.com':
        print('@'.join(email))
    else:
        print('DOMAIN NAME is not supported')
