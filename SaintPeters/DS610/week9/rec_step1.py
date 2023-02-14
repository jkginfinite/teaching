from mrjob.job import MRJob
class rec_step1(MRJob):
    def mapper(self, _, line):
        try:
            (userID, movieID, rating, timestamp) = line.split('\t')
        except:
            (userID, movieID, rating, timestamp) = None,None,0,None
        yield  userID, (movieID, float(rating)) 

    def reducer(self, user_id, itemRatings):
        ratings = []
        for movieID, rating in itemRatings:
            ratings.append((movieID, rating))
        #reducer: for every user_id key, we have a list of ratings in the form [(movieID1,rating1),(movieID2,rating2),...]
        yield user_id, ratings

        
if __name__ == '__main__':
    rec_step1.run()
