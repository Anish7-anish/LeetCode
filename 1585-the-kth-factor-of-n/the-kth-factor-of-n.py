class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

    # Iterate only up to sqrt(n)
        for j in range(1, int(n**0.5) + 1):
            if n % j == 0:
                factors.append(j)
                if j != n // j:  # Avoid duplicate factors (for perfect squares)
                    factors.append(n // j)

        # Sort factors to get them in order
        factors.sort()

        # Return the k-th factor if it exists, else return -1
        return factors[k - 1] if k <= len(factors) else -1

            
        

        