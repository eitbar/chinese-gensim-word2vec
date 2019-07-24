# Chinese-word2vec-gensim
- **概要**

  针对中文语料数据，基于gensim实现word2vec训练

- **代码**

  wiki_to_txt.py -- 将中文wiki语料库转换为txt的demo

  segmentation.py -- 对原文进行停用词、简繁转换、分词处理 

  train.py -- 利用gensim包进行词向量训练

  main.py -- 使用示例

- **语料**

  存于data_txt文件夹中

- **效果**

```
>>> word_vectors = KeyedVectors.load_word2vec_format("result.model.bin", binary= True)
>>> res = word_vectors.most_similar(u"张无忌", topn=10)
>>> for item in res:
...     print(item[0] + "," + str(item[1]))
```
```
赵敏,0.6036754250526428
周芷若,0.6033296585083008
小昭,0.551782488822937
范遥,0.5341595411300659
赵姑娘,0.5281729698181152
虚竹,0.5051340460777283
任我行,0.4973219037055969
公孙谷主,0.489465594291687
孙刚峰,0.4861780107021332
白龟寿,0.48617029190063477
```

