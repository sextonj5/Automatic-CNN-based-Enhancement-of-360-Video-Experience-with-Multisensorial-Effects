import torch
from torch.autograd import Variable as V
import torchvision.models as models
from torchvision import transforms as trn
from torch.nn import functional as F
import os
from PIL import Image
import winsound


correct   = 0
incorrect = 0
total = 0
right = [243, 48, 342, 279, 319, 151, 112, 167, 190, 81] #342
accum = [0,0,0,0,0,0,0,0,0,0]
smells =['o','o','o','a','d','o','d','o','o','n']
corrsmell = 0

correct5   = 0
incorrect5 = 0
total5 = 0

device = 'cuda'
# th architecture to use
arch = 'resnet18'
#arch = 'resnet50'
#arch = 'alexnet'

# load the pre-trained weights
model_file = '%s_places365.pth.tar' % arch
if not os.access(model_file, os.W_OK):
    weight_url = 'http://places2.csail.mit.edu/models_places365/' + model_file
    os.system('wget ' + weight_url)

model = models.__dict__[arch](num_classes=365)
checkpoint = torch.load(model_file, map_location=lambda storage, loc: storage)
state_dict = {str.replace(k,'module.',''): v for k,v in checkpoint['state_dict'].items()}
model.load_state_dict(state_dict)
model.to(device)
model.eval()

# load the image transformer
centre_crop = trn.Compose([
        trn.Resize((256,256)),
        trn.CenterCrop(224),
        trn.ToTensor()#,
       # trn.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# load the class label
file_name = 'categories_places365.txt'
if not os.access(file_name, os.W_OK):
    synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/categories_places365.txt'
    os.system('wget ' + synset_url)
classes = list()
with open(file_name) as class_file:
    for line in class_file:
        #classes.append(line.strip().split(' ')[0][3:])
        classes.append(line.strip().split(' '))
classes = tuple(classes)


def Prediction(img):
    input_img = V(centre_crop(img).unsqueeze(0))
    logit = model.forward(input_img.cuda())
    h_x = F.softmax(logit, 1).data.squeeze()
    return h_x

def Split_Prediction_4_Softmax(img):
    # the width and height of the cropped images
    h = int(img.size[0] / 3)
    w = int(img.size[1] / 2)

    # crop the image 6 times adding
    for j in range(0, 3):
        for k in range(0, 2):

            im1 = img.crop((h * (j), w * k, h * (j + 1), w * (k + 1)))

            input_img = V(centre_crop(im1).unsqueeze(0))

            # flip the back face to the right orientation
            if (j == 1 and k == 1):
                angle = 90
                im1 = im1.rotate(angle)

            logit = model.forward(input_img.cuda())
            h_x = F.softmax(logit, 1).data.squeeze()
            if(j == 0 and k == 0):
              h_xtemp = h_x
            elif ((j == 0 or j == 2) and k == 1):
                pass
            else:
              h_xtemp = h_x.add(h_xtemp)
    return h_xtemp

def Split_Prediction(img):

#the width and height of the cropped images
    h = int(img.size[0]/3)
    w = int(img.size[1]/2)


#crop the image 6 times adding 
    for j in range(0,3):
      for k in range(0,2):
      
        im1 = img.crop((h*(j) , w*k, h*(j+1) , w*(k+1)))
      
        input_img = V(centre_crop(im1).unsqueeze(0))
        
        #flip the back face to the right orientation
        #if(j==1 and k==1):
        #  angle = 90
        #  im1 = im1.rotate(angle)
          
        # forward pass
        logit = model.forward(input_img.cuda())
        if(j == 0 and k == 0):
          h_xtemp = logit
        
        #Discard the ground and sky faces of the cube map
        elif((j==0 or j == 2) and k==1):
          pass
        #The other 4 faces get passed through the network
        else:
          h_xtemp = logit.add(h_xtemp)

    #the softmax is applied on the final vector
    h_x = F.softmax(h_xtemp, 1).data.squeeze()
    return h_x


def Split_Prediction_Six_Faces(img):
    # the width and height of the cropped images
    h = int(img.size[0] / 3)
    w = int(img.size[1] / 2)

    # crop the image 6 times adding
    for j in range(0, 3):
        for k in range(0, 2):

            im1 = img.crop((h * (j), w * k, h * (j + 1), w * (k + 1)))

            input_img = V(centre_crop(im1).unsqueeze(0))

            # flip the back face to the right orientation
            if (j == 1 and k == 1):
                angle = 90
                im1 = im1.rotate(angle)

            # forward pass
            logit = model.forward(input_img.cuda())
            if (j == 0 and k == 0):
                h_xtemp = logit
            else:
                h_xtemp = logit.add(h_xtemp)

    # the softmax is applied on the final vector
    h_x = F.softmax(h_xtemp, 1).data.squeeze()
    return h_x

loc =  r"dataset\\sub\\"
for count in range(1,10001):

    img = Image.open(loc +str(count).zfill(9)+".jpg")
    num = int(count/1000);
    if(num == 10):
        num =9

    probs, idx = Split_Prediction(img).sort(0, True)
    #probs, idx = Prediction(img).sort(0, True)
    #probs, idx = Split_Prediction_Six_Faces(img).sort(0, True)
    #probs, idx = Split_Prediction_4_Softmax(img).sort(0, True)

    if(classes[idx[0]][2] == smells[num]):
        corrsmell+=1

    # top1 accuracy
    if (int(idx[0]) == right[num]):
        correct += 1
        total += 1
        accum[num]+=1
    else:
        total += 1
        incorrect += 1

    if (int(idx[0]) == right[num] or int(idx[1]) == right[num] or int(idx[2]) == right[num] or int(idx[3]) == right[
        num] or int(idx[4]) == right[num]):
        correct5 += 1
        total5 += 1
    else:
        total5 += 1
        incorrect5 += 1
    if(count == 10000):
        print(accum)
        print("Top1: " + str(float(correct / total) * 100.0) +'%')
        print("Top5: " + str(float(correct5 / total5) * 100.0) +'%')
        print("Smell: " + str(float(corrsmell / total) * 100.0) + '%')
        print("correct after " + str(total) + " images tested on " + arch)
        print(str(count) + '.jpg')
        # output the prediction
        for i in range(0, 1):
            print('{:.3f} -> {}'.format(probs[i], classes[idx[i]]))
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)