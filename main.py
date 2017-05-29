import numpy
import diag
arr = numpy.array([[6.7, 1.1, 0.97, 1.18, -0.36],
                  [1.1, 3.72, 1.3, -1.63, -0.33],
                  [0.97, -2.46, 5.88, 2.1, 0.133],
                  [1.3, 0.16, 2.1, 5.66, 0.],
                  [0.84, -0.33, 0.133, 0., 4.]])
b = numpy.array([2.1, 0.48, 0., 3.68, -0.48])
ob = arr
print arr, '\n'
n, m = arr.shape
res = numpy.zeros(n)
arr, det = diag.bla(arr, b, n, m)
print arr, '\n'
print 'det = ', det, '\n'
res = diag.re(arr, b, res, n, m)
print 'res = ', res, '\n'
nev = b - numpy.dot(ob, res)
print 'vector neviazki: ', nev, '\n'
ob1 = numpy.linalg.inv(ob)
print 'obrtnaya\n', ob1, '\n'
ob2 = numpy.dot(arr, ob1)
print 'proverka\n', ob2
'''
print numpy.linalg.solve(arr, b)
'''