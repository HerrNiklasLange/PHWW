x = True
while (x == True):
    import os
    import time
    from time import gmtime, strftime
    print(strftime("%H:%M", gmtime()))
    Time = strftime("%H:%M", gmtime())
    print(type(Time))
    if (Time == "22:43"):
        print("It works")
        os.system("git add .")
        os.system("git commit -m'DailyUpdate'")
        os.system("git push origin main")
        time.sleep(60)

    elif (strftime("%H:%M", gmtime()) == "2:40"):
        import pandas as pd
        # read by default 1st sheet of an excel file
        dataframe1 = pd.read_excel('book2.xlsx')
    x = False