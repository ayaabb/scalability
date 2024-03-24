from lorem.text import TextLorem

from results_operations.calculate_runtime import calculate_runtime


def count_word_occurrences_fast(text):
    words = text.split()
    word_counts = {}
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def count_word_occurrences_slow(text):
    words = text.split()
    word_counts = {}
    for i in range(len(words)):
        word = words[i].lower()
        if word not in word_counts:
            word_counts[word] = 1
            for j in range(i + 1, len(words)):
                if words[j].lower() == word:
                    word_counts[word] += 1
    return word_counts


def calculate_word_occurences_results():
    sizes = [10 ** size for size in range(1, 8)] + [10 ** size // 2 for size in range(5, 8)]
    sizes = sorted(sizes)
    slow_results = []
    fast_results = []
    for size in sizes:
        lorem = TextLorem(srange=(size, size))
        lorem_text = lorem.sentence()
        slow_results.append(calculate_runtime(count_word_occurrences_slow, lorem_text))
        fast_results.append(calculate_runtime(count_word_occurrences_fast, lorem_text))

    return sizes, slow_results, fast_results
