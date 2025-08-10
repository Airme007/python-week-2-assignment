my_list = []
my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)

print ("My List After Append:", my_list)
my_list. insert(1, 15)

print("My List after Insertion:", my_list)

new_list= [50, 60, 70]
my_list.extend(new_list)
print ("My list after Extend:", my_list)

my_list.pop(-1)
print ("My lisy After removing last item:", my_list)

my_list.sort(reverse=True)
print("My List After Sorting in Descending order:", my_list)

print("Printing List Item:",my_list[3])