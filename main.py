from decorators.decorators import log

@log("logs/log_file.txt")
def adds(x, y):
    return x + y

if __name__ == "__main__":
    print(adds(4, 5))  # Успешный вызов
    print(adds(4, 'a'))  # Ошибка
