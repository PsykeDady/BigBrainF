#!/bin/python3

######################################################################
# BigBrainFuck - brainfuck code generator and compiler
#
# Author  = Davide Galati (aka PsykeDady)
# email   = psdady@msn.com
# version = 0.1
######################################################################
# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

def b2t(s):
        data=[0]*len(s) #caso peggiore
        ptr=0
        n=0
        ris=""
        while n < len(s):
                i=s[n]
                try: n= s.index(']',n) if i=='[' and data[ptr]==0  else len(s)-s[::-1].index('[',len(s)-n) if i==']' and data[ptr]!=0 else  n+1 
                except: pass
                ptr=ptr+1 if i=='>' else ptr-1 if  i=='<'  else ptr
                data[ptr]= data[ptr]+1 if i=='+' else data[ptr]-1 if i=='-' else ord(input()[0])-ord('0') if i==',' else data[ptr]
                if i=='.': ris=ris+chr(data[ptr])
        #while
        return ris
#b2t

if "__main__"==__name__ : 
	modality=["stdin","arg"]
	mstdin=modality.index("stdin")
	marg=modality.index("arg")

	mode=modality[mstdin]
	#print(str(modality)+' '+str(mstdin)+' '+str(marg)+' '+str(mode)+' '+str(sys.argv)+' '+str(len(sys.argv)))
	debugga=0
	arg=""
	for i in sys.argv[1::]:
		if i=="-d" or i=="--debug":
			print("[debug mode enabled]")
			debugga=1
		else :
			if debugga==1:
				print(
					"[DEBUG] arg="+arg+"\n"+
					"[DEBUG] i"+i+"\n");
			mode=modality[marg]
			arg=arg+i
	#for
	if debugga==1:
		print("[DEBUG] mode="+mode);
	if mode==modality[mstdin] :
		if debugga==1:
			print("[DEBUG] input mode");
		print("b2t",end=":>")
		arg=input()
	#if

	print(b2t(arg));
#main

