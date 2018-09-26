#program to print even numbers in given intervals
lower_limit, upper_limit=map(int,raw_input().split())
for i in range(lower_limit,upper_limit+1):
  if(i%2 == 0):
    print(i),
