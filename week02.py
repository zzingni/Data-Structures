


n = int(input("10 단위 수 입력: "))

result = 0
result = n * (n+1) // 2 # O(1) 루프 반복 안 함, 속도 향상 >> 상수 시간
print(result) # 실행 alt + shift + F10