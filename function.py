def month_exp(exp):
    total_exp=0
    for i in exp:
        total_exp=total_exp+i
    print(" Yes I am in month_exp")
    return total_exp

feb_exp=[4,2,3]
mar_exp=[4,5,3]
total=0
for i in feb_exp:
    total=total+i
print("Feb total expense is ",total)
total=0
for i in mar_exp:
    total=total+i
print("Mar total expense is ",total)
total_feb=month_exp(feb_exp)
print("Total expense in Feb is : ",total_feb)
total_mar=month_exp(mar_exp)
print("Total expense in mar is : ",total_mar)

