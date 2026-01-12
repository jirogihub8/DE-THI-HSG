def read_data():
    with open("DAYCON.INP", "r") as f:
        N = int(f.readline())
        A = [0] + list(map(int, f.read().split()))
        # A[1..N], B nối tiếp ngay sau
        M = A[N+1]
        B = [0] + A[N+2:N+2+M]
        A = A[:N+1]
    return N, M, A, B


def solution(N, M, A, B):
    # L[i][j] = LCS của A[1..i], B[1..j]
    L = [[0]*(M+1) for _ in range(N+1)]
    print(L)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if A[i] == B[j]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    print(L)
    return L


def write_data(N, M, A, B, L):
    with open("DAYCON.OUT", "w") as f:
        f.write(str(L[N][M]) + "\n")

        # --- Truy vết ---
        i, j = N, M
        LA = []  # chỉ số trong A
        LB = []  # chỉ số trong B

        while i > 0 and j > 0:
            if A[i] == B[j]:
                LA.append(i)
                LB.append(j)
                i -= 1
                j -= 1
            else:
                if L[i-1][j] > L[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        print(LA,LB)
        LA.reverse()
        LB.reverse()

        # In dãy con
        for idx in LA:
            f.write(str(A[idx]) + " ")
        f.write("\n")

        # In vị trí trong A
        for x in LA:
            f.write(str(x) + " ")
        f.write("\n")

        # In vị trí trong B
        for x in LB:
            f.write(str(x) + " ")


# ========================
# MAIN
# ========================

N, M, A, B = read_data()
L = solution(N, M, A, B)
write_data(N, M, A, B, L)
