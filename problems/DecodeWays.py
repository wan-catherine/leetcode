class Solution:
    def numDecodings_timeout(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) < 0 or s[0] == "0":
            return 0

        if len(s) > 1 and s[1] == "0":
            if int(s[0:2]) > 20:
                return 0
            before = [[s[0:2]]]
            i = 2
        else:
            before = [[s[0]]]
            i = 1
        current = []
        while i < len(s):
            oldindex = i
            if s[i] == "0":
                return 0
            if i + 1 < len(s) and s[i+1] == "0":
                temp = s[i:i+2]
                i += 2
                if int(temp) > 20:
                    return 0
            else:
                temp = s[i]
                i += 1

            # if oldindex < len(s) - 1 and int(temp) > 2:
            #     continue
            for j in before:
                jcopy = j.copy()
                if int(j[-1]) > 2 and int(temp) > 2:
                    current.append(jcopy)
                    continue
                else:
                    jcopy.append(temp)
                    current.append(jcopy)
                if (j[-1] == "1" and int(temp) < 10) or (j[-1] == "2" and int(temp) <= 6):
                    jcopy = j.copy()
                    jcopy[-1] = jcopy[-1] + temp
                    current.append(jcopy)

            before = current
            current = []
            print(len(before))
        return len(before)

    def numDecodings_(self, s):
        if s == None or len(s) < 0 or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        i = 1
        before = 1
        after = before

        res = after
        while i < len(s):
            res = after
            if s[i] == "0" and (int(s[i-1]) > 2 or s[i-1] == "0"):
                return 0
            if i+1 < len(s) and s[i+1] == "0":
                if int(s[i]) > 2 or s[i] == "0":
                    return 0
                i += 2
                continue

            if s[i-1] != "0" and s[i] != "0" and int(s[i-1:i+1]) < 27:
                res += before
            before = after
            after = res
            i += 1

        return res

    def numDecodings_dp(self, s):
        if not s or s[0] == '0':
            return 0
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, length):
            dp[i + 1] += dp[i] if s[i] != '0' else 0
            val = int(s[i - 1:i + 1])
            if val >= 10 and val <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        s = '0' + s
        length = len(s)
        dp = [0] * (length)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, length):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            else:
                if s[i - 1] not in '12':
                    return 0
                else:
                    dp[i] = dp[i - 2]
                    continue
            if s[i - 1] not in '12':
                continue
            if s[i - 1] == '1':
                dp[i] += dp[i - 2]
            elif s[i] in '0123456':
                dp[i] += dp[i - 2]
        return dp[-1]

