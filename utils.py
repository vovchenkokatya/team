def is_strong_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Перевірка
my_pass = "12345"
if is_strong_password(my_pass):
    print("Пароль надійний")
else:
    print("Пароль занадто короткий!")
