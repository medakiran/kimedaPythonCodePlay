''' Learn about a probabalistic, space-efficient data structure for membership testing.
    Compare the speed and memory utilization of several underlying data stores
    including sets, lists, bytearrays, and bitarrays.
    Learn about the random module and how to create well named helper functions.
    Review why xrange() is space efficient.
    Learn about how any() and all() can clean-up looping logic.
'''

from random import seed, sample
from bitarray import BitArray

class BloomFilter:

    def __init__(self, iterable=(), population=56, probes=6):
        self.population = xrange(population)
        self.probes = probes
        self.data = BitArray(population)
        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        for i in lucky:
            self.data[i] = 1

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        return all([self.data[i] for i in lucky])


if __name__ == '__main__':
    medaFamily = BloomFilter('kiran kumar meda swapna raja java'.split())
    print 'kiran' in medaFamily
    print 'king' in medaFamily
