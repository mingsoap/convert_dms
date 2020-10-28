import csv
from dms2dec.dms_convert import dms2dec
import sys

def convert_lat(dmsstr):
    t = dmsstr[:2] + '.' + dmsstr[2:]
    return dms2dec(t)


def convert_long(dmsstr):
    t = dmsstr[:3] + '.' + dmsstr[3:]
    return dms2dec(t)

def main():
    with open(sys.argv[1], mode='r') as r:
        with open('out_' + sys.argv[1], mode='w', newline='') as w:
            cw = csv.writer(w)
            cr = csv.reader(r)

            for row in cr:
                coor = row[2]
                if not coor:
                    #cw.writerow(['', ''])
                    continue
                print(coor)
                lat, lg = coor.split(' ')

                cw.writerow([convert_lat(lat), convert_long(lg)])
                

if __name__ == '__main__':
    main()