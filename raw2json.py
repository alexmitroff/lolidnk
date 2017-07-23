#!/usr/bin/python
import sys
import getopt
import argparse
import re
import json

total_row = 0
help_text = "raw2json.py -i <input file> -o <output file>"

def line2obj(line):
    obj = {}
    obj["time"] = int(line[0])
    obj["type"] = line[1]
    obj["trial"] = int(line[2])
    
    #Raw position for left and right eyes [px]
    obj["l_raw_x"] = float(line[3])
    obj["l_raw_y"] = float(line[4])
    obj["r_raw_x"] = float(line[5]) 
    obj["r_raw_y"] = float(line[6]) 
    
    #Pupil Diameter [mm]
    obj["l_p_d"] = float(line[7])
    obj["r_p_d"] = float(line[8])

    obj["l_por_x"] = float(line[9])
    obj["l_por_y"] = float(line[10])
    obj["r_por_x"] = float(line[11])
    obj["r_por_y"] = float(line[12])
    
    obj["l_gvec_x"] = float(line[13])
    obj["l_gvec_y"] = float(line[14])
    obj["l_gvec_z"] = float(line[15])
    obj["r_gvec_x"] = float(line[16])
    obj["r_gvec_y"] = float(line[17])
    obj["r_gvec_z"] = float(line[18])
    return obj

def readfile(inputfile,outputfile):
    f = open(inputfile, 'r')
    unit = {}
    index = 1 #started from 1 line
    json_index = 0
    for line in f:
        if index > 38: #skip all additional data
            line = re.split(r'\t+', line.rstrip('\t'))
            obj = line2obj(line)
            unit[json_index] = obj
            json_index += 1
            print(index)
        index += 1
    unit = json.dumps(unit)
    j = open(outputfile, 'w')
    j.write(unit)
    j.close()

def main():
    parser = argparse.ArgumentParser(description='Conver txt from BeGaze to json')
    parser.add_argument('-i', help="input file")
    parser.add_argument('-o', help="output file")
    args = parser.parse_args()
    if args.i:
        inputfile = args.i
    else:
        sys.exit(help_text)
    if args.o:
        outputfile = args.o
    else:
        sys.exit(help_text)

    readfile(inputfile, outputfile)
    
    
if __name__ == "__main__":
    main()
