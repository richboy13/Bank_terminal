import json

def main_menu():
    """
    Отображает главное меню и обрабатывает выбор пользователя.
    """
    print('\n1. Создать аккаунт')
    print('2. Войти в личный кабинет.')
    action = int(input('\nВыберите действие (1 или 2): '))
    if action == 1:
        create_account()
    if action == 2:
        login_result = login()
        if login_result:
            _login = login_result
            is_active = True
            while is_active:
                print('\n1. Просмотр баланса')
                print('\n2. Пополнить баланс')
                print('3. Депозит средств.')
                print('4. Перевод средств между счетами')
                print('5. История транзакций')
                print('6. Выход')
                action = int(input('\nВыберите действие (1, 2, ...): '))
                if action == 1:
                    view_balance(_login)
                if action == 2:
                    add_to_balance(_login)
                if action == 3:
                    deposit(_login)
                if action == 4:
                    transfer(_login)
                if action ==5:
                    transaction_history(_login)
                if action == 6:
                    is_active  = logout()



def create_account():
    """
    Создает новую учетную запись.
    """
    with open('data.json', 'r') as file:
        data = json.load(file)
    login = input('Enter login: ')
    password = input('Enter password: ')
    new_account = {
        "login": login,
        "password": password,
        "balance": 0,
        "deposit": 0,
        "history": []
    }
    data.setdefault('bank_data', []).append(new_account)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    print('Account created successfully.')


def login():
    """
    Вход в существующую учетную запись.
    """
    with open('data.json', 'r') as file:
        bd = json.load(file)
    _login = input('Enter login: ')
    password = input('Enter password: ')
    for account in bd.get('bank_data', []):
        if account["login"] == _login and account["password"] == password:
            print('Login and password are correct')
            return _login
    print('Wrong login or password')
    return False




def view_balance(login):
    """
    Показывает текущий баланс учетной записи.
    """
    with open('data.json', 'r') as file:
        data = json.load(file)
    for acc in data.get('bank_data', []):
        if acc["login"] == login:
            balance = acc['balance']
            print(f'Баланс для пользователя {login}: {balance}')
            return
    print(f'Пользователь {login} не найден.')


def add_to_balance(login):
    """
    Пополнить баланс
    """
    with open('data.json', 'r') as file:
        db = json.load(file)
    for acc in db.get('bank_data', []):
        if acc["login"] == login:
            balance = acc['balance']
            history = acc.get("history", [])
            print('Пополнение баланса.')
            sum = int(input('\nНапишите на какую сумму желаете пополнить баланс: '))
            balance += sum
            history.append(f'Вы пополнили баланс на сумму {sum}.')

            print(f'Вы пополнили баланс на сумму {sum}.')
            print(f'Ваш баланс составляет {balance}.')

            acc['balance'] = balance
            acc['history'] = history
            break
    with open('data.json', 'w') as file:
        json.dump(db, file, indent=4)



def deposit(login):
    """
    Депозит средств на счет.
    """
    with open('data.json', 'r') as file:
        data = json.load(file)
    for acc in data.get('bank_data', []):
        if acc["login"] == login:
            deposit = acc['deposit']
            print(f'Депозит для пользователя {login}: {deposit}')
            return
    print(f'Пользователь {login} не найден.')


def transfer(login):
    """
    Перевод средств между счетами.
    """
    with open('data.json', 'r') as file:
        db = json.load(file)

    for acc in db.get('bank_data', []):
        if acc["login"] == login:
            balance = acc['balance']
            _deposit = acc['deposit']
            history = acc.get("history", [])

            print('\n1. Перевод средств между счетами. Выберите действие:')
            print('\n1. Перевод средств с баланса на депозит.')
            print('2. Перевод средств с депозита на баланс.')
            action = int(input('\nВыберите действие (1 или 2): '))

            if action == 1:
                sum = int(input('Напишите сумму перевода: '))
                if sum <= balance:
                    _deposit += sum
                    balance -= sum
                    history.append(f'Вы перевели с баланса на депозит сумму {sum}.')
                    print(f'Ваш баланс составляет: {balance}')
                    print(f'Ваш депозит составляет: {_deposit}')
                else:
                    print('Недостаточно средств на депозите.')

            elif action == 2:
                sum = int(input('Напишите сумму перевода: '))
                if sum <= _deposit:
                    balance += sum
                    _deposit -= sum
                    history.append(f'Вы перевели с депозита на баланс сумму {sum}.')
                    print(f'Ваш баланс составляет: {balance}')
                    print(f'Ваш депозит составляет: {_deposit}')
                else:
                    print('Недостаточно средств на депозите.')

            for acc in db.get('bank_data', []):
                if acc["login"] == login:
                    acc['balance'] = balance
                    acc['deposit'] = _deposit
                    acc['history'] = history

    with open('data.json', 'w') as file:
        json.dump(db, file, indent=4)

def transaction_history(_login):
    """
    Показывает историю транзакций по счету.
    """
    with open('data.json', 'r') as file:
        data = json.load(file)
    for acc in data.get('bank_data', []):
        if acc["login"] == _login:
            history = acc.get("history", [])
            if history:
                print(f"История транзакций для пользователя {_login}:")
                print(history)
            else:
                print(f"У пользователя {_login} нет истории транзакций.")
            return


def logout():
    """
    Выход из учетной записи.
    """
    print("Выход из учетной записи.")
    return False


if __name__ == "__main__":
    main_menu()

