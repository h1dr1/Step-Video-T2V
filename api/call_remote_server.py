import pickle
import io

class SafeUnpickler:
    def __init__(self, file):
        self.file = file

    def load(self):
        return pickle.load(self.file)

def load_data(file):
    with open(file, 'rb') as f:
        unpickler = SafeUnpickler(f)
        return unpickler.load()

# Your other API functionality would go here

# Example of loading data using the safe unpickler:
# data = load_data('data.pkl')