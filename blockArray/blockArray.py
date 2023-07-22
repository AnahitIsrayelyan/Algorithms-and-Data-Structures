class BlockArray:
    def __init__(self, block_size=8):
        self._block_size = block_size
        self._blocks = []

    def __len__(self):
        return sum(len(block) for block in self._blocks)
    
    def print(self):
        print(self._blocks)
    
    def append(self, value):
        self.insert(len(self), value)

    def insert(self, index, value):
        if index > len(self):
            raise IndexError("Index out of range.")
        
        block_index, local_index = divmod(len(self), self._block_size)
        if len(self) % self._block_size == 0:
            self._blocks.append([None for _ in range(self._block_size)])
        else:
            for i in range(self._block_size - len(self._blocks[-1])):
                self._blocks[block_index].append(None)

        i_block, i_index = divmod(index, self._block_size)

        for i in range(block_index, i_block, -1):
            for j in range(self._block_size-1, 0, -1):
                self._blocks[i][j] = self._blocks[i][j-1]
            if i != 0:
                self._blocks[i][0] = self._blocks[i-1][self._block_size-1]

        for i in range(self._block_size-1, i_index, -1):
            self._blocks[i_block][i] = self._blocks[i_block][i-1]
        self._blocks[i_block][i_index] = value

        while True:
            if self._blocks[-1][-1] is not None:
                break
            self._blocks[-1].pop()

    def pop(self):
        if not len(self):
            raise IndexError('BlockArray is empty.')
        self._blocks[-1].pop()

    def delete(self, index):
        i_block, i_index = divmod(index, self._block_size)
        self._blocks[i_block][i_index] = None

    def remove(self, index):
        if index >= len(self):
            raise IndexError("Index out of range.")

        i_block, i_index = divmod(index, self._block_size)
        value_to_remove = self._blocks[i_block][i_index]

        last_block_index = len(self._blocks) - 1

        for i in range(i_index, self._block_size - 1):
            self._blocks[i_block][i] = self._blocks[i_block][i + 1]

        for i in range(i_block, last_block_index):
            self._blocks[i][self._block_size - 1] = self._blocks[i + 1][0]
            for j in range(0, self._block_size - 1):
                self._blocks[i + 1][j] = self._blocks[i + 1][j + 1]

        if len(self) % self._block_size == 0:
            self._blocks[last_block_index].pop()

        if len(self._blocks[last_block_index]) == 0:
            self._blocks.pop()

        return value_to_remove
    


