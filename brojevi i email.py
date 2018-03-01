import re
text = " Uprava društva \n " \
       "Kolodvorska br. 12, Tel. 276-691,sastan@sarajevostan.com.ba  \n" \
       "Dispečersko servisni centar hitne intervencije \n" \
       "Paromlinska br.51, Tel. 715-680,servis1@bih.net.ba \n" \
       "TERENSKE SLUZBE CENTAR \n" \
       "Skenderija br.52 Tel. 551-580, 266-980 sgrad.punkt01@bih.net.ba centar.punkt02@bih.net.ba \n" \
       "Dolina br.8 Radno vrijeme: 07:30-15:30 N. SARAJEVO \n" \
       "  E. Šehovića br.9 Tel. 716.111, 716-641 nsarajevo.punkt01@bih.net.ba \n" \
       " E.Šehovića br.9 Radno vrijeme: 07:30-15:30 N.GRAD Ive Andrića br. 1 Tel. 760-880 ngrad.punkt01@bih.net.ba \n" \
       "  Ive Andrića br.1  Radno vrijeme: 07:30-15:30 N.GRAD - DOBRINJA S.Lagumdžije br. 13 Tel. 760-870 "

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?         # pozivni
    (\s|-|\.)?                 # Razmak
    (\d{3})                    # Prva 3 broja
    (\s|-|\.)?                 # Razmak
    (\d{3})                    # Druga 4 broja
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

mailRegex = re.compile(r'''(
                       [a-zA-Z0-9%+-._]+   # username
                       @      #@
                       [a-zA-Z0-9.-]+   # ime domene
                       (\.[a-zA-Z]{2,4})  # tacka nesto
                       )''', re.VERBOSE)
def imenik(text):
    matches =[]
    for groups in phoneRegex.findall(text):
        phone_numbers = '-'.join([groups[1], groups[3], groups[5]])
        matches.append(phone_numbers)
    for groups in mailRegex.findall(text):
        matches.append(groups[0])
    if len(matches) > 0:
        print('Nadjeni brojevi i mailovi su: ')
        print('\n'.join(matches))
imenik(text)