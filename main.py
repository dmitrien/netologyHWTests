def tusckOne():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    unique_numbers = []
    for title in ids.values():
      unique_numbers.extend(title)

    return list(set(unique_numbers))

def tusckTwo():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    for sales in stats.values():
        if sales >= (max(stats.values())):
            return list(filter(lambda s: stats[s] == sales, stats))[0]

def tusckThree():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    count = 0
    result = []
    for visit in geo_logs:
        count += 1
        if "Россия" in visit["visit" + str(count)]:
            result.append(visit)
    return result

if __name__=='__main__':
    yaCreatFolder = YaCreatFolder()
    yaCreatFolder.create_folder('Уникальная папка')
    print(yaCreatFolder.show_folder('Уникальная папка'))
    yaCreatFolder.delete_folder('Уникальная папка')












