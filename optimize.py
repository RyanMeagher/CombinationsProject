import pandas as pd
import numpy as np
import CreateDraftKingsCombinations as cc
import HelperFxn as hf


def optimizeCol(df, col_name, percentile=None):
    # filter by the column you are trying to optimize to finf the top  percecntile of players in that
    # catagory

    df = df[df[col_name] > 0]
    df_optimized = df[(df[col_name] >= df[col_name].median())]

    if bool(percentile):
        df_optimized = df_optimized[(df_optimized[col_name] >= np.percentile(df_optimized[col_name], [percentile])[0])]

    df_optimized = df_optimized[['Player', 'Salary', f'{col_name}']].values.tolist()

    return df_optimized


def findTopScores(gen, point_threshold, min_salary=45000, max_salary=50000, iter=10000000):
    count = 0
    m = []
    for x in gen:

        count += 1
        amount = sum([player[1] for player in x])
        points = sum([player[2] for player in x])

        if amount >= min_salary and amount <= max_salary:
            if points >= point_threshold:
                m.append((x, amount, points))

        if count > iter:
            break
    return m


def FindColTeamInfo(df, col_name, percentile=25, min_salary=45000, max_salary=50000, point_threshold=150,
                    iter1=20, iter2=100000000):
    avg_scores = []
    for i in range(iter1):
        qb, wr, rb, te, d = hf.createPositionDF(df)

        qb = optimizeCol(qb, f'{col_name}', percentile)
        rb = optimizeCol(rb, f'{col_name}', percentile)
        wr = optimizeCol(wr, f'{col_name}', percentile)
        te = optimizeCol(te, f'{col_name}', percentile)
        d = optimizeCol(d, f'{col_name}', percentile)

        np.random.shuffle(qb)
        np.random.shuffle(wr)
        np.random.shuffle(rb)
        np.random.shuffle(te)
        np.random.shuffle(d)

        gen = cc.CreateCombo(qb=qb, wr=wr, rb=rb, te=te, flex=True)

        x = findTopScores(gen, point_threshold, min_salary, max_salary, iter2)

        avg_scores.append(max(x, key=lambda x: x[2]))

    return avg_scores
