class Operation:
    """
    PROVIDED CLASS to represent an operation in the input file. Please do not update.
    """
    def __init__(self, operation_type, key, message=None):
        self.type = operation_type
        self.key = key
        self.message = message

    def to_dict(self):
        return {
            "type": self.type,
            "key": self.key,
            "message": self.message
        }

class FileParser:
    """
    PROVIDED CLASS to parse the input file. Please do not update.
    """
    def __init__(self, filename):
        self.filename = filename
        self.insert_ops, self.delete_ops, self.mixed_ops = self.load_operations()

    def get_meta_data(self):
        tableSize = None
        loadFactorThreshold = None
        with open(self.filename, 'r') as file:
            for line in file:
                if line.startswith("TableSize:"):
                    tableSize = int(line.strip().split(": ")[1])
                elif line.startswith("LoadFactorThreshold:"):
                    loadFactorThreshold = float(line.strip().split(": ")[1])
                if tableSize is not None and loadFactorThreshold is not None:
                    break
        return tableSize, loadFactorThreshold

    def load_operations(self):
        insert_ops = []
        delete_ops = []
        mixed_ops = []
        current_list = None
        with open(self.filename, 'r') as file:
            for line in file:
                if "# Insert" in line:
                    current_list = insert_ops
                elif "# Delete" in line:
                    current_list = delete_ops
                elif "# Mixed" in line:
                    current_list = mixed_ops

                if line.strip() and not line.startswith("#") and current_list is not None:
                    parts = line.strip().split(", ")
                    operation_type = parts[0]
                    key = parts[1].strip('"')
                    message = parts[2].strip('"') if len(parts) > 2 else None
                    current_list.append(Operation(operation_type, key, message))

        return insert_ops, delete_ops, mixed_ops
    
    def get_insert_ops(self):
        return self.insert_ops
    
    def get_delete_ops(self):
        return self.delete_ops
    
    def get_mixed_ops(self):
        return self.mixed_ops
    



    
