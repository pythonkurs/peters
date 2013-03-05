from collections import Counter
import sys


def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return len(list(set(factors)))
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return len(list(set(factors)))
        elif p > 2:
            p += 2
        else:
            p += 1


def ipython_parallel():
    from IPython.parallel import Client

    cli = Client()
    dview = cli[:]

    @dview.parallel(block=True)
    def factorize(n):
        if n < 2:
            return []
        factors = []
        p = 2

        while True:
            if n == 1:
                return len(list(set(factors)))
            r = n % p
            if r == 0:
                factors.append(p)
                n = n / p
            elif p * p >= n:
                factors.append(n)
                return len(list(set(factors)))
            elif p > 2:
                p += 2
            else:
                p += 1

    result = factorize.map(range(2, 500000))
    print(Counter(result))


def multi():
    import multiprocessing
    pool = multiprocessing.Pool(processes=2)
    result = pool.map(factorize, range(2, 500000))
    print(Counter(result))


def normal():
    list_num_unique = []

    for i in range(2, 500000):
        temp_factor_list = factorize(i)
        list_num_unique.append(temp_factor_list)

    print Counter(list_num_unique)


def main(argvs):
    if argvs[1] == "s":
        normal()
    elif argvs[1] == "m":
        multi()
    elif argvs[1] == "i":
        ipython_parallel()


if __name__ == "__main__":
    main(sys.argv)
