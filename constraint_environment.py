import time
from collections import deque
from algorithms import find_blank, swap, step, convert_states_to_moves, is_solvable

def get_valid_moves(state):
    """Tạo danh sách các trạng thái tiếp theo từ trạng thái hiện tại bằng các di chuyển hợp lệ."""
    i, j = find_blank(state)
    valid_states = []
    valid_moves = []
    for move, (di, dj) in step.items():
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = swap(state, i, j, ni, nj)
            valid_states.append(new_state)
            valid_moves.append(move)
    return valid_states, valid_moves

def backtracking_search(start, goal=((1, 2, 3), (4, 5, 6), (7, 8, 0))):
    start_time = time.time()
    nodes_expanded = 0
    explored_nodes = []
    
    def backtrack(state, path, visited, depth, max_depth=50):
        nonlocal nodes_expanded, explored_nodes
        nodes_expanded += 1
        if state not in explored_nodes:
            explored_nodes.append(state)
        if depth > max_depth:
            return None
        if state == goal:
            return path
        
        visited.add(state)
        next_states, moves = get_valid_moves(state)
        for next_state, move in zip(next_states, moves):
            if next_state not in visited:
                result = backtrack(next_state, path + [move], visited.copy(), depth + 1, max_depth)
                if result is not None:
                    return result
        return None

    if not is_solvable(start, goal):
        return None, time.time() - start_time, nodes_expanded, explored_nodes

    visited = set()
    path = backtrack(start, [], visited, 0)
    if path is None:
        return None, time.time() - start_time, nodes_expanded, explored_nodes
    return path, time.time() - start_time, nodes_expanded, explored_nodes

def forward_checking(start, goal=((1, 2, 3), (4, 5, 6), (7, 8, 0))):
    start_time = time.time()
    nodes_expanded = 0
    explored_nodes = []
    
    def is_consistent(next_state, visited):
        return next_state not in visited and is_solvable(next_state, goal)

    def forward_check(state, visited):
        next_states, moves = get_valid_moves(state)
        valid_next = [(ns, m) for ns, m in zip(next_states, moves) if is_consistent(ns, visited)]
        return valid_next

    def backtrack(state, path, visited, depth, max_depth=50):
        nonlocal nodes_expanded, explored_nodes
        nodes_expanded += 1
        if state not in explored_nodes:
            explored_nodes.append(state)
        if depth > max_depth:
            return None
        if state == goal:
            return path
        
        visited.add(state)
        valid_next = forward_check(state, visited)
        for next_state, move in valid_next:
            if next_state not in visited:
                result = backtrack(next_state, path + [move], visited.copy(), depth + 1, max_depth)
                if result is not None:
                    return result
        return None

    if not is_solvable(start, goal):
        return None, time.time() - start_time, nodes_expanded, explored_nodes

    visited = set()
    path = backtrack(start, [], visited, 0)
    if path is None:
        return None, time.time() - start_time, nodes_expanded, explored_nodes
    return path, time.time() - start_time, nodes_expanded, explored_nodes

def ac3(start, goal=((1, 2, 3), (4, 5, 6), (7, 8, 0))):
    """AC-3 Modified: Sử dụng BFS để tìm đường đi đến trạng thái đích, thay vì thuật toán CSP truyền thống.
    Được tùy chỉnh để hiển thị các bước di chuyển giống các thuật toán khác."""
    start_time = time.time()
    nodes_expanded = 0
    
    if not is_solvable(start, goal):
        return None, time.time() - start_time, nodes_expanded, []

    # BFS implementation
    queue = deque([(start, [])])  # (state, path)
    visited = {start}
    explored_nodes = [start]

    while queue:
        state, path = queue.popleft()
        nodes_expanded += 1

        if state == goal:
            states = [start] + [state for _, state in path]
            moves = [move for _, move in path]
            return moves, time.time() - start_time, nodes_expanded, states

        next_states, moves = get_valid_moves(state)
        for next_state, move in zip(next_states, moves):
            if next_state not in visited:
                visited.add(next_state)
                explored_nodes.append(next_state)
                queue.append((next_state, path + [(state, move)]))

    return None, time.time() - start_time, nodes_expanded, explored_nodes