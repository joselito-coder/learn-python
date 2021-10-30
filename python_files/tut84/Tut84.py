import pickle

# cars = ["Audi" ,"Ferrari","Maruti Suzuki","BMW","Harryti Tuzuki"]
# fileObj = open('cars.pkl','wb')
# pickle.dump(cars, fileObj)
# fileObj.close()

with open('cars.pkl','rb') as fileObj:
    cars  = pickle.load(fileObj)
    print(cars)
    print(type(cars))

# Quick quick answer

# pickle.loads = yeah function depickle karta hai data  ek byte pickle object se