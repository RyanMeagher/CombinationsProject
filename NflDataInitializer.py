import HelperFxn as hf
import pandas as pd
import AddStats
import optimize as opt


class NflDataInitializer:

    def __init__(self, week_num, csv_paths):
        self.week_num = week_num
        self.csv_paths = csv_paths
        self.df_salary = hf.getSalary(self.week_num, self.csv_paths)
        self.df_inj_filtered = hf.getPracticeInjReport(self.df_salary, self.week_num, self.csv_paths)
        self.passing_df = pd.DataFrame()
        self.rushing_df = pd.DataFrame()
        self.receiving_df = pd.DataFrame()

    def getDK(self):
        return self.df_salary

    def filterInj(self):
        return self.df_inj_filtered

    def getPassingStats(self, time_span=0):
        return AddStats.chooseWeeks(self.df_inj_filtered, AddStats.addStatsPassing, self.week_num,
                                    time_span=time_span)

    def getRushingStats(self, time_span=0):
        return AddStats.chooseWeeks(self.df_inj_filtered, AddStats.addStatsRushing, self.week_num,
                                    time_span=time_span)

    def getReceivingStats(self, time_span=0):
        return AddStats.chooseWeeks(self.df_inj_filtered, AddStats.addStatsReceiving, self.week_num, self.csv_paths,
                                    time_span=time_span)


class DraftKingsOptimization:
    def __init__(self, df, col_name, point_threshold, num_teams=20, search_space=100000000,
                 min_salary=45000, max_salary=50000, percentile=None):
        self.df = df
        self.col_name = col_name
        self.percentile = percentile
        self.num_teams = num_teams
        self.max_salary = max_salary
        self.min_salary = min_salary
        self.search_space = search_space
        self.qb, self.wr, self.rb, self.te, self.d = hf.createPositionDF(self.df)
        self.optimized_qb = opt.optimizeCol(self.qb, self.col_name, self.percentile)
        self.optimized_wr = opt.optimizeCol(self.wr, self.col_name, self.percentile)
        self.optimized_rb = opt.optimizeCol(self.rb, self.col_name, self.percentile)
        self.optimized_te = opt.optimizeCol(self.te, self.col_name, self.percentile)
        self.optimized_d = opt.optimizeCol(self.d, self.col_name, self.percentile)
        self.optimal_teams = None
        self.point_threshold = point_threshold


    def findTopTeams(self):

        self.optimal_teams = opt.FindColTeamInfo(self.df, self.col_name, self.percentile, min_salary=self.min_salary,
                                                 max_salary=self.max_salary,
                                                 point_threshold=self.point_threshold,
                                                 iter1=self.num_teams, iter2=self.search_space)

        return self.optimal_teams
