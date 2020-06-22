count = []
main_matrix = []
count_r = 0

#PRINT INFORMATION
def show_result():
    print("The input image contatins ", len(count), " black regions")
    for i in range(0, len(count)):
        print("Region ", i, ": ", count[i][2], " pixels", sep='', end=", ")
        print("first pixel (", count[i][0][0], ",", count[i][0][1], sep='', end="), ")
        print("last pixel (", count[i][1][0], ",", count[i][1][1], sep='', end=")\n")


def execute():
    global count
    global main_matrix
    global count_r
    #CHECK EVERY POINT FOR IT'S VALUE
    for i in range(0, len(main_matrix)):
        for j in range(0, len(main_matrix[i])):
            if main_matrix[i][j] == 0:
                count_r = 0
                #BUILD REGION
                coords = move(i, j)
                coords[0] = coords[0] + 1
                coords[1] = coords[1] + 1
                coord = [i+1, j+1]
                #APPEND REGION COUNTER
                count.append([coord, coords, count_r])


def move(i, j):
    global main_matrix
    global count_r
    #CHECK IF VALUE BELONGS TO THE REGION
    if main_matrix[i][j] > 0:
        return[0, 0]
    else:
        main_matrix[i][j] = 2
        count_r=count_r+1
    #COLLECT ADJACENT ELEMENTS
    if j - 1 >= 0:
        tmp_1 = move(i, j-1)
    else:
        tmp_1 = [0, 0]
    if i + 1 < len(main_matrix):
        tmp_2 = move(i+1, j)
    else:
        tmp_2 = [0, 0]
    if j + 1 < len(main_matrix[i]):
        tmp_3 = move(i, j+1)
    else:
        tmp_3 = [0, 0]
    if i - 1 >= 0:
        tmp_4 = move(i - 1, j)
    else:
        tmp_4 = [0, 0]
    #FIND LAST POINT OF A REGION
    if tmp_2[0] > tmp_1[0] or (tmp_2[0] == tmp_1[0] and tmp_2[1]>tmp_1[1]):
        tmp_1 = tmp_2
    if tmp_3[0] > tmp_1[0] or (tmp_3[0] == tmp_1[0] and tmp_3[1] > tmp_1[1]):
        tmp_1 = tmp_3
    if tmp_4[0] > tmp_1[0] or (tmp_4[0] == tmp_1[0] and tmp_4[1] > tmp_1[1]):
        tmp_1 = tmp_4
    if i > tmp_1[0] or (i == tmp_1[0] and j > tmp_1[1]):
        tmp_1 = [i, j]
    return tmp_1


def main():
    global main_matrix
    #READ DATA FROM THE FILE
    f = open('text.txt', 'r')
    main_matrix.append([int(x) for x in next(f).split()])
    for line in f:  # read rest of lines
        main_matrix.append([int(x) for x in line.split()])
    execute()
    show_result()


if __name__== "__main__" :
    main()