from collections import defaultdict


def load_crunch_data(filename):
    '''
    filename: name of imdb edge data file

    Read in the data and create two dictionaries of adjacency lists, one for
    the actors and one for the movies.
    '''
    f = open(filename)
    companies = defaultdict(set)
    articles = defaultdict(set)
    for line in f:
        company, article = line.strip().split('\t')
        companies[company].add(article)
        articles[article].add(company)
    f.close()
    return companies, articles
