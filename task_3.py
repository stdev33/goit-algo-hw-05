import pathlib
import timeit
from substring_searchers import algorithms as alg


current_dir = pathlib.Path(__file__).parent

with open(current_dir / "стаття_1.txt", "r", encoding="utf-8") as file:
    text1 = file.read()

with open(current_dir / "стаття_2.txt", "r", encoding="utf-8") as file:
    text2 = file.read()


existing_substring1 = "алгоритм"
non_existing_substring1 = "неіснуючийпідрядок"

existing_substring2 = "рекомендаційної системи"
non_existing_substring2 = "вигаданийпідрядок"


def measure_time(algorithm_func, text, pattern):
    start_time = timeit.default_timer()
    result = algorithm_func(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time, result


results = {
    "Boyer-Moore": {"text1_existing": {}, "text1_non_existing": {}, "text2_existing": {}, "text2_non_existing": {}},
    "Knuth-Morris-Pratt": {"text1_existing": {}, "text1_non_existing": {}, "text2_existing": {}, "text2_non_existing": {}},
    "Rabin-Karp": {"text1_existing": {}, "text1_non_existing": {}, "text2_existing": {}, "text2_non_existing": {}}
}

# Measure time for стаття_1.txt
results["Boyer-Moore"]["text1_existing"]["time"], results["Boyer-Moore"]["text1_existing"]["result"] = measure_time(alg.boyer_moore, text1, existing_substring1)
results["Boyer-Moore"]["text1_non_existing"]["time"], results["Boyer-Moore"]["text1_non_existing"]["result"] = measure_time(alg.boyer_moore, text1, non_existing_substring1)
results["Knuth-Morris-Pratt"]["text1_existing"]["time"], results["Knuth-Morris-Pratt"]["text1_existing"]["result"] = measure_time(alg.knuth_morris_pratt, text1, existing_substring1)
results["Knuth-Morris-Pratt"]["text1_non_existing"]["time"], results["Knuth-Morris-Pratt"]["text1_non_existing"]["result"] = measure_time(alg.knuth_morris_pratt, text1, non_existing_substring1)
results["Rabin-Karp"]["text1_existing"]["time"], results["Rabin-Karp"]["text1_existing"]["result"] = measure_time(alg.rabin_karp, text1, existing_substring1)
results["Rabin-Karp"]["text1_non_existing"]["time"], results["Rabin-Karp"]["text1_non_existing"]["result"] = measure_time(alg.rabin_karp, text1, non_existing_substring1)

# Measure time for стаття_2.txt
results["Boyer-Moore"]["text2_existing"]["time"], results["Boyer-Moore"]["text2_existing"]["result"] = measure_time(alg.boyer_moore, text2, existing_substring2)
results["Boyer-Moore"]["text2_non_existing"]["time"], results["Boyer-Moore"]["text2_non_existing"]["result"] = measure_time(alg.boyer_moore, text2, non_existing_substring2)
results["Knuth-Morris-Pratt"]["text2_existing"]["time"], results["Knuth-Morris-Pratt"]["text2_existing"]["result"] = measure_time(alg.knuth_morris_pratt, text2, existing_substring2)
results["Knuth-Morris-Pratt"]["text2_non_existing"]["time"], results["Knuth-Morris-Pratt"]["text2_non_existing"]["result"] = measure_time(alg.knuth_morris_pratt, text2, non_existing_substring2)
results["Rabin-Karp"]["text2_existing"]["time"], results["Rabin-Karp"]["text2_existing"]["result"] = measure_time(alg.rabin_karp, text2, existing_substring2)
results["Rabin-Karp"]["text2_non_existing"]["time"], results["Rabin-Karp"]["text2_non_existing"]["result"] = measure_time(alg.rabin_karp, text2, non_existing_substring2)

# Display results
for algorithm in results:
    print(f"\nResults for {algorithm}:")
    for case in results[algorithm]:
        time_taken = results[algorithm][case]["time"]
        print(f"{case}: {time_taken:.6f} seconds")
