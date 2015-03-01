    from collections import defaultdict
    
    
    class Trie:
    
        def __init__(self):
            self.root = defaultdict(Trie)
            self.word = None
            self.count = 0
    
        def find(self, prefix):
            '''find word in subtree given prefix and increase number of times the
    word has been visited'''
            if not prefix:
                if self.word:
                    self.count += 1
                return self
            key, suffix = prefix[0], prefix[1:]
            if key not in self.root:
                return None
            return self.root[key].find(suffix)
        
        def add(self, prefix, word=None):
            '''save original word in leave for simplicity'''
            if not word:
                word = prefix
            if not prefix:
                self.word = word
                return
            key, suffix = prefix[0], prefix[1:]
            self.root[key].add(suffix, word)
    
        def top(self, prefix):
            '''retrieve top 10 most frequently visited words along with its count'''
            subtree = self.find(prefix)
            if not subtree:
                return "fell off the tree"
            counts = subtree.traverse()
            return sorted(counts, key=lambda x: x.count, reverse=True)[:10]
    
        def traverse(self):
            '''traverse substree of current node and return all words below'''
            results = []
            if self.word:
                results.append(self)
            for v in self.root.values():
                results += v.traverse()
            return results
    
    
    # testing client
    # construct a trie
    trie = Trie()
    words = ["No","matter","how","little","knowledge","one","might","have","on","a","certain","topic","","the","content","that","was","made","available","by","the","website","owner","","and","the","content","that","is","readily","available","","","to","study","","","","","","on","the","Internet","by","others","are","a","good","hint","on","what","to","read","up","on","","Make","sure","to","ask","","The","editors","","writers","","owners","will","most","likely","be","more","than","glad","to","explain","their","area","of","expertise","in","detail","","but","in","case","their","schedule","prevents","them","from","being","available","to","you","all","the","time","","you","can","always","turn","to","others","who","are","well","versed","in","the","topic","","Doing","a","search","on","Google","much","like","any","interested","user","would","do","will","not","only","allow","to","get","familiar","with","the","terminology","of","the","specific","area","","but","also","provide","insight","for","what","seems","to","be","the","norm","in","the","depth","and","amount","of","related","keywords","and","phrases","on","a","website","","","","see","the","paragraph","3","3","","Summary","","","Expert","","","","Identifying","patterns","of","what","words","","","synonyms","were","likely","to","be","present","along","what","the","query","was","made","for","will","soon","give","a","lot","of","ideas","for","people","s","associations","","thus","more","searches","","which","will","result","in","more","websites","to","look","at","and","study","","Another","pattern","that","might","be","interesting","is","when","certain","resources","seem","to","be","ranked","prominently","across","many","related","searches","","Which","in","case","of","similarly","built","publications","might","be","the","sign","of","a","poplar","and","or","well","marketed","website","","Seemingly","lower","profile","domains","might","also","produce","high","positions","","and","such","are","more","likely","to","be","doing","so","because","of","their","often","revolutionary","content","","or","simply","their","good","choice","of","words","","Even","without","any","previous","education","or","skills","in","the","topic","","one","could","quickly","catch","up","with","the","basics","","Those","who","feel","they","re","well","informed","","and","use","the","proper","terminology","","a","different","danger","is","imminent","","which","is","using","the","expert","","the","","inner","circle","","language","of","a","certain","area","industry","","without","taking","into","account","the","fact","that","the","public","at","large","might","not","be","looking","for","their","content","using","such","queries","","Which","might","not","be","a","problem","with","certain","academic","or","even","business","to","business","online","publications","","but","would","practically","bar","any","eCommerce","","informative","","or","generic","purpose","websites","from","ranking","well","in","organic","search","","Not","to","mention","their","","lack","of","","relevance","to","the","more","widely","user","words","would","raise","their","costs","when","applying","for","AdWords","as","well","","Both","for","those","who","are","just","learning","of","the","theme","specific","terminology","","and","those","who","believe","they","have","it","mastered","","visiting","community","and","hobby","websites","and","even","forums","created","on","the","topic","might","be","essential","","The","current","wording","and","terminology","the","public","uses","might","not","be","all","that","different","from","which","is","used","within","the","","trade","","but","even","slight","differences","can","see","a","huge","difference","in","the","number","of","searches","made","","not","to","mention","","the","price","one","would","bid","for","a","keyword","when","using","paid","advertising"]
    
    for w in words:
        trie.add(w)
    
    
    from random import randrange
    
    
    for _ in range(5000):
        r = randrange(0, len(words))
        trie.find(words[r])
    
    for w in trie.top('c'):
        print w.word, w.count
