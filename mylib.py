##This might be the ugliest solution for deleting some text from string but whatever
def edit(lst):
    length = len(lst)
    i = 0
    while i < length:
        lst[i] = lst[i].replace('Ev Telefonu ', '')
        lst[i] = lst[i].replace('Cep Telefonu ', '')
        lst[i] = lst[i].replace('E-mail ', '')
        i += 1
    return lst
