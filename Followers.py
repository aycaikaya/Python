import xlrd
from tkinter.filedialog import askopenfilename

def path():
    p=askopenfilename()
    return p

def part():
    p=path()
    workbook=xlrd.open_workbook(p)
    worksheet=workbook.sheet_by_index(0)
    parts=[]
    for i in range(9, 21):
        party = worksheet.cell_value(10, i)
        parts.append(party)
    return parts
def dists():
    path1=path()
    wb=xlrd.open_workbook(path1)
    ws=wb.sheet_by_index(0)
    di=[]
    for i in range(11, 50):
        district = ws.cell_value(i, 2)
        di.append(district)
    return di
print(dists())
def check():
    path1=path()
    parties=part()
    districts=dists()
    whole={}
    workbook=xlrd.open_workbook(path1)
    worksheet=workbook.sheet_by_index(0)
    vote1 = []
    vote2 = []
    vote3 = []
    vote4 = []
    vote5 = []
    vote6 = []
    vote7 = []
    vote8 = []
    vote9 = []
    vote10 = []
    vote11 = []
    vote12 = []
    for i in range(11,50):
        vote_saadet=worksheet.cell_value(i,9)
        vote_btp=worksheet.cell_value(i,10)
        vote_tkp=worksheet.cell_value(i,11)
        vote_vatan=worksheet.cell_value(i,12)
        vote_bbp=worksheet.cell_value(i,13)
        vote_chp=worksheet.cell_value(i,14)
        vote_ak=worksheet.cell_value(i,15)
        vote_dp=worksheet.cell_value(i,16)
        vote_mhp=worksheet.cell_value(i,17)
        vote_iyi=worksheet.cell_value(i,18)
        vote_hdp=worksheet.cell_value(i,19)
        vote_dsp=worksheet.cell_value(i,20)
        vote1.append(vote_saadet)
        vote2.append(vote_btp)
        vote3.append(vote_tkp)
        vote4.append(vote_vatan)
        vote5.append(vote_bbp)
        vote6.append(vote_chp)
        vote7.append(vote_ak)
        vote8.append(vote_dp)
        vote9.append(vote_mhp)
        vote10.append(vote_iyi)
        vote11.append(vote_hdp)
        vote12.append(vote_dsp)

    whole[parties[0]] = vote1
    whole[parties[1]] = vote2
    whole[parties[2]] = vote3
    whole[parties[3]] = vote4
    whole[parties[4]] = vote5
    whole[parties[5]] = vote6
    whole[parties[6]] = vote7
    whole[parties[7]] = vote8
    whole[parties[8]] = vote9
    whole[parties[9]] = vote10
    whole[parties[10]] = vote11
    whole[parties[11]] = vote12

    return whole
#print(check())

def check2():
    path1=path()
    parties=part()
    districts=dists()
    workbook=xlrd.open_workbook(path1)
    worksheet=workbook.sheet_by_index(0)
    whole={}
    vote1 = []
    vote2 = []
    vote3 = []
    vote4 = []
    vote5 = []
    vote6 = []
    vote7 = []
    vote8 = []
    vote9 = []
    vote10 = []
    vote11 = []
    vote12 = []

    for i in range(11,50):
        vote_saadet=worksheet.cell_value(i,9)
        vote_btp=worksheet.cell_value(i,10)
        vote_tkp=worksheet.cell_value(i,11)
        vote_vatan=worksheet.cell_value(i,12)
        vote_bbp=worksheet.cell_value(i,13)
        vote_chp=worksheet.cell_value(i,14)
        vote_ak=worksheet.cell_value(i,15)
        vote_dp=worksheet.cell_value(i,16)
        vote_mhp=worksheet.cell_value(i,17)
        vote_iyi=worksheet.cell_value(i,18)
        vote_hdp=worksheet.cell_value(i,19)
        vote_dsp=worksheet.cell_value(i,20)
        vote1.append(vote_saadet)
        vote2.append(vote_btp)
        vote3.append(vote_tkp)
        vote4.append(vote_vatan)
        vote5.append(vote_bbp)
        vote6.append(vote_chp)
        vote7.append(vote_ak)
        vote8.append(vote_dp)
        vote9.append(vote_mhp)
        vote10.append(vote_iyi)
        vote11.append(vote_hdp)
        vote12.append(vote_dsp)
    vote=[vote1,vote2,vote3,vote4,vote5,vote6,vote7,vote8,vote9,vote10,vote11,vote12]
    whole[parties[0]] = vote1
    whole[parties[1]] = vote2
    whole[parties[2]] = vote3
    whole[parties[3]] = vote4
    whole[parties[4]] = vote5
    whole[parties[5]] = vote6
    whole[parties[6]] = vote7
    whole[parties[7]] = vote8
    whole[parties[8]] = vote9
    whole[parties[9]] = vote10
    whole[parties[10]] = vote11
    whole[parties[11]] = vote12
    for k in parties:
        for val in range(0,39):
                whole[k][val]=districts[val]
    print(whole)
check2()

