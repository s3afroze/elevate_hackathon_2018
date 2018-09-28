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
* Just download the dependencies from the *final_requirements.txt* file.

```
pip install -r requirements.txt

```

* Python 3


## Installing
You can follow the steps below if you dont know how to use the directory and/or github:
1. Click __download or clone__ button above and download in _zip file_. 
2. Unzip the folder in case you are downloading in the __zip form__.

## Setup (30 seconds max)
1. For legality purposes, I can't upload the song files.
2. You need to put the song files in the songs folder.
3. Copy the name of those song files; and put it on the excel file (removing the .mp3 extension).
4. The Machine Learning Model differentiates gender and emotion while the IBM Tone Analyzer API offers only emotion level. 

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
			
2. Type(exclude the quotation marks) __"crontab -e"__ to set a cronjob.
3. Press __"i"__ to go in insert mode.
4. Copy(exclude the quotation marks) __"* * * * * python "__ 
5. Open the folder where you have downloaded this program and go to __Code__ folder.
6. Drag the file __multiplefiles.py__ to the terminal and drop. It is to be noted that there is __space__ between each __*__ and then __space__ after the __5th *__ and then __space__ again before you drop file. It might look something like this: 
> _* * * * * python /Users/Itsacruellife/Desktop/github_projects/automate-my-tabs/Code/multiplefiles.py_
7. Press __esc button__ and copy/write(exclude the quotations) __":wq"__ 
8. Congrats! You are done :smiley:

## How to use?
1. There is a demo.txt file to show how the to add links and set time. __Highly Recommended__
2. Currently, you can set the repeat to __daily,weekends or weekdays__(_updates coming soon for more flexibility_)
3. Create a .txt file.
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









