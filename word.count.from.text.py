from collections import Counter
import string

f = open("test.txt", "r")
d = []
excludeWords = ['the', 'that', 'with', 'all', 'has', 'its', 'for', 'they', 'their', 'and', 'this', 'but', 'into', 'are', 'more', 'not', 'from', 'which', 'have', 'these', 'one', 'therefore', 'was', 'itself', 'every', 'will', 'most', 'when', 'been', 'than', 'what', 'same', 'other', 'some', 'would', 'yet', 'far', 'may', 'each', 'many', 'any', 'can', 'two', 'thus', 'between', 'several', 'very', 'there', 'great', 'only', 'such', 'our', 'case', 'being', 'much', 'those', 'under', 'cases', 'first', 'now', 'had', 'how', 'why','having', 'see', 'were', 'even', 'must', 'could', 'long', 'them', 'less', 'then', 'mr', 'whole', 'few', 'both', 'seems', 'hence', 'parts', 'either', 'however', 'should', 'within', 'should', 'who', 'his', 'know', 'almost', 'well', 'found', 'still', 'like', 'also', 'here', 'over', 'also', 'is', 'out', 'again', 'seen', 'come', 'use', 'made', 'does', 'look', 'without', 'latter', 'kind', 'kinds', 'before', 'close', 'perhaps', 'high', 'vary', 'nor', 'where', 'above', 'otherwise', 'ever', 'already', 'wide', 'dr', 'side', 'about']                                                                                                              
excluirPalavras = ()
with open('test.txt','r') as f:
    for line in f:
        for word in line.split():
            if len(word) > 2:
                d.append(word.strip(',').strip('.').strip('?').strip(':').strip('\'').strip('\"').strip(';').strip(':'))
            else:
                pass

["".join(j for j in i if j not in string.punctuation) for i in d]
f.close()
d = [k.lower() for k in d]
counts = (Counter(d))
MostCommon = counts.most_common()
out_tup = [i for i in MostCommon if i[0] not in excludeWords]
palavras = open("palavras.txt", "w")
with open('palavras.txt', 'w') as fp:
    json.dump(out_tup, fp)

palavras.close()