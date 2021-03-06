class Solution:
    def letterCombinations_my_answer(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        digit2Letters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        resCount = 1
        for i in digits:
            resCount  *= len(digit2Letters[i])

        res = [""] * resCount
        times = resCount
        for i in range(len(digits)):
            letters = digit2Letters[digits[i]]
            round = resCount // times
            times = times // len(letters)
            for r in range(round):
                count = r * times * len(letters)
                for k in range(len(letters)):
                    j = 0
                    while j < times:
                        res[j + times * k + count] += letters[k]
                        j += 1
        return  res

    def letterCombinations(self, digits):
        mapping = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        if not digits:
            return []
        rtn = set({""})

        for digit in digits:
            tmp = set()
            chars = mapping[int(digit)]
            for char in chars:
                for item in rtn:
                    tmp.add(item + char)
            rtn = tmp
        return list(rtn)
