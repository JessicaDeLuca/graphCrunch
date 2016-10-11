'''
This script creates edge files for the company only graph and article only graph.

Created files:
    * data/company_edges.tsv
    * data/article_edges.tsv

Needs this file to run:
    * data/crunchbase_holddups_totransform.tsv (company, article edges)
'''

from itertools import combinations
from load_crunch_data import load_crunch_data


def crunchbase_make_edge_file(filename, d):
    '''
    filename: name of file to write to
    d: dictionary of edge data

    Write edge list to the file.
    '''
    f = open(filename, 'w')
    edges = set()
    for key, values in d.iteritems():
        for edge in combinations(values, 2):
            edges.add(tuple(sorted(edge)))
    for one, two in edges:
        f.write("%s\t%s\n" % (one, two))
    f.close()


if __name__ == '__main__':
    companies, articles = load_crunch_data('/Users/jessicadeluca/gDS16/capstone/JAD-Capstone/data/crunchbase_holddups_totransform.tsv')
    crunchbase_make_edge_file('data/company_edges.tsv', articles)
    crunchbase_make_edge_file('data/article_edges.tsv', companies)
