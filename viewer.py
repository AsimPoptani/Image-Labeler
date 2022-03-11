# importing the tkinter module and PIL that
# is pillow module
from tkinter import *
from traceback import print_tb
# import _tkinter
from PIL import ImageTk, Image
import glob,os
 
 
# Change these
# Classes
classes=['No Glasses','Glasses']

# Directory
dir_path = './lfw/'

# Previous CSV file
previous_csv_filename=None


# Images paths
images_paths=[]
previous_paths=[]
if previous_csv_filename:
    # Read the CSV file
    previous_csv_file=open(previous_csv_filename,'r')
    previous_csv_file=previous_csv_file.readlines()
    if previous_csv_file:
        print("Previous CSV file found")
    # CSV file
        csv_file=previous_csv_filename



    
    for line in previous_csv_file:
        previous_paths.append(line.split(',')[0])
else:
    csv_file = './data.csv'
# Get all images
for filename in glob.iglob(os.path.join(dir_path)+'**/*.jpg', recursive=True):
    images_paths.append(filename)

# Remove previous paths from images paths
for path in previous_paths:
    if path in images_paths:
        images_paths.remove(path)



# Image
current_image=None



# Current index
current_index=0


# Shuffle the images
# import random
# random.shuffle(images_paths)

# If there is no images in the directory then return and exit
if len(images_paths)==0:
    print("No images in the directory")
    exit()

# Check if csv file exists if so then create a new one
while os.path.isfile(csv_file) and not previous_csv_filename:
    
    csv_file=os.path.basename(csv_file).split('.')[0]+'_'+str(int(len(csv_file.split('_')))+1)+'.csv'

file=open(csv_file,'a+')



# Calling the Tk (The initial constructor of tkinter)
root = Tk()
 
def QuitApp():
    file.close()
    root.quit()

# Open the first image
def NextImage():
    global current_image,current_index
    if current_index>=len(images_paths):
        return False
    
    current_image = ImageTk.PhotoImage(Image.open(images_paths[current_index]))
    print(current_image)
    # label=Label(image=current_image)
    label.configure(image=current_image)
    label.image=current_image
    current_index+=1
    return label




# We will make the title of our app as Image Viewer
root.title("Image Viewer")
 
# The geometry of the box which will be displayed
# on the screen
root.geometry("700x700")


 

 
label = Label()
NextImage()
def ProgressImage():
    global label
    a=NextImage()
    if a:
        label=a
    else:
        print("No more images")
        file.close()
        root.quit()

# We have to show the the box so this below line is needed
label.grid(row=1, column=0, columnspan=3)
 
def Press(event):
    try:
        event=int(event)
        print(event,len(classes),images_paths[current_index-1])
        global current_image
        if event<len(classes):
            file.write(images_paths[current_index-1]+','+str(event)+'\n')
            print("hit")
            ProgressImage()
    except Exception as e:
        print(e)

root.bind("<Key>",lambda e: Press(e.char))

for i in range(len(classes)):
    button_class=Button(root, text=classes[i]+f" [{i}]", command=lambda: Press(i))
    button_class.grid(row=6,column=i)
 

 
root.mainloop()