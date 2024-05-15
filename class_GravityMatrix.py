class GravityMatrix:
    def __init__(self, matrix):
        '''Creates a Gravitational Matrix that takes a list with nested lists of 
        the same length, If you are missing any values they are replaced with a 
        string of the letter m. This then proceeds to shift all of the missing 
        values to the top of the matrix'''
        col_list = []
        for i in range(len(matrix[0])):
            lst = []
            for j in range(len(matrix)):
                lst.append(matrix[j][i])
            col_list.append(lst)
        col_list2 = col_list.copy()
        sorted_col = []
        for i in col_list:
            if 'm' not in i:
                sorted_col.append(i)
            else:
                col = []
                for j in i:
                    if j == 'm':
                        col.insert(0, 'm')
                    else:
                        col.append(j)
                sorted_col.append(col)
        matrix = []
        for i in range(len(sorted_col[0])):
            row = []
            for j in range(len(sorted_col)):
                row.append(sorted_col[j][i])
            matrix.append(row)

        self.matrix = matrix

    def RotateLeft(self):
        '''Rotates the Gravitational Matrix to the left if the m's are not on 
        the top then they would shift to the top of the matrix after it is rotated'''
        left_matrix = []
        # Running through the columns backwards; amount of columns is the amount 
        for i in range(len(self.matrix[0])-1, -1, -1):
            lst = []
            # Running through the rows forwards
            for j in range(len(self.matrix)):
                lst.append(self.matrix[j][i])
            left_matrix.append(lst)

        col_list = []
        for i in range(len(left_matrix[0])):
            lst = []
            for j in range(len(left_matrix)):
                lst.append(left_matrix[j][i])
            col_list.append(lst)
        col_list2 = col_list.copy()
        sorted_col = []
        for i in col_list:
            if 'm' not in i:
                sorted_col.append(i)
            else:
                col = []
                for j in i:
                    if j == 'm':
                        col.insert(0, 'm')
                    else:
                        col.append(j)
                sorted_col.append(col)
        matrix = []
        for i in range(len(sorted_col[0])):
            row = []
            for j in range(len(sorted_col)):
                row.append(sorted_col[j][i])
            matrix.append(row)

        self.matrix = matrix

    def RotateRight(self):
        '''Rotates the Gravitational Matrix to the right if the m's are not on 
        the top then they would shift to the top of the matrix after it is rotated'''
        right_matrix = []
        # Running through the columns forward; the amount of columns is also the length of the rows
        for i in range(len(self.matrix[0])):
            lst = []
            # Running through the rows backwards; the amount of rows is also the length of the matrix
            for j in range(len(self.matrix)-1, -1, -1):
                lst.append(self.matrix[j][i])
            right_matrix.append(lst)

        col_list = []
        for i in range(len(right_matrix[0])):
            lst = []
            for j in range(len(right_matrix)):
                lst.append(right_matrix[j][i])
            col_list.append(lst)
        col_list2 = col_list.copy()
        sorted_col = []
        for i in col_list:
            if 'm' not in i:
                sorted_col.append(i)
            else:
                col = []
                for j in i:
                    if j == 'm':
                        col.insert(0, 'm')
                    else:
                        col.append(j)
                sorted_col.append(col)
        matrix = []
        for i in range(len(sorted_col[0])):
            row = []
            for j in range(len(sorted_col)):
                row.append(sorted_col[j][i])
            matrix.append(row)

        self.matrix = matrix