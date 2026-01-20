import sys
import threading
def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    maxx = max(a)

    b = [0] * (n + 5)

    # ================= SUB 1 =================
    def sub_1():
        for x in range(1, 2001):
            ok = False
            for i in range(1, n + 1):
                b[i] = a[i]

            for _ in range(k):
                st = 1
                while st <= n and b[st] == 0:
                    st += 1

                for i in range(st, n + 1):
                    dec = max(0, x - (i - st) * (i - st))
                    b[i] -= dec
                    if b[i] < 0:
                        b[i] = 0

                st = 1
                while st <= n and b[st] == 0:
                    st += 1
                if st > n:
                    ok = True
                    break

            if ok:
                print(x)
                return

    # ================= SUB 2 =================
    def sub_2():
        l, r = 1, 5 * 10**10
        res = r
        while l <= r:
            mid = (l + r) // 2
            ok = True
            for i in range(1, n + 1):
                tmp = max(0, mid - (i - 1) * (i - 1))
                if a[i] > tmp:
                    ok = False
                    break
            if ok:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        print(res)

    # ================= SUB 3 =================
    def sub_3():
        l, r = 1, 5 * 10**10
        res = r
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for i in range(1, n + 1):
                b[i] = a[i]

            for i in range(1, n + 1):
                if b[i] == 0:
                    continue
                luot_i = (b[i] + mid - 1) // mid
                cnt += luot_i
                if cnt > k:
                    break

                for j in range(i + 1, n + 1):
                    tmp = max(0, mid - (j - i) * (j - i))
                    if tmp == 0:
                        break
                    if b[j] <= luot_i * tmp:
                        b[j] = 0
                    else:
                        b[j] -= luot_i * tmp

            if cnt <= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        print(res)

    # ================= SUB 4 =================
    A = [0] * (n + 5)
    B = [0] * (n + 5)
    C = [0] * (n + 5)

    def can(x):
        l, r = 1, 10**6
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

    def sub_4():
        l, r = 1, 5 * 10**10
        res = r
        while l <= r:
            mid = (l + r) // 2

            for i in range(1, n + 1):
                A[i] = B[i] = C[i] = 0
                b[i] = a[i]

            length = can(mid)
            cnt = 0
            sumA = sumB = sumC = 0

            for i in range(1, n + 1):
                sumA += A[i]
                sumB += B[i]
                sumC += C[i]
                b[i] -= (sumA + sumB * i + sumC * i * i)
                if b[i] < 0:
                    b[i] = 0
                if b[i] == 0:
                    continue

                luot_i = (b[i] + mid - 1) // mid
                cnt += luot_i
                if cnt > k:
                    break

                last = min(n, i + length)
                A[i + 1] += luot_i * mid - luot_i * i * i
                B[i + 1] += 2 * luot_i * i
                C[i + 1] -= luot_i

                A[last + 1] -= luot_i * mid - luot_i * i * i
                B[last + 1] -= 2 * luot_i * i
                C[last + 1] += luot_i

            if cnt <= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        print(res)

    # ================= MAIN LOGIC =================
    if n <= 30 and k <= 30 and maxx <= 30:
        sub_1()
    elif k == 1:
        sub_2()
    elif n <= 1000:
        sub_3()
    else:
        sub_4()


if __name__ == "__main__":
    main()
