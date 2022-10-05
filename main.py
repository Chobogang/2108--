import math

n = int(input())
arr = []
result = []

for _ in range(n):
  a = int(input())
  arr.append(a)

if len(arr) == 1:
  result = [arr[0], arr[0], arr[0], 0]

else:
  for i in range(4):
    # 산술평균
    if i == 0:
      result.append(round(sum(arr) / n))
    # 중앙값
    if i == 1:
      arr.sort()
      result.append(arr[round(len(arr) / 2)])
    
    # 최빈값 1,2
    if i == 2 :
        ct = m = 0
        case = []

        for k in range(n) :
            if arr.count(arr[k]) > ct :
                ct = arr.count(arr[k]) 
                case = []
                case.append(arr[k])
            elif arr.count(arr[k]) == ct :
                if case.count(arr[k]) == 1 :
                    continue
                else : 
                    case.append(arr[k])

        if len(case) >= 2 :
            result.append(case[1])
        else :
            result.append(case[0])
      
    # 범위
    if i == 3:
      result.append(max(arr) - min(arr))

for i in result :
    print(i)