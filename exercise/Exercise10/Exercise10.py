# Exercise 10 solution:
import pickle
import requests

if __name__ == "__main__":
    # Getting the data and writing it to a file
    res = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    with open('data.txt','w') as file:
        file.write(res.text)

    # Reading from the file and storing it as a list of list
    with open('data.txt') as data:
        lines = data.readlines()
        # Store the data as list of list
        # using list comprehension and strip the newline character
        # Also ignore the empty lists
        data_list = [d.rstrip().split(',') for d in lines if d.rstrip() != "" ]

    # Pickle the list of lists
    with open('data.pkl','wb') as p_data:
        pickle.dump(data_list, p_data)

    # unpickle the pickled data
    with open('data.pkl','rb') as dp_data:
        unpickle = pickle.load(dp_data)
        print(unpickle)

