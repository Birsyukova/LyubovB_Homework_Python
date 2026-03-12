def month_to_season(month_num):
    """

    Зима: 12, 1, 2
    Весна: 3, 4, 5
    Лето: 6, 7, 8
    Осень: 9, 10, 11

    Args:
        month_num (int): Номер месяца от 1 до 12

    Returns:
        str: Название сезона или сообщение об ошибке
    """
    if month_num in (12, 1, 2):
        return "Зима"
    elif month_num in (3, 4, 5):
        return "Весна"
    elif month_num in (6, 7, 8):
        return "Лето"
    elif month_num in (9, 10, 11):
        return "Осень"
    else:
        return "Ошибка: номер месяца должен быть от 1 до 12"


if __name__ == "__main__":
    print(month_to_season(2))    # Зима
    print(month_to_season(5))    # Весна
    print(month_to_season(8))    # Лето
    print(month_to_season(11))   # Осень
    print(month_to_season(13))   # Ошибка
