from gensim.models.keyedvectors import KeyedVectors

def main():
	word_vectors = KeyedVectors.load_wordvec_format("result.model.bin", binary = True)
	print("词语 张无忌 最想似的词为")
	res = word_vectors.most_similar(u"张无忌", topn=5)
	for item in res:
		print(item[0] + "," + str(item[1]))
