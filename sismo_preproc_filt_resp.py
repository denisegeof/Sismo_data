import matplotlib.pyplot as plt
import os
import obspy
from obspy import UTCDateTime
from obspy import read


#####################################################################################
# Programa baseado em Obspy para remover a resposta do sismógrafo com arquivo RESP  #
# e decimar o dado. Três componentes HHN, HHE e HHZ.                                #
# Por Denise Moura: denise.moura@usp.br                                             #
#####################################################################################


filewrite = list ()

# searchfiles faz uma lista com endereço/nome dos arquivos que contenham HH? no nome e sejam .SAC
def searchfiles(namepart):
    with open("filenames.txt", "w") as filewrite:
        for r, d, f in os.walk("./FRTB_sismo"): #pasta com sismogramas
            direc = str(r)
            for file in f:
                if file.__contains__(namepart) and file.endswith('SAC'):
                    filewrite.write(direc + "/" + file + "\n")

# prepara entrada do seedresp
pre_filt = (0.007, 0.01, 0.1, 0.2)   # define a filter band to prevent amplifying noise during the deconvolution

date = UTCDateTime("2018-01-1T00:00:00.000")  # this can be the date of your raw data or any date for which the RESP-file is valid

# Remove resposta do instrumento para as três componentes
#HHE
searchfiles('HHE')
with open('filenames.txt', 'r') as f:
    for line in f:
        st = read(line[:-1])     # tira o \n

        #remove mean trend 
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)
    
        respf = ("./FRTB_resp/RESP.BL.FRTB..HHE") #caminho e nome do RESP file

        seedresp = {'filename': respf,  # RESP filename
                    'date': date,
                    'units': 'DIS' # Units to return response in ('DIS', 'VEL' or ACC)
                    }

        # Remove instrument response using the information from the given RESP file
        st.simulate(paz_remove=None, pre_filt=pre_filt, seedresp=seedresp)

        name = line[:-1]+".disp" 
        st.write(name, format="SAC")  #salva arquivo corrigido com outro nome, só para teste

        #remove mean trend 
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)

        #Decimate data
        st.decimate(7, strict_length=False, no_filter=False)
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)
        st.decimate(7, strict_length=False, no_filter=False)

        name = line[:-1]+".dec"
        st.write(name, format="SAC") #salva arquivo decimado com outro nome

#HHN
searchfiles('HHN')
with open('filenames.txt', 'r') as f:
    for line in f:
        st = read(line[:-1])

        #remove mean trend 
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)
    
        respf = ("./FRTB_resp/RESP.BL.FRTB..HHN")

        seedresp = {'filename': respf,  # RESP filename
                    'date': date,
                    'units': 'DIS'      # Units to return response in ('DIS', 'VEL' or ACC)
                    }

        # Remove instrument response using the information from the given RESP file
        st.simulate(paz_remove=None, pre_filt=pre_filt, seedresp=seedresp)  

        name = line[:-1]+".disp"
        st.write(name, format="SAC")

        #remove mean trend 
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)

        #Decimate data
        st.decimate(7, strict_length=False, no_filter=False)
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)
        st.decimate(7, strict_length=False, no_filter=False)

        name = line[:-1]+".dec"
        st.write(name, format="SAC")

        

#HHZ
searchfiles('HHZ')
with open('filenames.txt', 'r') as f:
    for line in f:
        st = read(line[:-1])

        #remove mean trend 
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)
    
        respf = ("./FRTB_resp/RESP.BL.FRTB..HHZ")

        seedresp = {'filename': respf,  # RESP filename
                    'date': date,
                    'units': 'DIS'       # Units to return response in ('DIS', 'VEL' or ACC)
                    }

        # Remove instrument response using the information from the given RESP file
        st.simulate(paz_remove=None, pre_filt=pre_filt, seedresp=seedresp)

        name = line[:-1]+".disp"
        st.write(name, format="SAC")

        #remove mean trend 
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)

        #Decimate data
        st.decimate(7, strict_length=False, no_filter=False)
        st.detrend(type="demean")
        st.detrend(type="linear")
        st.taper(max_percentage=0.05)
        st.decimate(7, strict_length=False, no_filter=False)

        name = line[:-1]+".dec"
        st.write(name, format="SAC")
