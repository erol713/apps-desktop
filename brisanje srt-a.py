import os, shutil
baza = 'C:\\USers\\HP\\Desktop\\cinema2'
novinastavak='.srt'
staroime=''
novoime=''
for folder, subfolders,files in os.walk(baza):
    for file in files:
        if file[-8:]== '.srt.srt':
            staroime = file
            #print('staro ime je: ' + staroime)
            #print('nastavak je: ' + file[-8:])
            novoime = file[:-8] + novinastavak
            #print('novo ime je: '+novoime)
            adresa = os.path.join(folder,file)
            novinaziv = os.path.join(folder, novoime)
            dugoime = os.path.join(folder, staroime)
            print('Preimenovanje foldera "%s" u "%s' % (dugoime, novinaziv))
            #os.rename(dugoime, novinaziv)

