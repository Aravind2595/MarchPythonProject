# read4subject marks and find total
#180-200 A+
#168-179 A
#140-159 B+
#120-139 B
#100-119 C+
#80-99 C
#60-79 D+
sub1=int(input("Enter the mark of subject1"))
sub2=int(input("Enter the mark of subject2"))
sub3=int(input("Enter the mark of subject3"))
sub4=int(input("Enter the mark of subject4"))
total=sub1+sub2+sub3+sub4
print("The total mark is",total)
if(180<=total<=200):
    print("The grade is A+")
elif(160<=total<=179):
    print("The grade is A")
elif(140<=total<=159):
    print("The grade is B+")
elif(120<=total<=139):
    print("The grade is B")
elif(100<=total<=119):
    print("The grade is C+")
elif(80<=total<=99):
    print("Th grade is C")
elif(60<=total<=79):
    print("The grade is D")
else:
    print("failed")
