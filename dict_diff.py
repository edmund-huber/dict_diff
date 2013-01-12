import colorama

def dict_diff(d1, d2):
    s = ''
    if type(d1) == dict and type(d2) == dict:
        # If both dicts have a single (different) key, and their
        # values match, it may be more reasonable to describe the diff
        # as a change in the key.
        if len(d1) == 1 and len(d2) == 1 and d1.keys() != d2.keys() and d1.values() == d2.values():
            return colorama.Fore.YELLOW + d2.keys()[0] + colorama.Fore.RESET + ': ' + dict_diff(d1.values()[0], d1.values()[0])
        else:
            items = []
            # Keys unique to d1 are deletions.
            for k1 in set(d1) - set(d2):
                items.append(colorama.Fore.RED + str(k1) + ': ' + dict_diff(d1[k1], d1[k1]) + colorama.Fore.RESET)
            # Keys unique to d2 are additions.
            for k2 in set(d2) - set(d1):
                items.append(colorama.Fore.GREEN + str(k2) + ': ' + dict_diff(d2[k2], d2[k2]) + colorama.Fore.RESET)
            # Keys present in both may have different values.
            for k in set(d1) & set(d2):
                items.append(str(k) + ': ' + dict_diff(d1[k], d2[k]))
            return '{' + ', '.join(items) + '}'
    elif d1 == d2:
        return str(d1)
    else:
        return colorama.Fore.YELLOW + str(d2) + colorama.Fore.RESET

print dict_diff(4, 3)
print dict_diff(4, {'a': 3})
print dict_diff({'a': 4}, {'a': 3})
print dict_diff({'a': {'b': {'c': 3}}}, {'a': {'b': {'c': 6}}})
print dict_diff({'a': {'b': {'c': 3}}}, {'a': {'b': {'d': 3}}})
print dict_diff({'a': {'b': {'c': 3}}}, {'a': {'c': {'b': 3}}})
