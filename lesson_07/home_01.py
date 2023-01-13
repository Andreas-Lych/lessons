"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы,
которая считывает название города и выводит на печать страну.
"""

from typing import Optional

country_and_city = {
    "Russia": ["Moskow", "Rostov", "Smolensk", "Kazan"],
    "Belarus": ["Minsk", "Brest", "Mogilev", "Vitebsk"],
    "Germany": ["Berlin", "Koln", "Dortmund", "Bremen"]}

def main():
    city = input("Введите город: ")
    country = find_country(city)
    if country is not None:
        print(f"{city} находится в {country}")
    else:
        print(f"Не найден {city}")

def find_country(city: str) -> Optional[str]:
        for country, cities in country_and_city.items():
            if city in cities:
                return country


if __name__ == "__main__":
    main()