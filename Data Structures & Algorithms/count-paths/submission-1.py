class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom row
        row = [1] * n
        
        #iterate through each row
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                #newRow[j+1] is to the right of newRow[j] and row[j] is cell below
                newRow[j] = newRow[j+1] + row[j]
            #update row by shifting to the row above
            row = newRow
        return row[0]