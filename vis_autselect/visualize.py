


def select(data):
    data = organiseInList(data)
    data_dict = dict()
    [data_dict.update(classify(item)) for item in data]
    create_possible_visualizations(data_dict)
    return data


def classify(data):
    if all(isinstance(item, float) for item in data):
        return {'confidence_scores' : data}
    elif all(isinstance(item, bool) | isinstance(item, int) for item in data):
        return {'undefined' : data}
    elif all(isinstance(item, list) for item in data):
        dimensions = [len(data), len(data[0])]
        containing_floats = all(isinstance(item, float) for item in array for array in data)
        print(dimensions)
        print(containing_floats)
    

# Wraps single list in another list on top
def organiseInList(data):
    if any(isinstance(item, list) for item in data):
        return data
    else: 
        return [data]


def create_possible_visualizations(data_dict):
    key_list = list(data_dict.keys())
    