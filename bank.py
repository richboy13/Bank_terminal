def main_menu():
    """
    Отображает главное меню и обрабатывает выбор пользователя.
    """
    pass


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
        main_menu()
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
