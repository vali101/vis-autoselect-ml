from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

def plot_confusion_matrix(cm_data):
    return ConfusionMatrixDisplay(cm_data).plot()
