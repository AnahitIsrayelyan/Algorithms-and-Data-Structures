class Bitarray:
    def __init__(self, args=None):
        self._bits = None
        if args:
            self.extend(args)

    def __str__(self) -> str:
        if self._bits is None:
            return f"bitarray()"
        else:
            return f"bitarray('{bin(self._bits)[2:]}')"
        
    def __repr__(self) -> str:
        if self._bits is None:
            return ''
        else:
            return bin(self._bits)[2:]
        
    def __delitem__(self, index):
        if self._bits is None or index >= len(self):
            raise IndexError("Index out of range")
        if index == 0:
            self._bits = (self._bits & ((1 << (len(self) - 1)) - 1))
        else:
            bits_left = self._bits >> (len(self) - index)
            bits_right = self._bits & ((1 << (len(self) - index - 1)) - 1)
            self._bits = ((bits_left << (len(self) - index - 1)) | bits_right)

    def __getitem__(self, index):
        if self._bits is None or index >= len(self):
            raise IndexError("Index out of range")
        return (self._bits >> (len(self) - index - 1)) & 1

    def __setitem__(self, index, value):
        if self._bits is None or index >= len(self):
            raise IndexError("Index out of range")
        mask = 1 << (len(self) - index - 1)
        if value:
            self._bits |= mask
        else:
            self._bits &= ~mask

    def __len__(self):
        if self._bits is None:
            return 0
        return self._bits.bit_length()

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def all(self) -> bool:
        if self._bits is None:
            return False
        return self._bits == 2 ** len(self) - 1

    def any(self) -> bool:
        return self._bits is not None and self._bits != 0

    def append(self, item):
        if item not in (0, 1, False, True):
            raise ValueError("Invalid value. Bitarray only accepts 0, 1, False, or True.")
        if self._bits is None:
            self._bits = 0
        self._bits <<= 1
        self._bits |= item

    def clear(self):
        self._bits = None

    def copy(self):
        new_bitarray = Bitarray()
        new_bitarray._bits = self._bits
        return new_bitarray

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def fill(self) -> int:
        current_length = len(self)
        remainder = current_length % 8
        bits_added = (8 - remainder) % 8
        self.extend([0] * bits_added)
        return bits_added
    
    def index(self, sub_bitarray, start=0, stop=None) -> int:
        if not isinstance(sub_bitarray, Bitarray):
            raise TypeError("sub_bitarray must be a Bitarray instance")
        bits_string = repr(sub_bitarray)
        if stop is None or stop > len(self):
            stop = len(self)
        for i in range(start, stop - len(bits_string)):
            if str(bin(self._bits)[2:][i:i + len(bits_string)]) == bits_string:
                return i
        raise ValueError("sub_bitarray not found")                

    def insert(self, index, value) -> None:
        if value not in (0, 1, False, True):
            raise ValueError("Invalid value. Bitarray only accepts 0, 1, False, or True.")
        if self._bits is None:
            self._bits = 0
        if index > len(self):
            raise IndexError("Index out of range")
        if index == 0:
            self._bits = (value << len(self) + 1) | self._bits
        else:
            bits_right = self._bits & ((1 << (len(self) - index)) - 1)
            bits_left = self._bits >> (len(self) - index)
            self._bits = (((bits_left << 1) | value) << (len(self) - index) | bits_right)
            # problem in case of insert(0,0) 

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        value = self[index]
        del self[index]
        return value

    def remove(self, value):
        index = self.index(Bitarray([value]))
        self.pop(index)

    def setall(self, value):
        if value not in (0, 1, False, True):
            raise ValueError("Invalid value. Bitarray only accepts 0, 1, False, or True.")
        if value:
            self._bits |= ((1 << len(self)) - 1)
        else:
            self._bits = 0

    def to01(self):
        return repr(self)

    def tolist(self):
        return [int(bit) for bit in self]
