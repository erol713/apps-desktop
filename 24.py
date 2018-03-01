import os, sys, re
from glob import glob

def promjena(prije , poslije):
    print ('mv  prije: "%s" i  poslije: "%s"' % (prije, poslije))
    #os.rename(prije, poslije) #mjenjanje imena

baza =  'C:\\USers\\HP\\Desktop\\24'

video_files = sorted(glob(os.path.join(baza, '*.mkv')))
sub_files = sorted(glob(os.path.join(baza, '*.srt')))


for videofile, subfiles in zip(video_files, sub_files):
    new_subfile = re.sub(r'\.mkv', '.srt', videofile)
    if subfiles == new_subfile:
        print('%s OK' % (subfiles,))
        continue


    promjena(subfiles, new_subfile)



