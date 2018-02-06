import csv
with open('southpark.csv', newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    acc = 0
    L101 = {}
    L102 = {}
    L103 = {}
    L104 = {}
    L105 = {}
    L106 = {}
    L107 = {}
    L108 = {}
    L109 = {}
    L110 = {}
    L111 = {}
    L112 = {}
    L113 = {}
    L114 = {}

    for row in spamreader:
        if row[0] == '10' and row[1] == '1':
            L101[acc] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '2':
            L102[acc - len(L101.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '3':
            L103[acc - len(L101.keys()) - len(L102.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '4':
            L104[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '5':
            L105[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '6':
            L106[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '7':
            L107[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '8':
            L108[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys()) - len(L107.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '9':
            L109[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys()) - len(L107.keys()) - len(L108.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '10':
            L110[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys()) - len(L107.keys()) - len(L108.keys()) - len(L109.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '11':
            L111[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys()) - len(L107.keys()) - len(L108.keys()) - len(L109.keys()) - len(L110.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '12':
            L112[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys()) - len(L107.keys()) - len(L108.keys()) - len(L109.keys()) - len(L110.keys()) - len(L111.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '13':
            L113[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys()) - len(L107.keys()) - len(L108.keys()) - len(L109.keys()) - len(L110.keys()) - len(L111.keys()) - len(L112.keys())] = (row, acc)
            acc += 1
        if row[0] == '10' and row[1] == '14':
            L114[acc - len(L101.keys()) - len(L102.keys()) - len(L103.keys()) - len(L104.keys()) - len(L105.keys()) - len(L106.keys()) - len(L107.keys()) - len(L108.keys()) - len(L109.keys()) - len(L110.keys()) - len(L111.keys()) - len(L112.keys()) - len(L113.keys())] = (row, acc)
            acc += 1








print(L114[0])

