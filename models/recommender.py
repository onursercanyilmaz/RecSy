from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

def bookRecommendations(fav_book_title, df):
    # Text to matrix
    cm = CountVectorizer().fit_transform(df['combined_features'])
    cs = cosine_similarity(cm)
    book_id = df[df.Book_Title == fav_book_title]['book_id'].iloc[0]
    fav_book_author = df[df['book_id'] == book_id]['Author_Name'].iloc[0]
    scores = list(enumerate(cs[book_id]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]

    j = 0
    print("Top 10 Most Recommended Books for '", fav_book_title, " ---- ", fav_book_author, "' Readers \n")
    for item in sorted_scores:
        book_title = df[df.book_id == item[0]]['Book_Title'].values[0]
        author = df[df.book_id == item[0]]['Author_Name'].values[0]
        print(j + 1, book_title, '------', author, "------ Similarity:", round(item[1], 2))
        j = j + 1
        if j >= 10:
            break


def tvSeriesRecommendations(fav_series_title, df):
    # Text to matrix
    cm = CountVectorizer().fit_transform(df['combined_features'])
    cs = cosine_similarity(cm)
    mov_id = df[df.Series_Title == fav_series_title]['movie_id'].iloc[0]
    scores = list(enumerate(cs[mov_id]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]

    j = 0
    print("Top 10 Most Recommended Books for '", fav_series_title, " ----  Followers \n")
    for item in sorted_scores:
        series_title = df[df.movie_id == item[0]]['Series_Title'].values[0]

        print(j + 1, series_title, '------', "------ Similarity:", round(item[1], 2))
        j = j + 1
        if j >= 5:
            break


df_Books = pd.read_csv('../ml/df_books.csv')
bookRecommendations("The Time Machine", df_Books)

df_TVSeries = pd.read_csv('../ml/df_tvSeries.csv')
tvSeriesRecommendations("Stranger Things", df_TVSeries)
