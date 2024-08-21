class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        k = ""
        for a in strs[0]:
          k += a
          for b in strs:
            if b.startswith(k):
              continue
            else:
              k = k[:-1]
              break
          if k == "":
            break
        return k