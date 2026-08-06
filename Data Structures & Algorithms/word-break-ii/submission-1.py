class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dict = defaultdict(list)

        def helper(sub):
            if sub in dict:
                return dict[sub]
            
            result = []

            # recursion
            for i in range(len(sub)):
                prefix = sub[:i+1]
                if prefix in wordSet:
                    if prefix == sub:
                        result.append(prefix)
                    else:
                        restOfWords = helper(sub[i+1:])
                        for phrase in restOfWords:
                            result.append(prefix+' '+phrase)
            dict[sub] = result
            return result

        return helper(s)
