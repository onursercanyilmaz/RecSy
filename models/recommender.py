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

    bookDict = {
        "item1": {
            "id": "",
            "title": "",
            "author": "",
            "similarity": ""
        },
        "item2": {
            "id": "",
            "title": "",
            "author": "",
            "similarity": ""
        },
        "item3": {
            "id": "",
            "title": "",
            "author": "",
            "similarity": ""
        },
        "item4": {
            "id": "",
            "title": "",
            "author": "",
            "similarity": ""
        },
        "item5": {
            "id": "",
            "title": "",
            "author": "",
            "similarity": ""
        }
    }
    for item in sorted_scores:
        book_title = df[df.book_id == item[0]]['Book_Title'].values[0]
        author = df[df.book_id == item[0]]['Author_Name'].values[0]
        id = df[df.book_id == item[0]]['book_id'].values[0]
        similarity = round(item[1],2)


        j = j + 1
        if j == 1:
            bookDict["item1"]["id"] = id
            bookDict["item1"]["title"] = book_title
            bookDict["item1"]["author"] = author
            bookDict["item1"]["similarity"] = similarity
        if j == 2:
            bookDict["item2"]["id"] = id
            bookDict["item2"]["title"] = book_title
            bookDict["item2"]["author"] = author
            bookDict["item2"]["similarity"] = similarity
        if j == 3:
            bookDict["item3"]["id"] = id
            bookDict["item3"]["title"] = book_title
            bookDict["item3"]["author"] = author
            bookDict["item3"]["similarity"] = similarity
        if j == 4:
            bookDict["item4"]["id"] = id
            bookDict["item4"]["title"] = book_title
            bookDict["item4"]["author"] = author
            bookDict["item4"]["similarity"] = similarity
        if j >= 5:
            bookDict["item5"]["id"] = id
            bookDict["item5"]["title"] = book_title
            bookDict["item5"]["author"] = author
            bookDict["item5"]["similarity"] = similarity
            break
    return bookDict



def tvSeriesRecommendations(fav_series_title, df):
    # Text to matrix
    cm = CountVectorizer().fit_transform(df['combined_features'])
    cs = cosine_similarity(cm)
    mov_id = df[df.Series_Title == fav_series_title]['movie_id'].iloc[0]
    scores = list(enumerate(cs[mov_id]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]

    tvSeriesDict = {
        "item1": {
            "id": "",
            "title": "",
            "similarity": ""
        },
        "item2": {
            "id": "",
            "title": "",
            "similarity": ""
        },
        "item3": {
            "id": "",
            "title": "",
            "similarity": ""
        },
        "item4": {
            "id": "",
            "title": "",
            "similarity": ""
        },
        "item5": {
            "id": "",
            "title": "",
            "similarity": ""
        }
    }
    j = 0
    for item in sorted_scores:
        series_title = df[df.movie_id == item[0]]['Series_Title'].values[0]
        id = df[df.movie_id == item[0]]['movie_id'].values[0]
        similarity = round(item[1],2)


        j = j + 1
        if j == 1:
            tvSeriesDict["item1"]["id"] = id
            tvSeriesDict["item1"]["title"] = series_title
            tvSeriesDict["item1"]["similarity"] = similarity

        if j == 2:
            tvSeriesDict["item2"]["id"] = id
            tvSeriesDict["item2"]["title"] = series_title
            tvSeriesDict["item2"]["similarity"] = similarity

        if j == 3:
            tvSeriesDict["item3"]["id"] = id
            tvSeriesDict["item3"]["title"] = series_title
            tvSeriesDict["item3"]["similarity"] = similarity

        if j == 4:
            tvSeriesDict["item4"]["id"] = id
            tvSeriesDict["item4"]["title"] = series_title
            tvSeriesDict["item4"]["similarity"] = similarity

        if j >= 5:
            tvSeriesDict["item5"]["id"] = id
            tvSeriesDict["item5"]["title"] = series_title
            tvSeriesDict["item5"]["similarity"] = similarity
            break
    return tvSeriesDict

"""
df_Books = pd.read_csv('../ml/df_books.csv')
a=bookRecommendations("The Time Machine", df_Books)
print(a["item1"]["title"],a["item1"]["author"],a["item1"]["similarity"],)

df_TVSeries = pd.read_csv('../ml/df_tvSeries.csv')
a=tvSeriesRecommendations("Stranger Things", df_TVSeries)
print(a["item"+str(1)]["similarity"])"""
