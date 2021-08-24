# Automatic-CNN-based-Enhancement-of-360-Video-Experience-with-Multisensorial-Effects

# Installing Software 

1. Install 32-bit java version 8 included which is used to run the Olfaction API

2. Install exhalia drivers contained in the installation folder  

3. run the exhalia server java package using the 32-bit JVM just installed, The IP address of the 
API is 127.0.0.1 and the port is 4000

4. Install the steelseries engine 3 contained in the installation folder, the IP address and port 
for the API is stored in coreprops.json file in the steelseries engine 3 installation folder

the IP addresses and ports of both APIs must be inputted into the test.js file


(for VR headset playback)
Install oculus software and set up headset

In the oculus app navigate to settings>general and check unknown sources

Install firefox extended support, in the headset open firefox extended support and navigate to the hosted webpage

# Mulsemedia Detection

1.  The VideoPrediction.ipynb file in the Olfaction_Haptic Detection directory is used to detect Smell and Haptics in Equiangular Cubemep videos.
2.  You can run this file in Google colab, it will ask for you google log in and a link to the google drive containinig your EAC video
3.  run the cells sequentially, haptic and olfaction JSON files will be created automatically using the Algorithms.
4.  copy the olfaction and Haptic files to their folders inside the mulsemedia players folder.
5.  open a server within this directory on the localhost of your machine.
6.  input the address and port into firefox extended support
7.  playback should commence in the headset.
