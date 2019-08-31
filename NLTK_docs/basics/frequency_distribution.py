from nltk.book import *

# Frequency distribution
from nltk.probability import FreqDist
fdist1 = FreqDist(text1)  # fdist1 is an instance of FreqDist class
print(fdist1)  # FreqDist.__str__
fdist1.most_common(50)
fdist1['whale']

fdist1.plot(50, cumulative=True)  # generate a cumulative frequency plot

# Functions Defined for NLTK's Frequency Distributions or methods set in FreqDist class
fdist = FreqDist(samples) 	# create a frequency distribution containing the given samples
fdist[sample] += 1 	# increment the count for this sample
fdist['monstrous'] 	# count of the number of times a given sample occurred
fdist.freq('monstrous') 	# frequency of a given sample
fdist.N() 	# total number of samples
fdist.most_common(n) 	# the n most common samples and their frequencies
for sample in fdist: 	# iterate over the samples
fdist.max() 	# sample with the greatest count
fdist.tabulate() 	# tabulate the frequency distribution
fdist.plot() 	# graphical plot of the frequency distribution
fdist.plot(cumulative=True) 	# cumulative plot of the frequency distribution
fdist1 |= fdist2 	# update fdist1 with counts from fdist2
fdist1 < fdist2 	# test if samples in fdist1 occur less frequently than in fdist2
