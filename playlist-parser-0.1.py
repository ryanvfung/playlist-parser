# -*- coding: utf-8 -*-
""" iTunes Playlist Parser from m3u to csv
    Version 0.1 release
    @author: Ryan Fung
    Create Date: 2013-10-22
"""


def parsePlaylist(filename):
    file_ = open(filename, "r")
    lines = open(filename).readlines()
    file_.close()
    tracklines = []
    for line in lines:
        if line[:7] == "#EXTINF":
            tracklines.append(line[7:])
    playlist = []
    for trackline in tracklines:
        a = trackline.split(",")[1]
        playlist.append(a.split(" - "))
    csvout = ""
    for entry in playlist:
        entry0 = entry[0]
        entry1 = entry[1].rstrip("\n")
        csvout += entry1 + "," + entry0 + "\n"
    csvout = csvout.replace("\xc3\xab", "\xeb")
    csvout = csvout.replace("Ã«", "\xeb")
    csvout = csvout.replace("Ø", "\xd8")
    csvdirectory = filename.rstrip(filename.split("\\")[-1])
    csvfilename = filename.split("\\")[-1].rstrip("m3u")+"csv"
    csv = open(csvdirectory + csvfilename, "w")
    csv.write(csvout)
    csv.close()
    msg = "----------\n"
    msg += "Parsing Successful. Following playlist copied to csv:\n\n"
    print(msg+csvout)
    return csvout

msg = """Input full playlist location for playlist parsing from m3u into csv:
"""
filename = raw_input(msg)
parsePlaylist(filename)
