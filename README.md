# Notebook for data science autoselect. 

This is an experimental Project. The aim of this library is to autoselect visuaizations to evaluate machine learning models. 

## Import the library 
You can import th library locally i from this repo via 
```python
import vis_autselect.visualize as visualize
```

Instatiate a visualizer object: 
```pyhton
vis = visualize.Visualizer()
```

## Input data with the select function 
You can import data in two different ways 
1. Pass in an output array from your ml experiment 
`vis.select(somer_arr)`
2. Pass in an annotated array to help classify the input data `vis.input_dict({Confidence Scores': y_score})`


There is also the possibillity to import multiple object as such: 
```python
annotaded_data = {
    'Confidence Scores': y_score, 
    'Confusion Matrix' : cm,
    'ROC' : roc,
    'Ground Truth Values' : y_test, 
    'Predictions' : y_pred
}

vis.input_dict(annotaded_data)
```
## Get info about the classified data
```python 
vis.info()
```

## Visualize Experimental Feature

After you have inputed all the data you can just call the `visualize()` function and it will generated all possible vissualizations.

## Try it yourself and explore examples

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vali101/vis-autoselect-ml/master)
