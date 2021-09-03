class BinaryTree:
    # 생성자에서 이진트리의 노드를 만든다.
    def __init__(self, data = None):
        self.left = None  # 왼쪽 자식 노드의 주소를 기억한다.
        self.data = data  # 트리에 저장할 데이터
        self.right = None # 오른쪽 자식 노드의 주소를 기억한다.
        
    # 트리에 노드를 넣어주는 메소드
    def insert(self, data):
        # 트리에 넣어줄 데이터의 값과 부모 노드의 데이터 값을 비교해서 트리에 데이터를 삽입한다.
        # 트리에 삽입할 데이터가 부모 노드의 데이터보다 작으면 부모 노드의 왼쪽에 삽입한다.
        # 트리에 삽입할 데이터가 부모 노드의 데이터보다 크면 부모 노드의 오른쪽에 삽입한다.
        print('이진트리에 삽입하려는 데이터 {}의 부모 노드는 {}입니다.'.format(data, self.data))
        
        # 삽입하려는 데이터가 부모 데이터보다 작은가?
        if data < self.data:
            # 부모 노드의 왼쪽에 삽입한다.
            print('부모 노드의 데이터가 크기 때문에 부모 노드의 왼쪽에 데이터를 삽입한다.')
            # 부모 노드의 왼쪽 링크(self.left)가 비어(None)있어야 데이터를 삽입할 수 있다.
            if self.left is None:
                # 부모 노드의 왼쪽 링크가 비어있으므로 데이터를 추가한다.
                print('부모({})의 왼쪽에 {} 추가 가능'.format(self.data, data))
                # 새 데이터를 추가해야 하므로 이진트리에 추가할 데이터로 BinaryTree 클래스 객체를 생성해서 부모 노드의 비어있는
                # 왼쪽 링크에 생성된 BinaryTree 클래스 객체의 주소를 넣어준다.
                self.left = BinaryTree(data)
                print('부모({}) 왼쪽에 {} 추가 완료'.format(self.data, data))
            else:
                # 부모 노드의 왼쪽 링크가 비어있지 않기 때문에 데이터를 추가할 수 없다.
                print('부모({}) 왼쪽에 {}이(가) 있기 때문에 {} 추가가 불가능하므로 부모 왼쪽 노드 {}로 가서 insert()' \
                      ' 함수를 실행한다.'.format(self.data, self.left.data, data, self.left.data))
                self.left.insert(data)
            
        # 삽입하려는 데이터가 부모 데이터보다 큰가?
        elif data > self.data:
            # 부모 노드의 오른쪽에 삽입한다.
            print('부모 노드의 데이터가 작기 때문에 부모 노드의 오른쪽에 데이터를 삽입한다.')
            # 부모 노드의 오른쪽 링크(self.right)가 비어(None)있어야 데이터를 삽입할 수 있다.
            if self.right is None:
                # 부모 노드의 오른쪽 링크가 비어있으므로 데이터를 추가한다.
                print('부모({})의 오른쪽에 {} 추가 가능'.format(self.data, data))
                # 새 데이터를 추가해야 하므로 이진트리에 추가할 데이터로 BinaryTree 클래스 객체를 생성해서 부모 노드의 비어있는
                # 오른쪽 링크에 생성된 BinaryTree 클래스 객체의 주소를 넣어준다.
                self.right = BinaryTree(data)
                print('부모({}) 오른쪽에 {} 추가 완료'.format(self.data, data))
            else:
                # 부모 노드의 오른쪽 링크가 비어있지 않기 때문에 데이터를 추가할 수 없다.
                print('부모({}) 오른쪽에 {}이(가) 있기 때문에 {} 추가가 불가능하므로 부모 오른쪽 노드 {}로 가서 insert()' \
                      ' 함수를 실행한다.'.format(self.data, self.right.data, data, self.right.data))
                self.right.insert(data)
            
        # 삽입하려는 데이터와 부모 데이터가 같은가? 삽입하려는 데이터가 이미 트리에 존재하는가?
        else:
            print('{}는(은) 트리에 존재하는 데이터입니다.')
    
    # 트리를 구성하는 노드 목록을 inorder 방식으로 탐색해서 출력하는 함수
    def inorder(self):
        # 왼쪽 자식 노드가 있나 검사한다. => link(self.left, self.right)에 주소가 저장되어있으면 True, None 이면 False
        if self.left:
            self.left.inorder()
        # 더 이상 자식 노드가 없으면 출력한다.
        print(self.data, end=' ')
        # 오른쪽 자식 노드가 있나 검사한다.
        if self.right:
            self.right.inorder()
            
    # 트리를 구성하는 노드 목록을 preorder 방식으로 탐색해서 출력하는 함수
    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
            
    # 트리를 구성하는 노드 목록을 postorder 방식으로 탐색해서 출력하는 함수
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')

        # 이진트리의 root 노드를 만든다.
root = BinaryTree(12)
# 이진트리에 데이터를 넣어준다.
root.insert(6)
print('=' * 120)
root.insert(20)
print('=' * 120)
root.insert(3)
print('=' * 120)
root.insert(25)
print('=' * 120)
root.insert(10)
print('=' * 120)
root.insert(15)
print('=' * 120)

# 이진트리의 운행은 같은 노드를 중복해서 방문하지 않고 모든 노드를 방문하는 방법으로 부로(root) 노드를 언제 방문하느야에 따라
# 아래와 같이 3가지 방법으로 나눈다.
# inorder   : Left => Root => Right : 3 => 6 => 10 => 12 => 15 => 20 => 25 : 오름차순 정렬
# preorder  : Root => Left => Right : 12 => 6 => 3 => 10 => 20 => 15 => 25
# postorder : Left => Right => Root : 3 => 10 => 6 => 15 => 25 => 20 => 12

root.inorder()
print()
root.preorder()
print()
root.postorder()
print()