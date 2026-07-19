import os 

# Check kiya ki kya sach mein aisa koi folder computer mein hai ya nahi
if os.path.exists("clutteredFolder"):
    files = os.listdir("clutteredFolder")
    i = 1

    for file in files:
        if file.endswith(".png"):
            old_path = f"clutteredFolder/{file}"
            new_path = f"clutteredFolder/{i}.png"
            
            # SURAKSHA CHECK: Agar naye naam wali file pehle se maujood hai, 
            # toh ginti ko tab tak badhao jab tak khali seat (naam) na mil jaye!
            while os.path.exists(new_path):
                i += 1
                new_path = f"clutteredFolder/{i}.png"
            
            # Ab rename karenge, koi data delete nahi hoga!
            print(f"Renaming: {file} ---> {i}.png")
            os.rename(old_path, new_path)
            i += 1
            
    print("\nClutter clean ho gaya! Saari PNG files rename ho gayi hain. ")
else:
    print("Oops! 'clutteredFolder' naam ka koi folder nahi mila. ")
