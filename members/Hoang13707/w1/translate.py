"""C++ starting point

#include <iostream>
#include <string>
#include <algorithm>

std::string reverse_sequence(std::string data) {
    std::reverse(data.begin(), data.end());
    return data;
}
"""


def reverse_sequence(data):
    return data[::-1]


if __name__ == "__main__":
    print(reverse_sequence("hello"))
    print(reverse_sequence([1, 2, 3, 4]))

"""C++ starting point

#include <vector>
#include <algorithm>

void reverse_in_place(std::vector<int>& data) {
    std::reverse(data.begin(), data.end());
}
"""


def reverse_in_place(data):
    data.reverse()


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    reverse_in_place(arr)
    print(arr)

"""C++ starting point

#include <vector>
#include <cmath>

std::vector<int> primes_up_to(int n) {
    std::vector<int> primes;
    for (int is_prime = 2; is_prime <= n; ++is_prime) {
        bool prime = true;
        for (int i = 2; i <= std::sqrt(is_prime); ++i) {
            if (is_prime % i == 0) {
                prime = false;
                break;
            }
        }
        if (prime) {
            primes.push_back(is_prime);
        }
    }
    return primes;
}
"""


def primes_up_to(n):
    primes = []
    for is_prime in range(2, n + 1):
        if all(is_prime % i != 0 for i in range(2, int(is_prime ** 0.5) + 1)):
            primes.append(is_prime)
    return primes


if __name__ == "__main__":
    print(primes_up_to(20))