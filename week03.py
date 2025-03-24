

def duplicate_city(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2: # 중복값이 들어왔다는 의미 -> anyang이 있는 상태에서 s의 길이가 +1 되면 다른 값 / 똑같으면 중복값이 되는 것(잘 이해하기)
            result.append(city)
    return result



cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
# cities = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'}
# cities = set(city) # set 함수 인수로 리스트나 튜플 주면 중복값 제거 / set = value 가 없는 딕셔너리

cities.append('Anyang')
cities.append('Seoul')
print(cities)
# print(duplicate_city(cities))
print(set(duplicate_city(cities)))


