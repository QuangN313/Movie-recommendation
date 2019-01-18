import pandas as pd
from os.path import join, dirname
from sklearn.metrics import classification_report, confusion_matrix, f1_score


def evaluate():
    report = classification_report(data_df["label"].values, data_df["prediction_label"].values)
    matrix = confusion_matrix(data_df["label"].values, data_df["prediction_label"].values)
    print('Evaluating ...')
    with open(join(BASE_DIR, REPORT_FILE_PATH), 'a') as f:
        f.writelines(report)
        f.writelines(f'\nMatrix: \n{str(matrix)} ')


if __name__ == '__main__':
    BASE_DIR = dirname(dirname(dirname(__file__)))
    DATA_PATH = 'egs/content-base/tmp/output.csv'
    REPORT_FILE_PATH = 'egs/content-base/tmp/report.txt'
    data_df = pd.read_csv(join(BASE_DIR, DATA_PATH))
    evaluate()
