#  #
from random import sample
import string
import csv


def next_step():
    next_s = input("new data base input <ENTER>")
    return next_s


def make_data_base():
    name_db = input("Input name your data base:  ").strip().upper()
    return name_db


def save_db(name_db):
    with open(f"{name_db}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Название аккаунта",
                "Електронная почта",
                "Пароль"
            )
        )


def make_account():
    name_account = input("Input name account:  ").strip().lower()
    user_mail = input("Input email address:   ").strip().lower()
    account_password = "Qwerty77"
    passwd_select = {
        "low": (8, string.digits, string.ascii_lowercase),
        "medium": (16, string.digits, string.ascii_lowercase, string.ascii_uppercase),
        "high": (24, string.punctuation, string.digits, string.ascii_lowercase, string.ascii_uppercase)
    }
    password_level = input('Choice level [ "low", "medium" or "high"]:   ').strip().lower()
    if password_level == "low":
        level = 8
        passwd_symbol = string.digits + string.ascii_lowercase
    elif password_level == "medium":
        level = 16
        passwd_symbol = string.digits + string.ascii_lowercase + string.ascii_uppercase
    else:
        level = 24
        passwd_symbol = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    user_info = (name_account, user_mail, account_password, level, passwd_symbol)

    return user_info


def make_password(user_info: tuple):
    line_symbol = user_info[-1]
    count_symbol = user_info[-2]
    new_password = "".join(sample(line_symbol, count_symbol))
    new_account = (user_info[0], user_info[1], new_password)

    return new_account


def save_account(new_account: tuple, name_db: str):
    with open(f"{name_db}.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            new_account
        )


def main():
    name_db = make_data_base()
    if name_db != "BAD" and name_db != "exist":
        save_db(name_db)
    else:
        print("Data base exist")

    user_info = make_account()
    new_account = make_password(user_info)
    save_account(new_account, name_db)


if __name__ == '__main__':
    main()
