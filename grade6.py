####################################
# grade6.py                        #
#                                  #
# Brahm Gardner                    #
# Jason Hirschhorn                 #
# Doug Lloyd                       #
#                                  #
# Last revised: 2016-10-24 18:05   #
####################################

import os, check50

def main():
    
    # list of files this script catches
    recreated_files = ['caesar', 'crack', 'credit', 'greedy', 'mario', 'vigenere']
    
    # message
    print("Automatically grading Problem Set 6...")
    
    # set the root to be the current directory
    rootdir = './'

    # get a list of all student directories in the root
    directories = [d for d in os.listdir(rootdir) if os.path.isdir(os.path.join(rootdir, d))]
    
    # create a results directory if you don't already have one
    try:
        os.stat(rootdir + "results")
    except:
        os.mkdir(rootdir + "results") 
        
    # iterate over those directories
    for directory in directories:
        
        # ignore the results directory
        if directory == "results" or directory == ".git":
            continue
        
        # start a file for this student's check50 output
        f = open(rootdir + "results/" + directory + ".txt", "w")
        f.write("+------------------+\n\n")
        
        # breadcrumbs
        print("Now grading student {}...".format(directory))
        
        # see which files are there
        for target in recreated_files:
            if os.path.isfile(rootdir + directory + "/" + target + ".py"):
                if target == "greedy":
                    check50.greedy("{}{}".format(rootdir, directory), f)
                elif target == "caesar":
                    check50.caesar("{}{}".format(rootdir, directory), f)
                elif target == "credit":
                    check50.credit("{}{}".format(rootdir, directory), f)
                elif target == "vigenere":
                    check50.vigenere("{}{}".format(rootdir, directory), f)
                elif target == "mario":
                    check50.mario("{}{}".format(rootdir, directory), f)

        # close the file you're working on
        f.close()
        
    print("...grading complete!")

# execute process
if __name__ == "__main__":
    main()
