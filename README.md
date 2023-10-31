[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Bp585G7b)

## Client-Server Application Using Socket Programming

## Description: 

There exists a client program designed to establish connections with one of three distinct server programs upon execution. Upon receiving user input in the form of a numerical value, the connected server programs undertake the task of doubling the provided number and displaying the result. The client program operates dynamically, randomly transitioning its connection to one of the available servers during its runtime. Program is written in python programming language.

## Guide:

You can watch one-minute tutorial video how can you run the program from scratch. Or read the below guide.

https://www.youtube.com/watch?v=ztDKavceQ7M&feature=youtu.be

Python is cross-platform programming language, and code itself checked in case of any portability issues. Code should work on most of the operating systems like macOS and Linux in the same way. 

```diff 
+ How to install? 
```

To run the application, you need to have python installed on your computer (latest versions reccommended, like python3.11). You can install it from here. https://www.python.org/downloads/

Install project's repository (ex. in zip format) from github. You can use this link:  https://github.com/ADA-GWU/understanding-the-systems-with-complex-connections-aliamrahli
(click green "code" button and download zip)


```diff 
+ How to compile?
```

Open 4 different terminal windows, and navigate to the folder's location. The server programs run on port numbers 5000,5001, and 5002. You need to pass it as an argument to the server program. Type following command in three terminal windows to run the servers.

python server.py 5000 (for one of the server)

python server.py 5001 (for second server)

python server.py 5002 (for third server)

On fourth terminal window run the client program using following command:

python client.py

```diff 
+ How to run?
```

After compiling, client program will randomly connect to the one of the server programs, you will see "Successfully connected" message on that terminal. Then client program will ask you for an input. This program works with digits, so if you put any strings which contains non-digit character, program will say to add only digits. After adding your input as a number, the server program that you connected will print the double of that number. You can stop the connection from particular server using "exit" keyword. After stopping all the servers client program will also stop. 










