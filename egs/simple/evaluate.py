import pandas as pd
from os.path import join, dirname
from sklearn.metrics import classification_report, confusion_matrix, f1_score


def predict():
    label = [0 for x in range(test_df.shape[0])]
    for num_item, item in enumerate(test_df['item_id'].values.tolist()):
        if item in data_df['item_id'].values.tolist()[:100]:
            label[num_item] = 1
        else:
            label[num_item] = 0
    return label


def evaluate():
    report = classification_report(test_df["label"].values, test_df["prediction_label"].values)
    matrix = confusion_matrix(test_df["label"].values, test_df["prediction_label"].values)
    print('Evaluating ...')
    with open(join(BASE_DIR, REPORT_FILE_PATH), 'a') as f:
        f.writelines(report)
        f.writelines(f'\nMatrix: \n{str(matrix)} ')


if __name__ == '__main__':
    BASE_DIR = dirname(dirname(dirname(__file__)))
    DATA_PATH = 'egs/simple/tmp/output.csv'
    TEST_PATH = 'data/ml_100k/ua.test.csv'
    OUTPUT_PATH = 'egs/simple/tmp/output.csv'
    REPORT_FILE_PATH = 'egs/simple/tmp/report.txt'
    data_df = pd.read_csv(join(BASE_DIR, DATA_PATH))
    test_df = pd.read_csv(join(BASE_DIR, TEST_PATH))
    test_df['prediction_label'] = predict()
    evaluate()
