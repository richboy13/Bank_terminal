accounts = {}  # Словарь для хранения информации об учетных записях


def main_menu(login):
    """
    Отображает главное меню и обрабатывает выбор пользователя.
    """
    print(f'\nWelcome, {login}')
    is_active = True
    while is_active:
        print('\n1. Просмотр баланса')
        print('2. Депозит средств.')
        print('3. Перевод средств между счетами')
        print('4. История транзакций')
        print('5. Выход')
        action = int(input('\nВыберите действие (1, 2, ...): '))
        if action == 1:
            view_balance(login)
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


def login():
    """
    Вход в существующую учетную запись.
    """
    login = input('Enter login: ')
    password = input('Enter password: ')
    if accounts[login] == password:
        main_menu(login)
    else:
        print('Wrong login or password')


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
