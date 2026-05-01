import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

area       = np.random.randint(600, 4000, n)
rooms      = np.random.randint(1, 7, n)
age        = np.random.randint(1, 50, n)
garage     = np.random.randint(0, 2, n)          # 0 = No, 1 = Yes
location   = np.random.choice([1, 2, 3], n)      # 1=Rural 2=Suburban 3=Urban

noise      = np.random.randint(-20000, 20000, n)
price      = (area * 55
              + rooms * 15000
              - age  * 800
              + garage * 30000
              + location * 25000
              + noise)

price = np.clip(price, 50000, 900000)

df = pd.DataFrame({
    "Area_sqft"  : area,
    "Num_Rooms"  : rooms,
    "House_Age"  : age,
    "Garage"     : garage,
    "Location"   : location,
    "Price"      : price
})

df.to_csv("house_data.csv", index=False)
print("Dataset saved! Shape:", df.shape)
print(df.head())
