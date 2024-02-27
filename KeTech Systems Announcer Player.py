from playsound import playsound
import time
Message = 1
while True: 
    res = ''
    rec = ''
    recs = ''
    recss = ''
    rece = ''
    reces = ''
    res1 = ''
    rec1 = ''
    recs1 = ''
    recss1 = ''
    rece1 = ''
    reces1 = ''
    res2 = ''
    rec2 = ''
    recs2 = ''
    recss2 = ''
    rece2 = ''
    reces2 = ''
    print("hello world")
    file = open("DATLST.TXT", "r")
    line = file.readlines()
    print(line)
    s = ''.join(line)
    
    if(Message < 10):
        sub1 = "MES" + "00" + str(Message) + ":"
    
    if(Message < 100 and Message > 9):
        sub1 = "MES" + "0" + str(Message) + ":"
    
    if(Message < 1000 and Message > 99):
        sub1 = "MES" + str(Message) + ":"


    sub2 = "DW	0FFFFH"
    try:
        res = ''.join(s.split(sub1)[1].split(sub2)[0])
        rec = res.rstrip().splitlines()
        recs = ''.join(rec[0])
        recss = recs
        rece = recss.lstrip()
        reces = rece[3:]
        announce = reces
    except:
        print("Unused")
    try:
        recs1 = ''.join(rec[1])
        recss1 = recs1
        rece1 = recss1.lstrip()
        reces1 = rece1[3:]
        announce1 = reces1
    except:
        print("no second line!")
        announce1 = ""
    try:
        recs2 = ''.join(rec[2])
        recss2 = recs2
        rece2 = recss2.lstrip()
        reces2 = rece2[3:]
        announce2 = reces2
    except:
        print("no third line!")
        reces2 = ""
    try:
        print(reces + ",")
    except:
        print("cant print 0")
    try:
        print(reces1 + ",")
    except:
        print("cant print 1")
    try:
        print(reces2)
    except:
        print("cant print 2")
    announcement = reces
    try:
        announcement += "," + reces1
    except:
        print("cant add 1")
    try:
        announcement += "," + reces2
    except:
        print("cant add 2")

    print("final announcement:")
    print("")
    announcementList = announcement.split(",")
    print(announcementList)
    for i in announcementList:
        try:
            if(i[:1] != "G"):
                playsound('C:\\Users\\William.locket\\Downloads\\LU Northen Line announcements 2019 (1)\\LU Northen Line announcements 2019\\NL\\NL AA 20150804 v9B\\NL AA 20150804 v9B\\' + i + '.wav')
            print(i[:1])
            if(i[:1] == "G"):
                time.sleep((int(i[1:]) / 1000))
        except:
            print("Announcement Finished!")
    file.close()
    Message += 1