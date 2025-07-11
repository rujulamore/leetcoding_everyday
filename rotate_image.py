class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        final = []
        row=len(matrix)
        columns=len(matrix[0])

        for i in range(0,row):
            temp=[]
            for j in range(0,columns):
                temp.append(matrix[j][i])
            final.append(temp)
        print(final)

        for i in range(0,row):
            matrix[i]=final[i][::-1]
        print(matrix)


        def rotate(matrix):
            n = len(matrix)

            # Step 1: Transpose
            for i in range(n):
                for j in range(i + 1, n):  # only upper triangle
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # Step 2: Reverse each row
            for row in matrix:
                row.reverse()
