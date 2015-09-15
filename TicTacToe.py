'''
Created on May 12, 2015

@author: Isaac

The MIT License (MIT)

Copyright (c) [2015] [Isaac Nason]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import random
import time
import sys


class Tac:
    
    def __init__(self, Bempty, Bexample, Bmission, gofirst, user, comp, selection, turn, randommove) :
        self.__Bempty = Bempty
        self.__Bexample = Bexample
        self.__Bmission = Bmission
        self.__gofirst = gofirst
        self.__user = user
        self.__comp = comp
        self.__selection = selection
        self.__turn = turn
        self.__randommove = randommove
        
    def emptyboard(self):
        B = self.__Bempty
        print("\t\t*\t*")
        print("\t    " + B[1] + "\t*   " + B[2] + "\t*   " + B[3] +"")
        print("\t\t*\t*")
        print("\t  * * * * * * * * * * *")
        print("\t\t*\t*")
        print("\t    " + B[4] + "\t*   " + B[5] + "\t*   " + B[6] +"")
        print("\t\t*\t*")
        print("\t  * * * * * * * * * * *")
        print("\t\t*\t*")
        print("\t    " + B[7] + "\t*   " + B[8] + "\t*   " + B[9] +"")
        print("\t\t*\t*")
        return "---------------------------------------------------"
    def exampleboard(self):
        B = self.__Bexample
        print("\t\t*\t*")
        print("\t    " + B[1] + "\t*   " + B[2] + "\t*   " + B[3] +"")
        print("\t\t*\t*")
        print("\t  * * * * * * * * * * *")
        print("\t\t*\t*")
        print("\t    " + B[4] + "\t*   " + B[5] + "\t*   " + B[6] +"")
        print("\t\t*\t*")
        print("\t  * * * * * * * * * * *")
        print("\t\t*\t*")
        print("\t    " + B[7] + "\t*   " + B[8] + "\t*   " + B[9] +"")
        print("\t\t*\t*")
        return "---------------------------------------------------"
    
    def gofirst(self):
        print("Computer, who is going first X's or O's?")
        time.sleep(3)
        if self.__gofirst == 1:
            self.__gofirst = "X"
            return "X"
        
        if self.__gofirst == 2:
            self.__gofirst = "O" 
            return "O" 
           
        
    def missionboard(self, Bmission): ### This is the main board
        B = self.__Bmission
        
        print("\t\t*\t*")
        print("\t    " + B[1] + "\t*   " + B[2] + "\t*   " + B[3] +"")
        print("\t\t*\t*")
        print("\t  * * * * * * * * * * *")
        print("\t\t*\t*")
        print("\t    " + B[4] + "\t*   " + B[5] + "\t*   " + B[6] +"")
        print("\t\t*\t*")
        print("\t  * * * * * * * * * * *")
        print("\t\t*\t*")
        print("\t    " + B[7] + "\t*   " + B[8] + "\t*   " + B[9] +"")
        print("\t\t*\t*")
        print("---------------------------------------------------")
        return None
    
    def CompMainMove(self):
        self.__turn = user ### switches to user turn
        u = self.__user ### assigning different variable so don't have to type as much
        C = self.__comp ### I used a cap C because small c brought up an annoying pop-up
        b = self.__Bmission
        r = self.__randommove
        while True:
            ############# AI FOR COMP OFFENSE #############
            # AI for B1
            if (b[1] == " ") and ((b[4] == C and b[7] == C) or (b[5] == C and b[9] == C) or (b[2] == C and b[3] == C)):
                r = 1
                return r
            # AI for B2
            elif (b[2] == " ") and ((b[1] == C and b[3] == C) or (b[5] == C and b[8] == C)):
                r = 2
                return r
            # AI for B3
            elif (b[3] == " ") and ((b[1] == C and b[2] == C) or (b[5] == C and b[7] == C) or (b[9] == C and b[6] == C)):
                r = 3
                return r
            # AI for B4
            elif (b[4] == " ") and ((b[1] == C and b[7] == C) or (b[5] == C and b[6] == C)):
                r = 4
                return r
            # AI for B5
            elif (
                  (b[5] == " ") and ((b[1] == C and b[9] == C) or (b[2] == C and b[8] == C) or (b[3] == C and b[7] == C)
                  or (b[4] == C and b[6] == C)) 
                  ):
                r = 5
                return r
            # AI for B6
            elif (b[6] == " ") and ((b[3] == C and b[9] == C) or (b[4] == C and b[5] == C)):
                r = 6
                return r
            # AI for B7
            elif (b[7] == " ") and ((b[1] == C and b[4] == C) or (b[5] == C and b[3] == C) or (b[8] == C and b[9] == C)):
                r = 7
                return r
            # AI for B8
            elif (b[8] == " ") and ((b[7] == C and b[9] == C) or (b[2] == C and b[5] == C)):
                r = 8
                return r
            # AI for B9
            elif (b[9] == " ") and ((b[1] == C and b[5] == C) or (b[7] == C and b[8] == C) or (b[3] == C and b[6] == C)):
                r = 9
                return r
            
            ######## AI FOR COMP DEFENSE #############
                
            ### AI for B1
            if (b[1] == " ") and ((b[4] == u and b[7] == u) or (b[5] == u and b[9] == u) or (b[2] == u and b[3] == u)):
                r = 1
                return r
            # AI for B2
            elif (b[2] == " ") and ((b[1] == u and b[3] == u) or (b[5] == u and b[8] == u)):
                r = 2
                return r
            # AI for B3
            elif (b[3] == " ") and ((b[1] == u and b[2] == u) or (b[5] == u and b[7] == u) or (b[9] == u and b[6] == u)):
                r = 3
                return r
            # AI for B4
            elif (b[4] == " ") and ((b[1] == u and b[7] == u) or (b[5] == u and b[6] == u)):
                r = 4
                return r
            # AI for B5
            elif (
                  (b[5] == " ") and ((b[1] == u and b[9] == u) or (b[2] == u and b[8] == u) or (b[3] == u and b[7] == u)
                  or (b[4] == u and b[6] == u)) 
                  ):
                r = 5
                return r
            # AI for B6
            elif (b[6] == " ") and ((b[3] == u and b[9] == u) or (b[4] == u and b[5] == u)):
                r = 6
                return r
            # AI for B7
            elif (b[7] == " ") and ((b[1] == u and b[4] == u) or (b[5] == u and b[3] == u) or (b[8] == u and b[9] == u)):
                r = 7
                return r
            # AI for B8
            elif (b[8] == " ") and ((b[7] == u and b[9] == u) or (b[2] == u and b[5] == u)):
                r = 8
                return r
            # AI for B9
            elif (b[9] == " ") and ((b[1] == u and b[5] == u) or (b[7] == u and b[8] == u) or (b[3] == u and b[6] == u)):
                r = 9
                return r
            
            else:
                r = random.randint(1,9)
                if self.__Bmission[r] == " ":
                    return r
                
    def UserMainMove(self):
        self.__turn = comp ### switches to comp's turn
        while True:
            self.__selection = input("Where's your move?: ")
            print()
            if  (
                self.__selection == "1" or self.__selection == "2" or self.__selection == "3" or self.__selection == "4" or 
                self.__selection == "5" or self.__selection == "6" or self.__selection == "7" or self.__selection == "8" or 
                self.__selection == "9"
                ):
                selection = int(self.__selection) ### turned this into an int so I could assign it to Bmission[]
                if self.__Bmission[selection] == "X" or self.__Bmission[selection] == "O":
                    print("Can't move there! Common now!")
                    print()
                    continue
                else:
                    return selection
            else:
                print("Enter a movable number")
                print()
                continue
    
    def WhosTurn(self):
        return self.__turn ### this method grabs who's ever turn it currently is
    def FullBoard(self):
        findclosedspace = [i for i in Bmission if i == "X" or i == "O"] ###Creates new list with all X's and O's already entered
        howmany = len(findclosedspace)
        if howmany == 9:
            return "DONE"
        else:
            return "Not DONE yet"
    def anyonewon(self):
        b = self.__Bmission ### assigning different variable so don't have to type as much
        u = self.__user
        c = self.__comp
        # CHECK IF USER WON
        if  (
            (b[1] == u and b[2] == u and b[3] == u) or (b[4] == u and b[5] == u and b[6] == u) or
            (b[7] == u and b[8] == u and b[9] == u) or (b[1] == u and b[4] == u and b[7] == u) or
            (b[2] == u and b[5] == u and b[8] == u) or (b[3] == u and b[6] == u and b[9] == u) or
            (b[1] == u and b[5] == u and b[9] == u) or (b[7] == u and b[5] == u and b[3] == u)
            ):
            return "u"
        # CHECK IF COMP WON
        elif  (
              (b[1] == c and b[2] == c and b[3] == c) or (b[4] == c and b[5] == c and b[6] == c) or
              (b[7] == c and b[8] == c and b[9] == c) or (b[1] == c and b[4] == c and b[7] == c) or
              (b[2] == c and b[5] == c and b[8] == c) or (b[3] == c and b[6] == c and b[9] == c) or
              (b[1] == c and b[5] == c and b[9] == c) or (b[7] == c and b[5] == c and b[3] == c)
              ):
            return "c"
        else:
            return "ERROR"
        
########### Default Variables ##############
while True: ### This loop is to play the game again if the user wants to
    Bempty = [" "," "," "," "," "," "," "," "," "," "] ### when I tried using Bmission board instead of Bempty I got errors
    Bexample = [" ","1","2","3","4","5","6","7","8","9"] 
    Bmission = [" "," "," "," "," "," "," "," "," "," "]
    gofirst = random.randint(1,2)
    user = " "
    comp = " "
    selection = " "
    turn = user ### by default it's user but will change once game starts
    randommove = 0
    clear = "\n" * 100 ### clears the screen if player wants to play again
############ MAIN ############


    print("Welcome to Isaac's Tic Tac Toe! Enjoy!")
    print()
    
    while True:
        UserInput = input("What would you like to be? X's or O's?: ")
        UserCaps = UserInput.upper()
        if UserCaps == "X":
            print("X's it is!")
            time.sleep(2)
            user = UserCaps
            comp = "O"
            break
        elif UserCaps == "O":
            print("O's it is!")
            time.sleep(2)
            user = UserCaps
            comp = "X"
            break
        else:
            print("Please enter either an X or O")
    print()
    print("Here's the layout and the #'s you'll select:")
     
    x = Tac(Bempty, Bexample, Bmission, gofirst, user, comp, selection, turn, randommove) ################# HERE'S MAIN CLASS CALL
    Exampleboard = x.exampleboard()
    print(Exampleboard)
    while True:
        ready = input("Ready for the computer to randomly select who goes first? 1 yes or 2 no: ")
        if ready == "1":
            print("Let's get to it!")
            break
        elif ready == "2":
            print("No?! It's only fair!")
            continue
        else:
            print("Please enter either a 1 or 2")
    
    ### ACTIVATING GOFIRST FUNCTION IN CLASS ###
    gofirst = x.gofirst()
    print(gofirst) ### randomly generated X or O
    time.sleep(2)
    ### FIRST USER INPUT ON BOARD ###
    if gofirst == user:
            Emptyboard = x.emptyboard() ### Just to show user an empty board for reference ###
            print(Emptyboard)
            firstmove = x.UserMainMove()
            Bmission[firstmove] = user
            firstmove = x.missionboard(Bmission)
            
    elif gofirst == comp:
            compmove = x.CompMainMove()
            Bmission[compmove] = comp
            compmove = x.missionboard(Bmission)
            
    turn = x.WhosTurn()    ###returns who's turn it is
    
    ################## LOOP THAT COMPLETES ALL THE MOVES ################
    while True:
        Done = x.FullBoard() ### checks to see if the board is full
        if Done =="DONE":
            print("Tie...better luck next time")
            print()
            again = input("Play again? 1 YES or 2 NO: ")
            if again == "1":
                print(clear)
                break
            elif again == "2":
                print("Goodbye")
                sys.exit(0)
            else:
                print("Please enter either a 1 or 2")
                continue
        WON = x.anyonewon() ###Checks to see if anyone won. If returns u = user won, c = comp won
        if WON == "u":
            print("WINNER WINNER!!! You won! Congrats!")
            print()
            again = input("Play again? 1 YES or 2 NO: ")
            if again == "1":
                print(clear)
                break
            elif again == "2":
                print("Goodbye")
                sys.exit(0)
            else:
                print("Please enter either a 1 or 2")
                continue
        elif WON == "c":
            print("Got your ass kicked!")
            print()
            again = input("Play again? 1 YES or 2 NO: ")
            if again == "1":
                print(clear)
                break
            elif again == "2":
                print("Goodbye")
                sys.exit(0)
            else:
                print("Please enter either a 1 or 2")
                continue
        if turn == user:
            move = x.UserMainMove()
            print()
            Bmission[move] = user
            move = x.missionboard(Bmission)
            turn = x.WhosTurn() 
            
        elif turn == comp:
            move = x.CompMainMove()
            print()
            Bmission[move] = comp
            move = x.missionboard(Bmission)
            turn = x.WhosTurn() 
    continue
