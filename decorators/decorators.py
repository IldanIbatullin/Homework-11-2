import os
from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования работы функции.

    Этот декоратор оборачивает функцию и записывает в лог информацию о ее выполнении.
    Если функция выполняется успешно, в лог записывается сообщение о ее успешном выполнении.
    В случае возникновения ошибки логируется сообщение об ошибке вместе с входными параметрами функции.

    Параметры:
    ----------
    filename : str, optional
        Путь к файлу, в который будут записываться логи. Если не задан, логи выводятся в консоль.

    Возвращает:
    ----------
    function
        Обернутая функция с добавленной функциональностью логирования.
    """

    def wrapper(func):
        """
        Обертка для функции, которая добавляет функциональность логирования.

        Параметры:
        ----------
        func : function
            Функция, которую нужно обернуть.

        Возвращает:
        ----------
        function
            Обернутая функция с логированием.
        """

        @wraps(func)
        def inner(*args, **kwargs):
            """
            Внутренняя функция, которая выполняет основную логику и обрабатывает ошибки.

            Параметры:
            ----------
            *args : tuple
                Позиционные аргументы, передаваемые в функцию.
            **kwargs : dict
                Именованные аргументы, передаваемые в функцию.

            Возвращает:
            ----------
            any
                Результат выполнения обернутой функции.
            """
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

            if filename:
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")
            else:
                print(message)

            return result

        return inner

    return wrapper
