import json

with open('users.csv', 'r', encoding='utf-8') as users:
    users_list = []
    for ln in users:
        users_list.append(' '.join(ln.split()[0].split(',')))
    print(users_list)
    users_dict = {}.fromkeys(users_list)
with open('hobby.csv', 'r', encoding='utf-8') as hobby:
    for ln, lm in zip(hobby, users_list):
        users_dict[lm] = ' '.join(ln.split())
print(users_dict)
with open('users_dict.json', 'w', encoding='utf-8') as dict_file:
    json.dump(users_dict, dict_file)
with open('users_dict.json', 'r', encoding='utf-8') as dict_file:
    users_dict = json.load(dict_file)
print(users_dict)
