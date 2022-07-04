#num=input("Enter a no : ")
#if num%2==0:
    #print(num,"is even")
#else:
    #print(num,'is odd')


india=["Samosa","Paneer Tikka","Naan"]
chines=["Munchurian","Fried Rice","Noodles"]
italian=["Pizza","Roll","Pasta"]

dish=raw_input("Enter your dish name:")
if dish in india:
    print("Indian Dish")
elif dish in chines:
    print("Chinese Dish")
elif dish in italian:
    print("Italian Dish")
else:
    print("Your dish",dish,"is not our list")
   


