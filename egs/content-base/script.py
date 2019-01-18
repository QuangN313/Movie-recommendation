import numpy as np
import pandas as pd
from os.path import join, dirname
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import Ridge
from sklearn.metrics import classification_report, confusion_matrix, f1_score


def build_profile_item():
    item_gerne_matrix = item_df.values[:, -19:]
    transformer = TfidfTransformer(smooth_idf=True, norm='l2')
    tfidf = transformer.fit_transform(item_gerne_matrix.tolist()).toarray()
    # cosine_sim = linear_kernel(tfidf, tfidf)
    return tfidf


def items_rated_by_user(rate_matrix, user_id):
    y = rate_matrix[:, 0]
    ids = np.where(y == user_id + 1)[0]
    item_ids = rate_matrix[ids, 1] - 1  # index starts from 0
    scores = rate_matrix[ids, 2]
    return item_ids, scores


def build_model(tfidf_matrix, alpha):
    d = tfidf_matrix.shape[1]
    n_users = user_df.shape[0]
    W = np.zeros((d, n_users))
    b = np.zeros((1, n_users))
    for n in range(n_users):
        ids, scores = items_rated_by_user(base_df.values, n)
        clf = Ridge(alpha, fit_intercept=True)
        Xhat = tfidf_matrix[ids, :]

        clf.fit(Xhat, scores)
        W[:, n] = clf.coef_
        b[0, n] = clf.intercept_
    return W, b


def predict():
    W, b = build_model(tfidf_matrix, alpha=0.01)
    Yhat = tfidf_matrix.dot(W) + b
    label = [Yhat[i[1] - 1, i[0] - 1] for i in test_df.values.tolist()]
    return label


if __name__ == '__main__':
    THRESHOLD_RANGE = [0, 20]
    BASE_DIR = dirname((dirname(dirname(__file__))))
    ITEM_PATH = join(BASE_DIR, 'data/ml_100k/u.item.csv')
    BASE_DATA_PATH = join(BASE_DIR, 'data/ml_100k/ua.base.csv')
    TEST_DATA_PATH = join(BASE_DIR, 'data/ml_100k/ua.test.csv')
    USER_PATH = join(BASE_DIR, 'data/ml_100k/u.user.csv')
    OUTPUT_PATH = join(BASE_DIR, 'egs/content-base/tmp/output.csv')
    item_df = pd.read_csv(ITEM_PATH)
    base_df = pd.read_csv(BASE_DATA_PATH)
    user_df = pd.read_csv(USER_PATH)
    test_df = pd.read_csv(TEST_DATA_PATH)

    tfidf_matrix = build_profile_item()
    test_df['prediction_rating'] = predict()
    test_df.to_csv(OUTPUT_PATH, index=False)
