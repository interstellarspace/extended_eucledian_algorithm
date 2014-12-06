import math

def Extended_Eucledian_Alg(num, mod):
    qi_list = list()
    remainder_list = list()
    #i_list = list()
    gcd_for_inverse(num, mod, qi_list, remainder_list)
    #print(qi_list)
    #print(remainder_list)
    inv = calculate_inverse(qi_list)
    if inv < 0:
        inv = inv % mod
    if remainder_list[len(remainder_list)-2] == 1.0:
        return inv
    else:
        #print("Error: num '%' mod " + str(mod) + " has not multiplicative inverse")
        return( str(num) + " mod " + str(mod) + " has no multiplicative inverse.")
    
def gcd_for_inverse(a,b, qi_list, remainder_list):
    if b == 0:
        return a
    else:
        qi_list.append(math.trunc(a / b))
        remainder_list.append(a % b)
        return gcd_for_inverse(b, a % b, qi_list, remainder_list)

def calculate_inverse(qi_list):
    xjold = 0
    xjnew = 1
    for x in range(1,len(qi_list)-1):
        inv = xjold - (qi_list[x] * xjnew)
        xjold = xjnew
        xjnew = inv    
    return inv
