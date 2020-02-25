
fruits = ["pomegranate", "cherry", "apricot", "apple"]

ufruits = []

for f in fruits:
    # f = get_next_item_of(fruits)   AKA next(fruits)
    print(f, f.upper())
    ufruits.append(f.upper())

print(ufruits)
print("-" * 60)

s = "abc"
for c in s:
    print(s)
print("-" * 60)

for f in fruits[1:]:
    print(f)
print()
