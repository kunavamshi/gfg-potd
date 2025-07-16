import math

class Solution:
    def countNumbers(self, n):
        limit = int(n ** 0.5) + 1
        is_prime = [True] * (limit)
        is_prime[0] = is_prime[1] = False

        primes = []
        for i in range(2, limit):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, limit, i):
                    is_prime[j] = False

        count = 0

        # Case 1: p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1
            else:
                break

        # Case 2: p^2 * q^2, where p != q
        num_primes = len(primes)
        for i in range(num_primes):
            p = primes[i]
            for j in range(i + 1, num_primes):
                q = primes[j]
                if (p * p) * (q * q) <= n:
                    count += 1
                else:
                    break

        return count