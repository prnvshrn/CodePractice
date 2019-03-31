class Solution(object):

    def matrixScore(self, A):
        R, C = len(A), len(A[0])
        ans = 0
        for c in range(C):
            col = 0
            for r in range(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans

if __name__ == "__main__":
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    obj = Solution()
    print(obj.matrixScore(A))