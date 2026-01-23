from collections import deque 

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
            
        queue = deque([root])
        result = []  # 평균값들을 담을 리스트

        while queue:
            # 1. 현재 레벨의 크기(노드 개수)를 '스냅샷' 찍습니다.
            # 이 시점에 큐에는 '이번 레벨의 노드들'만 들어있습니다.
            level_len = len(queue)
            
            level_sum = 0  # 이번 레벨의 합계 초기화
            
            # 2. 딱 이번 레벨의 노드 개수만큼만 반복합니다.
            for _ in range(level_len):
                current_node = queue.popleft()
                
                # 값 더하기
                level_sum += current_node.val
                
                # 3. 자식들은 큐의 맨 뒤에 넣습니다. (다음 레벨을 위해)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            # 4. for문이 끝나면 이번 레벨 처리가 끝난 것입니다. 평균 계산!
            average = level_sum / level_len
            result.append(average)
            
        return result


        