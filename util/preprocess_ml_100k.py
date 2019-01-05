import csv
from os import remove
from os.path import join, dirname, exists
import pandas as pd

genre = ['unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Fantasy', 'Film_Noir', 'Horror', 'Musical', 'Mystery',
        'Romance', 'Sci_Fi', 'Thriller', 'War', 'Western']


def convert_txt_to_csv(txt_path, csv_path, headers, delimiter):
    f_csv = open(join(BASE_DIR, csv_path), 'a', encoding='utf-8')
    writer = csv.writer(f_csv, delimiter=',')
    writer.writerow(headers)
    with open(join(BASE_DIR, txt_path), 'r', encoding="ISO-8859-1") as f_lines:
        for line in f_lines:
            line = line.strip().split(delimiter)
            writer.writerow(line)
    f_csv.close()


def get_csv_file():
    if exists((join(BASE_DIR, csv_data_file))):
        remove((join(BASE_DIR, csv_data_file)))
    if exists(join(BASE_DIR, csv_item_file)):
        remove((join(BASE_DIR, csv_item_file)))
    if exists(join(BASE_DIR, csv_user_file)):
        remove((join(BASE_DIR, csv_user_file)))

    convert_txt_to_csv(training_file, csv_training_file, ['user_id', 'item_id', 'rating', 'timestamp'], '\t')
    convert_txt_to_csv(test_file, csv_test_file, ['user_id', 'item_id', 'rating', 'timestamp'], '\t')
    # convert_txt_to_csv(item_file, csv_item_file,
    #                    headers=['movie_id', 'movie_title', 'release_time', 'release_video_date', 'IMDB_url'] + genre,
    #                    delimiter='|')
    # convert_txt_to_csv(user_file, csv_user_file, ['user_id', 'age', 'gender', 'occupation', 'zip_code'], '|')


def generate_training_test_data(path):
    df = pd.read_csv(join(BASE_DIR, path))
    label = []
    for rating in df['rating']:
        if rating >=3:
            label.append(1)
        else:
            label.append(0)
    df['label'] = label
    df.to_csv(join(BASE_DIR, path), index=False)


if __name__ == '__main__':
    BASE_DIR = dirname(dirname(__file__))
    data_file = 'data/raw_data/u.data'
    item_file = 'data/raw_data/u.item'
    user_file = 'data/raw_data/u.user'
    training_file = 'data/raw_data/ua.base'
    test_file = 'data/raw_data/ua.test'
    csv_training_file = 'util/tmp/ua.base.csv'
    csv_test_file = 'util/tmp/ua.test.csv'
    csv_data_file = 'util/tmp/u.data.csv'
    csv_item_file = 'util/tmp/u.item.csv'
    csv_user_file = 'util/tmp/u.user.csv'
    get_csv_file()
    # generate_training_test_data(csv_training_file)
    # generate_training_test_data(csv_test_file)
    # convert_txt_to_csv(training_file, csv_training_file, )
