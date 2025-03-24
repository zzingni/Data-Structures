

groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
ratings = [1, 2, 4, 3] # 정상적으로 동작하려면 리스트의 원소 개수가 동일해야 함. (실행은 되지만 없는 원소만큼 짤림)

groups_rating = list(zip(groups, ratings))
print(groups_rating)