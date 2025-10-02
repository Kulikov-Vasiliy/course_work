def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if not card_number.isdigit():
        raise TypeError("некорректный тип данных")

    if len(card_number) != 16:
        raise ValueError(
            "номер карты должен состоять из 16 символов или нет открытых продуктов"
        )

    last_num = card_number[-4:]

    return f"**** **** **** {last_num}"


def get_mask_account(client_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    if not client_account.isdigit():
        raise TypeError("некорректный тип данных или нет открытых счетов")

    if len(client_account) != 20:
        raise ValueError("банковский счет должен состоять из 20 символов")

    late_num = client_account[-4:]

    return f"**{late_num}"
