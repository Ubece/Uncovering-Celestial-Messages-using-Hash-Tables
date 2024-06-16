import re

class CelestialMessageDecoder:
    def __init__(self, celestialHash, shift=3):
        self.celestialHash = celestialHash

    def decode_message(self, encodedMessage):
        """
        TO BE IMPLEMENTED
        Decode the message according to the specified algorithm in the hw text.
        """
        patterns = encodedMessage.split('|')
        decoded_message = []
        for pattern in patterns:
            message = self.hash_table.search(pattern)
            decoded_message.append(message if message else "[UNKNOWN]")
        return ' '.join(decoded_message)



