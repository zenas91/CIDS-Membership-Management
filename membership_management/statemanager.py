def check_state(trust, peak_trust=10, trusted=80, review=50):
    """
    This checks for the state of the entity being considered based on the percentage of the trust value with respect to
    peak or maximum trust value.

    :param trust: int
        The cumulative trust value of the entity
    :param peak_trust: int
        The maximum value for the cumulative trust
    :param trusted: int
        The trusted entity threshold. Entities with cumulative trust above this threshold is regarded as trusted.
        Default value is 80%
    :param review: int
        The threshold for entites under review. Entities with cumulative trust below this threshold is placed under
        review.
    :return: string
        The state of the entity. It is either "probation", "trusted", or "review"
    """

    state = "probation"
    per = (trust / peak_trust) * 100
    if per >= trusted:
        state = "trusted"
    elif per <= review:
        state = "review"

    return state
