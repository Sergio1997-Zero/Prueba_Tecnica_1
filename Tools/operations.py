

class prime_numbers:

    def prime_numbers(prime):

        count_prime = 0

        for x in prime: 

            if x <= 1:

                break

            elif x == 2:

                count_prime += 1

            else:

                for y in range(2, x):

                    if x % y == 0:

                        break

                    else:

                        count_prime += 1

                        break

        return count_prime

class pair_numbers:

    def pair_numbers(pair):

        count_pair = 0

        for x in pair:

            if x % 2 == 0:

                count_pair += 1

        return count_pair


class odd_numbers:

    def odd_numbers(odd):

        count_odd = 0

        for x in odd:

            if x % 2 != 0:

                count_odd += 1

        return count_odd
