import datetime

def get_day_of_week(day, month, year):
    """Определяет день недели для данной даты"""
    date = datetime.date(year, month, day)
    return date.strftime('%A')

def is_leap_year(year):
    """Определяет, является ли год високосным"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birth_year, birth_month, birth_day):
    """Определяет возраст пользователя"""
    today = datetime.date.today()
    birthday = datetime.date(birth_year, birth_month, birth_day)
    age = today.year - birthday.year
    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1
    return age

def format_date(day, month, year):
    """Форматирует дату рождения с использованием звёздочек"""
    formatted_day = ''.join(['*' if char.isdigit() else char for char in str(day).zfill(2)])
    formatted_month = ''.join(['*' if char.isdigit() else char for char in str(month).zfill(2)])
    formatted_year = ''.join(['*' if char.isdigit() else char for char in str(year).zfill(4)])
    return f"{formatted_day} {formatted_month} {formatted_year}"

def main():
    # Запрашиваем дату рождения у пользователя
    birth_day = int(input("Введите день рождения: "))
    birth_month = int(input("Введите месяц рождения: "))
    birth_year = int(input("Введите год рождения: "))

    # Определяем день недели
    day_of_week = get_day_of_week(birth_day, birth_month, birth_year)
    print(f"День недели: {day_of_week}")

    # Определяем, был ли год високосным
    if is_leap_year(birth_year):
        print(f"Год {birth_year} был високосным")
    else:
        print(f"Год {birth_year} не был високосным")

    # Определяем возраст пользователя
    age = calculate_age(birth_year, birth_month, birth_day)
    print(f"Вам {age} лет")

    # Форматируем дату рождения с использованием звёздочек
    formatted_date = format_date(birth_day, birth_month, birth_year)
    print(f"Ваша дата рождения: {formatted_date}")

if __name__ == "__main__":
    main()
