import time

def get_primes(num_of_primes_desired):
    primes = set()
    number = 2

    while len(primes) < (num_of_primes_desired - 1):
        for i in range(1, number):
            if (number == 2) or (number % i != 0):
                primes.add(number)
                continue
            else:
                if number in primes:
                    primes.remove(number)
                break

        number += 1
        print(f"found {len(primes)} primes")

    return primes

if __name__ == "__main__":
    start_time = time.time()
    prime_set = get_primes(10001)
    print(f"{max(prime_set)}")


    print("--- %s seconds ---" % (time.time() - start_time))