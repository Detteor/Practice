# zork = 0
# print ('Before', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + thing
#     print (zork, thing)
# print ('After', zork)

# count = 0 
# sum = 0
# print ('Before', count, sum)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count +1
#     sum = sum + value
#     print (count, sum, value)
# print ('After', count, sum, sum / count)

# print ('Before')
# for value in [9,41,12,3,74,15]:
#     if value > 20:
#         print ('Large Number', value)
# print ('After')

# found = False
# print ('Before', found)
# for value in [9,41,12,3,74,15]:
#     if value == 3:
#         found = True
#         break
#     print (found, value)
# print ('After', found)

# largest_so_far = -1 
# print ('Before', largest_so_far)
# for the_num in [9,41,12,3,74,15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print (largest_so_far, the_num)
# print ('After', largest_so_far)

smallest = None
print ('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest, value)
print ('After', smallest)