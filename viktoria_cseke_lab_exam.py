#Program made by Viktoria Cseke

def welcome():
    print("{}".format("="*20))
    print("Welcome to the application usage analyser")
    print("{}".format("="*20))

def read_user_details():
    app_name=input("App used >>> ")
    number_of_days=int(input("Number of days >>>"))
    name=input("name >>>")
    return app_name, number_of_days,name

def get_times(number_of_days):
    #days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    usages=[]
    for i in range(0,number_of_days):
        i+=1
    #for day in days:
        use=int(input("{}".format("Time (minutes) on ")))
        usages.append(use)

    return usages

def display_details(usages, app_name,name):
    total=0
    largest=0
    average=0
    for time in usages:
        if time>60 and time>largest:
            largest=time

    for t in usages:
        total += t
        average = total / len(usages)
    print("The average is:",average)
    print(name,",on you have spent the most time on", app_name," , ",largest, "minutes")

def main():
    welcome()
    app_name,number_of_days,name = read_user_details()
    usages = get_times(number_of_days)
    display_details(usages, app_name,name)

main()