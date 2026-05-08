def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """

    top_k = recommended[:k] #get first k predictions
    relevant = set(relevant)
    hits = len(set(top_k)& relevant)

    pres = hits/k 
    recall = hits/len(relevant) if len(relevant) > 0 else 0.0 
    return [pres,recall]