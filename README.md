# multiclass-multilabel-evaluation

This repository provides a series of functions that help with a very specific objective. The functions in this repository provide various evaluation metrics for multiclass-multilabel algorithm outputs. This is an area that most machine learning library wrappers overlook. Algorithms that output a series of probabilities that are associated with multiple labels can be difficult to evaluate for accuracy, especially if the user wants to know accuracy at a specific pobability threshold. These functions solve this problem and can be easily pasted into a script, jupyter notebook, or applied within cross-fold validation.

These are the functions currently included in the repository, their inputs, their outputs, and what they accomplish:

1) exact_match

This function provides the percent of results that are an exact match across all labels at a certain threshold. For example, an algorithm that outputs five labels with outcomes of 0.55, 0.11, 0.78, 0.99, 0.02, would return a result of 0% accuracy if the threshold was set at 75% and the correct labels were True, False, True, True, False. Only the first item would be marked as incorrect, but since it is not an exact match if this was the only output, the accuracy would be 0%. If the threshold was changed to 50% then the accuracy would be 100%. 

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

2) true_positives

This function provides the accuracy for true positives in the results at a certain threshold. For example, an algorithm that outputs five labels with outcomes of 0.55, 0.11, 0.78, 0.99, 0.02, would return a result of 66% accuracy if the threshold was set at 75% and the correct labels were True, False, True, True, False. There are three possibilities of a true positive and only two were predicted correctly at the 75% threshold.

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

3) per_label

This function provides the accuracy for both true positives and true negatives in the results at a certain threshold. For example, an algorithm that outputs five labels with outcomes of 0.55, 0.11, 0.78, 0.99, 0.02, would return a result of 80% accuracy if the threshold was set at 75% and the correct labels were True, False, True, True, False. There are five possibilities of a true positive or true negative and four were predicted correctly at the 75% threshold.

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.


4) individual_label_accuracies

This function provides the accuracy for each individual label (including both true positives and true negatives) across all results. For example, an algorithm that outputs five labels with outcomes of 0.55, 0.11, 0.78, 0.99, 0.02, would return a result of five accuracy results of 0%, 100%, 100%, 100%, 100% if the threshold was set at 75% and the correct labels were True, False, True, True, False.

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

5) individual_label_accuracies_tp

This function provides the accuracy for each individual label (ONLY true positives) across all results. For example, an algorithm that outputs five labels with outcomes of 0.55, 0.11, 0.78, 0.99, 0.02, would return a result of five accuracy results of 0%, NA, 100%, 100%, NA if the threshold was set at 75% and the correct labels were True, False, True, True, False.

The inputs to this function are:
A list of lists or an array that contains the probability outputs (this is the typical output of `.predict` call in most machine learning libraries).
A list of lists or an array that contains the labels for the associated results (this is typically stored in the y_test of your split).
A threshold for the probability that is associated with a correct result.

NOTE: In my opinion this may be the most important function for someone evaluating a multiclass-multilabel algorithm as it alerts the programmer of which labels are performing well at identifying the desired result.
