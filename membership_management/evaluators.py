def compute_trust(model, x, y, threshold=70, alpha=1.5, beta=2, method=0):
    """
    This function computes the trust value of a model based on the provided challenge dataset. The performance of the
    entity is classified into weak and strong classification, afterwards the trust value is computed accordingly.

    :param model:
        The model of the entity for which the trust value is being computed.
    :param x: array
        The challenge dataset
    :param y: array
        The label of the challenge dataset.
    :param threshold: int
        The separation threshold for weak and strong classification
    :param alpha: float
         The exponent value for strong classification trust computation
    :param beta: float
        The exponent value for weak classification trust computation
    :param method: int
        Signifies the trust computation method to be adopted. 0 means a faster decline than increase in the trust value.
        1 means equal increase and decrease speed.
    :return: float
        The trust value based on the current challenge
    """

    if method != 0 and method != 1:
        raise ValueError("Invalid input for parameter 'method'. Method can only be 0 or 1.")

    pred_prob = model.predict_proba(x)
    y_sc = 0
    y_sf = 0
    y_wc = 0
    y_wf = 0

    for i, p in enumerate(pred_prob):
        if p.max() < threshold:
            if p.argmax() == y[i]:
                y_wc += 1
            else:
                y_wf += 1
        else:
            if p.argmax() == y[i]:
                y_sc += 1
            else:
                y_sf += 1

    n = y.size
    strong = n ** (-alpha) * (y_sc - y_sf)

    if method == 0:
        weak = (n ** (-beta) * y_wc) - (n ** (-alpha) * y_wf)
    else:
        weak = n ** (-beta) * (y_wc - y_wf)

    t_v = strong + weak
    return t_v


def add_trust(t_old, t_v, max_value=10):
    """
    This function adds the newly computed trust value to the cumulative trust

    :param t_old: float
        The current cumulative trust at the point of computation
    :param t_v: float
        The newly computed trust value
    :param max_value: int
        The maximum value for the cumulative trust
    :return: float
        The newly computed cumulative trust
    """

    n_t = t_old + t_v
    if n_t > max_value:
        return max_value
    else:
        if n_t < 0:
            return 0
        else:
            return n_t
