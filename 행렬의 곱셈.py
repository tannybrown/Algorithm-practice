def solution(arr1, arr2):
    ## 6μ 35λΆ μμ
    answer = []
    for i in range(len(arr1)) :
        list = []
        
        for j in range(len(arr2[0])) :
            summation = 0
            for k in range(len(arr2)) :
                summation += arr1[i][k] * arr2[k][j]
            list.append(summation)
        answer.append(list)
    return answer
