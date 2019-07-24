import jieba
import os
from hanziconv import HanziConv


class Segmentation(object):

	def __init__(self):
		self.stopwordset = set()

	def set_stopword(self):
		with open("stopwords.txt", "r", encoding = "utf-8") as stopwords:
			for stopword in stopwords:
				self.stopwordset.add(stopword.strip('\n'))
	
	def traditional_to_simplified(self):
		simplified = open("simplified.txt", "w", encoding="utf-8")
		sFolderPath = 'data_txt'
		lsFiles = []
		for root, dirs, files in os.walk(sFolderPath):
			for file in files:
				if file.endswith(".txt"):
					lsFiles.append(os.path.join(root, file))
		raw_word_list = []
		for item in lsFiles:		
			with open(item, "r", encoding="utf-8") as traditional:
				i = 0
				for s in traditional:
					simplified.write(HanziConv.toSimplified(s))
					i += 1
					if i % 10000 == 0 :
						print("finish " + str(i))
		simplified.close()

	def segmentation(self):
		segmentation = open("segmentation.txt", "w", encoding = "utf-8")
		with open("simplified.txt", "r", encoding="utf-8") as Corpus:
			for sentence in Corpus:
				sentence = sentence.strip("\n")
				pos = jieba.cut(sentence, cut_all = False)
				for term in pos:
					if term not in self.stopwordset:
						segmentation.write(term + " ")
		segmentation.close()

if __name__ == "__main__":
	segmentation = Segmentation()
	segmentation.set_stopword()
	segmentation.traditional_to_simplified()
	segmentation.segmentation()
