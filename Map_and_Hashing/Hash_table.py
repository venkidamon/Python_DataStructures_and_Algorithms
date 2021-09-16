"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""



class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        index = self.calculate_hash_value(string)
        if index!=-1:
            if self.table[index] != None:
                self.table[index].append(string)

            else:
                self.table[index] = [string]
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        index = self.calculate_hash_value(string)
        if index !=-1:
            if self.table[index] != None:
                if string in self.table[index]:
                    return index

        return -1

    def calculate_hash_value(self, string):
        if len(string) >= 2:
            code = ord(string[0])*100 +  ord(string[1])
            return code
        return -1
    
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
