# Course-Registration-Bot

## What is this project?
This project was created after my friends asked if I could code something to help them get into their classes. Initially, I wasn't sure, but after some research, I had a basic working prototype by the end of the day.

## How does it work?
It works by using a library called Selenium which allows you to open a Chrome browser that you can control using Python code. Then I have it search for the course registration page, and spam the refresh button until the registration page opens. Once the registration is open it instantly enters the class codes you entered and hits submit.

## How to use it?
1. Download the required packages
2. Open Terminal and go to where you saved the file
3. Then run the following command: python courseReg.py [Your UVM netID] [Your UVM Password] [List your class codes with spaces between each]
4. Then hit enter and let the code do its magic!

## Results
So far it has a 100% success rate getting me and my friend into all of our classes. My friend even had only 3 spots in a few of the classes and got into all of them using the bot. When typically that would be near impossible.

## Selenium
- https://www.selenium.dev/
