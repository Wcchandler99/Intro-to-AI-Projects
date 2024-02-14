import pandas as pd

# df=pd.read_csv("Actor_combined-temp.csv")
# #print(df)
# # print(df['final_result'].unique())
# # Find the index of the first occurrence of 0 in 'Unnamed: 0'
# # last_index_where_zero = df[df['Unnamed: 0'] == 0].last_valid_index()

# # # Select rows from the last row up to the end_index
# # new_df = df.loc[last_index_where_zero:]
# new_df = df.drop_duplicates()
# df_caught = new_df[new_df['final_result'] == "CAUGHT"]
# df_caught = df_caught[:3500]
# df_rescued = new_df[new_df['final_result'] == "RESCUED"]
# df = pd.concat([df_caught, df_rescued])

# print(df)

# Read the data (modify the file name as per your data)
caught_df=pd.read_csv("Balanced_Actor_caught.csv")
rescued_df=pd.read_csv("Balanced_Actor_rescued.csv")
caught_df1=pd.read_csv("Balanced_Actor_caught1.csv")
rescued_df1=pd.read_csv("Balanced_Actor_rescued1.csv")
caught_df2=pd.read_csv("Balanced_Actor_caught2.csv")
rescued_df2=pd.read_csv("Balanced_Actor_rescued2.csv")
caught_df3=pd.read_csv("Balanced_Actor_caught3.csv")
rescued_df3=pd.read_csv("Balanced_Actor_rescued3.csv")

caught_combined = pd.concat([caught_df, caught_df1, caught_df2, caught_df3], ignore_index=True)


rescued_combined = pd.concat([rescued_df, rescued_df1, rescued_df2, rescued_df3], ignore_index=True)

# Ensure that rescued_combined is no longer than caught_combined
if len(rescued_combined) > len(caught_combined):
    rescued_combined = rescued_combined[:len(caught_combined)]



df = pd.concat([rescued_combined, caught_combined])
df['Unnamed: 0'] = df['Unnamed: 0']%150
df = df.dropna()
X_df = df.drop(columns=['action_taken', 'final_result'])
Y = df['final_result']
