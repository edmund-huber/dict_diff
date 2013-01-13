import colorama

def dict_diff(d1, d2):
    s = ''
    if type(d1) == dict and type(d2) == dict:
        # If both dicts have a single (different) key, and their
        # values match, it may be more reasonable to describe the diff
        # as a change in the key.
        if len(d1) == 1 and len(d2) == 1 and d1.keys() != d2.keys() and d1.values() == d2.values():
            diff, printed, _ = dict_diff(d1.values()[0], d1.values()[0])
            return (
                {(d1.keys()[0], d2.keys()[0]): diff},
                colorama.Fore.YELLOW + str(d2.keys()[0]) + colorama.Fore.RESET + ': ' + printed,
                True)
        else:
            diff_items = []
            printed_items = []
            diffs = False
            # Keys unique to d1 are deletions.
            for k1 in set(d1) - set(d2):
                diff, printed, _ = dict_diff(d1[k1], d1[k1])
                diff_items.append(((k1, None), diff))
                printed_items.append(colorama.Fore.RED + str(k1) + ': ' + printed + colorama.Fore.RESET)
                diffs = True
            # Keys unique to d2 are additions.
            for k2 in set(d2) - set(d1):
                diff, printed, _ = dict_diff(d2[k2], d2[k2])
                diff_items.append(((None, k2), diff))
                printed_items.append(colorama.Fore.GREEN + str(k2) + ': ' + printed + colorama.Fore.RESET)
                diffs = True
            # Keys present in both may have different values.
            for k in set(d1) & set(d2):
                diff, printed, any_diffs = dict_diff(d1[k], d2[k])
                diff_items.append((k, diff))
                printed_items.append(str(k) + ': ' + printed)
                diffs |= any_diffs
            return (
                dict(diff_items),
                '{' + ', '.join(printed_items) + '}',
                diffs)
    elif d1 == d2:
        return d1, str(d1), False
    else:
        return (
            (d1, d2),
            colorama.Fore.YELLOW + str(d2) + colorama.Fore.RESET,
            True)

