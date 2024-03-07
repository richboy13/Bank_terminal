import json


def main_menu():
    """
    Отображает главное меню и обрабатывает выбор пользователя.
    """
    pass


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


def login():
    """
    Вход в существующую учетную запись.
    """
    pass


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
