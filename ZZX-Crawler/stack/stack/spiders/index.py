class indexes:
    indexing=['introduction',
                'Merge algorithm for proximity queries using a positional index',
                'Algorithms for postings list compression',
                'Spelling correction',
                'Probabilistic IR: Binary Independence Model',
                'Computing Scores and BM25F',
                'Recent evaluation, NDCG, using clickthrough; rate queries & results',
                'Systems issues in efficient retrieval and scoring',
                ' Mapreduce with Java',
                'Naive Bayes, kNN, decision boundaries',
                'Support vector machines',
                'Learning to rank',
                'Link analysis',
                'Crawling, near-dups',
                'Distributed word representations for IR ',
                'Personalization'
            ]
    def ifmatch(self,ind,li):
        for item in li:
            if li.find(ind)==-1:
                return False
            else:
                return True

