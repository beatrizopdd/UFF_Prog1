moeda = [8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

a1 = moeda[0:9]
a2 = moeda[9:18]
a3 = moeda[18:27]

if (sum(a1) < sum(a2)): # pesagem 1
    b1 = a1[0:3]
    b2 = a1[3:6]
    b3 = a1[6:9]
    
    if (sum(b1) < sum(b2)): # pesagem 2
        c1 = b1[0]
        c2 = b1[1]
        c3 = b1[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(1))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(2))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(3))
            
    if (sum(b2) < sum(b1)): # pesagem 2
        c1 = b2[0]
        c2 = b2[1]
        c3 = b2[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(4))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(5))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(6))
    
    if (sum(b1) == sum(b2)): # pesagem 2
        c1 = b3[0]
        c2 = b3[1]
        c3 = b3[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(7))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(8))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(9))
            
if (sum(a2) < sum(a1)): # pesagem 1
    b1 = a2[0:3]
    b2 = a2[3:6]
    b3 = a2[6:9]
    
    if (sum(b1) < sum(b2)): # pesagem 2
        c1 = b1[0]
        c2 = b1[1]
        c3 = b1[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(10))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(11))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(12))
            
    if (sum(b2) < sum(b1)): # pesagem 2
        c1 = b2[0]
        c2 = b2[1]
        c3 = b2[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(13))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(14))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(15))
    
    if (sum(b1) == sum(b2)): # pesagem 2
        c1 = b3[0]
        c2 = b3[1]
        c3 = b3[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(16))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(17))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(18))
            
if (sum(a1) == sum(a2)): # pesagem 1
    b1 = a3[0:3]
    b2 = a3[3:6]
    b3 = a3[6:9]
    
    if (sum(b1) < sum(b2)): # pesagem 2
        c1 = b1[0]
        c2 = b1[1]
        c3 = b1[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(19))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(20))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(21))
            
    if (sum(b2) < sum(b1)): # pesagem 2
        c1 = b2[0]
        c2 = b2[1]
        c3 = b2[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(22))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(23))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(24))
    
    if (sum(b1) == sum(b2)): # pesagem 2
        c1 = b3[0]
        c2 = b3[1]
        c3 = b3[2]
        
        if (c1 < c2): # pesagem 3
            print("A moeda {} é falsa!".format(25))
            
        if (c2 < c1): # pesagem 3
            print("A moeda {} é falsa!".format(26))
        
        if (c1 == c2): # pesagem 3
            print("A moeda {} é falsa!".format(27))
