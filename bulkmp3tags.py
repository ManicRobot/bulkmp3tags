""#!/usr/bin/env python

import argparse
import mutagen
import os


const = {}
values = {"title": "Title: ", "artist": "Artist: ", "tracktotal": "Total Tracks: ", "tracknumber": "Track Number: ", "album": "Album: ", "album_artist": "Album Artist: ", "date": "Date (year): "}
parser = argparse.ArgumentParser(description='Edit audio tags of many files at once.')
verbose = False

if os.name is 'nt':
    wd = os.getcwd() + '\\'
else:
    wd = os.getcwd() + '/'


def v_print(text, bypass=False):
    if verbose:
        print('[V] ' + text)
        return True
    elif bypass:
        print('[V] ' + text)
        return True
    return False


def welcome():
    global const
    global wd
    print("Welcome to BulkMP3Tags.")
    print("This tool allows you to edit the tags of many audio files at once.")
    print("Please remind that this tool will edit the tags of ALL audio files in " + str(wd))
    print("---------------------------")
    print("Before we begin to edit tags, you can define some constant values.")
    print("Constant values remain the same for all of the audio files.")
    print("If you don't want a value to be constant, just skip that value.")
    const['title'] = input("Constant Title: ")
    const['artist'] = input("Constant Artist: ")
    const['tracktotal'] = input("Constant Total Tracks: ")
    const['tracknumber'] = input("Constant Track Number: ")
    const['album'] = input("Constant Album: ")
    const['album_artist'] = input("Constant Album Artist: ")
    const['date'] = input("Constant Date (year): ")
    print("Alright. Now we go through all the audio files in the working directory and you can manually edit the non-constant values for each file.")
    print("Before changing a file, you will be asked, if you want to change them at all.")
    #file_list = next(os.walk(wd))[1]
    #file_list = (x for x in Path(wd) if x.is_file())
    file_list = os.listdir(wd)
    for x in file_list:
        if os.path.isdir(x):
            file_list.remove(x)
    v_print(str(file_list))
    print("---------------------------")
    for f in file_list:
        edit_tags(wd + f)
        print("---------------------------")


def edit_tags(file_path):
    yn = input("Do you want to edit '" + file_path + "'? (Y/n): ")
    if yn is '' or yn is 'y' or yn is 'Y' or yn is None:
        audio_file = mutagen.File(file_path)
        if audio_file is None:
            v_print("Skipping " + file_path + " because it's not an audio file.")
        else:
            print("Editing " + file_path + "...")
            for v in values:
                if const[v] is None or const[v] is '':
                    meta_input = input(values[v])
                    audio_file[v] = str(meta_input)
                else:
                    v_print(v + " is constant.")
                    audio_file[v] = str(const[v])
            print("Completed editing of '" + file_path + "'.")
            choice = input("Are you sure you want to save? (Y/n): ")
            if choice is '' or yn is 'y' or yn is 'Y' or yn is None:
                v_print(audio_file.pprint())
                audio_file.save()
            else:
                print("Discarding changes...")
    else:
        print("Skipping " + file_path + " because you denied editing it.")



def init_arguments():
    global parser

    parser.add_argument('-v', '--verbose',
                        help='Enables verbose mode for more information', action='store_true')
    parser.add_argument('-wd', '--working-directory',
                        help='Overwrites the working directory from CWD to the given directory',
                        metavar='DIRECTORY')
    args = parser.parse_args()
    args_dict = vars(args)  # Put all the arguments into a dict

    if 'verbose' in args_dict:
        global verbose
        verbose = True
    if 'working_directory' in args_dict:
        if os.path.isdir(args_dict['working_directory']):
            global wd
            if args_dict['working_directory'].endswith('/') and os.name is 'posix':
                wd = args_dict['working_directory']
            elif os.name is 'posix':
                wd = args_dict['working_directory'] + '/'
            if args_dict['working_directory'].endswith('\\') and os.name is 'nt':
                wd = args_dict['working_directory']
            elif os.name is 'nt':
                wd = args_dict['working_directory'] + '\\'

        else:
            v_print('Error parsing --working-directory. Using CWD.')


if __name__ == '__main__':
    from sys import argv
    init_arguments()
    v_print('Verbose mode is active.')
    welcome()
