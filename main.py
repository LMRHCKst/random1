import random
import string

def generate_random_russian_name():
    first_names = ['Александр', 'Мария', 'Иван', 'Анастасия', 'Дмитрий', 'Екатерина', 'Сергей', 'Ольга']
    last_names = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлова']
    return random.choice(first_names) + ' ' + random.choice(last_names)

def generate_random_email(name):
    domains = ['gmail.com', 'yandex.ru', 'mail.ru', 'rambler.ru', 'bk.ru']
    username = name.lower().replace(' ', '_') + ''.join(random.choice(string.digits) for _ in range(2))
    domain = random.choice(domains)
    return f'{username}@{domain}'

def generate_random_age():
    return random.randint(18, 80)

def generate_random_phone():
    formats = ['+7-9##-###-##-##', '+7(9##)###-##-##', '+7 9## ###-##-##']
    return ''.join(random.choice(string.digits) if c == '#' else c for c in random.choice(formats))

def generate_random_address():
    streets = ['ул. Ленина', 'ул. Пушкина', 'пр. Октября', 'пр. Гагарина', 'ул. Маяковского']
    cities = ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Новосибирск', 'Казань']
    return f'{random.choice(random.choices(cities, k=2))}, {random.choice(streets)}, д. {random.randint(1, 100)}'

def generate_random_salary():
    return round(random.uniform(20000, 100000), 2)

def generate_random_occupation():
    occupations = ['Инженер', 'Медсестра', 'Учитель', 'Программист', 'Врач', 'Бухгалтер', 'Дизайнер']
    return random.choice(occupations)

def generate_random_education_level():
    education_levels = ['Среднее', 'Среднее специальное', 'Высшее бакалавр', 'Высшее магистр', 'Высшее кандидат наук']
    return random.choice(education_levels)

def generate_random_interests():
    interests = ['Путешествия', 'Фотография', 'Кулинария', 'Литература', 'Спорт', 'Искусство', 'Технологии']
    return random.sample(interests, random.randint(1, len(interests)))

def generate_random_data(num_entries=10):
    data = []
    for _ in range(num_entries):
        name = generate_random_russian_name()
        email = generate_random_email(name)
        age = generate_random_age()
        phone = generate_random_phone()
        address = generate_random_address()
        salary = generate_random_salary()
        occupation = generate_random_occupation()
        education_level = generate_random_education_level()
        interests = generate_random_interests()
        data.append({
            'Имя': name,
            'Email': email,
            'Возраст': age,
            'Телефон': phone,
            'Адрес': address,
            'Зарплата': salary,
            'Род занятий': occupation,
            'Образование': education_level,
            'Интересы': interests
        })
    return data

if __name__ == "__main__":
    num_entries = 5
    random_data = generate_random_data(num_entries)
    for entry in random_data:
        print(entry)
