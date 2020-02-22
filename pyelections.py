
import pandas as p

excel_data_df = p.read_csv(".\\pyelections.csv", delimiter=";")
count = excel_data_df.shape[0]
print("Houston Mayoral Election Results\n-----------------------------------------\nTotal Cast Votes:", count)
print("-----------------------------------------")


df_sorted = excel_data_df.groupby('Candidate')['Voter ID'].nunique().sort_values(ascending=False)

for i in range(0, len(df_sorted)):
    print("%s: %.2f%% (%d)" % (df_sorted.index[i], (100 * df_sorted[i] / float(count)), df_sorted[i]))

print("-----------------------------------------")
print("1st Advancing Candidate: %s\n2nd Advancing Candidate: %s" % (df_sorted.index[0], df_sorted.index[1]))
print("-----------------------------------------")

    