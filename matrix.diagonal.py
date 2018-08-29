#soma e valor absoluto de uma matriz e sua diagonal.
import math

arr = [(1, 1, 3), (1, 5, 0), (1, 1, 1)]
diag = [arr[i][i] for i in range(0, len(arr))]
otherDiag = [arr[i][~i] for i in range(0, len(arr))]
result, resultOther = 0, 0
for i in diag:
    result += i
for i in otherDiag:
    resultOther += i

resultFinal = math.fabs(result - resultOther)
print(resultFinal)
print(result)
print(resultOther)
print(diag)
print(otherDiag)