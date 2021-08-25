# Automatic-CNN-based-Enhancement-of-360-Video-Experience-with-Multisensorial-Effects

# Installing Software 

1. Install 32-bit java version 8 is used to run the Olfaction API
2. Install exhalia drivers contained in the installation folder  
3. run the exhalia server java package using the 32-bit JVM just installed, The IP address of the 
API is 127.0.0.1 and the port is 4000
4. Install the steelseries engine 3, the IP address and port 
for the API is stored in coreprops.json file in the steelseries engine 3 installation folder

the IP addresses and ports of both APIs must be inputted into the test.js file

(for VR headset playback)
Install oculus software and set up headset

In the oculus app navigate to settings>general and check unknown sources

Install firefox extended support, in the headset open firefox extended support and navigate to the hosted webpage

# Mulsemedia Detection

1.  The VideoPrediction.ipynb file in the "Olfaction_Haptic Detection" directory is used to detect Smell and Haptics in Equiangular Cubemep (EAC) videos.
2.  You can run this file in Google colab or Jupyter Notebook, in Colab it asks for your google log in and a link to the google drive containinig your EAC video. If you are using Jupyter you will have to point to the video yourself and your code will need to be modified slightly to accomplish this.
3.  The code splits the VR video into video and audio components for Haptic and olfaction prediction.
4.  For the video the frames are sampled once per second and they are cropped up into smaller 2-Dimensional tiles, the individual faces of the cubemap. These cubemap faces are passed into a ResNet18 CNN, pretrained on the Places365 Dataset. The algorithm combines the output vectors of the CNN's predictions to form one prediction for 3-Dimensional space. Each of the 365 categories in Places365 has been encoded with a specific smell in the script. 
5.  For the audio we perform a RMS on the signal in time steps of equal length, if the RMS exceeds a calibrated tolerance, Haptic feedback will be played back
6.  Run the cells sequentially, haptic and olfaction JSON files will be created automatically using the Algorithms and saved into the same folder containing the Python script. If you are using Colab you will need to download these to the Mulsemedia player folder, along with the VR video. If you are using Jupyter Notebook you can have everything set up in the same directory so moving files is not necessary.
7.  Open a server within the directory on the host machine containing the JSON files, VR Video and MulseMedia Player.
8.  Input the IP address and port of the server into firefox extended support
9.  Playback should commence in the headset.

# This Project Uses The following Dependencies.

* VideoJS
* Three.js
* webvr-polyfill
* Omnitone
* Videojs-VR By Brandon O'Casey
