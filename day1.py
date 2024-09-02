name = 'suraj'
#using title,lower and upper
print(f"Hello {name.title()}")
print(f"Hello {name.lower()}")
print(f"Hello {name.upper()}")

print(f"\t{name}")

#using rstrip it removes blank space.
name_2 = 'suraj   '
print(name_2)
print(name_2.rstrip())


#try some simple maths

print(2+3)
print(2 + 5**5)

# import this
#uncomment and use the above one

sur_list = ['pen','game','kid','amerika','lol']
print(sur_list)
print(sur_list[1])
#also
print(sur_list[1].title())
print(sur_list[-1])


#overriding values
sur_list[0] = 'pan'
print(sur_list)

sur_list.append('uff')
print(sur_list)

#add to custom index

sur_list.insert(1,'ice')
print(sur_list)

#delete
del sur_list[0]
print(sur_list)

pop_list = sur_list.pop()
print(sur_list)
print(f"{pop_list} has been removed")
print(sur_list)
# u can also use pop(1) and 2 3 4
# also use remove('cold') easy way

#organize
sur_list.sort()
print(sur_list)
sur_list.sort(reverse=True)
print(sur_list)

#use sorted(sur_list) for temp sorting

#use .reverse for reverse
sur_list.reverse()
print(sur_list)
print(len(sur_list))


for sur in sur_list:
    print(sur)

for sur in sur_list:
    print(f"{sur.title()} is a cool name")

#using range

for sur in range(1,11):
    print(f"sup {sur}")

#using range and converting to list
nums = list(range(1,6))
print(nums)

squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# use min max sum

nums = list(range(1,11))

small = min(nums)
print(small)
big = max(nums)
print(big)
sums = sum(nums)
print(sums)

#slicing [:3] or [1:4]
# if u need from 3 item to the end use [2:] u can also loop thru that

#tuples same as list but cant change and uses ()

