
import array

arr = array.array('f',[11, 9, -77, 8]) # 하나의 문자열로 작동

for i in range(len(arr)):
    print(f"{arr[i]:3}, {id(arr[i])}")
print(arr[2])

