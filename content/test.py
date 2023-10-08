x = True
while (x == True):
    import os
    import time
    from time import gmtime, strftime
    # note one hour behind
    if (strftime("%H:%M", gmtime()) == "11:00"):
        print("It works")
        os.system("git add .")
        os.system("git commit -m'DailyUpdate'")
        os.system("git push origin main")
        time.sleep(60)

    #else: # (strftime("%H:%M", gmtime()) == "2:40"):
        #import pandas as pd
        # read by default 1st sheet of an excel file
        #dataframe1 = pd.read_excel('C:/Users/nikla/OneDrive/Desktop/PHW/PWS/PWS/data/phwMaindt.xlsx')
        #print(dataframe1)
