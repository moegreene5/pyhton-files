num = 1
x = "sign"
y = 5
score = 0
if num > 0:
    print("num is positive")
    score +=1
    if x == "sign":
        print("won second level")
        score +=1
        if y == 5:
            print("passed final test")
            score +=1
print(f"total score {score}")

        
