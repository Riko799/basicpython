a = 1
b = -6
c = 9

# TODO
x1 = a + b
x2 = a - b

print(x1, x2)
#２次方程式の解を求める

def solve_f(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('解は {0}, {1}'.format(x_1,x_2))
    
solve_f(1,-6,9)
solve_f(1,2,-8)
solve_f(8,-6,-35)
solve_f(1,0,1)