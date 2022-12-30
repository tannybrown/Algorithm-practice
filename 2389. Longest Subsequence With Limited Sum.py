/----------------------첫번째 시도----------------------------------/
def answerQueries( nums, queries):
        def recur(sum, arr, answer):
            if len(arr) == 0:
                0
            else:
                for i in range(len(arr)):
                    arr2 = list(arr)
                    arr2.remove(arr[i])
                    nsum = sum - arr[i]
                    recur(nsum, arr2, answer)
                    if [nsum, len(arr2)] not in answer:
                        answer.append([nsum, len(arr2)])

        answer = []

        # make subsequence list
        sum = 0
        for i in nums:
            sum += i

        subsequence = [[sum, len(nums)]]
        recur(sum, nums, subsequence)

        # find longest subsequence
        m = len(queries)
        for i in range(m):

            max = [0, 0]
            for j in range(len(subsequence)):
                if subsequence[j][0] <= queries[i]:
                    if max[0] <= subsequence[j][0]:
                        max = subsequence[j]
            answer.append(max[1])

        return answer
/----------------------두번째 시도-------------------------/
class Solution(object):
    

    def answerQueries(self, nums, queries):
            answer = []
            nums.sort()
            n = len(nums)
            m = len(queries)
            for i in range(m):
                count = -1
                check = queries[i]
                for j in range(n):
                    if check < 0:
                        break
                    else :
                        check -= nums[j]
                        count +=1
                if check >= 0 and count == n -1:
                    count += 1
                answer.append(count)
            
            return answer
