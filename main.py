import HelperFxn as hf
import os
from NflDataInitializer import NflDataInitializer, DraftKingsOptimization

cwd = os.getcwd()
csv_paths = list(hf.walk_through_files(cwd))

Nfl_info = NflDataInitializer(5, csv_paths)
dk = Nfl_info.getDK()
inj_df=Nfl_info.filterInj()



col_name='AvgPointsPerGame'

print(DraftKingsOptimization(inj_df, col_name, 150, num_teams=1, search_space=100000000, percentile=25).findTopTeams())
