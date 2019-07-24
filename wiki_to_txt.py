import sys
from gensim.corpora import WikiCorpus

class Wiki_to_txt(object):
	def __init__(self):
		pass

	def set_wiki_to_txt(self, wiki_data_path = None):
		if wiki_data_path == None:
            # 系统参数
			if len(sys.argv) != 2:
				print("Please Usage: python3 " + sys.argv[0] + " wiki_data_path")
				exit()
			else:
				wiki_corpus = WikiCorpus(sys.argv[1], dictionary = {})
		else:
			wiki_corpus = WikiCorpus(wiki_data_path, dictionary = {})
 
		with open("data_txt/wiki_text.txt", 'w', encoding = 'utf-8') as output:
			text_count = 0
			for text in wiki_corpus.get_texts():
				output.write(' '.join(text) + '\n')
				text_count += 1
				if text_count % 10000 == 0:
					logging.info("已处理 %d 篇文章" % text_count)
			print("转换结束")

if __name__ == "__main__":
	wiki_to_txt = Wiki_to_txt()
	wiki_to_txt.set_wiki_to_txt()

