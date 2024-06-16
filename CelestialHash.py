class CelestialHash:
    def __init__(self, tableSize, loadFactorThreshold):
        self.tableSize = tableSize
        self.loadFactorThreshold = loadFactorThreshold
        self.hashTable = [None] * self.tableSize
        self.numElements = 0

    def count(self):
        return self.numElements
    
   
    def __init__(self, table_size):
        self.table_size = table_size

    
       
    
    
    def __init__(self, tableSize, loadFactorThreshold):
        self.table_size = tableSize
        self.load_factor_threshold = loadFactorThreshold
        # other initialization code...


    def serialize(self):
        """
        Converts the entire hash table to a dictionary format, including valid entries, 'TOMBSTONE' markers, and None values.
        Provided for testing purposes. Please do not modify.
        """
        serialized_data = {}
        for index, entry in enumerate(self.hashTable):
            if entry is None:
                serialized_data[f"Slot {index}"] = None
            elif entry == 'TOMBSTONE':
                serialized_data[f"Slot {index}"] = 'TOMBSTONE'
            else:
                key, value = entry
                serialized_data[key] = value
        return serialized_data
    
    
    def hash1(key, table_size):
        return sum(ord(char) * (i + 1) ** 2 for i, char in enumerate(key)) % table_size


    def hash2(self, key):
        return 1 + sum(ord(char) * (i + 1) for i, char in enumerate(key)) % (self.table_size - 1)



    def insert(self, key, message):
        """
        TO BE IMPLEMENTED
        Insert elements into the hash table using the primary hash function, avoiding 'TOMBSTONE's.
        Handle collisions using the secondary hash function. 
        Handle table resizing when necessary.
        """
        if self.count / self.table_size > self.load_factor_threshold:
            self.resize()
        step = self.hash2(key)
        idx = self.hash1(key)
        while self.table[idx] not in (None, "TOMBSTONE"):
            idx = (idx + step) % self.table_size
        self.table[idx] = (key, message)
        self.count += 1
        if self.count() / self.table_size > self.load_factor_threshold:
            self.resize()

        

    def delete(self, key):
        """
        TO BE IMPLEMENTED
        Remove specified elements from the hash table, replacing them with placeholder: 'TOMBSTONE'.
        Handle table resizing when necessary.
        """
        idx = self.hash1(key)
        step = self.hash2(key)
        while self.table[idx] is not None:
            if self.table[idx] != "TOMBSTONE" and self.table[idx][0] == key:
                self.table[idx] = "TOMBSTONE"
                self.count -= 1
                return True
            idx = (idx + step) % self.table_size
        return False
        

    def search(self, key):
        """
        TO BE IMPLEMENTED
        Retrieve and display stored messages based on celestial patterns, handling 'TOMBSTONE's.
        """
        idx = self.hash1(key)
        step = self.hash2(key)
        while self.table[idx] is not None:
            if self.table[idx] != "TOMBSTONE" and self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + step) % self.table_size
        return None

