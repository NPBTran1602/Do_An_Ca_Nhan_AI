import time
from collections import deque
import random
from algorithms import find_blank, swap, step, is_solvable

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

def generate_random_states(goal, num_states=1):
    """Tạo trạng thái ngẫu nhiên từ trạng thái đích."""
    states = []
    for _ in range(num_states):
        flat = list(sum(goal, ()))
        random.shuffle(flat)
        while not is_solvable(tuple(tuple(flat[i:i+3]) for i in range(0, 9, 3)), goal):
            random.shuffle(flat)
        state = tuple(tuple(flat[i:i+3]) for i in range(0, 9, 3))
        states.append(state)
    return states

def belief_state(initial_states, goal=((1, 2, 3), (4, 5, 6), (7, 8, 0))):
    """Tìm đường đi cho từng niềm tin bằng BFS."""
    start_time = time.time()
    nodes_expanded = 0
    solutions = []

    for initial_state in initial_states:
        if not is_solvable(initial_state, goal):
            solutions.append((None, []))
            continue

        queue = deque([(initial_state, [])])  # (state, path)
        visited = {initial_state}
        explored_nodes = [initial_state]

        while queue:
            state, path = queue.popleft()
            nodes_expanded += 1

            if state == goal:
                states = [initial_state] + [state for _, state in path]
                moves = [move for _, move in path]
                solutions.append((moves, states))
                break

            next_states, moves = get_valid_moves(state)
            for next_state, move in zip(next_states, moves):
                if next_state not in visited:
                    visited.add(next_state)
                    explored_nodes.append(next_state)
                    queue.append((next_state, path + [(state, move)]))

        # Đảm bảo có giải pháp cho mọi niềm tin, nếu không tìm thấy thì thêm None
        if len(solutions) < len(initial_states):
            solutions.append((None, []))

    # Trả về giải pháp đầu tiên (nếu có), thời gian thực thi, số node mở rộng, và danh sách giải pháp cho từng niềm tin
    first_solution = solutions[0][0] if solutions and solutions[0][0] is not None else None
    return first_solution, time.time() - start_time, nodes_expanded, solutions

def and_or_search(initial_states, goal=((1, 2, 3), (4, 5, 6), (7, 8, 0))):
    """Tìm đường đi cho từng niềm tin bằng BFS (giả lập AND-OR Search)."""
    start_time = time.time()
    nodes_expanded = 0
    solutions = []

    for initial_state in initial_states:
        if not is_solvable(initial_state, goal):
            solutions.append((None, []))
            continue

        queue = deque([(initial_state, [])])  # (state, path)
        visited = {initial_state}
        explored_nodes = [initial_state]

        while queue:
            state, path = queue.popleft()
            nodes_expanded += 1

            if state == goal:
                states = [initial_state] + [state for _, state in path]
                moves = [move for _, move in path]
                solutions.append((moves, states))
                break

            next_states, moves = get_valid_moves(state)
            for next_state, move in zip(next_states, moves):
                if next_state not in visited:
                    visited.add(next_state)
                    explored_nodes.append(next_state)
                    queue.append((next_state, path + [(state, move)]))

        # Đảm bảo có giải pháp cho mọi niềm tin, nếu không tìm thấy thì thêm None
        if len(solutions) < len(initial_states):
            solutions.append((None, []))

    first_solution = solutions[0][0] if solutions and solutions[0][0] is not None else None
    return first_solution, time.time() - start_time, nodes_expanded, solutions

def search_with_partial_observation(initial_states, goal=((1, 2, 3), (4, 5, 6), (7, 8, 0))):
    """Tìm đường đi cho từng niềm tin bằng BFS (giả lập Search with Partial Observation)."""
    start_time = time.time()
    nodes_expanded = 0
    solutions = []

    for initial_state in initial_states:
        if not is_solvable(initial_state, goal):
            solutions.append((None, []))
            continue

        queue = deque([(initial_state, [])])  # (state, path)
        visited = {initial_state}
        explored_nodes = [initial_state]

        while queue:
            state, path = queue.popleft()
            nodes_expanded += 1

            if state == goal:
                states = [initial_state] + [state for _, state in path]
                moves = [move for _, move in path]
                solutions.append((moves, states))
                break

            next_states, moves = get_valid_moves(state)
            for next_state, move in zip(next_states, moves):
                if next_state not in visited:
                    visited.add(next_state)
                    explored_nodes.append(next_state)
                    queue.append((next_state, path + [(state, move)]))

        # Đảm bảo có giải pháp cho mọi niềm tin, nếu không tìm thấy thì thêm None
        if len(solutions) < len(initial_states):
            solutions.append((None, []))

    first_solution = solutions[0][0] if solutions and solutions[0][0] is not None else None
    return first_solution, time.time() - start_time, nodes_expanded, solutions