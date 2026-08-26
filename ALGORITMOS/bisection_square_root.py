def square_root_bisection(number,tolerance=0.0001,max_iter=1000):
    if number<0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number==0 or number==1:
        print(f'The square root of {number} is {number}')
        return number
    else:
        a=0
        b=number+1
        root=(a+b)/2
        num_iter=0
        previous_root=0
        while abs(root-previous_root)>=tolerance and num_iter<max_iter:
            if (root*root-number)>0:
                b=root
            else: 
                a=root
            previous_root=root
            root=(a+b)/2
            num_iter+=1
        # Al salir del bucle, verificar si se alcanzó la tolerancia o se superó max_iter
        if abs(root - previous_root) >= tolerance and num_iter >= max_iter:
            print(f'Failed to converge within {max_iter} iterations')
            return None
            
        print(f'The square root of {number} is approximately {root}')
        return root

print(square_root_bisection(0))
print(square_root_bisection(1))

print(square_root_bisection(0.001, 1e-7,50))
#square_root_bisection lab freecodecamp