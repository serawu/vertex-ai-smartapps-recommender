import pickle

with open('model.pkl', 'rb') as pickle_file:
    x = pickle.load(pickle_file)