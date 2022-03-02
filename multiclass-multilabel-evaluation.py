def exact_match(results, labels, threshold):
    # accuracy, exact
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


def individual_label_accuracy(results, labels, threshold):
    # accuracy
    results_transformed = np.array(results).T
    labels_transformed = np.array(labels).T
    final = []
    for result, label in zip(results_transformed, labels_transformed):
        tps_tns = []
        for r, l in zip(result, label):
            if l:
                if r >= threshold:
                    tps_tns.append(1)
            else:
                if r < threshold:
                    tps_tns.append(1)
        try:
            final.append(f'{round(sum(tps_tns)/len(result)*100, 2)}%')
        except ZeroDivisionError:
            final.append('No labels in test sample')
    return final


def individual_label_precision(results, labels, threshold):
    results_transformed = np.array(results).T
    labels_transformed = np.array(labels).T
    final = []
    for result, label in zip(results_transformed, labels_transformed):
        tps = []
        tps_fps = []
        for r, l in zip(result, label):
            if l:
                if r >= threshold:
                    tps.append(1)
            if r >= threshold:
                tps_fps.append(1)
        try:
            final.append(f'{round(sum(tps)/sum(tps_fps)*100, 2)}%')
        except ZeroDivisionError:
            final.append('No labels in test sample')
    return final


def individual_label_recall(results, labels, threshold):
    results_transformed = np.array(results).T
    labels_transformed = np.array(labels).T
    final = []
    for result, label in zip(results_transformed, labels_transformed):
        tps_fns = []
        tps = []
        for r, l in zip(result, label):
            if l:
                tps_fns.append(1)
                if r >= threshold:
                    tps.append(1)
        try:
            final.append(f'{round(sum(tps)/sum(tps_fns)*100, 2)}%')
        except ZeroDivisionError:
            final.append('No positive labels in test sample')
    return final


def per_label_f1_scores(results, labels, threshold):
    f1_scores = []
    precision = individual_label_precision(results, labels, threshold)
    recall = individual_label_recall(results, labels, threshold)
    for p, r in zip(precision, recall):
        try:
            p = float(p.strip('%'))/100
            r = float(r.strip('%'))/100
            f1_scores.append(2*((p*r)/(p+r)))
        except ValueError:
            f1_scores.append('f1 score not possible')
    return f1_scores
