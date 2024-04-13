# # 407
# a=input()
# a=a.split(" ")
# a.sort()
# print(a)

# 408
# a=input()
# a=a.split(" ")
# a.sort(reverse=True)
# print(a)

# 409
# a=input()
# a=a.split(" ")
# print(a[: :-1])

# 410
# a=input()
# a=a.split(" ")
# b=a[: :-1]
# print(b)

# # 508
# a=input()
# d={"232": "Hi, Alice!", 550: "Hi, Bob!", 190: "Hi, Jack!", 500: "hi, to all!"}
# if a=="232":
#   print(d["232"])
# if a==550:
#   print(dict[550])
# if a==190:
#   print(dict[190])
# if a==500:
#   print(dict[500])

# # 509
# # player_inventory={"key":3, "mace":1, "gold coin":24, "lantern":1, "stone":10}
# # b=player_inventory.items()
# # print(b.)

# # 510
# films = {'Avengers: Endgame': 2019,
#          'Iron Man': 2008,'Thor': 2011,'Guardians of the Galaxy': 2014}
# sorted = sorted(films.items())
# for name, year in sorted:
#     print(f"('{name}', {year})", end=' ')

# # 511
# countryes = {'Ukraine': 'Kyiv','France': 'Paris','Denmark': 'Copenhagen',
#     'China': 'Beijing',
#     'Canada': 'Ottawa'}
# sorted = sorted(countryes.items(), reverse=True)
# for country, state in sorted:
#     print(f"('{country}', '{state}')", end=' ')

player_inventory={"key":3, "mace":1, "gold coin":24, "lantern":1, "stone":10}
for things in player_inventory:
   print(f"('{things}')")