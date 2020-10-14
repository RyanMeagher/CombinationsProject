import pandas as pd
import numpy as np

def addStatsPassing(draft_kings_df, week_num, csv_paths):
    df_store = pd.DataFrame(draft_kings_df)
    pass_paths = []

    pass_paths = pass_paths + [file for file in csv_paths if 'passing' in file and f'week{week_num}' in file]

    for file in pass_paths:
        if 'redzone' in file:
            df = pd.read_csv(file, header=1)
            df = df[['Name', 'QBR', 'COMP', 'ATT', 'YDS', 'TD', 'INT', 'In20', 'In10', 'In5']]
            df.columns = [x + f'_passing_week{week_num}' if x != 'Name' else 'Player' for x in df.columns]
            print(df.columns)
            df_store = pd.merge(df_store, df, on='Player', how='left')

        if 'advanced' in file:
            df = pd.read_csv(file, header=1)
            df = df[['Name', '20+', '40+', 'Bad Pass %', 'Avg Target Depth', 'Avg YAC']]
            df.columns = [x + f'_passing_week{week_num}' if x != 'Name' else 'Player' for x in df.columns]
            print(df.columns)
            df_store = pd.merge(df_store, df, on='Player', how='left')
    return df_store


def addStatsRushing(draft_kings_df, week_num, csv_paths):
    df_store = pd.DataFrame(draft_kings_df)
    pass_paths = []

    pass_paths = pass_paths + [file for file in csv_paths if 'rushing' in file and f'week{week_num}' in file]

    for file in pass_paths:
        if 'redzone' in file:
            df = pd.read_csv(file, header=1)
            df = df[['Name', 'ATT', 'YDS', 'TD', '%Tm', 'In20', 'In10', 'In5']]
            df = df.rename(columns={'YDS': 'total_YDS'})
            df.columns = [x + f'_rushing_week{week_num}' if x != 'Name' else 'Player' for x in df.columns]

            df_store = pd.merge(df_store, df, on='Player', how='left')

        if 'advanced' in file:
            df = pd.read_csv(file, header=1)
            df = df[['Name', 'In', 'Out', 'Stuffed', 'BT', 'YDS']]
            df.columns = ['Name', 'Inside_runs', 'Outside_runs', 'Stuffed_runs', 'Broken_tackles', 'YDS_after_contact']
            df.columns = [x + f'_rushing_week{week_num}' if x != 'Name' else 'Player' for x in df.columns]

            df_store = pd.merge(df_store, df, on='Player', how='left')
    return df_store


def addStatsReceiving(draft_kings_df, week_num,csv_paths):
    df_store = pd.DataFrame(draft_kings_df)
    pass_paths = []

    pass_paths = pass_paths + [file for file in csv_paths if 'receiving' in file and f'week{week_num}' in file]

    for file in pass_paths:
        if 'redzone' in file:
            df = pd.read_csv(file, header=1)

            df = df[['Name', 'In20', 'In10', 'In5', '%Tm']]
            df = df.rename(columns={'YDS': 'total_YDS'})
            df.columns = [x + f'_receiving_week{week_num}' if x != 'Name' else 'Player' for x in df.columns]

            df_store = pd.merge(df_store, df, on='Player', how='left')

        if 'advanced' in file:
            df = pd.read_csv(file, header=1)
            print(df.columns)
            df = df[['Name', 'TAR', 'REC', 'YDS', 'AY', 'Cmp AY', 'aDOT',
                     'Catch %', 'AY.1', 'TAR.1', 'YDS.1']]
            df.columns = ['Name', 'TAR', 'REC', 'Total_YDS', 'Total_AY', 'Cmp AY', 'aDOT',
                          'Catch %', '%Tm AY', '%Tm TAR', 'After_catch_YDS']
            df.columns = [x + f'_receiving_week{week_num}' if x != 'Name' else 'Player' for x in df.columns]

            df_store = pd.merge(df_store, df, on='Player', how='left')
    return df_store


def chooseWeeks(draft_kings_df, addStats, week_num, csv_paths, time_span=0):
    df_store = draft_kings_df

    if time_span > 0:
        for i in range(week_num - time_span, week_num):
            df = addStats(draft_kings_df, i, csv_paths)
            cols_to_use = df.columns.difference(draft_kings_df.columns).insert(0, 'Player')
            df_store = pd.merge(df_store, df[cols_to_use], on='Player', how='left')

        return df_store

    else:
        for i in range(1, week_num):
            df = addStats(draft_kings_df, i,csv_paths)
            cols_to_use = df.columns.difference(draft_kings_df.columns).insert(0, 'Player')
            df_store = pd.merge(df_store, df[cols_to_use], on='Player', how='left')

        return df_store
