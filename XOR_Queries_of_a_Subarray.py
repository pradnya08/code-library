class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        # Compute accumulated xor from head
        for e in arr:
            pref.append(e ^ pref[-1])
        ans = []
        # query result equal to xor[0, l] xor x[0, r]
        for [l, r] in queries:
            ans.append(pref[r+1] ^ pref[l])
        return ans