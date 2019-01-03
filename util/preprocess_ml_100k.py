import csv
from os import remove
from os.path import join, dirname, exists

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


if __name__ == '__main__':
    BASE_DIR = dirname(dirname(__file__))
    data_file = 'data/raw_data/u.data'
    item_file = 'data/raw_data/u.item'
    user_file = 'data/raw_data/u.user'
    csv_data_file = 'util/tmp/u.data.csv'
    csv_item_file = 'util/tmp/u.item.csv'
    csv_user_file = 'util/tmp/u.user.csv'

    if exists((join(BASE_DIR, csv_data_file))):
        remove((join(BASE_DIR, csv_data_file)))
    if exists(join(BASE_DIR, csv_item_file)):
        remove((join(BASE_DIR, csv_item_file)))
    if exists(join(BASE_DIR, csv_user_file)):
        remove((join(BASE_DIR, csv_user_file)))

    convert_txt_to_csv(data_file, csv_data_file, ['user_id', 'item_id', 'rating', 'timestamp'], '\t')
    convert_txt_to_csv(item_file, csv_item_file,
                       headers=['movie_id', 'movie_title', 'release_time', 'release_video_date', 'IMDB_url'] + genre,
                       delimiter='|')
    convert_txt_to_csv(user_file, csv_user_file, ['user_id', 'age', 'gender', 'occupation', 'zip_code'], '|')
