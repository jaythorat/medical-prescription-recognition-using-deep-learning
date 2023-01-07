from PIL import Image
from keras.models import load_model
import numpy as np
import os

# Predict the class of an image
def predict(image_path):
    import os
    cwd = os.getcwd()
    print(cwd)
    folder=f'{cwd}\\sunhacksapp\\models\\'
    model = load_model(f'{folder}\\model50epoach.h5')
    # model = load_model('models/model.h5')
    img = Image.open(image_path).convert('L').resize((28, 28), Image.ANTIALIAS)
    img = np.array(img)
    results =model.predict(img[None,:,:])
    print(np.argmax(results))
    dict = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "G", "7": "H", "8": "I", "9": "J", "10": "K","11": "L", "12": "M", "13": "N", "14": "O", "15": "P", "16": "Q", "17": "R", "18": "S", "19": "T", "20": "U", "21": "V", "22": "W", "23": "X", "24": "Y", "25": "Z"}
    print(dict[str(np.argmax(results))])
    return dict[str(np.argmax(results))]

# def main():
#     prescriptions=[]
#     import os
#     cwd = os.getcwd()
#     print(cwd)
#     folder=f'{cwd}\\sunhacksapp\\result\\characters'
#     flag="1"
#     s=""
#     for filename in os.listdir(folder):
#         if filename.startswith(flag):
#             s+=predict(os.path.join(folder,filename))
#         else:
#             prescriptions.append(s)
#             s=""
#             flag=filename[0]
#     return prescriptions

if __name__ == '__main__':
    predict("sample_images\q.jpg")


