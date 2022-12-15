import pandas as pd

outPath = "G:/My Drive/Math_EE_Wordle.xlsx"

writer = pd.ExcelWriter(outPath, engine="xlsxwriter")

writer.save()