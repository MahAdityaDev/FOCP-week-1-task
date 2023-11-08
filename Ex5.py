#number 5
grp_s=24
class_s=[113,175,12]
for stu in class_s:
    full_grp=stu//grp_s
    left_overs=stu%grp_s
    print("for",stu,"no. of students:")
    print("no. of full groups:",full_grp)
    print("no. left over students",left_overs)