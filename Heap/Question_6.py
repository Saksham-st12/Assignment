
# Given an array of string words and an integer k, return the k most frequent words.
# Words = ['priya','bhatia','aryan','priya',aryan','priya']
# k = 3
# Output =['priya','aryan','bhatia']

from collections import Counter
import heapq

def top_k_frequent(words, k):
    word_count = Counter(words)
    heap = [(-freq, word) for word, freq in word_count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]

words = ['priya', 'bhatia', 'aryan', 'priya', 'aryan', 'priya']
k = 3
output = top_k_frequent(words, k)
print(output)

# Given an array of string words and an integer k, return the k most frequent words.
# Words = ['priya','bhatia','aryan','priya',aryan','priya']
# k = 3
# Output =['priya','aryan','bhatia']

from collections import Counter
import heapq

def top_k_frequent(words, k):
    word_count = Counter(words)
    heap = [(-freq, word) for word, freq in word_count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]

words = ['priya', 'bhatia', 'aryan', 'priya', 'aryan', 'priya']
k = 3
output = top_k_frequent(words, k)
print(output)

