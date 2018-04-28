import os
base = 'C:\\USers\\HP\\Desktop\\24'
movieName = ''
titles= ''
newTitles= ''
for folder, subfolders,files in os.walk(base):
    for file in files:

        if file[-4:] == '.mkv' or file[-4:] =='.mp4' or file[-4:] =='.avi':
            movieName = file[:-4]
            addition = file[-4:]
            if movieName=='sample':
                print('This is a sample: ' + movieName)
            print('The name of the movie is: ' + movieName)
            print('The type of file is: '+ addition)
        elif file[-4:] == '.srt':
            titles = file
            newTitles = movieName+ '.srt'
            print('Subs are: ' + titles)
            print('Subs should be called: '+ newTitles)
            # os.rename(titles, newTitles)
        elif file[-4:] != '.srt' and file[-4:] != '.mkv' and file[-4:] !='.mp4' and file[-4:] !='.avi':
            if file[-4:] == '.ini':
                continue
            # os.remove(file)
            print('NOT A MOVIE OR SUBS: ' + file)

    print('')


