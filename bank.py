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
                    pass
                if action == 3:
                    deposit(login)
                if action == 4:
                    transfer(login)
                if action ==5:
                    transaction_history(login)
                if action == 6:
                    logout()



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
        "history": ""
    }
    data.setdefault('bank_data', []).append(new_account)
    with open('data.json', 'w') as file:
        json.dump(data, file)

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




def deposit(account_id):
    """
    Депозит средств на счет.
    """
    with open('data.json', 'r') as file:
        data = json.load(file)
    for acc in data.get('bank_data', []):
        if acc["login"] == login:
            balance = acc['deposit']
            print(f'Депозит для пользователя {login}: {balance}')
            return
    print(f'Пользователь {login} не найден.'


def transfer(account_id):
    """
    Перевод средств между счетами.
    """
    pass


def transaction_history(account_id):
    """
    Показывает историю транзакций по счету.
    """
    pass


def logout():
    """
    Выход из учетной записи.
    """
    pass


if __name__ == "__main__":
    main_menu()

