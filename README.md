# QrcodeGenerator

<b>PROJECT TITLE 
QRCodegenerator v1

DESCRIPTION
The QRCode Generator is a GUI program to generate QRCodes based on some user metrics. These metrics are the user's full name, email address, website address and phone number. Furthermore, the program asks the user to input the name of the file with the svg file extension. The current version is version 1.0 but more features will be added soon.
USAGE
STEP 1: When the application loads, you will see the Graphical User Interface (GUI) as shown below:
ADD IMAGE
STEP 2: Input your Full Name, Email Address, Website, and the name of the svg file in each field's respective textbox (See Figure 1 above)
STEP 3: Click the Click to Generate button to generate the file in the current directory where the python file is executed from (Figure 2)

ERROR CORRECTION
As with any good program, each input is checked first before  generating the QRCode.
VERSION UPDATE
The version is QRCode Ver 1 and any update will be shown here.  
DEPLOYMENT
To run this file, make sure that python is installed (Using Python 3.9 or more) and press F5 using IDLE IDE. But any IDE like Visual Studio Code or any IDE will do.
To convert to an executable (.exe), you have two options: 
STEP 1: First install pyinstaller via the command line or terminal by typing...pip install pyinstaller
STEP 2: Type the following in the command line
pyinstaller --onefile --windowed --add-data "xi.icon;" qrcodegenerator.py
STEP 3: Allow pyinstaller to compile the file and add all the resources and dependencies needed to create the executable.
STEP 4: Check the folder and run the exe in another computer. It will successfully run
Alternatively (and even better option), you can use auto-py-to-exe to generate the executable. This normally opens a GUI for compiling your programs. First install auto-py-to-exe by typing the following in the commandline: pip install auto-py-to-exe and then follow the steps as shown below:
ADD IMAGE
Notice that python39.dll was added. This will help run the program in older versions of Windows eg Windows 7, 8, 8.1 (probably they have not been updated for a long time. This will avoid generating errors such as the one shown in issues section). 
ISSUES
Please note that your Windows Defender Antivirus (and some other antimalware programs) may block the application from running. This is a false positive error message. Kindly pause the protection for a while and run again
The dependency python39 must be added to avoid errors such as the one shown below:
ADD IMAGE
The python39 is saved in the AppData folder. As shown in the image below:
ADD IMAGE

