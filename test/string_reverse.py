def str_reverse(a_string):
    if len(a_string) < 2:
        return a_string
    else:
        return a_string[-1] + str_reverse(a_string[1:-1]) + a_string[0]

print(str_reverse('hello ciallo'))
