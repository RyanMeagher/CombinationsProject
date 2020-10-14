def CreateCombosAll(qb, wr, rb, te, flex=False):
    if flex:
        gen = (
            (QB, WR1, WR2, WR3, RB1, RB2, TE, FLEX)
            for QB in qb
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
            for RB1 in rb
            for RB2 in rb if RB1 != RB2
            for TE in te
            for FLEX in rb + wr + te if FLEX not in (QB, WR1, WR2, WR3, RB1, RB2, TE)
        )

    else:
        gen = (
            (QB, WR1, WR2, WR3, RB1, RB2, TE)
            for QB in qb
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
            for RB1 in rb
            for RB2 in rb if RB1 != RB2
            for TE in te
        )
    return gen


def CreateCombo(qb=None, wr=None, rb=None, te=None, flex=False):
    # create combinations using only WR
    if te is None:
        te = []
    if wr is None:
        wr = []
    if rb is None:
        rb = []
    global gen
    if bool(wr) and not bool(qb) and not bool(te) and not bool(rb):  # Combo WR
        gen = (
            (WR1, WR2, WR3)
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
        )
    # create combo of WR and QB
    elif bool(wr) and bool(qb) and not bool(te) and not bool(wr):  # Combo wr/qb
        gen = (
            (QB, WR1, WR2, WR3)
            for QB in qb
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
        )

    elif bool(wr) and bool(te) and not bool(qb) and not bool(rb):  # Combo wr/te
        gen = (
            (WR1, WR2, WR3, TE)
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
            for TE in te
        )

    elif bool(wr) and bool(qb) and bool(te) and not bool(rb):  # combo wr/qb/te
        gen = (
            (QB, WR1, WR2, WR3, TE)
            for QB in qb
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
            for TE in te
        )
    elif bool(wr) and bool(rb) and not bool(te) and not bool(qb):  # combo wr/rb
        gen = (
            (WR1, WR2, WR3, RB1, RB2)
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
            for RB1 in rb
            for RB2 in rb if RB1 != RB2
        )
    elif bool(wr) and bool(rb) and bool(te) and not bool(qb):  # combo wr/rb/te
        gen = (
            (WR1, WR2, WR3, RB1, RB2, TE)
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
            for RB1 in rb
            for RB2 in rb if RB1 != RB2
            for TE in te
        )

    elif bool(wr) and bool(rb) and bool(qb) and not bool(te):  # combo wr/rb/qb
        gen = (
            (WR1, WR2, WR3, RB1, RB2)
            for WR1 in wr
            for WR2 in wr if WR2 != WR1
            for WR3 in wr if WR3 != WR2 and WR3 != WR1
            for RB1 in rb
            for RB2 in rb if RB1 != RB2
        )

    elif bool(rb) and bool(qb) and bool(wr) and not bool(te):  # combo rb/qb
        gen = (
            (QB, RB1, RB2)
            for QB in qb
            for RB1 in rb
            for RB2 in rb if RB1 != RB2

        )

    elif bool(rb) and bool(te) and not bool(qb) and not bool(wr):  # combo rb/te
        gen = (
            (RB1, RB2, TE)
            for RB1 in rb
            for RB2 in rb if RB1 != RB2
            for TE in te
        )
    elif bool(rb) and bool(te) and bool(qb) and not bool(wr):  # combo rb/te/qb
        gen = (
            (QB, RB1, RB2, TE)
            for QB in qb
            for RB1 in rb
            for RB2 in rb if RB1 != RB2
            for TE in te
        )
    elif bool(te) and bool(qb) and bool(rb) and not bool(wr):  # combo te/qb
        gen = (
            (QB, RB1, RB2, TE)
            for QB in qb

            for TE in te
        )
    elif bool(wr) and bool(rb) and bool(qb) and bool(te):  # combo all
        gen = CreateCombosAll(qb, wr, rb, te, flex)

    return gen

