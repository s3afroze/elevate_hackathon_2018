# Bebop.ai

How to improve the emotion of customers calling to call centers? Increasing ROI on call centers and reducing the call times.

## Software Engineer 
* Islam Azeddine Mennouchi 
* Shahzeb Afroze 

## Business & Strategy
* Abdulaziz Chalya 
* Harry Feng 
* Masami Oslon 

## Product Manager
* Eric D'Souza 

## UI/UX
* Christina Park 

## Prerequisites
* Python 3

## Installing
You can follow the steps below if you dont know how to use the directory and/or github:
1. Click __download or clone__ button above and download in _zip file_. 
2. Unzip the folder in case you are downloading in the __zip form__.
3. Just download the dependencies from the *final_requirements.txt* file.
4. Recommended: Create a virtualenv for this program because there are a lot of dependencies. In case you don't know how to create and run a virtual env. Follow the __Creating & Running Virtualenv Demo__ below.

```
pip install -r requirements.txt

``` 
## Creating & Running Virtualenv Demo

* Install the library
```
pip install virtualenv
```
* Creating a virtualenv
```
which python3
```
* Copy the output and replace the __(dir/python3)__
```
virtualenv -p (dir/python3) email_env
```
* Activating the virtualenv
```
source email_env/bin/activate
```
* Setting up the virtualenv for the code.
```
pip install -r final_requirements.txt
```

## Setup
1. For legality purposes, I can't upload the song files.
2. You need to put the song files in the songs folder.
3. Copy the name of those song files; and put it on the excel file (removing the .mp3 extension).
4. The Machine Learning Model differentiates gender and emotion while the IBM Tone Analyzer API offers only emotion level. 
5. The IBM API integration is deleted in this code due to passkey secrecy.
6. Go to __email_invoice.py__ and fill in the login information. It is to be noted that different email client will have varying SMTP. Currrently, it is set up for Gmail.
7. If you are using some other client, you will need to change __server SMTP__ in __email_invoice.py__

| Emotions from ML model | IBM Watson API|
| ---------------------- |:-------------:|
| female_angry           | Joy           |
| female_calm            | Fear          |
| female_fearful         | Sadness       |
| female_happy           | Anger         |
| female_sad             | analytical    |
|                        | confident     |
| male_angry             | tentative     |
| male_calm              |               |
| male_fearful           |               |
| male_happy             |               |
| male_sad               |               |			
			

## How to use?
1. Follow the setup and installing guide. __Highly Recommended__
2. Open terminal and go to the __directory__ of the folder where you downloaded the code.

 ```
 python recognize.py

 ```
3. Run 
4. First line should be the schedule(__set in 24 hours only__) for opening the sites. The formatting for setting time is: __daily/weekends/weekdays@__ time in _24 hours_ with __hours__ and __minuites__ split by __.__.Setting a schedule to open a list of websites at __1pm daily__ will look lke this: 
> __daily@13.00__ 

## Notes
This was done, as I was personally frusrated to regularly open tabs to catch up with sites that I visit regularly. Also, this was a good coding exercise...

## Upcoming updates
1. Chrome Extension
2. Compatibility with python 3x

## Built With
Python 2.7

## Acknowledgments
The resouces that has been the bedrock of my project:

1. [Automate the Boring Stuff with Python written by Al Sweigart.](https://automatetheboringstuff.com/)
2. MIT OpenCourseWare - [MIT course 6.0001](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) taught by Dr. Ana Bell, Prof. Eric Grimson & Prof. John Guttag.

## License
Licensed under GNU General Public License v3.0. - afl-3.0









