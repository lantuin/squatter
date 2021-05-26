# SQUATTER
SQUATTER finds all occurrences of a given domain and, if a registered domain has an HTTP(S) website, checks if it is similar to the original domain. If similarity is major than 50% then SQUATTER raises an alarm

```
$ python3 squatter.py dark-admin.net
Hyphenation: 0 
Insertion: 0 
Omission:  1 darkadmin.net 
Repetition: 0 
Replacement: 0 
Subdomain: 1 dark-a.dmin.net 
Transposition: 0 
Vowel Swap: 0 
Addition: 0 
Bitsquatting: 0 
Homoglyph: 0 
3 registered web domain have been found. 1 domains have an associated HTTP(S) web site
Analyzing website dark-a.dmin.net (1 on 1): 0.04437761032924999
['dark-admin.net', 'darkadmin.net', 'dark-a.dmin.net']

```

This project is based on the wonderful [DNSTWIST](https://github.com/elceef/dnstwist) project and the [IMGKIT](https://github.com/jarrekk/imgkit) Python library.

## INSTALL

```
$ sudo apt install google-chrome-stable
$ sudo apt install chromedriver
$ git clone https://github.com/lantuin/squatter.git --recurse
$ cd squatter
$ pip3 install -r requirements.txt
```

## CONTAINER (DOCKER/PODMAN)
There is also a Docker/Podman dockerfile to create a container.


### Install docker app

```
$ cd docker
$ podman build -t squatter .
```

### Run the docker app

```
$ podman run -e "DOMAIN=dark-admin.net" localhost/squatter
```

#######################################################################

Thanks to [0xb4db01](https://github.com/0xb4db01) for some coding help!
