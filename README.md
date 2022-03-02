# Overview

This repository provides a series of functions that help with a very specific objective - determining the success of deep learning algorithms that are either multiclass-multilabel or multiclass. This is an area that is overlooked by many machine learning libraries. Algorithms that output a series of probabilities that are associated with multiple labels can be difficult to evaluate for accuracy, especially if the user wants to know accuracy at a specific pobability threshold. These functions solve this problem and can be easily pasted into a script, jupyter notebook, or applied within cross-fold validation.


## multiclass-multilabel-evaluation

1) exact_accuracy
This function provides the accuracy of the model as a whole, treating TP and FN as all labels being predicted correctly for an item.
Accuracy is the ratio of correctly predicted observations to all observations.
Accuracy = TP+FN/TP+FN+FP+TN

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

Return:
A list of accuracy scores in percentages for each label in the order of the labels given.


2) individual_label_accuracy
This function provides the accuracy for each individual label accross all results.
Accuracy is the ratio of correctly predicted observations to all observations.
Accuracy = TP+FN/TP+FN+FP+TN

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

Return:
A list of accuracy scores in percentages for each label in the order of the labels given.


3) individual_label_precision

This function provides the precision for each individual label (including both true positives and true negatives) across all results.
Precision is the ratio of correctly predicted positive observations to the total predicted positive observations or the number of correct positive predictions made.
Precision = TP/TP+FP

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

Return:
A list of precision scores in percentages for each label in the order of the labels given.


4) individual_label_recall

This function provides the recall for each individual label (ONLY true positives) across all results.
Recall is a metric that quantifies the number of correct positive predictions made out of all positive predictions that could have been made.
Recall = TP/TP+FN

The inputs to this function are:
A list of arrays that contain the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of arrays that contain the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

Return:
A list of recall scores in percentages for each label in the order of the labels given.


5) per_label_f1_scores (f1 scores for each label)
This function provides the f1 score for each individual label. This is 2*((precision*recall)/(precision+recall))

The inputs to this function are:
A list of arrays that contain the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of arrays that contain the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

Return:
A list of f1 scores for each label in the order of the labels given.


## multiclass-evaluation

1) multiclass_accuracy
This function provides the accuracy of the model as a whole, treating TP and FN as all labels being predicted correctly for an item.
Accuracy is the ratio of correctly predicted observations to all observations.
Accuracy = TP+FN/TP+FN+FP+TN

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with the needed confidence to signify a correct result.

Return:
Accuracy of the model and the percent of excluded results based on the threshold value.


2) multiclass_per_label_accuracy
This function provides the accuracy of the model at the individual label level - treating TP and FN as all labels being predicted correctly for an item.
Accuracy is the ratio of correctly predicted observations to all observations.
Accuracy = TP+FN/TP+FN+FP+TN

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with the needed confidence to signify a correct result.

Return:
Accuracy of the model and the percent of excluded results based on the threshold value.
The model also prints out the accuracy of each individual label.
