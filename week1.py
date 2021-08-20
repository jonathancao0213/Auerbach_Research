import pandas as pd
data = pd.io.stata.read_stata("cross_sectional.dta")
data.to_csv("cross_sectional.csv")
