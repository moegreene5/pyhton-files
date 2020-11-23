print("FIND OUT YOUR POSTING STATUS")
gender = input("Enter you gender: ")
marr_status = input("Enter your Marital Status: ")
age = eval(input("Enter age: "))

# for female
if gender.lower() == "f" or "female":
    print("Hey")
    print("You have been posted to the Urban Areas.")
elif (gender.lower() == "m" or "male") and (marr_status.lower() == "single"):
    if age in range(18, 30):
        print("You have been posted to the Rural Areas.")
    elif age in range(31, 50):
        print("You have been posted to the Sub-urban Areas.")
    else:
        print("You are ineligible to render this service.")
# For the married male
elif gender.lower() == "m" or "male" and marr_status.lower() == "married":
    if age in range(18, 30):
        print("You have been posted to the Sub-urban Areas.")
    elif age in range(31, 60):
        print("You have been posted to the Urban Areas.")
    else:
        print("You are ineligible to render this service.")
print ('hello world')