import os
import imageio
import moviepy.editor
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filelocation = askopenfilename()

print('Conversion in progress...')

basename = os.path.basename(filelocation)

filename = os.path.splitext(basename)[0]

video = moviepy.editor.VideoFileClip(filelocation)
audio = video.audio

audio.write_audiofile(filename+".wav")
# print(aud)

print('Conversion Done Successfully!')


#######################################################################################################

import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile(str(filename+'.wav')) as source:
    audio = r.listen(source)
    try:
        text =r.recognize_google(audio)
        print("working on....")
        print(text)
    except:
        print('Sorry... pleaser try again....')


#################################################################
# Python program to find the k most frequent words
# from data set
from collections import Counter

data_set = text

# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(20)

print("The Most Frequently occuring words in the video is : ")
for item in most_occur:
    if len(item[0])>=5:
        print(item)