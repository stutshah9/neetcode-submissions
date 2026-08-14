class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) == 1:
            return 1
        # sliding window appoarch
        # start with a window size of 2
        left = 0
        right = left + 1

        maxFruit = 2

        # key = fruit
        # value = count in sliding window
        fruitMap = defaultdict(int)
        fruitMap[fruits[0]] += 1
        fruitMap[fruits[1]] += 1

        while right < len(fruits) - 1:
        # check if increasing the window size by 1 would increase the types of fruits in the window 
        # use a hashmap to keep track of the fruit in the window and how many counts of that fruit there are
        # if it doesnt your window can expand
            if fruits[right + 1] in fruitMap:
                count = 0
                right += 1
                fruitMap[fruits[right]] += 1
                count = sum(fruitMap.values())
                maxFruit = max(maxFruit, count)
        # if it does must move the window to the right
            else:
                right += 1
                fruitMap[fruits[right]] += 1
        # keep moving the window to the right until there are only 2 types of fruits left in the hashmap
                while len(fruitMap) != 2:
                    fruitMap[fruits[left]] -= 1
                    if fruitMap[fruits[left]] == 0:
                        del fruitMap[fruits[left]]
                    left += 1
        return maxFruit