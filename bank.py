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
        is_active = login()
        while is_active:
            print('\n1. Просмотр баланса')
            print('\n2. Пополнить баланс')
            print('3. Депозит средств.')
            print('4. Перевод средств между счетами')
            print('5. История транзакций')
            print('6. Выход')
            action = int(input('\nВыберите действие (1, 2, ...): '))
            if action == 1:
                view_balance(login)
            elif action == 2:
                deposit(login)
            elif action == 3:
                transfer(login)
            elif action == 4:
                transaction_history(login)
            elif action == 5:
                logout()
            elif action == 6:
                is_active = False
            else:
                print('Некорректный выбор. Пожалуйста, выберите снова.')



def create_account(data={}):
    """
    Создает новую учетную запись.
    """
    accounts = {}
    login = input('Enter login: ')
    password = input('Enter password: ')
    accounts[login] = password
    accounts['balance'] = 0
    accounts['deposit'] = 0
    accounts['history'] = ""
    data['bank_data']= [accounts]
    with open('data.json', 'w') as file:
        json.dump(data, file)

    print(len(accounts))


def login():
    """
    Вход в существующую учетную запись.
    """
    with open('data.json', 'r') as file:
        bd = json.load(file)
    _login = input('Enter login: ')
    password = input('Enter password: ')
    for account in bd.get('bank_data', []):
        if _login in account and account[_login] == password:
            print('Login and password are correct')
            return _login, account
        else:
            print('Wrong login or password')
            return False



def view_balance(_login):
    """
    Показывает текущий баланс учетной записи.
    """
    with open('data.json', 'r') as file:
        bd = json.load(file)
    _login, account = login()
    for account in bd.get('bank_data', []):
        balance = str(account[_login]["balance"])
        print(f'Баланс для пользователя {login}: {balance}')



def deposit(account_id):
    """
    Депозит средств на счет.
    """
    pass


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

