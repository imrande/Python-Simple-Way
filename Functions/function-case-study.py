# Case Study 1

def caseStudyFunction(arg1, arg2, arg3=4, arg4=8):
	print(arg1, arg2, arg3, arg4)

caseStudyFunction(3, 2) # => 3 2 4 8
caseStudyFunction(10, 20, 30, 40) # => 10 20 30 40
caseStudyFunction(25, 50, arg4=100) # => 25 50 4 100
caseStudyFunction(arg4=2, arg1=3, arg2=4) # => 3 4 4 2
caseStudyFunction() => TypeError
caseStudyFunction(arg3=10, arg4=20, 30, 40) => TypeError
caseStudyFunction(4, 5, arg2=10) => TypeError
caseStudyFunction(4, 5, arg3=4, arg5=10) => TypeError