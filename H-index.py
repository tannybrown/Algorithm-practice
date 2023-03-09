def solution(citations):
    ans = 0
    h = 1
    citations.sort(reverse = True)
    # h를 1개씩 올려가면서 n까지 볼건데 이제 체크하는거임.
    for i in range(len(citations)) :
        if h <= citations[i] :
            if h <= i+1 :
                ans = h
                h += 1
                continue
    return ans
