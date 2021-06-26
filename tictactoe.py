# https://www.codechef.com/MAY21C/problems/TCTCTOE

T = int(input())

for i in range(T):
    row1 = input()
    row2 = input()
    row3 = input()
    rows = [row1, row2, row3]
    
    Xsol = 0
    Osol = 0
    
    for i in range(3):
        if (rows[i].count("X") == 3):
            Xsol = 1
        if (rows[i].count("O") == 3):
            Osol = 1

    # test for vertical soln
    if (rows[0][0] == 'X' and rows[1][0] == 'X' and rows[2][0] == 'X'):
        Xsol = 1
    if (rows[0][1] == 'X' and rows[1][1] == 'X' and rows[2][1] == 'X'):
        Xsol = 1
    if (rows[0][2] == 'X' and rows[1][2] == 'X' and rows[2][2] == 'X'):
        Xsol = 1
    if (rows[0][0] == 'O' and rows[1][0] == 'O' and rows[2][0] == 'O'):
        Osol = 1
    if (rows[0][1] == 'O' and rows[1][1] == 'O' and rows[2][1] == 'O'):
        Osol = 1
    if (rows[0][2] == 'O' and rows[1][2] == 'O' and rows[2][2] == 'O'):
        Osol = 1
    # print(" horizontal SOl; ", soln)
    
    # print("vertical SOl; ", soln, "X: ", Xsol, "Osol: ", Osol)
        
    # test for diagonal soln
    if (rows[0][0] == 'X' and rows[1][1] == 'X' and rows[2][2] == 'X'):
        Xsol = 1
    if (rows[0][2] == 'X' and rows[1][1] == 'X' and rows[2][0] == 'X'):
        Xsol = 1
    if (rows[0][0] == 'O' and rows[1][1] == 'O' and rows[2][2] == 'O'):
        Osol = 1
    if (rows[0][2] == 'O' and rows[1][1] == 'O' and rows[2][0] == 'O'):
        Osol = 1
    # print("diagonal SOl; ", soln, "X: ", Xsol, "Osol: ", Osol)
                
                
                
    Xs = rows[0].count("X") + rows[1].count("X") + rows[2].count("X")
    Os = rows[0].count("O") + rows[1].count("O") + rows[2].count("O")
    _s = rows[0].count("_") + rows[1].count("_") + rows[2].count("_")
    
    # print("Xs: ",Xs, "Os: ", Os, "_S: ", _s)
    if ((Xsol == 1 and Osol == 1) or (Xs - Os < 0) or (Xs - Os> 1) ):
        print("3")
        continue
    if (Xs == 0 and Os == 0 and _s == 9):
        print("2")
        continue
    if (Xsol == 1 and Osol == 0 and Xs > Os):
        print("1")
        continue
    if (Xsol == 0 and Osol == 1 and Xs == Os):
        print("1")
        continue
    if (Xsol == 0 and Osol == 0 and _s == 0):
        print("1")
        continue
    if (Xsol == 0 and Osol == 0 and _s > 0):
        print("2")
        continue
    print("3") 