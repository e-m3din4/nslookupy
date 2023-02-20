#!/usr/bin/python3

import socket

#   NSLookupy
### Author: Edgar Medina, 2023.
##  Based on the python core module and socket function, which is used for networking,
##  also can be used to resolve domain names and retrieve IPs linked to a given domain. Script takes as input a text files contained the domains listed to resolve and the output is a text file including hosts and IPs, related to the domains lsited.

sourcefile = 'sourcefile.txt' #file with domain names
outfile = 'results.txt' #file to write the IP addresses

with open(sourcefile, 'r') as inputf:
    #This opens the sourcefile in read mode to see what are the domains


    with open(outfile, 'a') as outputf:
        #This opens the outfile in append mode to write the results


        domains = inputf.readlines()
        #This reads all the domains in sourcefile line by line


        for domain in domains:
            #This for loop will go one by one on domains.


            domain = domain.strip("\n")
                #as the every domain in the file are in newline,
                #the socket function will have trouble, so strip off the newline char


            try:
                resolution = (socket.getaddrinfo(domain, port=80,type=2))
                for ip in resolution:
                    outputf.write(str(ip[4][0])+" "+domain+ " www."+domain+"\n" )
            except:
                outputf.write("Could not resolve "+domain+" www."+domain+"\n")
                #getaddinfo("domain") gets all the IP addresses.
