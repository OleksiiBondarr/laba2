import numpy
e = 0.00001


def bla(arr, b, n, m):
    det = 1
    if arr[0, 0] != 0:
        for i in range(0, n - 1, 1):
            for k in range(i + 1, n, 1):
                for j in range(i, m, 1):
                    if arr[i, j] == 0:
                        l = i
                        while arr[l, j] != 0:
                            det *= -1
                            l += 1
                            if l == n - 1:
                                l = i
                                break
                        for jj in range(0, m, 1):
                            buff = arr[i, jj]
                            arr[i, jj] = arr[l, jj]
                            arr[l, jj] = buff
                        for jj in range(0, m, 1):
                            buff = b[i]
                            b[i] = b[l]
                            b[l] = buff
                    if i == j:
                        f = abs(arr[k, j] / arr[i, j])
                        if k == i+1:
                            det *= arr[i, j]
                        if numpy.sign(arr[i, j]) == numpy.sign(arr[k, j]):
                            f *= -1
                    if arr[i, j] != 0:
                        arr[k, j] = arr[i, j] * f + arr[k, j]
                        if i == j:
                            if abs(arr[k, j]) < e:
                                arr[k, j] = 0.
                    if j == i:
                        b[k] = b[i] * f + b[k]
                    if i == n-2 and j == n-1:
                        det *= arr[i+1, j]
                    print arr, '\n'

    return arr, det


def re(arr, b, res, n, m):
    buf = 0
    j = n - 1
    for i in range(n - 1, -1, -1):
        res[i] = (b[i] - buf) / arr[i, j]
        buf = 0
        for j in range(m - 1, i - 1, -1):
            k = i - 1
            buf += arr[k, j] * res[j]
        j = i - 1
    return res
