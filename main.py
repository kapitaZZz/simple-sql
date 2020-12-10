import sqlite3
from random import randint

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
            )""")

db.commit()


def registration():
    '''
    Add user in database
    '''
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()

        print('Registered!')
    else:
        print('Error, data exists!')


def delete_db():
    sql.execute(f'DELETE FROM users WHERE login = "{user_login}"')
    db.commit()

    print('Record deleted')


def casino():
    '''
    Imitate casino game
    '''
    global user_login
    user_login = input('Log in: ')
    dice = randint(1, 2)

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    balance = sql.fetchone()[0]

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Wrong login.')
        registration()
    else:
        if dice == 1:
            sql.execute(f'UPDATE users SET cash = {1000 + balance} WHERE login = "{user_login}"')
            db.commit()
        else:
            print('-')
            delete_db(user_login)


def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)


def run():
    casino()
    enter()


run()
