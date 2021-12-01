from time import perf_counter
import threading
import time
import SudokuCreater
import matplotlib.pyplot as plt


def puzzle2(a):
    for i in range(0, 9):
        for j in range(0, 9):
            print(a[i][j], end=" ")
        print()
    print()

w = open('veriler.txt', 'w')

eleman = []


def solve(grid, no, row, col, num):
    SudokuCreater.orta()
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    if no == 1:
        if row >= 6 and col >= 6:
            for x in range(9):
                if SudokuCreater.sudoku3[row - 6][x] == num:
                    return False

            for x in range(9):
                if SudokuCreater.sudoku3[x][col - 6] == num:
                    return False

    if no == 2:
        if row >= 6 and col <= 2:
            for x in range(9):
                if SudokuCreater.sudoku3[row - 6][x] == num:
                    return False

            for x in range(9):
                if SudokuCreater.sudoku3[x][col + 6] == num:
                    return False

    if no == 4:
        if row <= 2 and col >= 6:
            for x in range(9):
                if SudokuCreater.sudoku3[row + 6][x] == num:
                    return False

            for x in range(9):
                if SudokuCreater.sudoku3[x][col - 6] == num:
                    return False

    if no == 5:
        if row <= 2 and col <= 2:
            for x in range(9):
                if SudokuCreater.sudoku3[row + 6][x] == num:
                    return False

            for x in range(9):
                if SudokuCreater.sudoku3[x][col + 6] == num:
                    return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Sudo(grid, no, row, col):
    if (row == 9 - 1 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Sudo(grid, no, row, col + 1)
    for num in range(1, 9 + 1, 1):

        if solve(grid, no, row, col, num):

            grid[row][col] = num

            if Sudo(grid, no, row, col + 1):
                eleman.append('')
                w.write("Sudoku Numarasi: %d, Row: %d, Col: %d, Yeni Rakam: %d\n" % (no, row, col, num))
                return True
        grid[row][col] = 0
    return False

"""
def SolUst():
    if (Sudo(SudokuCreater.sudoku1, 1, 0, 0)):
        SudokuCreater.orta()
        print("Sol Üst Sudoku Çözüldü")
    else:
        print("Sol Üst Sudoku Çözülemedi")


def SagUst():
    if (Sudo(SudokuCreater.sudoku2, 2, 0, 0)):
        SudokuCreater.orta()
        print("Sağ Üst Sudoku Çözüldü")
    else:
        print("Sağ Üst Sudoku Çözülemedi")


def SolAlt():
    if (Sudo(SudokuCreater.sudoku4, 4, 0, 0)):
        SudokuCreater.orta()
        print("Sol Alt Sudoku Çözüldü")
    else:
        print("Sol Alt Sudoku Çözülemedi")


def SagAlt():
    if (Sudo(SudokuCreater.sudoku5, 5, 0, 0)):
        SudokuCreater.orta()
        print("Sağ Alt Sudoku Çözüldü")
    else:
        print("Sağ Alt Sudoku Çözülemedi")


def Orta():
    if (Sudo(SudokuCreater.sudoku3, 3, 0, 0)):
        SudokuCreater.orta()
        print("Orta Sudoku Çözüldü")
    else:
        print("Orta Sudoku Çözülemedi")
"""

def final():
    a = input("5'li thread için 1, 10'lu thread için 2 giriniz...  ")
    if a == '1':
        basla = perf_counter()

        tSOU = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku1, 1, 0, 0))
        tSAU = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku2, 2, 0, 0))
        tSOA = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku4, 4, 0, 0))
        tSAA = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku5, 5, 0, 0))
        tO = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku3, 3, 0, 0))

        tSOU.start()
        tSAU.start()
        tSOA.start()
        tSAA.start()

        tSOU.join()
        tSAU.join()
        tSOA.join()
        tSAA.join()

        tO.start()
        tO.join()

        puzzle2(SudokuCreater.sudoku1)
        puzzle2(SudokuCreater.sudoku2)
        puzzle2(SudokuCreater.sudoku3)
        puzzle2(SudokuCreater.sudoku4)
        puzzle2(SudokuCreater.sudoku5)

        bit = perf_counter()
        print(f'Çözüm Süresi = {round(bit - basla, 3)}, Eleman Sayısı = {len(eleman)} ')

        if SudokuCreater.checker(SudokuCreater.sudoku1):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku2):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku3):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku4):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku5):
            print("Çözüm Yok Tekrar Başlatınız")
            return False

        x = [0, round(bit - basla, 3)]
        y = [0, len(eleman)]
        plt.plot(x, y)
        plt.xlabel("Geçen Süre")
        plt.ylabel("Eleman Sayısı")
        plt.show()

        return True

    elif a == '2':
        basla = perf_counter()

        tSOU = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku1, 1, 0, 0))
        tSOU2 = threading.Thread(target=Sudo   , args =(SudokuCreater.sudoku1, 1, 6, 2))

        tSAU = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku2, 2, 0, 0))
        tSAU2 = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku2, 2, 0, 4))

        tSOA = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku4, 4, 0, 0))
        tSOA2 = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku4, 4, 2, 0))

        tSAA = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku5, 5, 0, 0))
        tSAA2 = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku5, 5, 5, 2))

        tO = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku3, 3, 0, 0))
        tO2 = threading.Thread(target=Sudo  ,args =(SudokuCreater.sudoku3, 3, 4, 6))

        tSOU.start()
        tSOU2.start()
        tSAU.start()
        tSAU2.start()
        tSOA.start()
        tSOA2.start()
        tSAA.start()
        tSAA2.start()

        tSOU.join()
        tSOU2.join()
        tSAU.join()
        tSAU2.join()
        tSOA.join()
        tSOA2.join()
        tSAA.join()
        tSAA2.join()


        tO.start()
        tO2.start()

        tO.join()
        tO2.join()

        puzzle2(SudokuCreater.sudoku1)
        puzzle2(SudokuCreater.sudoku2)
        puzzle2(SudokuCreater.sudoku3)
        puzzle2(SudokuCreater.sudoku4)
        puzzle2(SudokuCreater.sudoku5)

        bit = perf_counter()
        print(f'Çözüm Süresi = {round(bit - basla, 3)}, Eleman Sayısı = {len(eleman)} ')

        if SudokuCreater.checker(SudokuCreater.sudoku1):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku2):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku3):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku4):
            print("Çözüm Yok Tekrar Başlatınız")
            return False
        if SudokuCreater.checker(SudokuCreater.sudoku5):
            print("Çözüm Yok Tekrar Başlatınız")
            return False

        x = [0, round(bit - basla, 3)]
        y = [0, len(eleman)]
        plt.plot(x, y)
        plt.xlabel("Geçen Süre")
        plt.ylabel("Eleman Sayısı")
        plt.show()

        return True





