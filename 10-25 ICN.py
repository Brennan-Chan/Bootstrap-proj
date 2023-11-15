import pandas as pd
from matplotlib import pyplot as plt
from plotnine import *
import os
os.chdir("C:/Users/Hi_I_/Downloads")
dat = pd.read_csv("2017_Fuel_Economy_Data")

adfjkln= dat["Combined Mileage (mpg)"]
n = len(adfjkln)

# in cm units 
# right 
goob = pd.DataFrame({"hand_span": [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5, 21.5, 18, 18, 20.5, 20, 20.3, 
            21.5, 19, 20.4, 22.7, 22.9, 17, 23, 23.8, 22, 21.5, 21.5]})

goob_means = []
for _ in range(10000):
    goobus = goob.sample(26, replace = True)
    #goob_means.append(float(goobus.mean()))
    goob_means.append(float(goobus.median()))

plt.hist(goob_means)
plt.xlabel("hand size")
plt.ylabel("Amount of observations")
plt.title("Gingle gingleton")
plt.show()

gloob = pd.DataFrame({ "Data" : goob_means})
(
    ggplot(gloob, aes(x = "Data"))
    + geom_histogram()
    
)



# put in any data set and bootstrap class that will display histograms and getting all the means 
# ect, ect, iterate more fucken cook a pizza and kill a donkey 