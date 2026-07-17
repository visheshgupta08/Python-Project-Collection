#  Project_name = Kaun Banega Crorepati 
questions = [ 
    ["1. what is the capital of india?","A.UP","B.Delhi","C.Chennai","D.gujrat","B",1000], 
    ["2. who is called the god of cricket?","A.MS Dhoni","B.Virat Kohli","C.sachin Tendulkar","D.Rohit Sharma", "C",10000], 
    ["3. Who is the first pm of india?","A.jahawar lal nehru","B.Narendra Modi","C. Rajendra Prasad","D.Indra gandhi","A",50000],
    ["4. Which Indian scientist won the Nobel Prize in Physics in 1930?", "A. APJ Abdul Kalam","B. C.V. Raman","C. Homi J. Bhabha","D. Vikram Sarabhai","B", 100000],
    ["5.Which is the longest river in the world?", "A. Amazon River", "B. Nile River", "C. Yangtze River", "D. Mississippi River", "B", 1000000],
    ["6. Which country is known as the Land of the Rising Sun?", "A. China", "B. Japan", "C. South Korea", "D. Thailand", "B", 5000000],
    ["7. In which year did India win its first Cricket World Cup?", "A. 1975", "B. 1983", "C. 2007", "D. 2011", "B", 7500000],
    ["8. Who wrote the famous Indian play 'Abhijnanasakuntalam'?", "A. Kalidasa", "B. Tulsidas", "C. Kabir", "D. Harivansh Rai Bachchan", "A", 10000000]
]

print("==============================================")
print("     WELCOME TO KAUN BANEGA CROREPATI!        ")
print("==============================================")
print("Rules: Har sahi jawab par paise milenge.")
print("Agar jawab nahi pata, toh 'Q' daba kar QUIT karein.\n")
print("so lets start the game...")
print("Ye raha swal aapki computer screen pr")
import time
money=0
round_no = 0
for q in questions:
    print(f"Question for Rs. {q[6]}")
    print(q[0])   
    time.sleep(3)  
    print(f"  {q[1]}         {q[2]} ")       
    print(f"  {q[3]}    {q[4]} ")
    
    Reply = input("Apna jawab dalein (A/B/C/D) ya QUIT karne ke liye 'Q' dalein: ")
    
    if(Reply.upper() == "Q"):
        print("\nAapne game beech mein hi chhodne ka faisla kiya.")
        break   
        
    elif(Reply.upper() == q[5]):
        print("sahi javab") 
        money = q[6]  
        print(f"aapne jite h rs {q[6]}") 
        print("congratulations.\n")
        round_no += 1
          
    else:
        print("galat javab ,Khela Samapt") 
        if round_no > 2 and round_no <= 4:   
            money = 10000                    
        elif round_no > 4 and round_no <= 6: 
            money = 100000                    
        elif round_no > 6:                   
            money = 5000000                   
        else:
            money = 0   
        break   

print(f"ghar le jane wali rashi: Rs.{money}")
print("Thank you for playing KBC!")


