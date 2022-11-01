# plate 1:
def cal(x, y, loc, d1):
    Pyr_conc_in_well = ((x / 300) * 405) / 10
    NADH_conc_in_well = ((y / 300) * 5) / 10
    for a in loc:
        d1[a] = {'Pyr': {'conc': Pyr_conc_in_well, 'unit': 'mM'}, 'NADH': {'conc': NADH_conc_in_well, 'unit': 'mM'}}


# plate 2:
def cal2(a, b, pos, d2):
    Pyr_conc_in_well = ((a / 300) * 405) / 10
    NADH_conc_in_well = ((b / 300) * 5) / 10
    for p in pos:
        d2[p] = {'Pyr': {'conc': Pyr_conc_in_well, 'unit': 'mM'}, 'NADH': {'conc': NADH_conc_in_well, 'unit': 'mM'}}
