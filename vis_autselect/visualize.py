from vis_autselect.classifiedArray import classifiedArray
import numpy as np


class Visualizer:

    

    def __init__(self):
        self.data_classified = list()

    # Function which selects the type of the input array. 
    def select(self, data):
        if(isinstance(data, np.ndarray)):
                data = data.tolist()
        data = organiseInList(data)
        data = standardize_precition_or_test_values(data) 
        self.data_classified.append(classify(data))

    def select_annoted(self = None, test= None, pred = None, score = None, confusion_matrix = None, roc = None):
        self.data_classified.extend([item for item in locals().values() if type(item) == list])
        

    # Returns the classified data.
    def get_classified_data(self):
        evaluate_classification(self.data_classified)
        return self.data_classified

    # Describes tha classified and not classified arrays.
    def info(self):
        if len(self.data_classified) == 0: 
            print("No data has been entered.")
        else:
            # Find data if is correctly classified.
            availble_data = [x.type[0] for x in self.data_classified if len(x.type) < 2]
            print("The following arrays have beem classified: ", availble_data, "\n")

            not_classified = [x for x in self.data_classified if len(x.type) > 1]
            for item in not_classified:
                print("For the given array a decision between the types: ", item.type, " could have not been made.")
                print("Input Data: ", item.data, "\n") 

    # Deletes all the entered data.
    def delete_data(self):
        self.data_classified = list()




# Classifys the data in dict
def classify(data):
    return classifiedArray(data, classify_types(data))

def classify_types(data):
    if contains_type(list, data):
        if len(data) == 2:
            if contains_type_deep(int, data):
                return['Confusion Matrix'] 
            if contains_type_deep(float, data):
                return ['ROC']
    else:
        if contains_type(float, data):
            return ['Confidence Scores']
        elif contains_type(bool, data) or contains_type(int, data) or contains_type(str, data):
            return ['Ground Truth Values', 'Predictions']
        else:
            raise Exception("No type found")

# Wraps single list in another list on top
def organiseInList(data):
    if any(isinstance(item, list) for item in data):
        return data
    else: 
        return data


def standardize_precition_or_test_values(arr):
    if all(isinstance(item, bool) for item in arr):
        return (['1' if item  else '2' for item in arr])
    elif all(isinstance(item, int) for item in arr):
        return [str(item) for item in arr]
    else:
        return arr

def contains_type_deep(type, data):
    if all(isinstance(item, list) for item in data):
        return all(isinstance(item, type) for array in data for item in array)
    else: 
        return all(isinstance(item, type) for item in data)

def contains_type(type, data):
    return all(isinstance(item, type) for item in data)


def evaluate_classification(data):
    exact_guesses = len([x for x in data if len(x.type) < 2])
    amount_inputs = len(data)
    print(exact_guesses, 'out of ', amount_inputs, 'inputed array can be classified')



    


    