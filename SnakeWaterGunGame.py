import random 

a = input("Choose snake or water or gun: ")


if a in ['snake', 'water', 'gun']:
    
   
    l = ['snake', 'water', 'gun']
    b = random.choice(l)
    
    print(f"\nYou chose: {a}")
    print(f"Computer chose: {b}\n")
    
    
    if(a == b):
        print("Result: Match Draw! ")
        
    elif(a == 'snake' and b == 'water'):
        print("Result: You Win! ")
        
    elif(a == 'snake' and b == 'gun'):
        print("Result: You Loss! ")
        
    elif(a == 'water' and b == 'snake'):
        print("Result: You Loss! ")
        
    elif(a == 'water' and b == 'gun'):
        print("Result: You Win! ")
        
    elif(a == 'gun' and b == 'snake'):
        print("Result: You Win! ")
        
    elif(a == 'gun' and b == 'water'):
        print("Result: You Loss! ")


else:
    print("\nInvalid input, please write correct spelling! ")
