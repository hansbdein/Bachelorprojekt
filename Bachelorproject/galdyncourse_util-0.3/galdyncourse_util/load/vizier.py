# vizier.py: download catalogs from Vizier
import sys
import os, os.path
import shutil
import tempfile
from ftplib import FTP
import subprocess
_ERASESTR= "                                                                                "
def vizier(cat,filePath,ReadMePath,
           catalogname='catalog.dat',readmename='ReadMe'):
    """
    NAME:
       vizier
    PURPOSE:
       download a catalog and its associated ReadMe from Vizier
    INPUT:
       cat - name of the catalog (e.g., 'III/272' for RAVE, or J/A+A/... for journal-specific catalogs)
       filePath - path of the file where you want to store the catalog (note: you need to keep the name of the file the same as the catalogname to be able to read the file with astropy.io.ascii)
       ReadMePath - path of the file where you want to store the ReadMe file
       catalogname= (catalog.dat) name of the catalog on the Vizier server
       readmename= (ReadMe) name of the ReadMe file on the Vizier server
    OUTPUT:
       (nothing, just downloads)
    HISTORY:
       2016-09-12 - Written as part of gaia_tools - Bovy (UofT)
       2017-09-12 - Copied to galdyncourse (yes, same day!) - Bovy (UofT)
    """
    _download_file_vizier(cat,filePath,catalogname=catalogname)
    _download_file_vizier(cat,ReadMePath,catalogname=readmename)
    catfilename= os.path.basename(catalogname)
    with open(ReadMePath,'r') as readmefile:
        fullreadme= ''.join(readmefile.readlines())
        if catfilename.endswith('.gz') and not catfilename in fullreadme:
            # Need to gunzip the catalog 
            try:
                subprocess.check_call(['gunzip',filePath])
            except subprocess.CalledProcessError as e:
                print("Could not unzip catalog %s" % filePath)
                raise
    return None

def _download_file_vizier(cat,filePath,catalogname='catalog.dat'):
    sys.stdout.write('\r'+"Downloading file %s from Vizier ...\r" \
                         % (os.path.basename(filePath)))
    sys.stdout.flush()
    try:
        # make all intermediate directories
        os.makedirs(os.path.dirname(filePath)) 
    except OSError: pass
    # Safe way of downloading
    downloading= True
    interrupted= False
    file, tmp_savefilename= tempfile.mkstemp()
    os.close(file) #Easier this way
    ntries= 1
    while downloading:
        try:
            ftp= FTP('cdsarc.u-strasbg.fr')
            ftp.login()
            ftp.cwd(os.path.join('pub','cats',cat))
            with open(tmp_savefilename,'wb') as savefile:
                ftp.retrbinary('RETR %s' % catalogname,savefile.write)
            shutil.move(tmp_savefilename,filePath)
            downloading= False
            if interrupted:
                raise KeyboardInterrupt
        except:
            raise
            if not downloading: #Assume KeyboardInterrupt
                raise
            elif ntries > _MAX_NTRIES:
                raise IOError('File %s does not appear to exist on the server ...' % (os.path.basename(filePath)))
        finally:
            if os.path.exists(tmp_savefilename):
                os.remove(tmp_savefilename)
        ntries+= 1
    sys.stdout.write('\r'+_ERASESTR+'\r')
    sys.stdout.flush()        
    return None
