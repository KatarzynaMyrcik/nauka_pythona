zabawki = ['kucyki', 'lalki', 'klocki']

print(zabawki[0])
print(zabawki[1])
print(zabawki[2])

print("pierwsza petla:")
for s in zabawki:
    print("zabawki to " + s)

print("druga petla:")
for idx in [0,1,2]:
    print("zabawka to " + zabawki[idx])

print("trzecia petla:")
for idx in range(len(zabawki)):
    print("zabawka to takze: " + zabawki[idx])


print(range(5))
