n = input("수식 입력(예: 20 * 40) : ")
n1, op, n2 = n.split()

n1 = float(n1)
n2 = float(n2)

if op == '+' :
    print("%f %s %f = %f" % (n1, op, n2, n1+n2))
elif op == '-':
    print("%f %s %f = %f" % (n1, op, n2, n1-n2))
elif op == '*':
    print("%f %s %f = %f" % (n1, op, n2, n1*n2))
elif op == '/':
    print("%f %s %f = %f" % (n1, op, n2, n1/n2))
else:
    print("{} 지원하지 않는 연산자입니다.".format(op))