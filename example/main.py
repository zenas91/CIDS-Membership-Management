from membership_management.evaluators import compute_trust, add_trust
from membership_management.statemanager import check_state
from sklearn.ensemble import RandomForestClassifier
from preprocessing.processing import get_train_data, get_test_data

if __name__ == '__main__':
    x, y = get_train_data("caida")
    tx, ty = get_test_data("global")
    model = RandomForestClassifier(n_estimators=100).fit(x, y)

    cumulative_trust = 7

    for i in range(1000):
        trust = compute_trust(model, tx, ty)
        cumulative_trust = add_trust(cumulative_trust, trust)

    print("The cumulative trust after a thousand iterations is: ", cumulative_trust)

    print("The current state of the entity is: ", check_state(cumulative_trust, peak_trust=10))
