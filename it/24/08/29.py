#только начал, еще не знаю вим или вс код
def is_prime(i):
    for j in range (1, i):
        if i%j==0:
            if j==i or j==1:
                return True
            else:
                return False
print(is_prime(4))
