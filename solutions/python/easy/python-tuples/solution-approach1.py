# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python
# Status      Accepted
# Submitted   2026-10-07, 01:07 p.m.
# Technique   tuple-hashing
# Time        O(n)
# Space       O(n)
# Insight     The implementation converts a list of integers into an immutable tuple, which allows the built-in hash function to compute a unique integer representation based on the tuple's contents.
# Interview   Before: "How do you generate a hash for a collection of integers in Python?" After: "You can cast the list to a tuple, which is hashable, and pass it to hash(). This runs in O(n) time and space, where n is the number of elements in the tuple."
# Pitfalls    (1) Attempting to hash a list directly will raise a TypeError because lists are mutable and unhashable.  (2) Using input() instead of raw_input() in Python 2 environments may cause unexpected behavior when reading the integer string.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))
    
