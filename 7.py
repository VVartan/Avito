# -*- coding: utf-8 -*-
"""6,7,8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fgHBtqMawDAUCWTIXDCdRVpMytO7CMHz
"""

# 2 term frequency

def __init__(self, rounding =True):

    self.rounding = round

def tf_transform(count_matrix):

     # term frequency

      return [[round(count / sum(row), 4) for count in row] for row in count_matrix]


def idf_transform(count_matrix):

    # 3 inverse document-frequency

    frequency_words = [0] * len(count_matrix[0])

    for i in count_matrix:

        frequency_words = [x + bool(y) for x, y in zip(frequency_words, i)]

    return [round(log((len(count_matrix) + 1) / (count + 1)) + 1,4) for count in frequency_words]

 def fit_transform(self, count_matrix):

        #tf-idf transformer"

        tf_matrix = tf_transform(count_matrix)

        idf_matrix = idf_transform(count_matrix)

        return [ round([tf * idf for (tf, idf) in zip(tf_d, idf_matrix)],4) for tf_d in tf_matrix]


class TfidfVectorizer(CountVectorizer):
     #   f-idf vectorizer
    def fit_transform(self, corpus):
        CountVectorizer.fit_transform(self, corpus)
        transformer = TfidfTransformer()
        return transformer.fit_transform(self.count_matrix)