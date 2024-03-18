import random
from auth_fun import *

from auth_fun import get_rights

users = ["Ivan", "Boris", "Kolyan", "Aktan", "Vlados", "Sergey", "Gamza", "Elena", "Admin"]
objects = ["Object1", "Object2", "Object3", "Object4"]
M = 9

T_users = [[0] * 1 for _ in range(M)]
T_objects = [[0] * 1 for _ in range(4)]

for i in range(M):
    for j in range(1):
        T_users[i][j] = random.randint(1, 3)

for i in range(4):
    for j in range(1):
        T_objects[i][j] = random.randint(1, 3)

for j in range(0):
    T_users[8][j] = 3

i = 0
for row in T_users:
    print(f"{users[i]}: {row}")
    i += 1

i = 0
for row in T_objects:
    print(f"{objects[i]}: {row}")
    i += 1

rights = []
command = ""
while True:
    user_auth = input("User: ")
    if user_auth in users:
        print("Идентификация прошла успешно, добро пожаловать в систему")
        rights = get_rights(user_auth, users, T_users)
        while True:
            access_objects = get_access_objects(user_auth, users, objects, T_users, T_objects)
            print(f"Список доступных объектов: {access_objects}")
            command = input("Жду ваших указаний>")
            if command == "quit":
                break
            num_object = int(input("Над каким объектом производится операция? "))
            request(access_objects, num_object, objects)
