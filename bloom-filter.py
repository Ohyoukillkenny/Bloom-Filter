class bloom_filter:
    def __init__(self, num_of_bits, num_of_K):
        self._hash_table = [0 for i in range(num_of_bits)]
        self._num_of_bits = num_of_bits
        self._num_of_K = num_of_K

    def filter_hash_func(self, key_input):
        result = [i*(key_input**2 + key_input**3) % self._num_of_bits for i in range(1, self._num_of_K+1)]
        flag = True
        for item in result:
            if self._hash_table[item] == 0:
                self._hash_table[item] = 1
                flag = False
            else:
                continue
        return flag

    def show_hash_table(self):
        print self._hash_table

if __name__ == '__main__':
    my_bloom_filter = bloom_filter(32,3)
    for y in [2013, 2010, 2007, 2004, 3200]:
        if my_bloom_filter.filter_hash_func(y):
            print 'Might Exist'
        else:
            print 'Not Exist'
            my_bloom_filter.show_hash_table()