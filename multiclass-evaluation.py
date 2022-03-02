def multiclass_accuracy(results, labels, threshold):
    correct = []
    incorrect = []
    excluded = []
    for result, label in zip(results, labels):
        label_index = label.tolist().index(max(label))
        result_index = result.tolist().index(max(result))
        if max(result) > threshold:
            if label_index == result_index:
                correct.append(1)
            else:
                incorrect.append(1)
        else:
            excluded.append(1)
    accuracy = round(sum(correct)/(sum(correct) + sum(incorrect))*100, 2)
    percent_excluded = round(sum(excluded)/len(labels)*100, 2)
    return accuracy, percent_excluded


def multiclass_per_label_accuracy(results, labels, threshold):
    correct = []
    correct_index = []
    incorrect = []
    incorrect_index = []
    excluded = []
    for result, label in zip(results, labels):
        label_index = label.tolist().index(max(label))
        result_index = result.tolist().index(max(result))
        if max(result) > threshold:
            if label_index == result_index:
                correct.append(1)
                correct_index.append(label_index)
            else:
                incorrect.append(1)
                incorrect_index.append(label_index)
        else:
            excluded.append(1)
            incorrect_index.append(label_index)
    accuracy = round(sum(correct)/(sum(correct) + sum(incorrect))*100, 2)
    percent_excluded = round(sum(excluded)/len(labels)*100, 2)
    counter = 0
    label_list = sorted(list(set(labels)))
    for label_name in label_list:
        print(f'Label {label_name} has individual accuracy of {round(correct_index.count(counter)/(incorrect_index.count(counter) + correct_index.count(counter))*100, 2)}%')
        counter = counter + 1
    return accuracy, percent_excluded
