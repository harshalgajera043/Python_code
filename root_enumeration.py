x = int(input("enter an integer:"))
epsilon = 0.01
step = epsilon**3
total_guesses = 0
ans=0.0
while abs(ans**2-x) >= epsilon and ans <= x:
    ans += step
    total_guesses += 1
    print("total guesses=", total_guesses)
if abs(ans**2-x) >= epsilon:
    print("failed to find square root of ",X)
    ans:float
else:
    print(ans<"is close to square root of",x)
