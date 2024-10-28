class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the case when n is negative
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_product = x

        # Iterate while n is greater than 0
        while n > 0:
            if n % 2 == 1:  # If n is odd, multiply result by current product
                result *= current_product
            # Square the current product and halve n
            current_product *= current_product
            n //= 2
        
        return result