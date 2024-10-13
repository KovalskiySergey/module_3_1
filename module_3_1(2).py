calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    le = len(string)
    up = string.upper()
    lo = string.lower()
    return [le, up, lo]
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)
print(string_info('RuN'))
print(string_info('UrBaN'))
print(is_contains('Urban', ['URban', 'RUb', 'AnaConDA']))
print(is_contains('Cycle', ['URban', 'RUb', 'AnaConDA']))
print(calls)
