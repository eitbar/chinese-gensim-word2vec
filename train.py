from gensim.models import word2vec

class Train(object):
	def __init__(self):
		pass
	def train(self):
		sentence = word2vec.Text8Corpus("segmentation.txt")
		model = word2vec.Word2Vec(sentence, size = 300, window = 5, min_count = 5, workers = 4, sg = 1)
		model.wv.save_word2vec_format(u"result.model.bin", binary= True)
if __name__ == "__main__":
	t = Train()
	t.train()
