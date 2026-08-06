class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbors = defaultdict(list)
        wordList.append(beginWord)

        # build the dictionary of neighbors
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])

        lengthPath = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return lengthPath
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in neighbors[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            lengthPath += 1
        return 0

