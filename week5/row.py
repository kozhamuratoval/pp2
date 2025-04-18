from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["№", "Наименование", "Кол-во", "Цена", "Стоимость"]

items = [
    (1, "Натрия хлорид 0,9%, 200 мл, фл", 2, "154,00", "308,00"),
    (2, "Борный спирт 3%, 20 мл, фл.", 1, "51,00", "51,00"),
    (3, "Шприц 2 мл, 3-х комп. (Bioject)", 2, "16,00", "32,00"),
    (4, "Система для инфузии Vogt Medical", 2, "60,00", "120,00"),
    (5, "Naturella прокладки Классик макси №8", 1, "310,00", "310,00"),
    (6, "AURA Ватные диски №150", 1, "461,00", "461,00"),
    (7, "Чистая линия скраб мягкий 50 мл", 1, "381,00", "381,00"),
    (8, "Чистая линия скраб очищающий абрикос 50 мл", 1, "386,00", "386,00"),
    (9, "Чистая линия скраб мягкий 50 мл", 1, "381,00", "381,00"),
    (10, "Carefree салфетки Алоэвоздухопроницаемые №20", 1, "414,00", "414,00"),
    (11, "Pro Series Шампунь яркий цвет 500мл", 1, "841,00", "841,00"),
    (12, "Pro Series бальзам-ополаскиватель для окрашенных волос 500мл", 1, "841,00", "841,00"),
    (13, "Clear шампунь Актив спорт 2в1 мужской 400 мл", 1, "1 200,00", "1 200,00"),
    (14, "Bio World (HYDRO THERAPY) Мицеллярная вода 5в1, 445мл", 1, "1 152,00", "1 152,00"),
    (15, "Bio World (HYDRO THERAPY) Гель-мусс для умывания, 250мл", 1, "1 152,00", "1 152,00"),
    (16, "[RX]-Натрия хлорид 0,9%, 100 мл, фл.", 1, "168,00", "168,00"),
    (17, "[RX]-Дисоль р-р 400 мл, фл.", 1, "163,00", "163,00"),
    (18, "Тагансорбент с иономи серебра №30, пор.", 1, "1 526,00", "1 526,00"),
    (19, "[RX]-Церукал 2%, 2 мл, №10, амп.", 2, "396,00", "792,00"),
    (20, "[RX]-Андазол 200 мг, №40, табл.", 1, "7 330,00", "7 330,00")
]
for item in items:
    table.add_row(item)

table.add_row(["", "ИТОГО", "", "", "18 009,00"])
print(table)
