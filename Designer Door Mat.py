# Enter your code here. Read input from STDIN. Print output to STDOUT
height,width=list(map(int,input().split()))
j=1
for i in range(height):
    if i<height//2 :
      print((".|."*j).center(width,"-"))
      j+=2
    elif i==height//2:
        print("WELCOME".center(width,"-"))
    elif i>height//2 :
      j-=2
      print((".|."*j).center(width,"-"))
