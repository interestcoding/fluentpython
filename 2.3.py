import os

# 2.3.1
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# 2.3.2
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print((quotient, remainder))

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

a, b, *rest = range(5)
print((a, b, rest))

a, b, *rest = range(3)
print((a, b, rest))

a, b, *rest = range(2)
print((a, b, rest))

a, *body, c, d = range(5)
print((a, body, c, d))

*head, b, c, d = range(5)
print((head, b, c, d))

# 2.3.3
