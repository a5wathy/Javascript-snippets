#find the sum of 2 binary numbers:

def addBinary( a, b):

    length = max(len(a),len(b) + 1)
    sum = ['0' for i in range(length)]
    if len(a)>len(b):
        b= '0' * (len(a)-len(b))+b
    elif len(b)>len(a):
        a = '0' * (len(b)-len(a))+a

    carry = 0
    i = len(a)-1
    while i>=0:
        if int(a[i])+int(b[i])==3:
            carry = 1
            sum[i+1] = 1
        elif int(a[i])+int(b[i])==2:
            carry = 1
            sum[i+1] = 0
        elif int(a[i])+int(b[i])==1:
            carry = 0
            sum[i+1] = 1
        else:
            sum[i+1] = 0
    if carry == 1:
        sum[0] = 1
    else:
        sum = sum[1:length]

    sum = ''.join(sum)
    return sum

sum= addBinary('110','011')
print(sum)
