####################################
# grade1.py                        #
#                                  #
# Doug Lloyd                       #
#                                  #
# Last revised: 2017-02-08 17:40   #
####################################

import os

def main():
    
    # list of files this script catches
    recreated_files = ['water', 'mario', 'greedy', 'credit']
    
    # message
    print("Automatically grading Problem Set 1...")
    
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
        
        # grade water
        os.system('git checkout cs50/2017/spring/water')
        os.system('check50 2016.water water.c > ../results/{}/water.txt'.format(directory))
      
        # grade mario - less
        os.system('git checkout cs50/2017/spring/mario')
        os.system('check50 2016.mario.less mario.c > ../results/{}/mario-less.txt'.format(directory))
        
        # grade mario - more
        os.system('check50 2016.mario.more mario.c > ../results/{}/mario-more.txt'.format(directory))
        
        # grade greedy
        os.system('git checkout cs50/2017/spring/greedy')
        os.system('check50 2016.greedy greedy.c > ../results/{}/greedy.txt'.format(directory))
        
        # grade credit
        os.system('git checkout cs50/2017/spring/credit')
        os.system('check50 2016.credit credit.c > ../results/{}/credit.txt'.format(directory))
        
        # back to the parent directory
        os.chdir('..')
        
    print("...grading complete!")
    print("Student reports are now ready in the results/ directory.")

# execute process
if __name__ == "__main__":
    main()