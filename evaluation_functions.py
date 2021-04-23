def exact_match(results, labels, threshold):
    correct = []
    total = []
    for result, label in zip(results, labels):
        all_correct_flag = True
        for r, l in zip(result, label):
            if l == 1:
                if r < threshold:
                    all_correct_flag = False
            if l == 0:
                if r >= threshold:
                    all_correct_flag = False
        if all_correct_flag:
            correct.append(1)
        total.append(1)
    return (len(correct)/len(total))*100


def true_positives(results, labels, threshold):
    tp_correct = []
    tp_total = []
    for result, label in zip(results, labels):
        for r, l in zip(result, label):
            if l == 1:
                if r >= threshold:
                    tp_correct.append(1)
                tp_total.append(1)
    return (len(tp_correct)/len(tp_total))*100


def per_label(results, labels, threshold):
    pl_correct = []
    pl_total = []
    for result, label in zip(results, labels):
        for r, l in zip(result, label):
            if l == 1:
                if r >= threshold:
                    pl_correct.append(1)
            if l == 0:
                if r < threshold:
                    pl_correct.append(1)
            pl_total.append(1)     
    return (len(pl_correct)/len(pl_total))*100


def individual_label_accuracies(results, labels, threshold):
    list_to_df = []
    for result, label in zip(results, labels):
        temp_list = []
        for r, l in zip(result, label):
            if l == 1:
                if r >= threshold:
                    temp_list.append(1)
                else:
                    temp_list.append(0)
            if l == 0:
                if r <= threshold:
                    temp_list.append(1)
                else:
                    temp_list.append(0)
        list_to_df.append(temp_list)
    df = pd.DataFrame(list_to_df)
    final_scores = [round(label_score/len(df), 3) for label_score in df.sum()]
    return final_scores


def individual_label_accuracies_tp(results, labels, threshold):
    list_to_df = []
    for result, label in zip(results, labels):
        temp_list = []
        for r, l in zip(result, label):
            if l == 1:
                if r >= threshold:
                    temp_list.append(1)
                else:
                    temp_list.append(0)
            else:
                temp_list.append(0)
        list_to_df.append(temp_list)
    df = pd.DataFrame(list_to_df)
    final_scores = [round(label_score/len(df), 3) for label_score in df.sum()]
    return final_scores