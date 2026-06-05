def simplify(x, n):
    x_parts = x.split('/')
    x_num = int(x_parts[0])
    x_den = int(x_parts[1])
    
    n_parts = n.split('/')
    n_num = int(n_parts[0])
    n_den = int(n_parts[1])
    
    product_num = x_num * n_num
    product_den = x_den * n_den
    
    return product_num % product_den == 0
