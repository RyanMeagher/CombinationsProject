import os
import pandas as pd


def walk_through_files(path, file_extension='.csv'):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith(file_extension):
                yield os.path.join(dirpath, filename)


def getSalary(week_num, csv_paths):
    path = [file for file in csv_paths if 'DK' in file and f'W{week_num}' in file][0]
    df = pd.read_csv(path)
    df = df[['Name', 'ID', 'Salary', 'Position', 'TeamAbbrev', 'AvgPointsPerGame']]
    df = df.rename(columns={'Name': 'Player'})

    return df


def getPracticeInjReport(draft_kings_df, week_num, csv_paths):
    prac_path = [file for file in csv_paths if 'practice-report' in file and f'week{week_num}' in file][0]
    inj_path = [file for file in csv_paths if 'injury-report' in file and f'week{week_num}' in file][0]

    # We are creating a dataframe that includes players injuries and filtering based on designation
    df_inj = pd.read_csv(inj_path)
    df_inj = df_inj[['Player', 'Injury', 'Status']]
    df_inj = pd.merge(draft_kings_df, df_inj, on='Player', how='left')
    df_inj = df_inj[(df_inj.Status != 'IR') & (df_inj.Status != 'Out')]

    # later I am going to create a feature based on an injured players weekly practice schedule
    # also based on the area the injury is "injuryRisk"
    df_prac = pd.read_csv(prac_path)
    df_prac = df_prac.rename(columns={'Player Name': 'Player'})
    df_prac = df_prac.drop_duplicates(subset='Player', keep="first")
    df_prac = df_prac[['Player', 'Wed', 'Thu', 'Fri', 'Sat']]
    df_prac.columns = ['Player', 'WedPractice', 'ThuPractice', 'FriPractice', 'SatPractice']

    df_salary_inj_practice = pd.merge(df_inj, df_prac, on='Player', how='left')

    return df_salary_inj_practice


def createPositionDF(df):
    qb = df[(df.Position == 'QB')]
    wr = df[(df.Position == 'WR')]
    rb = df[(df.Position == 'RB')]
    te = df[(df.Position == 'TE')]
    d = df[(df.Position == 'DST')]
    return qb, wr, rb, te, d



