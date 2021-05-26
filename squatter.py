import os
import imgkit
import json
from argparse import ArgumentParser
from wand.image import Image
from subprocess import *
from selenium import webdriver
from selenium.webdriver.chrome.options import *

def getDnstwist(base):
    dnstwist = getoutput('dnstwist/dnstwist.py %s -r -b -f json' % (base))
    json_dnstwist = json.loads(dnstwist)
    return json_dnstwist

def checkSpoofing(base, siti):
    o = Options()
    o.add_argument('--headless')
    o.add_argument('--no-sandbox')
    o.add_argument('--disable-dev-shm-usage')
    #o.add_argument('--disable-gpu')
    #o.add_argument('--disable-extensions')
    DRIVER = 'chromedriver'
    count=1

    driver = webdriver.Chrome(DRIVER,options=o)
    driver.set_window_position(0, 0)
    driver.set_window_size(1024, 768)
    driver.get('http://%s' % (base))
    driver.save_screenshot('tmp/out.png')

    for a in siti[1:]:
            print ("Analyzing website " + a + " (" + str(count) + " on " + str(len(siti)-1) + "): ", end='')
            driver.get('http://%s' % (a))
            driver.save_screenshot('tmp/out1.png')
            with Image(filename='tmp/out.png') as img1:
                    with Image(filename='tmp/out1.png') as img2:
                            a=img1.save(filename='tmp/out.jpg')
                            b=img2.save(filename='tmp/out1.jpg')
                            a=Image(filename='tmp/out.jpg')
                            b=Image(filename='tmp/out1.jpg')
                            result_image, result_metric = a.compare(b,metric='normalized_cross_correlation')
                            print (result_metric)

            if result_metric > 0.50:
                    print("[ALERT] - Spoofed WEB SITE")

            count += 1

    driver.quit()


def main():
    siti = []
    domini = []
    fuzzer = []
    data_set = []
    hyphenation=0
    insertion=0
    omission=0
    repetition=0
    replacement=0
    subdomain=0
    transposition=0
    vowel_swap=0
    addition=0
    bitsquatting=0
    homoglyph=0
    j=0
    parser = ArgumentParser(description="SQUATTER")
    parser.add_argument("sito1", help="Domain to check", metavar="[DOMAIN TO CHECK]", type=str)
    
    args = parser.parse_args()
    base = (args.sito1).strip('\n')

    json_dnstwist = getDnstwist(base)
    
    for d in json_dnstwist:
            try:
                    d["banner-http"]
                    siti.append(d["domain-name"])
            except KeyError:
                    continue
    
    for a in json_dnstwist:
    		domini.append(a["domain-name"])
    
    for b in json_dnstwist:
    	fuzzer.append(b["fuzzer"])

    for i in domini:
        data_set.append({fuzzer[j]:domini[j]})
        j += 1

    for c in fuzzer:
    	if c == "hyphenation":
                    hyphenation += 1
    	if c == "insertion":
                    insertion += 1
    	if c == "omission":
                    omission += 1
    	if c == "repetition":
                    repetition += 1
    	if c == "replacement":
                    replacement += 1
    	if c == "subdomain":
                    subdomain += 1
    	if c == "transposition":
                    transposition += 1
    	if c == "vowel-swap":
                    vowel_swap += 1
    	if c == "addition":
                    addition += 1
    	if c == "bitsquatting":
    		bitsquatting +=1
    	if c == "homoglyph":
    		homoglyph +=1
    
    total = hyphenation + insertion + omission + repetition + replacement + subdomain + transposition + vowel_swap + addition + bitsquatting + homoglyph

    print ("Hyphenation: " + str(hyphenation),end = ' ')
    for i in data_set:
        if 'hyphenation' in i:
            print(i['hyphenation'], end = ' ')
    print()
    print ("Insertion: " + str(insertion),end = ' ')
    for i in data_set:
        if 'insertion' in i:
            print(i['insertion'], end = ' ')
    print()
    print ("Omission: " , str(omission),end = ' ')
    for i in data_set:
        if 'omission' in i:
            print(i['omission'],end = ' ')
    print()
    print ("Repetition: " + str(repetition),end = ' ')
    for i in data_set:
        if 'repetition' in i:
            print(i['repetition'],end = ' ')
    print()
    print ("Replacement: " + str(replacement),end = ' ')
    for i in data_set:
        if 'replacement' in i:
            print(i['replacement'],end = ' ')
    print()
    print ("Subdomain: " + str(subdomain),end = ' ')
    for i in data_set:
        if 'subdomain' in i:
            print(i['subdomain'],end = ' ')
    print()
    print ("Transposition: " + str(transposition),end = ' ')
    for i in data_set:
        if 'transposition' in i:
            print(i['transposition'],end = ' ')
    print()
    print ("Vowel Swap: " + str(vowel_swap),end = ' ')
    for i in data_set:
        if 'vowel-swap' in i:
            print(i['vowel-swap'],end = ' ')
    print()
    print ("Addition: " + str(addition),end = ' ')
    for i in data_set:
        if 'addition' in i:
            print(i['addition'],end = ' ')
    print()
    print ("Bitsquatting: " + str(bitsquatting),end = ' ')
    for i in data_set:
        if 'bitsquatting' in i:
            print(i['bitsquatting'],end = ' ')
    print()
    print ("Homoglyph: " + str(homoglyph),end = ' ')
    for i in data_set:
        if 'homoglyph' in i:
            print(i['homoglyph'],end = ' ')
    print()
    print ("Total: " + str(total))


    if not siti:
        print (str(len(domini)) + " registered web domain have been found. NO domain with an associated HTTP(S) web site")
        exit (0)
    else:
        print (str(len(domini)) + " registered web domain have been found. " + str(len(siti)-1) + " domains have an associated HTTP(S) web site")
    
    checkSpoofing(base, siti) 
    print(domini)

if __name__ == "__main__":
    main()
