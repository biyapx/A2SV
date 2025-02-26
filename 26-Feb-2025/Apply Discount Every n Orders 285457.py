# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = {products[i]: prices[i] for i in range(len(products))}
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        # Increment customer count
        self.customer_count += 1
        
        # Calculate subtotal
        subtotal = sum(amount[i] * self.prices[product[i]] for i in range(len(product)))
        
        # Apply discount if it's the nth customer
        if self.customer_count % self.n == 0:
            subtotal = subtotal * ((100 - self.discount) / 100)
        
        return subtotal