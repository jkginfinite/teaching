from mrjob.job import MRJob
import os
class rec_step3(MRJob):
    def mapper_init(self,labelfilename='labels1.txt'):
        # Load database of movie names.
        self.movieNames = {}
        #change the file path to wherever your current main directory is
        filepath = '/Users/teaching/Documents/github/teaching/SaintPeters/DS610/week9'
        filepath = os.path.join(filepath,labelfilename)
        with open(filepath,'r') as f:
            for line in f:
                fields = line.split('|')
                self.movieNames[int(fields[0])] = fields[1]
                
    def mapper(self, _, line):
        moviePair,scores = line.split('\t')
        score, n = eval(scores)
        movie1, movie2 = eval(moviePair)
        yield (self.movieNames[int(movie1)], score),(self.movieNames[int(movie2)], n)
        
    def reducer(self, movieScore, similarN):
        movie1, score = movieScore
        for movie2, n in similarN:
            yield movie1, (movie2, score, n)
            
if __name__ == '__main__':
    rec_step3.run()
