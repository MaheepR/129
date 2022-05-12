import pandas as pd

dwarf_stars_df = pd.read_csv('dwarf_stars.csv')

dwarf_stars_df = dwarf_stars_df.dropna()

dwarf_stars_df_radius = dwarf_stars_df['Radius'] * 0.102763
print(dwarf_stars_df_radius)

dwarf_stars_df_mass = dwarf_stars_df['Mass']*0.000954588
#dwarf_stars_df_mass = dwarf_stars_df['Mass'] * 0.000954588
print(dwarf_stars_df_mass)

#dwarf_stars_df.to_csv('new.csv', index=True, index_label="id")

#print(dwarf_stars_df.head())