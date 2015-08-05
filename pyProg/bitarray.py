''' purpose:
    Learn how to build new Python data structures.
    Model the API after existing tools.
    Learn basic bit-flipping skills.
    Practice common dunder methods.
    Learn how all sequences are automatically iterable.
'''

class BitArray:

    def __init__(self, numbits):
        self.numbits = numbits
        numbytes = (numbits + 7) // 8              # ceiling division (divides and rounds up)
        self.data = bytearray(numbytes)

    def __len__(self):
        return self.numbits

    def __setitem__(self, index, value):
        if index >= self.numbits:
            raise IndexError('Out of range')
        if value not in {0, 1}:
            raise ValueError('bit must be a zero or one')
        bytenum, bitnum = divmod(index, 8)
        mask = 1 << bitnum
        if value:
            self.data[bytenum] |= mask
        else:
            self.data[bytenum] &= ~mask

    def __getitem__(self, index):
        if index >= self.numbits:
            raise IndexError('Out of range')
        bytenum, bitnum = divmod(index, 8)
        return (self.data[bytenum] >> bitnum) & 1

if __name__ == '__main__':
    ba = BitArray(20)
    print len(ba)
    ba[11] = 1
    ba[14] = 1
    ba[7] = 1
    ba[11] = 0
    print list(ba)
