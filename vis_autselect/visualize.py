from vis_autselect.classifiedArray import classifiedArray


class Visualizer:

    def __init__(self):
        self.data_classified = list()

    def select(self, data):
        data = organiseInList(data)
        data = standardize_precition_or_test_values(data) 
        self.data_classified.append(classify(data))
        return data

    def get_classified_data(self):
        return self.data_classified



# Classifys the data in dict
def classify(data):
    return classifiedArray(data, classify_types(data))

def classify_types(data):
    if contains_type(float, data):
        return 'confidence_scores'
    elif contains_type(bool, data) or contains_type(int, data) or contains_type(str, data):
        return 'undefined'
    elif contains_type(list, data):
        dimensions = len(data)
        #print(dimensions)
        #print(containing_floats)
        #print(containing_ints)
        #print()
        if dimensions == 2:
            if contains_type(float, data):
                return 'roc'
            elif contains_type(int, data):
                return 'cm'
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

def contains_type(type, data):
    if all(isinstance(item, list) for item in data):
        return all(isinstance(item, type) for array in data for item in array)
    else: 
        return all(isinstance(item, type) for item in data)


    


    