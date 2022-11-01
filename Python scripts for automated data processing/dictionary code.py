from methods import cal
from methods import cal2
import pickle

# plate 1:
d1 = {}
# exp1:
cal(x=300, y=300, loc=['A1', 'A2', 'A3'], d1=d1)
cal(x=280, y=300, loc=['B1', 'B2', 'B3'], d1=d1)
cal(x=200, y=300, loc=['C1', 'C2', 'C3'], d1=d1)
cal(x=100, y=300, loc=['D1', 'D2', 'D3'], d1=d1)
cal(x=50, y=300, loc=['E1', 'E2', 'E3'], d1=d1)
cal(x=33, y=300, loc=['F1', 'F2', 'F3'], d1=d1)
cal(x=25, y=300, loc=['G1', 'G2', 'G3'], d1=d1)

# exp3:
cal(x=300, y=200, loc=['A4', 'A5', 'A6'], d1=d1)
cal(x=280, y=200, loc=['B4', 'B5', 'B6'], d1=d1)
cal(x=200, y=200, loc=['C4', 'C5', 'C6'], d1=d1)
cal(x=100, y=200, loc=['D4', 'D5', 'D6'], d1=d1)
cal(x=50, y=200, loc=['E4', 'E5', 'E6'], d1=d1)
cal(x=33, y=200, loc=['F4', 'F5', 'F6'], d1=d1)
cal(x=25, y=200, loc=['G4', 'G5', 'G6'], d1=d1)

# exp5:
cal(x=300, y=40, loc=['A7', 'A8', 'A9'], d1=d1)
cal(x=280, y=40, loc=['B7', 'B8', 'B9'], d1=d1)
cal(x=200, y=40, loc=['C7', 'C8', 'C9'], d1=d1)
cal(x=100, y=40, loc=['D7', 'D8', 'D9'], d1=d1)
cal(x=50, y=40, loc=['E7', 'E8', 'E9'], d1=d1)
cal(x=33, y=40, loc=['F7', 'F8', 'F9'], d1=d1)
cal(x=25, y=40, loc=['G7', 'G8', 'G9'], d1=d1)

# exp 7:
cal(x=300, y=25, loc=['A10', 'A11', 'A12'], d1=d1)
cal(x=280, y=25, loc=['B10', 'B11', 'B12'], d1=d1)
cal(x=200, y=25, loc=['C10', 'C11', 'C12'], d1=d1)
cal(x=100, y=25, loc=['D10', 'D11', 'D12'], d1=d1)
cal(x=50, y=25, loc=['E10', 'E11', 'E12'], d1=d1)
cal(x=33, y=25, loc=['F10', 'F11', 'F12'], d1=d1)
cal(x=25, y=25, loc=['G10', 'G11', 'G12'], d1=d1)

with open('d1.pkl', 'wb') as f:
    pickle.dump(d1, f)

with open('d1.pkl', 'rb') as f:
    d1_new = pickle.load(f)

# plate 2:
d2 = {}
# exp2:
cal2(a=300, b=250, pos=['A1', 'A2', 'A3'], d2=d2)
cal2(a=280, b=250, pos=['B1', 'B2', 'B3'], d2=d2)
cal2(a=200, b=250, pos=['C1', 'C2', 'C3'], d2=d2)
cal2(a=100, b=250, pos=['D1', 'D2', 'D3'], d2=d2)
cal2(a=50, b=250, pos=['E1', 'E2', 'E3'], d2=d2)
cal2(a=33, b=250, pos=['F1', 'F2', 'F3'], d2=d2)
cal2(a=25, b=250, pos=['G1', 'G2', 'G3'], d2=d2)

# exp4:
cal2(a=300, b=50, pos=['A4', 'A5', 'A6'], d2=d2)
cal2(a=280, b=50, pos=['B4', 'B5', 'B6'], d2=d2)
cal2(a=200, b=50, pos=['C4', 'C5', 'C6'], d2=d2)
cal2(a=100, b=50, pos=['D4', 'D5', 'D6'], d2=d2)
cal2(a=50, b=50, pos=['E4', 'E5', 'E6'], d2=d2)
cal2(a=33, b=50, pos=['F4', 'F5', 'F6'], d2=d2)
cal2(a=25, b=50, pos=['G4', 'G5', 'G6'], d2=d2)

# exp 6:
cal2(a=300, b=30, pos=['A7', 'A8', 'A9'], d2=d2)
cal2(a=280, b=30, pos=['B7', 'B8', 'B9'], d2=d2)
cal2(a=200, b=30, pos=['C4', 'C5', 'C6'], d2=d2)
cal2(a=100, b=30, pos=['D4', 'D5', 'D6'], d2=d2)
cal2(a=50, b=30, pos=['E4', 'E5', 'E6'], d2=d2)
cal2(a=33, b=30, pos=['F4', 'F5', 'F6'], d2=d2)
cal2(a=25, b=30, pos=['G4', 'G5', 'G6'], d2=d2)

with open('d2.pkl', 'wb') as f:
    pickle.dump(d2, f)

with open('d2.pkl', 'rb') as f:
    d2_new = pickle.load(f)
