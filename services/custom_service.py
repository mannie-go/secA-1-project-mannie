import numpy as np


def calculate(a, b, c, d, x, y):
    # สร้างเมทริกและเวกเตอ
    M = np.array([[a, b], [c, d]])
    v = np.array([x, y])

    #คูณเมทริกกับเวกเตอ
    new_v = M @ v

    #หาdeterminant
    det = np.linalg.det(M)

    #หาinverse (ถ้า det = 0 จะหาไม่ได้)
    if det == 0:
        inv = None
    else:
        inv = np.linalg.inv(M).round(2)

    # สี่เหลี่ยมหนึ่งหน่วย ,สี่เหลี่ยมหลังถูกแปลง
    square = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 1, 1, 0]])
    new_square = M @ square

    return new_v, det, inv, square, new_square