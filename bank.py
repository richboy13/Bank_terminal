
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
                view_balance(login, account)
            if action == 2:
                deposit(login)
            if action == 3:
                transfer(login)
            if action == 4:
                transaction_history(login)
            if action == 4:
                logout()



def create_account():
    """
    Создает новую учетную запись.
    """
    global accounts
    login = input('Enter login: ')
    password = input('Enter password: ')
    accounts[login] = password

    print(len(accounts))


def login():
    """
    Вход в существующую учетную запись.
    """
    _login = input('Enter login: ')
    password = input('Enter password: ')
    if accounts[_login] == password:
        main_menu()
        return True
    else:
        print('Wrong login or password')
        return False



def view_balance(account_id):
    """
    Показывает текущий баланс учетной записи.
    """
    pass


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

