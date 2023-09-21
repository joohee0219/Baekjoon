import sys

sys.stdin = open("testcase/15683.txt", "r")

def print_mat(mat):
    for i in range(len(mat)):
        print(mat[i])
    print(" ")


min_square = 1e9 # N*M+1 # 구해야할 최소 사각지대의 수

def main():
    N, M = map(int, sys.stdin.readline().split(" "))
    room = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    

    cctv_list = []

    # CCTV 위치 저장
    for i in range(N):
        for j in range(M):
            if room[i][j] >= 1 and room[i][j] <= 5:
                cctv_list.append((i,j))
    
    # y,x 가 벽이 아니고 유효한 좌표일 때만 참
    def is_valid(y, x):
        if y>=0 and y<N and x>=0 and x<M:
            if room[y][x] != 6:
                return True
        return False
    
    def mark_up(cy, cx, room):
        for i in range(1, cy+1):
            if is_valid(cy-i, cx):
                if room[cy-i][cx] == 0:
                    room[cy-i][cx] = -1
            else:
                break

    def mark_down(cy, cx, room):
        for i in range(1, N-cy):
            if is_valid(cy+i, cx):
                if room[cy+i][cx] == 0:
                    room[cy+i][cx] = -1
            else:
                break

    def mark_right(cy, cx, room):
        for i in range(1, M-cx):
            if is_valid(cy, cx+i):
                if room[cy][cx+i] == 0:
                    room[cy][cx+i] = -1
            else:
                break

    def mark_left(cy, cx, room):
        for i in range(1, cx+1):
            if is_valid(cy, cx-i):
                if room[cy][cx-i] == 0:
                    room[cy][cx-i] = -1
            else:
                break

    def mark_dir(cy, cx, room, dir):        
        if dir == "up":
            mark_up(cy, cx, room)
        elif dir == "down":
            mark_down(cy, cx, room)
        elif dir == "right":
            mark_right(cy, cx, room)
        elif dir == "left":
            mark_left(cy, cx, room)
            
    def dfs(depth, room):
        global min_square
        if depth == len(cctv_list): # depth가 총개수와 같아지면 탐색 완료된거임
            # 사각지대 개수 세기 & 업데이트
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if room[i][j] == 0:
                        cnt += 1
            min_square = min(cnt, min_square)
            return
        
        cctv = cctv_list[depth]
        cctv_type = room[cctv[0]][cctv[1]]
        if cctv_type == 1:
            for d in ["up", "down", "right", 'left']:
                room_ = [r[:] for r in room]
                mark_dir(cctv[0], cctv[1], room_, d)
                dfs(depth + 1, room_)
        elif cctv_type == 2:
            room_ = [r[:] for r in room]
            mark_dir(cctv[0], cctv[1], room_, "up")
            mark_dir(cctv[0], cctv[1], room_, "down")
            dfs(depth + 1, room_)

            room_ = [r[:] for r in room]
            mark_dir(cctv[0], cctv[1], room_, "right")
            mark_dir(cctv[0], cctv[1], room_, "left")
            dfs(depth + 1, room_)
        
        elif cctv_type == 3:
            room_ = [r[:] for r in room]
            mark_dir(cctv[0], cctv[1], room_, "up")
            mark_dir(cctv[0], cctv[1], room_, "right")
            dfs(depth + 1, room_)

            room_ = [r[:] for r in room]
            mark_dir(cctv[0], cctv[1], room_, "right")
            mark_dir(cctv[0], cctv[1], room_, "down")
            dfs(depth + 1, room_)

            room_ = [r[:] for r in room]
            mark_dir(cctv[0], cctv[1], room_, "down")
            mark_dir(cctv[0], cctv[1], room_, "left")
            dfs(depth + 1, room_)

            room_ = [r[:] for r in room]
            mark_dir(cctv[0], cctv[1], room_, "left")
            mark_dir(cctv[0], cctv[1], room_, "up")
            dfs(depth + 1, room_)

        elif cctv_type == 4:
            for d in ["up", "down", "right", 'left']:
                room_ = [r[:] for r in room]
                for d2 in ["up", "down", "right", 'left']:
                    if d2 != d:
                        mark_dir(cctv[0], cctv[1], room_, d2)
                dfs(depth + 1, room_)

        elif cctv_type == 5:
            room_ = [r[:] for r in room]
            for d in ["up", "down", "right", 'left']:
                mark_dir(cctv[0], cctv[1], room_, d)
                dfs(depth + 1, room_)

    room_copy = [r[:] for r in room]
    dfs(0, room_copy)

    print(min_square)
    return min_square

main()
