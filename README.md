# goit-algo-hw-05

Homework 5. Basic Algorithms and Data Structures at GoIT Neoversity

# Substring Search Algorithms Comparison

## Description
In this task, we compared three substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp. We measured the execution time of each algorithm on two text files (`стаття_1.txt` and `стаття_2.txt`) for both an existing and a non-existing substring.

## Algorithms
1. **Boyer-Moore**: An algorithm that skips sections of the text based on mismatches from the end of the pattern.
2. **Knuth-Morris-Pratt**: An algorithm that uses the longest prefix which is also a suffix to skip sections of the text.
3. **Rabin-Karp**: An algorithm that uses hashing to find any one of a set of pattern strings in a text.

## Results

### `стаття_1.txt`

- **Existing substring ("алгоритм")**
  - Boyer-Moore: `0.000021` seconds
  - Knuth-Morris-Pratt: `0.000032` seconds
  - Rabin-Karp: `0.000042` seconds

- **Non-existing substring ("неіснуючийпідрядок")**
  - Boyer-Moore: `0.000237` seconds
  - Knuth-Morris-Pratt: `0.001891` seconds
  - Rabin-Karp: `0.002223` seconds

### `стаття_2.txt`

- **Existing substring ("рекомендаційної системи")**
  - Boyer-Moore: `0.000010` seconds
  - Knuth-Morris-Pratt: `0.000013` seconds
  - Rabin-Karp: `0.000015` seconds

- **Non-existing substring ("вигаданийпідрядок")**
  - Boyer-Moore: `0.000359` seconds
  - Knuth-Morris-Pratt: `0.002717` seconds
  - Rabin-Karp: `0.003281` seconds

## Conclusions

Based on the results, we can draw the following conclusions:

### `стаття_1.txt`
- For the existing substring, the Boyer-Moore algorithm was the fastest (`0.000021` seconds), followed by Knuth-Morris-Pratt (`0.000032` seconds) and Rabin-Karp (`0.000042` seconds).
- For the non-existing substring, the Boyer-Moore algorithm also performed the best (`0.000237` seconds), significantly faster than Knuth-Morris-Pratt (`0.001891` seconds) and Rabin-Karp (`0.002223` seconds).

### `стаття_2.txt`
- For the existing substring, the Boyer-Moore algorithm was again the fastest (`0.000010` seconds), closely followed by Knuth-Morris-Pratt (`0.000013` seconds) and Rabin-Karp (`0.000015` seconds).
- For the non-existing substring, Boyer-Moore performed the best (`0.000359` seconds), followed by Knuth-Morris-Pratt (`0.002717` seconds) and Rabin-Karp (`0.003281` seconds).

### Overall
The Boyer-Moore algorithm consistently outperformed the other two algorithms in both texts for both existing and non-existing substrings. The Knuth-Morris-Pratt algorithm was generally faster than Rabin-Karp but slower than Boyer-Moore. Rabin-Karp was the slowest among the three algorithms for both existing and non-existing substrings.

These results indicate that the Boyer-Moore algorithm is the most efficient for substring search in these texts, particularly when the substring does not exist in the text. Programmers often use the Boyer-Moore algorithm for its efficiency, especially in cases where the pattern length is smaller than the text length.

## Test Environment
The results were obtained on a MacBook Pro 2021 with an Apple M1 Pro processor.
