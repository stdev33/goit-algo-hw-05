from collections import defaultdict


def boyer_moore(text, pattern):
    def preprocess_bad_character(pattern):
        bad_char = defaultdict(lambda: -1)
        for i in range(len(pattern)):
            bad_char[ord(pattern[i])] = i
        return bad_char

    bad_char = preprocess_bad_character(pattern)
    m = len(pattern)
    n = len(text)
    s = 0
    iterations = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        iterations += 1
        if j < 0:
            return (iterations, s)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return (iterations, -1)


def knuth_morris_pratt(text, pattern):
    def compute_lps_array(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps_array(pattern)
    i = 0
    j = 0
    iterations = 0

    while i < n:
        iterations += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return (iterations, i - j)
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return (iterations, -1)


def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    iterations = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        iterations += 1
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return (iterations, i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return (iterations, -1)
