# Voice Matters
The WordCloud, Uberblick and Confidence all in one place.... in cardboard boxes.
 
  ******************************************************************************
## HOW TO RUN ALL SCRIPTS

### Cost and Word Count.
	python3 WordCount.py
	python3 CostCounter.py

### Last Word + Confidence
   	/AzureSpeechCC/ dotnet run
   	sudo python3 write_to_screen.py

### WordCloud
   	sudo python3 WordCloudGenerator.py

### Summary, Themes, Haiku and Image
	sudo python3 main.py
   	Then open all the .png files 

  ******************************************************************************
## HOW TO CLONE FROM GITHUB

**1. delete the folder WordCloud on your device**

**2. Make sure that you've got an ssh key on your device**
if not, do following:
The first step involves creating a set of RSA keys for use in authentication.
This should be done on the client.
To create your public and private SSH keys on the command-line:
'''
$ mkdir ~/.ssh
$ chmod 700 ~/.ssh
$ ssh-keygen
'''
You will be prompted for a location to save the keys, and a passphrase for the keys. This passphrase will protect your private key while it's stored on the hard drive:

Generating public/private rsa key pair.
Enter file in which to save the key (/home/b/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/b/.ssh/id_rsa.
Your public key has been saved in /home/b/.ssh/id_rsa.pub.

display your ssh key with following line and copy it

$ cat ~/.ssh/id_rsa.pub

insert your new ssh key into your git account - setting ssh keys

3. clone the git repository with ssh:
```
$ git clone <link> 'WordCloud'
```

NETWORK NAME THAT UBEERBLICKS REMEMBER:

SSID: Uniform Go 5
Password: InUniform

  ******************************************************************************
ADD NEW WIFI CREDENTIALS

To add a wifi network to the WordCLoud follow the instructions on this link:
https://linuxconfig.org/ubuntu-20-04-connect-to-wifi-from-command-line


1. First step is to identify the name of your wireless network interface. To do so execute:

$ ls /sys/class/net
enp0s25  lo  wlp3s0

Depending on your Ubuntu 20.04 system the wireless network interface name would be something like: wlan0 or like in this case it is wlp3s0.

2. Next, navigate to the /etc/netplan directory and locate the appropriate Netplan configuration files. The configuration file might have a name such as 01-network-manager-all.yaml or 50-cloud-init.yaml.

$ ls /etc/netplan/

3. Edit the Netplan configuration file:
   
$ sudoedit /etc/netplan/50-cloud-init.yaml

and insert the following configuration stanza while replacing the SSID-NAME-HERE and PASSWORD-HERE with your SSID network name and password. Make sure that the wifis block is aligned with the above ethernets or version block if present. The entire configuration file may look similar to the one below:

network:
    ethernets:
        eth0:
            dhcp4: true
            optional: true
    version: 2
    wifis:
        wlp3s0:
            optional: true
            access-points:
                "SSID-NAME-HERE":
                    password: "PASSWORD-HERE"
            dhcp4: true

4. Once ready, apply the changes and connect to your wireless interface by executing the bellow command:

$ sudo netplan apply


 ******************************************************************************
LANGUAGE CHANGE

All languages supported are here: https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt-tts

In dataplicity type:
su wordcloud
(enter password - wordcloud)
sudo nano /home/wordcloud/WordCloud/AzureSpeechCC/Program.cs

Now comment/uncomment the language you want using // and delete the // infront of the languages you do not want. Other languages can be added in here easily - see the full list here.


var speechConfig = SpeechConfig.FromSubscription(YourSubscriptionKey, YourServiceRegion);
        // Swiss German
        //speechConfig.SpeechRecognitionLanguage = "de-CH";
        // German
        //speechConfig.SpeechRecognitionLanguage = "de-DE";
        // English
        speechConfig.SpeechRecognitionLanguage = "en-US";



After editing the dotnet file (Program.cs) it first needs to complie, to do this type the following into terminal
dotnet clean
dotnet build
dotnet run

 ******************************************************************************
 AUTO RUN ON STARTUP
 
 This is done using systemd
There are two start-up files:
wordcloud.service
Startup.service

 To edit this file go:
 sudo nano etc/systemd/system/wordcloud.service
 
 Once saved run the following:
 sudo systemctl daemon-reload
 sudo systemctl start wordcloud.service		This runs the run.sh file
 sudo systemctl enable wordcloud.service	This enables the service file to run on startup


To debug it’s useful to look at:
 sudo systemctl status wordcloud.service

		
 
 TO TURN OF AUTO RUN
 
 sudo systemctl stop wordcloud.service		This stops the service file running in terminal
 sudo systemctl disable wordcloud.service	This stops the service file running on startup
 

 ******************************************************************************
GENERAL PROCESS

The run.sh file executes everything.
1. WordCloudGenerator.py .. This reads the contents.txt file, generates a wordcloud, dithers the image to make it E-Ink compatible and finally publishes it to the display.
2. AzureSpeechCC (C#) ..... This launches the speech to text service. The recognized phrases are published to the contents.txt file. The individiual words are send to the PiOLED via a pipe.
3. write_to_oled.py ....... This opens the pipe with AzureSpeechCC and prints the words to the display.
4. reset_button.py ........ This runs a script that deletes the contents.txt file when a button is pushed.
5. WifiStatusLED.py ....... This runs a script to light an LED when connected to the internet.


******************************************************************************
BUGS

initrims Issue fix:
fsck -y /dev/______
exit

 ******************************************************************************
USEFUL COMMANDS FOR DEBUGGING

ps -fA | grep python3 - 		Show all python scripts running
Top					Show all programs running
journalctl -f -u wordcloud.service	Print speech/text and process stuff in terminal

To escape the wordcloud generator in terminal use CTL Z
To escape the other scripts in terminal press CTL C
