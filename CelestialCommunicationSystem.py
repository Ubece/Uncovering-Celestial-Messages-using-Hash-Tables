from CelestialHash import CelestialHash
from CelestialMessageDecoder import CelestialMessageDecoder
from Parser import FileParser

class CelestialCommunicationSystem:
    def __init__(self, input_file = "CelestialMessagesInitialization.dat"):
        self.parser = FileParser(input_file)

        # get the init data from the .dat file
        self.tableSize, self.loadFactorThreshold = self.parser.get_meta_data()

        # get operations 
        self.insert_ops = self.parser.get_insert_ops()
        self.delete_ops = self.parser.get_delete_ops()
        self.mixed_ops = self.parser.get_mixed_ops()

        # create CelestialHash object
        self.celestialHash = CelestialHash(self.tableSize, self.loadFactorThreshold)

        # get the decoder
        self.messageDecoder = CelestialMessageDecoder(self.celestialHash)

    def handle_Insert(self):
        """
        Handles the insert operations. 
        """
        for operation in self.insert_ops:
            self.celestialHash.insert(operation.key, operation.message)

    def handle_Delete(self):
        """
        Handles the delete operations. 
        """
        for operation in self.delete_ops:
            self.celestialHash.delete(operation.key)

    def handle_Mixed(self):
        """
        Handles the mixed operations: insert or delete. 
        """
        for operation in self.mixed_ops:
            if operation.type == "Insert":
                self.celestialHash.insert(operation.key, operation.message)
            elif operation.type == "Delete":
                self.celestialHash.delete(operation.key)


    def handle_Search(self, key):
        """
        Handles the search operations. 
        """
        return self.celestialHash.search(key)
    
    def getHashTable(self):
        return self.celestialHash.serialize()


    def handle_Decode(self, encodedMessage):
        decodedMessage = self.messageDecoder.decode_message(encodedMessage)
        return decodedMessage