def generate_prefix(pattern):
    pat_len = len(pattern)
    pat_fun = [0] * pat_len
    pref_len = 0  # length of the previous longest prefix suffix

    if pat_len <= 1:  # eliminate trivial conditions
        return pat_fun

    pat_fun[0] = 0  # always 0
    i = 1

    while i < pat_len:
        if pattern[i] == pattern[pref_len]:
            pref_len += 1
            pat_fun[i] = pref_len
            i += 1
        else:
            # This is tricky. The pattern may contain multiple sub-prefixes. This allows to use them
            if pref_len != 0:
                pref_len = pat_fun[pref_len - 1]
                # we do not increment i here
                # the loop will execute again for the same i and pref_len
                # until a matching prefix would be found or we step down to pref_len == 0
            else:
                pat_fun[i] = 0
                i += 1
    return pat_fun


def search_kmp(pattern, text):
    pat_len = len(pattern)
    txt_len = len(text)
    pat_fun = generate_prefix(pattern)

    results_list = []

    p = 0  # index pointing to pattern
    t = 0  # index pointing to text

    while t < txt_len:
        if pattern[p] == text[t]:
            # print('DEBUG: ', pattern[:p+1],'matches',text[:t+1])
            t += 1
            p += 1
            if p == pat_len:
                # print ('DEBUG: ', "Found pattern at index", t-p)
                results_list.append(t - p)
                p = pat_fun[p - 1]
                # print('DEBUG: ', 'p comes back to', p)
        else:
            if p != 0:
                # print('DEBUG: ', 'Mismatch!', pattern[p], '<>', text[t], ' in ', pattern[:p+1], 'and', text[:t+1])
                p = pat_fun[p - 1]
                # print('DEBUG: ', 't reamains', t, 'p comes back to', p, 'we will compare ', pattern[:p+1], 'with text', text[:t+1])
            else:
                # print('DEBUG: ', 'Mismatch! Return to start!', pattern[p], '<>', text[t])
                t += 1
                # print('DEBUG: ', 't increase to', t, 'p remains', p, 'we will compare', pattern[:p+1], 'with text', text[:t+1])

    return results_list


def search_naive(pattern, text):
    result_list = []

    for text_start in range(len(text) - len(pattern) + 1):
        found = True
        for i in range(len(pattern)):
            if pattern[i] != text[text_start + i]:
                found = False
                break
        if found:
            result_list.append(text_start)

    return result_list


import random
import time

max_len = 1000000
allowed_chars = ['a', 'b']

print('Generating random text')
start = time.time()
text = ''.join(random.choice(allowed_chars) for i in range(max_len))
stop = time.time()
print(f'Text generation:    {stop - start}')

pattern = 'ababababababab'

print('Searching')
# checking time - naive search

start = time.time()
results_naive = search_naive(pattern, text)
stop = time.time()
print(f'Naive search: found {len(results_naive)} matches in {stop - start} seconds')

# checking time - KMP search

start = time.time()
results_kmp = search_kmp(pattern, text)
stop = time.time()
print(f'KMP search:   found {len(results_kmp)} matches in {stop - start} seconds')
