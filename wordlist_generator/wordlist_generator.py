#!/usr/bin/env python3
#-*-encoding:utf-8*-

from bers3rk import Berserk
import os, sys, argparse
from multiprocessing import Lock, Manager

parser = argparse.ArgumentParser()
parser.add_argument("wordlist", help="The base words to create as a wordlist")
parser.add_argument("outfile", help="The output file to generate")
args = parser.parse_args()

outf = open(args.outfile, "w")
outf.write("password\n")
OUTF_LOCK = Lock()

def fct_try(data, params):
    global OUTF_LOCK
    OUTF_LOCK.acquire(True)
    outf.write(data + "\n")
    OUTF_LOCK.release()
    return False

brute = Berserk(fct_try)
brute.add_word_default_modif()
brute.allow_random_modif()

try:
    brute.run(args.wordlist)
except KeyboardInterrupt:
    os.system("clear")
finally:
    outf.close()
    res = os.popen("wc -l " + args.outfile).read().split(" ")[0]
    print("Created a wordlist of " + str(res) + " words")
