"""หาจำนวนเฉพาะ"""
def primenumber():
    """ฟังก์ชันหาจำนวนเฉพาะ"""
    num_start, num_end = map(int, input().split())
    prime_numbers = []
    total_prime = 0
    for i in range(num_start, num_end + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if not i % j:
                    break
            else:
                prime_numbers.append(i)
                total_prime += 1
    if len(prime_numbers) > 0:
        print(" ".join(map(str, prime_numbers)))
    print(f"Total primes: {total_prime}")
primenumber()
