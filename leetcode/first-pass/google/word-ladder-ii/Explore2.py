from collections import deque


class Solution:
    def neighbors(self, word):
        if word in self.neicache:
            return self.neicache[word]
        nei = []
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                w = prefix + c + suffix
                if w != word and w in self.words:
                    nei.append(w)
        self.neicache[word] = nei
        return nei

    def bfs_len(self, beginWord):
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == self.endWord:
                return dist
            else:
                for w in self.neighbors(word):
                    if w in visited:
                        continue
                    visited.add(w)
                    queue.append((w, dist + 1))
        return -1

    def ssc(self, beginWord):
        stack = [beginWord]
        visited = set()
        while stack:
            word = stack.pop()
            if word in visited:
                continue
            visited.add(word)
            if word != self.endWord:
                stack.extend(self.neighbors(word))
        return visited

    def dfs(self, word, path, visited):
        if len(path) > self.min_len:
            None
        elif word == self.endWord:
            self.ans.append(path)
        else:
            for w in self.neicache[word]:
                if w in visited:
                    continue
                visited.add(w)
                self.dfs(w, path + [w], visited)
                visited.remove(w)

    def findLadders(self, beginWord, endWord, wordList):
        if len(beginWord) == 1:
            return [[beginWord, endWord]]
        self.endWord = endWord
        self.words = set(wordList)
        self.neicache = dict()
        self.neicache[beginWord] = self.neighbors(beginWord)
        self.words &= self.ssc(beginWord)
        self.min_len = 0
        if endWord in self.words:
            self.min_len = self.bfs_len(beginWord)
        self.ans = []
        if self.min_len > 0:
            self.dfs(beginWord, [beginWord], set([beginWord]))
        return self.ans

# main
beginWord = "cet"
endWord = "ism"
wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip",
         "kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
print(Solution().findLadders(beginWord, endWord, wordList))
