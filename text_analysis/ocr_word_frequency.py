from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os

path = 'path/to/ocr/folder/'

def clean_text(path):
  try:
    os.mkdir('output')
  except:
    pass

  out_path = 'output/'

  files = [f for f in os.listdir(path) if os.path.isfile(path+f)]
  file_paths = [path+f for f in files]
  file_names = [f.strip('.txt') for f in files]

  for idx, f in enumerate(file_paths):
    stop_words = set(stopwords.words('english'))
    file1 = open(f, encoding='latin-1')
    line = file1.read()
    words =  line.split()
    words = [word.lower() for word in words]
    print(words)

    for r in words:
        if not r in stop_words:
            appendFile = open(out_path + 'cleaned_output_{}.txt'.format(file_names[idx]),'a')
            appendFile.write(" "+r)
            appendFile.close()
    with open(out_path + 'cleaned_output_{}.txt'.format(file_names[idx])) as input_file:
        count = Counter(word for line in input_file
                            for word in line.split())

    print(count.most_common(10), file=open(out_path + 'test_{}.txt'.format(file_names[idx]),'a'))
clean_text(path)
