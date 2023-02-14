#make this cell a python file
from itertools import combinations
from math import sqrt
from mrjob.job import MRJob

class rec_step2(MRJob):
    def mapper(self, _, line):
        user_id,itemRatings = line.split('\t')
        for itemRating1, itemRating2 in combinations(eval(itemRatings), 2):
            movieID1,rating1 = itemRating1[0],itemRating1[1]
            movieID2,rating2 = itemRating2[0],itemRating2[1]
            yield (movieID1, movieID2), (rating1, rating2)
            yield (movieID2, movieID1), (rating2, rating1)
    def cosine_similarity(self, ratingPairs):
        numPairs = 0
        sum_xx = sum_yy = sum_xy = 0
        for ratingX, ratingY in ratingPairs:
            sum_xx += ratingX * ratingX
            sum_yy += ratingY * ratingY
            sum_xy += ratingX * ratingY
            numPairs += 1

        numerator = sum_xy
        denominator = sqrt(sum_xx) * sqrt(sum_yy)

        score = 0
        if (denominator):
            score = (numerator / (float(denominator)))
        return (score, numPairs)
    
    def reducer(self, moviePair, ratingPairs,minPairs=10,minScore=0.95):
        score, numPairs = self.cosine_similarity(ratingPairs)
        if (numPairs > minPairs and score > minScore):
            yield moviePair, (score, numPairs)

if __name__ == '__main__':
    rec_step2.run()
