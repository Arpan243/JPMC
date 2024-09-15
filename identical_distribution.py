import math

# Function to generate all primes up to a certain number using the Sieve of Eratosthenes
def generate_primes_up_to(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_num + 1, p):
                is_prime[multiple] = False
                
    primes = [p for p in range(2, max_num + 1) if is_prime[p]]
    return primes

# Optimized function using only prime packet sizes
def cardPackets(cardTypes):
    n = len(cardTypes)
    max_card_count = max(cardTypes)
    
    # Generate all prime numbers up to the maximum card count
    primes = generate_primes_up_to(max_card_count)
    
    min_additional_cards = float('inf')
    
    # Iterate over prime packet sizes only
    for packet_size in primes:
        additional_cards = 0
        
        # Calculate how many additional cards are needed for this packet size
        for count in cardTypes:
            remainder = count % packet_size
            if remainder != 0:
                additional_cards += packet_size - remainder
        
        # Keep track of the minimum additional cards needed
        min_additional_cards = min(min_additional_cards, additional_cards)
    
    return min_additional_cards

# Example usage:
cardTypes = [4, 7, 5, 11, 15]
result = cardPackets(cardTypes)
print(result)  # Output: 4
