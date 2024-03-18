def check_rights(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number == 3:
        return 3


def get_rights(user_auth, users: list, T_users):
    N = 4
    user_index = users.index(user_auth)
    rights = [check_rights(T_users[user_index][0])]
    return rights


def get_access_objects(user_auth, users: list, objects: list, T_users, T_objects):
    access_objects = []
    user_index = users.index(user_auth)
    rights = [check_rights(T_users[user_index][0])]
    if rights[0] == 1:
        for i in range(len(T_objects)):
            if T_objects[i][0] == 1:
                access_objects.append(objects[i])
    elif rights[0] == 2:
        for i in range(len(T_objects)):
            if T_objects[i][0] <= 2:
                access_objects.append(objects[i])
    else:
        for i in range(len(T_objects)):
            access_objects.append(objects[i])
    return access_objects


def request(access_objects: list, num_object, objects: list):
    num_object = num_object - 1
    if objects[num_object] not in access_objects:
        print("Отказ в выполнении операции. Недостаточно прав")
    else:
        file = open(f"objects_data/object{num_object + 1}.txt", "r")
        print("Операция прошла успешно")
        print(file.read())
