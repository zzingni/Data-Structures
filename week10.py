from idlelib.search import SearchDialog


class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

def pre_order(node):
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='->')


def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:  # 첫 번째 노드일때 처리
        return new_node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right  # move
    return root

# 첫번째 버전 : search 매개변수 없음. search 함수 안에서 숫자 찾고 출력까지
# 두번째 버전 : search 매개변수, 함수 안에서 입력 받기
# 세번째 버전 : 출력. search에서는 boolean 값 받기

def search(value):
    current = root
    while True:
        if value == current.data:
            return True
        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
               return False
            current = current.right

def delete(node, value):
    if node is None:
        return None # root 노드가 none -> 트리가 구성되어 있지 않음.
    if value < node.data: # node == root
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else: # == (같을경우, 삭제할 노드 발견) 자식이 1일때, 없을때, 2일때 처리

        # 자식이 없는 leaf 노드거나, 자식이 하나만 있는 경우
        if node.left is None: # node.right 가 None이면 위의 부모 노드가 return 값을 받음. None. 만약 값이 있으면 그 값을 return 받음
            return node.right
        elif node.right is None:
            return node.left

        # 자식이 2개인 경우
        # 왼쪽에서 가장 큰 값을 올리는 코드로 짜도 됨 > 해보기
        # min_larger_node = node.right
        while min_larger_node.left: # 오른쪽 노드 중 가장 작은 값 찾아야 하니까 left를 따라가야 함.
            min_larger_node = min_larger_node.left # 노드 이동
        node.data = min_larger_node.data
        node.right = delete(node.right, min_larger_node.data)

        # max_smaller_node = node.left
        # while max_smaller_node.right: # 왼쪽 노드 중 가장 큰 값 찾아야 하니까 right를 따라가야 함.
        #     max_smaller_node = max_smaller_node.right # 노드 이동
        # node.data = max_smaller_node.data
        # node.left = delete(node.left, max_smaller_node.data)

    return node
        
if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 14]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)  # 3 9 8 15 10
    print()
    in_order(root)
    print()
    pre_order(root)
    print()

    find_number = int(input("찾고자 하는 값 : "))
    search(find_number)
    if search(find_number) == True:
        print(f"{find_number}을(를) 찾았습니다")
    else:
        print(f"{find_number}가 존재하지 않습니다.")


    del_number = int(input("제거할 값 : "))
    root = delete(root, del_number)
    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()