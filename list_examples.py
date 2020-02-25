
list1 = list()

# listx = list(iterable-thing)

list2 = ['alpha', 'bravo', 'charlie']

list3 = []

cities = ["Waldorf", "La Plata", "Port Tobacco", "Welcome"]
print(cities)

cities.append("Alexandria")
print(cities)
cities.append("Baltimore")
print(cities)

more_cities = ["Yeocomico", "King George", "Port Royal"]

cities.extend(more_cities)
print(cities)

cities.insert(0, 'Annapolis')
cities.insert(5, 'Pasadena')
cities.insert(8, 'Glen Burnie')

print(cities)

del cities[4]
print(cities)


x = cities.pop(5)
print(x)
print(cities)

x = cities.pop()
print(x)
print(cities)

cities.remove('Yeocomico')
print(cities)


pos = cities.index('Pasadena')
print(pos)
print(cities[pos])

sorted_cities = sorted(cities)
print(sorted_cities)

cities.sort()
print(cities)















