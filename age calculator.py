from cgi import print_arguments


print("welcome to bill calculator :")
total_bill =input("what is your total bill?")
percentage =input("How much tip do you want to give : 12%,15% ?")
people =input("how many people split the bill?")
bill = (float(percentage) / 100 * int(total_bill) + int(total_bill))
print(bill)