import pandas as pd
from os.path import join, dirname


def err():
    return {'item_id': data_df.groupby(['item_id']).sum().index.values,
            'rating_count': data_df.groupby(['item_id']).count()['user_id'].values,
            'rating_avg': (data_df.groupby(['item_id']).sum() / data_df.groupby(['item_id']).count())['rating'].values}


def calculate_WR():
    """
    Weight Rating (WR) = (v/(v+m))*R + (m/(v+m))*C

    v is the number of votes for the movie;
    m is the minimum votes required to be listed in the chart;
    R is the average rating of the movie; And
    C is the mean vote across the whole report

    """
    C = df['rating_avg'].mean()
    m = df['rating_count'].quantile(0.9)
    v = df['rating_count']
    R = df['rating_avg']
    return (v/(v+m) * R) + (m/(m+v) * C)


if __name__ == '__main__':
    BASE_DIR = dirname(dirname(dirname(__file__)))
    DATA_PATH = 'data/ml_100k/ua.base.csv'
    OUTPUT_PATH = 'egs/simple/tmp/output.csv'
    data_df = pd.read_csv(join(BASE_DIR, DATA_PATH))

    item_rating = err()
    df = pd.DataFrame(item_rating, columns=['item_id', 'rating_count', 'rating_avg'])
    df['WR'] = calculate_WR()
    df = df.sort_values(by='WR', ascending=False)
    df.to_csv(join(BASE_DIR, OUTPUT_PATH), index=False)
