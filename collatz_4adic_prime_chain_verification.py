#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT

import sympy

def get_next_4adic(n):
    """
    Computes the next number in the 4-adic Collatz-like sequence.
    Applies the rule:
      - If n ≡ 1 mod 4: f(n) = (5n - 1) / 4
      - If n ≡ 3 mod 4: f(n) = (5n + 1) / 4
    Returns None if n is even (i.e., not 1 or 3 mod 4).
    """
    rem = n % 4
    if rem == 1:
        return (5 * n - 1) // 4
    elif rem == 3:
        return (5 * n + 1) // 4
    return None  # Even numbers terminate the chain

def verify_prime_chain(n0, target_len=7):
    """
    Verifies that a chain starting from n0:
      - Follows the 4-adic Collatz-like rule
      - Contains only prime numbers
    Prints each step and returns the verified chain.
    """
    print(f"--- Verification for n0 = {n0} ---")
    curr = n0
    chain = []

    for i in range(target_len):
        if not sympy.isprime(curr):
            print(f"Step {i}: {curr} -> COMPOSITE (Chain Broken)")
            break

        print(f"Step {i}: {curr} -> PRIME (Verified)")
        chain.append(curr)

        if i < target_len - 1:
            curr = get_next_4adic(curr)
            if curr is None:
                print("Error: Sequence terminated due to even number.")
                break

    print(f"\nFinal Result: Length {len(chain)} chain confirmed.\n")
    return chain

if __name__ == "__main__":
    # Example verifications
    discovery_1 = 455_847_361_774_092_289
    discovery_2 = 559_188_056_938_807_297

    verify_prime_chain(discovery_1)
    print("\n" + "=" * 60 + "\n")
    verify_prime_chain(discovery_2)


# In[ ]:




