def maximalSquare(matrix):
    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            area = 0
            while i + area < len(matrix) and j + area < len(matrix[i]):
                no = False
                for a in range(area):
                    if matrix[i + area][j + a] == '0' or matrix[i + a][j + area] == '0':
                        no = True
                if matrix[i+area][j+area] == '0':
                    no = True
                if no:
                    break
                area += 1
            print(area)
            if area > max_area:
                max_area = area
    return max_area*max_area
