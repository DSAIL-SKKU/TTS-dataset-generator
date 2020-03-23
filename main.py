from subprocess import call
import sys
import argparse
import os
import sys
import shutil

## 파일 이름 받으면 그 폴더 만들어서 저기 저장하게 해야한다.

def yt(url, folder, filename):

    command = 'youtube-dl -o ' + filename +".wav" ' -f bestaudio ' + url
    call(command.split(), shell=False)
    get_into_dir(folder, filename)


def get_into_dir(dirname,filename):
    path = ''                    
    print(os.getcwd())
    dir_name = dirname
    file_name = filename
    if dir_name not in os.listdir(os.getcwd()): #디렉토리가 없을시.
        #print("make new one because that directory is not in here")
        os.mkdir(dirname)
    
    shutil.move(path + file_name + ".wav" , path + dir_name + '/' + file_name+'.wav')
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--url', required=True, help="need")
    parser.add_argument('--folder', required=True, help=":>")
    parser.add_argument('--filename', required=True, help=":>")
    
    args = parser.parse_args()
    yt(args.url, args.folder, args.filename)