def gen_primes():
    # https://stackoverflow.com/questions/567222/simple-prime-generator-in-python/568618#568618
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def main():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        max_prime_number = int(input().split(" ")[0])
        ciphertext = [int(x) for x in input().split(" ")]

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        test_sets = []

        for prime_number in gen_primes():
            if ciphertext[0] % prime_number == 0:
                if (ciphertext[0] // prime_number) in gen_primes():
                    test_sets.append([prime_number, ciphertext[0] // prime_number])
                    break

        for test_set in test_sets:
            for test_value in test_set:
                tmp_value = test_value
                flag = True
                for enc_value in ciphertext:
                    if enc_value % tmp_value == 0:
                        tmp_value = enc_value // tmp_value
                    else:
                        flag = False
                        break
                if flag:
                    first_correct_prime = test_value
                    break

        primes_found = [first_correct_prime]
        for enc_value in ciphertext:
            primes_found.append(enc_value // primes_found[-1])

        primes_found = list(set(primes_found))
        primes_found.sort()

        decoded = alphabet[primes_found.index(first_correct_prime)]
        tmp_prime = first_correct_prime
        for enc_value in ciphertext:
            decoded += alphabet[primes_found.index(enc_value // tmp_prime)]
            tmp_prime = enc_value // tmp_prime


        print("Case #{}: {}".format(case_id, decoded))

if __name__ == '__main__':
    main()
