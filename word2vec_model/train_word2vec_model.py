# -*- coding: utf-8 -*-

'''
python train_word2vec_model.py input_file output_model_file output_vector_file
'''

# import modules & set up logging
import os
import sys
import logging
import multiprocessing
import time
import json

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def output_vocab(vocab):
    for k, v in vocab.items():
        print(k)

if __name__ == '__main__':
    start_time = time.time()

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print (globals()['__doc__'] % locals())
        sys.exit(1)
    input_file, output_model_file, output_vector_file = sys.argv[1:4] #三个参数 输入语料 w2v模型文件  词向量文件
    #输入语料要求：一个句子即一行，单词需要预先使用空格分隔
    #使用LineSentence或者Text8Corpus自动构建gensim需要的sentences格式 小文件也可以直接用列表


    model = Word2Vec(LineSentence(input_file), size=128, window=5, min_count=5,
            workers=multiprocessing.cpu_count()) #min_count过滤词频较低的词语

    model.save(output_model_file)
    model.wv.save_word2vec_format(output_vector_file, binary=False)

    end_time = time.time()
    print("used time : %d s" % (end_time - start_time))
