import pickle

def filewrite(file_name, data):
    file_handler = open(file_name, "wb")
    # write in binary
    pickle.dump(data, file_handler)
    file_handler.close()
    
def fileread(file_name):
    file_handler = open(file_name, "rb")
     # read in binary
    data = pickle.load(file_handler)
    return data
    


