def comapnyInfo(cname,loc):
    list=[
        {
            "company_name": cname,
            "company_location": loc
        }
    ]
    return list

cname = input("Enter your company name")
loc = input("Enter your company location")

print(comapnyInfo(cname,loc))



