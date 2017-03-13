####################################
# grade5.py                        #
#                                  #
# Doug Lloyd                       #
#                                  #
# Last revised: 2017-03-12 20:34   #
####################################

import os

def main():
    
    # list of files this script catches
    recreated_files = ['water', 'mario', 'greedy', 'credit']
    
    # message
    print("Automatically grading Problem Set 5...")
    
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
        
        try:
            os.stat(rootdir + "results/" + directory)
        except:
            os.mkdir(rootdir + "results/" + directory)
            
        # ignore the results directory
        if directory == "results" or directory == ".git" or directory[0] == "_":
            continue
            
        # ignore empty directories
        if not os.listdir(directory):
            continue
            
        # breadcrumbs
        print("Now grading student {}...".format(directory))
        
        # navigate to subdirectory
        os.chdir(directory)
        
        # grade speller
        os.system('git checkout e50b/2017/spring/speller')
        os.system('check50 2016.speller dictionary.c dictionary.h Makefile > ../results/{}/speller.txt'.format(directory))
      
        # back to the parent directory
        os.chdir('..')
        
    print("...grading complete!")
    print("Student reports are now ready in the results/ directory.")

# execute process
if __name__ == "__main__":
    main()
