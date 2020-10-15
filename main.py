import HelperFxn as hf
import os
from NflDataInitializer import NflDataInitializer, DraftKingsOptimization
week_num=5

cwd = os.getcwd()
csv_paths = list(hf.walk_through_files(cwd))
print([file for file in csv_paths if 'DK' in file and f'W{week_num}' in file][0])
Nfl_info = NflDataInitializer(csv_paths,5)
print([file for file in csv_paths if 'passing' in file and f'week{week_num}' in file])




#col_name='AvgPointsPerGame'


#print(DraftKingsOptimization(inj_df, col_name, 150, num_teams=1, search_space=100000000, percentile=25).findTopTeams())
