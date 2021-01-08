#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список магазинов.
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о товаре.
            product = input("Название товара? ")
            shop = input("Название магазина? ")
            price = float(input("Стоимость товара в руб.? "))

            # Создать словарь.
            markets = {
                'product': product,
                'shop': shop,
                'price': price,
            }

            # Добавить словарь в список.
            market.append(markets)
            # Отсортировать список в случае необходимости.
            if len(market) > 1:
                market.sort(key=lambda item: item.get('product', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Товар",
                    "Магазин",
                    "Стоимость в руб."
                )
            )
            print(line)

            # Вывести данные о всех товарах.
            for idx, markets in enumerate(market, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        markets.get('product', ''),
                        markets.get('shop', ''),
                        markets.get('price', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=2)
            period = str(parts[1])

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения товара из списка.
            for markets in market:
                if markets.get('product') >= period:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, markets.get('product', ''))
                    )
                    print('Название магазина:', markets.get('shop', ''))
                    print('Стоимость в руб.:', markets.get('price', ''))

            # Если счетчик равен 0, то товары не найдены.
            if count == 0:
                print("Продукт не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\nadd - добавить продукт\nlist - вывести список продуктов\nselect <товар> - информация о товаре\nhelp - отобразить справку\nexit - завершить работу с программой")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
