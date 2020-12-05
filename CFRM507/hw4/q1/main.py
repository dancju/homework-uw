#!/usr/bin/env python
import amplpy
import pandas as pd

df_fund = pd.read_csv("funds.csv", index_col="Index").pct_change().dropna()
df_factor = pd.read_csv("benchmarks.csv", index_col="Index").pct_change().dropna()

model = amplpy.AMPL()
model.read("main.mod")
model.getSet("date").setValues(df_factor.index.tolist())
model.getSet("factor").setValues(df_factor.columns.tolist())
model.getParameter("return_factor").setValues(
    pd.Series(
        df_factor.values.reshape(-1),
        index=pd.MultiIndex.from_product(
            [df_factor.index, df_factor.columns], names=["date", "factor"]
        ),
    )
)

for s_fund in df_fund.columns:
    print(s_fund)
    model.getParameter("return_fund").setValues(pd.Series(df_fund[s_fund]))
    model.solve()
    print(model.getVariable("alpha").getValues())
    print(model.getVariable("beta").getValues())
