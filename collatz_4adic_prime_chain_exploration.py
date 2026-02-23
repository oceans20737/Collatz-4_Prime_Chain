#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT

from sympy import isprime

def next_4adic(n):
    """
    Computes the next number in the 4-adic Collatz-like sequence.
    Applies the rule:
      - If n ≡ 1 mod 4: f(n) = (5n - 1) / 4
      - If n ≡ 3 mod 4: f(n) = (5n + 1) / 4
    Returns None if n is even (i.e., not 1 or 3 mod 4).
    """
    if n % 4 == 1:
        return (5 * n - 1) // 4
    elif n % 4 == 3:
        return (5 * n + 1) // 4
    else:
        return None  # Even numbers terminate the chain

def search_7chains():
    """
    Searches for prime chains of length 7 using a 4-adic Collatz-like function.
    Uses a skipping method to reduce the search space by checking numbers of the form:
      n0 = M * k ± 1
    where M = 4^7 * product of primes up to 23.
    Discovered chains are printed and saved to a text file.
    """
    target_len = 7
    M = (4 ** target_len) * (3 * 7 * 11 * 13 * 17 * 19 * 23)

    print(f"Starting 7-chain search...\nBase modulus M = {M}\n")

    found_chains = []

    for k in range(1, 1_600_000):
        for n0 in (M * k + 1, M * k - 1):
            if not isprime(n0):
                continue

            chain = [n0]
            curr = n0

            while True:
                nxt = next_4adic(curr)
                if nxt and isprime(nxt):
                    chain.append(nxt)
                    curr = nxt
                else:
                    break

            if len(chain) >= target_len:
                print(f"[FOUND] Length {len(chain)} chain at k = {k}")
                print(f"n0 = {n0}")
                print("Chain:")
                for i, val in enumerate(chain):
                    print(f"  n{i} = {val}")
                print()

                found_chains.append((k, chain))

        # Optional: show progress every 100,000 steps
        if k % 100_000 == 0:
            print(f"Checked up to k = {k}")

    # Save results to file
    with open("prime_chains_L7.txt", "w") as f:
        for k, chain in found_chains:
            f.write(f"Chain found at k = {k}\n")
            for i, val in enumerate(chain):
                f.write(f"  n{i} = {val}\n")
            f.write("\n")

    print(f"\nSearch complete. {len(found_chains)} chains saved to 'prime_chains_L7.txt'.")

if __name__ == "__main__":
    search_7chains()


# In[ ]:




