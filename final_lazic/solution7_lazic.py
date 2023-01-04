phone = str(input("Please enter your phone number (No dashes or area code): "))
length = len(phone)

if length == 10:
    print( "%s-%s-%s" % (phone[:3], phone[3:6], phone[6:]))
else:
    print("This is not a valid phone number")
