calls = 0
string = input('Введите строку: ')
def count_calls():
    global calls
    calls += 1
def string_info():
    count_calls()
    global string
    return [len(string), string.upper(), string.lower()]
def is_contains():
    count_calls()
    global string
    list_to_search = ['Urban', 'BAN', 'ArMaGeDoN', 'RoG']
    l = [x.upper() for x in list_to_search]
    s = string.upper()
    if s in l:
        print(True)
    else:
        print(False)
print(string_info())
print(is_contains())
print(calls)




