import os, re, pexpect, check50, filecmp

# caesar.py
def caesar(target, dest):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("caesar.py\n\n")

    # check if file exists
    if os.path.isfile(target + "/caesar.py"):
        #dest.write("*PASSED* " + '-- caesar.py exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- caesar.py exists\n')
        dest.write('\nCANNOT COMPLETE CAESAR CHECKS\n')
        dest.write("\n+------------------+\n\n")
        return
    
    totalcount += 1
    
    # encrypts 'a' as 'b' using 1 as key
    process = pexpect.spawnu('python3 {}/caesar.py 1'.format(target))
    process.expect('.*')
    process.sendline('a')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'b' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'a\' as \'b\' using 1 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'a\' as \'b\' using 1 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'barfoo' as 'yxocll' using 23 as key
    process = pexpect.spawnu('python3 {}/caesar.py 23'.format(target))
    process.expect('.*')
    process.sendline('barfoo')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'yxocll' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'barfoo\' as \'yxocll\' using 23 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'barfoo\' as \'yxocll\' using 23 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'BARFOO' as 'EDUIRR' using 3 as key
    process = pexpect.spawnu('python3 {}/caesar.py 3'.format(target))
    process.expect('.*')
    process.sendline('BARFOO')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'EDUIRR' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'BARFOO\' as \'EDUIRR\' using 3 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'BARFOO\' as \'EDUIRR\' using 3 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'BaRFoo' as 'FeVJss' using 4 as key
    process = pexpect.spawnu('python3 {}/caesar.py 4'.format(target))
    process.expect('.*')
    process.sendline('BaRFoo')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'FeVJss' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'BaRFoo\' as \'FeVJss\' using 4 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'BaRFoo\' as \'FeVJss\' using 4 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'barfoo' as 'onesbb' using 65 as key
    process = pexpect.spawnu('python3 {}/caesar.py 65'.format(target))
    process.expect('.*')
    process.sendline('barfoo')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'onesbb' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'barfoo\' as \'onesbb\' using 65 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'barfoo\' as \'onesbb\' using 65 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'world, say hello!' as 'iadxp, emk tqxxa!' using 12 as key
    process = pexpect.spawnu('python3 {}/caesar.py 12'.format(target))
    process.expect('.*')
    process.sendline('world, say hello!')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = ' '.join(captured_stdout[len(captured_stdout) - 3:])
    if output != 'iadxp, emk tqxxa!' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'world, say hello!\' as \'iadxp, emk tqxxa!\' using 12 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'world, say hello!\' as \'yiadxp, emk tqxxa!\' using 12 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
   
    # handles lack of argv[1]
    process = pexpect.spawnu('python3 {}/caesar.py'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles lack of argv[1]\n')
    else:
        dest.write("*PASSED* " + '-- handles lack of argv[1]\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    dest.write('\ncaesar.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")

# crack.py
def crack(dest):
    dest.write("crack.py\n\n")
    dest.write('\ncrack.py -- REQUIRES MANUAL EVALUATION\n')
    dest.write("\n+------------------+\n\n")
    
# credit.py
def credit(target, dest):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("credit.py\n\n")
    
    # check if file exists
    if os.path.isfile(target + "/credit.py"):
        #dest.write("*PASSED* " + '-- credit.py exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- credit.py exists\n')
        dest.write('\nCANNOT COMPLETE CREDIT CHECKS\n')
        dest.write("\n+------------------+\n\n")
        return
    
    totalcount += 1
    
    # input of 378282246310005 yields output of AMEX
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('378282246310005')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'AMEX' or process.isalive():
        dest.write("*FAILED* " + '-- input of 378282246310005 yields output of AMEX\n')
    else:
        dest.write("*PASSED* " + '-- input of 378282246310005 yields output of AMEX\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 371449635398431 yields output of AMEX
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('371449635398431')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'AMEX' or process.isalive():
        dest.write("*FAILED* " + '-- input of 371449635398431 yields output of AMEX\n')
    else:
        dest.write("*PASSED* " + '-- input of 371449635398431 yields output of AMEX\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 5555555555554444 yields output of MASTERCARD
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('5555555555554444')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'MASTERCARD' or process.isalive():
        dest.write("*FAILED* " + '-- input of 5555555555554444 yields output of MASTERCARD\n')
    else:
        dest.write("*PASSED* " + '-- input of 5555555555554444 yields output of MASTERCARD\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 5105105105105100 yields output of MASTERCARD
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('5105105105105100')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'MASTERCARD' or process.isalive():
        dest.write("*FAILED* " + '-- input of 5105105105105100 yields output of MASTERCARD\n')
    else:
        dest.write("*PASSED* " + '-- input of 5105105105105100 yields output of MASTERCARD\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 4111111111111111 yields output of VISA
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('4111111111111111')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'VISA' or process.isalive():
        dest.write("*FAILED* " + '-- input of 4111111111111111 yields output of VISA\n')
    else:
        dest.write("*PASSED* " + '-- input of 4111111111111111 yields output of VISA\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 4012888888881881 yields output of VISA
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('4012888888881881')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'VISA' or process.isalive():
        dest.write("*FAILED* " + '-- input of 4012888888881881 yields output of VISA\n')
    else:
        dest.write("*PASSED* " + '-- input of 4012888888881881 yields output of VISA\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 1234567890 yields output of INVALID
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('1234567890')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'INVALID' or process.isalive():
        dest.write("*FAILED* " + '-- input of 1234567890 yields output of INVALID\n')
    else:
        dest.write("*PASSED* " + '-- input of 1234567890 yields output of INVALID\n')
        passcount += 1
    totalcount += 1
    process.kill(0) 
 
    # rejects a non-numeric input of 'foo'
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('foo')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'foo\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'foo\'\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # rejects a non-numeric input of ''
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'\'\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    dest.write('\ncredit.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")
    
# greedy.py
def greedy(target, dest):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("greedy.py\n\n")

    # check if file exists
    if os.path.isfile(target + "/greedy.py"):
        #dest.write("*PASSED* " + '-- greedy.py exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- greedy.py exists\n')
        dest.write('\nCANNOT COMPLETE GREEDY CHECKS\n')
        dest.write("\n+------------------+\n\n")
        return
    
    totalcount += 1

    # input of 0.41 yields output of 4
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('0.41')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '4' or process.isalive():
        dest.write("*FAILED* " + '-- input of 0.41 yields output of 4\n')
    else:
        dest.write("*PASSED* " + '-- input of 0.41 yields output of 4\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 0.01 yields output of 1
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('0.01')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '1' or process.isalive():
        dest.write("*FAILED* " + '-- input of 0.01 yields output of 1\n')
    else:
        dest.write("*PASSED* " + '-- input of 0.01 yields output of 1\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 0.15 yields output of 2
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('0.15')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '2' or process.isalive():
        dest.write("*FAILED* " + '-- input of 0.15 yields output of 2\n')
    else:
        dest.write("*PASSED* " + '-- input of 0.15 yields output of 2\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 1.6 yields output of 7
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('1.6')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '7' or process.isalive():
        dest.write("*FAILED* " + '-- input of 1.6 yields output of 7\n')
    else:
        dest.write("*PASSED* " + '-- input of 1.6 yields output of 7\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 23 yields output of 92
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('23')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '92' or process.isalive():
        dest.write("*FAILED* " + '-- input of 23 yields output of 92\n')
    else:
        dest.write("*PASSED* " + '-- input of 23 yields output of 92\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 4.2 yields output of 18
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('4.2')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '18' or process.isalive():
        dest.write("*FAILED* " + '-- input of 4.2 yields output of 18\n')
    else:
        dest.write("*PASSED* " + '-- input of 4.2 yields output of 18\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # rejects a negative input like -.1
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('-.1')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a negative input like -.1\n')
    else:
        dest.write("*PASSED* " + '-- rejects a negative input like -.1\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects a non-numeric input of 'foo'
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('foo')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'foo\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'foo\'\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # rejects a non-numeric height of ''
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'\'\n')
        passcount += 1
    totalcount += 1
        
    process.kill(0)
    dest.write('\ngreedy.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")

# mario.py
def mario(target, dest):
    less = ""
    more = ""
    lesscount, less = mario_less(target, dest, less)
    morecount, more = mario_more(target, dest, more)
    
    if lesscount >= morecount:
        dest.write(less)
    else:
        dest.write(more)

# mario (less)
def mario_less(target, dest, string):
    passcount, totalcount = 0, 0
    
    # dest.write header
    string += "mario (less comfy)\n\n"
    
    if os.path.isfile(target + '/mario.py'):
        #string += "*PASSED* " + '-- mario.py exists\n'
        passcount += 1
    else:
        string += "*FAILED* " + '-- mario.py exists\n'
        string += '\nCANNOT COMPLETE MARIO CHECKS\n'
        string += "\n+------------------+\n\n"
        return
    
    totalcount += 1
    
    # rejects a height of -1
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('-1')
    if not process.isalive():
        string += "*FAILED* " + '-- rejects a height of -1\n'
    else:
        string += "*PASSED* " + '-- rejects a height of -1\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # handles a height of 0 correctly
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('0')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if '#' in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 0 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 0 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # handles a height of 1 correctly
    output = '''##'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('1')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 1 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 1 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)

    # handles a height of 2 correctly
    output = ''' ##
###'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('2')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 2 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 2 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)

    # handles a height of 23 correctly
    output = '''                      ##
                     ###
                    ####
                   #####
                  ######
                 #######
                ########
               #########
              ##########
             ###########
            ############
           #############
          ##############
         ###############
        ################
       #################
      ##################
     ###################
    ####################
   #####################
  ######################
 #######################
########################'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('23')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 23 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 23 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)

    # rejects a height of 24, then handles a height of 2 correctly
    output = ''' ##
###'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('24')
    process.expect('.*')
    process.sendline('2')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- rejects a height of 24, then accepts a height of 2\n'
    else:
        string += "*PASSED* " + '-- rejects a height of 24, then accepts a height of 2\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects a nonnumeric height of 'foo'
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('foo')
    if not process.isalive():
        string += "*FAILED* " + '-- rejects a non-numeric height of \'foo\'\n'
    else:
        string += "*PASSED* " + '-- rejects a non-numeric height of \'foo\'\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects a nonnumeric height of ''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('')
    if not process.isalive():
        string += "*FAILED* " + '-- rejects a non-numeric height of \'\'\n'
    else:
        string += "*PASSED* " + '-- rejects a non-numeric height of \'\'\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    string += '\nmario.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount)
    string += '\n+------------------+\n\n'   
    
    return passcount, string

# mario (more)
def mario_more(target, dest, string):
    passcount, totalcount = 0, 0
    
    # dest.write header
    string += "mario (more comfy)\n\n"
    
    if os.path.isfile(target + '/mario.py'):
        #string += "*PASSED* " + '-- mario.py exists\n'
        passcount += 1
    else:
        string += "*FAILED* " + '-- mario.py exists\n'
        string += '\nCANNOT COMPLETE MARIO CHECKS\n'
        string += "\n+------------------+\n\n"
        return
    
    totalcount += 1
    
    # rejects a height of -1
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('-1')
    if not process.isalive():
        string += "*FAILED* " + '-- rejects a height of -1\n'
    else:
        string += "*PASSED* " + '-- rejects a height of -1\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # handles a height of 0 correctly
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('0')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if '#' in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 0 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 0 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # handles a height of 1 correctly
    output = '''#  #'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('1')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 1 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 1 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)

    # handles a height of 2 correctly
    output = ''' #  #
##  ##'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('2')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 2 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 2 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)

    # handles a height of 23 correctly
    output = '''                      #  #
                     ##  ##
                    ###  ###
                   ####  ####
                  #####  #####
                 ######  ######
                #######  #######
               ########  ########
              #########  #########
             ##########  ##########
            ###########  ###########
           ############  ############
          #############  #############
         ##############  ##############
        ###############  ###############
       ################  ################
      #################  #################
     ##################  ##################
    ###################  ###################
   ####################  ####################
  #####################  #####################
 ######################  ######################
#######################  #######################'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('23')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- handles a height of 23 correctly\n'
    else:
        string += "*PASSED* " + '-- handles a height of 23 correctly\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects a height of 24, then accepts a height of 2
    output = ''' #  #
##  ##'''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('24')
    process.expect('.*')
    process.sendline('2')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = ''.join([i for i in process.before if i != '\r'])
    if output not in return_data or process.isalive():
        string += "*FAILED* " + '-- rejects a height of 24, then accepts a height of 2\n'
    else:
        string += "*PASSED* " + '-- rejects a height of 24, then accepts a height of 2\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects a nonnumeric height of 'foo'
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('foo')
    if not process.isalive():
        string += "*FAILED* " + '-- rejects a non-numeric height of \'foo\'\n'
    else:
        string += "*PASSED* " + '-- rejects a non-numeric height of \'foo\'\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects a nonnumeric height of ''
    process = pexpect.spawnu('python3 {}/mario.py'.format(target))
    process.expect('.*')
    process.sendline('')
    if not process.isalive():
        string += "*FAILED* " + '-- rejects a non-numeric height of \'\'\n'
    else:
        string += "*PASSED* " + '-- rejects a non-numeric height of \'\'\n'
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    
    string += '\nmario.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount)
    string += '\n+------------------+\n\n'   
    return passcount, string

def smile(target, dest):
    passcount, totalcount = 0, 0

    # dest.write header
    dest.write("smile\n\n")

    # check if file exists
    if os.path.isfile(target + "/smile"):
        #dest.write("*PASSED* " + '-- smile exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- smile exists\n')
        dest.write('\nCANNOT COMPLETE SMILE CHECKS\n')
        dest.write("\n+------------------+\n\n")
        return
    
    totalcount += 1
    
    # analyzes 'love' as ':)'
    output = ':)'
    process = pexpect.spawnu('python3 {}/smile love'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    return_data = process.before
    if output not in return_data or process.isalive():
        dest.write("*FAILED* " + '-- analyzes \'love\' as \':)\'\n')
    else:
        dest.write("*PASSED* " + '-- analyzes \'love\' as \':)\'\n')
        passcount += 1
    process.kill(0)
    totalcount += 1
    
    # analyzes 'hate' as ':('
    output = ':('
    process = pexpect.spawnu('python3 {}/smile hate'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    return_data = process.before
    if output not in return_data or process.isalive():
        dest.write("*FAILED* " + '-- analyzes \'hate\' as \':(\'\n')
    else:
        dest.write("*PASSED* " + '-- analyzes \'hate\' as \':(\'\n')
        passcount += 1
    process.kill(0)
    totalcount += 1
    
    # analyzes 'Stanford' as ':|'
    output = ':|'
    process = pexpect.spawnu('python3 {}/smile Stanford'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    return_data = process.before
    if output not in return_data or process.isalive():
        dest.write("*FAILED* " + '-- analyzes \'Stanford\' as \':|\'\n')
    else:
        dest.write("*PASSED* " + '-- analyzes \'Stanford\' as \':|\'\n')
        passcount += 1
    process.kill(0)
    totalcount += 1
    
    # analyzes 'LOVE' as ':)'
    output = ':)'
    process = pexpect.spawnu('python3 {}/smile LOVE'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    return_data = process.before
    if output not in return_data or process.isalive():
        dest.write("*FAILED* " + '-- analyzes \'LOVE\' as \':)\'\n')
    else:
        dest.write("*PASSED* " + '-- analyzes \'LOVE\' as \':)\'\n')
        passcount += 1
    process.kill(0)
    totalcount += 1
    
    # analyzes 'hAtE' as ':('
    output = ':('
    process = pexpect.spawnu('python3 {}/smile hAtE'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    return_data = process.before
    if output not in return_data or process.isalive():
        dest.write("*FAILED* " + '-- analyzes \'hAtE\' as \':(\'\n')
    else:
        dest.write("*PASSED* " + '-- analyzes \'hAtE\' as \':(\'\n')
        passcount += 1
    process.kill(0)
    totalcount += 1

    # analyzes 'hate love' as ':|'
    #output = ':|'
    #process = pexpect.spawnu('python3 {}/smile "hate love"'.format(target))
    #process.expect([pexpect.EOF, pexpect.TIMEOUT])
    #return_data = process.before
    #if output not in return_data or process.isalive():
    #    dest.write("*FAILED* " + '-- analyzes \'hate love\' as \':|\'\n')
    #else:
    #    dest.write("*PASSED* " + '-- analyzes \'hate love\' as \':|\'\n')
    #    passcount += 1
    #process.kill(0)
    #totalcount += 1
    
    # handles lack of argv[1]
    process = pexpect.spawnu('python3 {}/smile'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles lack of argv[1]\n')
    else:
        dest.write("*PASSED* " + '-- handles lack of argv[1]\n')
        passcount += 1
    process.kill(0)
    totalcount += 1
    
    # handles argc > 2
    process = pexpect.spawnu('python3 {}/smile foo bar'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles argc > 2\n')
    else:
        dest.write("*PASSED* " + '-- handles argc > 2\n')
        passcount += 1
    process.kill(0)
    totalcount += 1
    
    dest.write('\nsmile -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")

# tweets
def tweets(target, dest, config):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("tweets\n\nPlease note that the tweets check will (perhaps falsely) return FAILED if student's format does not match ours exactly!\n")
    dest.write("Please do a double-check before marking in Gradebook if this is the case.\n\n")
    
    # check if files exist
    test_student = os.path.isfile(target + "/tweets")
    staffsolution = "/home/cs50/pset6/tweets"
    test_staff = os.path.isfile(staffsolution)
    if test_student and test_staff:
        #dest.write("*PASSED* " + '-- tweets exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- tweets exists\n')
        dest.write('\nCANNOT COMPLETE TWEETS CHECKS\n')
        dest.write("\n+------------------+\n\n")
        return
    
    totalcount += 1
    
    # set environment variables
    os.environ['API_KEY'] = config['key']
    os.environ['API_SECRET'] = config['secret']
    
    # analyzes @cs50 identical to staff solution
    process = pexpect.spawnu('bash -c \'~cs50/pset6/tweets @cs50\'')
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    f = open('__staff.txt', 'w')
    f.write(process.before)
    process.kill(0)
    process2 = pexpect.spawnu('python3 {}/tweets @cs50'.format(target))
    process2.expect([pexpect.EOF, pexpect.TIMEOUT])
    g = open('__student.txt', 'w')
    g.write(process2.before)
    process2.kill(0)
    f.close()
    g.close()
    
    if filecmp.cmp('__staff.txt', '__student.txt', shallow=False):
        dest.write("*PASSED* " + '-- analyzes @cs50 identical to staff solution\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- analyzes @cs50 identical to staff solution\n')
    totalcount += 1
    
    # analyzes davidjmalan identical to staff solution (no @ symbol)
    process = pexpect.spawnu('bash -c \'~cs50/pset6/tweets davidjmalan\'')
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    f = open('__staff.txt', 'w')
    f.write(process.before)
    process.kill(0)
    process2 = pexpect.spawnu('python3 {}/tweets davidjmalan'.format(target))
    process2.expect([pexpect.EOF, pexpect.TIMEOUT])
    g = open('__student.txt', 'w')
    g.write(process2.before)
    process2.kill(0)
    f.close()
    g.close()
    
    if filecmp.cmp('__staff.txt', '__student.txt', shallow=False):
        dest.write("*PASSED* " + '-- analyzes davidjmalan (no @) identical to staff solution\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- analyzes davidjmalan (no @) identical to staff solution\n')
    totalcount += 1

    
    # analyzes @realdonaldtrump identical to staff solution
    process = pexpect.spawnu('bash -c \'~cs50/pset6/tweets realdonaldtrump\'')
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    f = open('__staff.txt', 'w')
    f.write(process.before)
    process.kill(0)
    process2 = pexpect.spawnu('python3 {}/tweets realdonaldtrump'.format(target))
    process2.expect([pexpect.EOF, pexpect.TIMEOUT])
    g = open('__student.txt', 'w')
    g.write(process2.before)
    process2.kill(0)
    f.close()
    g.close()
    
    if filecmp.cmp('__staff.txt', '__student.txt', shallow=False):
        dest.write("*PASSED* " + '-- analyzes @realdonaldtrump identical to staff solution\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- analyzes @realdonaldtrump identical to staff solution\n')
    totalcount += 1

    # analyzes @hillaryclinton identical to staff solution
    process = pexpect.spawnu('bash -c \'~cs50/pset6/tweets hillaryclinton\'')
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    f = open('__staff.txt', 'w')
    f.write(process.before)
    process.kill(0)
    process2 = pexpect.spawnu('python3 {}/tweets hillaryclinton'.format(target))
    process2.expect([pexpect.EOF, pexpect.TIMEOUT])
    g = open('__student.txt', 'w')
    g.write(process2.before)
    process2.kill(0)
    f.close()
    g.close()
    
    if filecmp.cmp('__staff.txt', '__student.txt', shallow=False):
        dest.write("*PASSED* " + '-- analyzes @hillaryclinton identical to staff solution\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- analyzes @hillaryclinton identical to staff solution\n')
    totalcount += 1


    # handles protected account (i.e., @mikesmith13)
    #process = pexpect.spawnu('python3 {}/tweets mikesmith13'.format(target))
    #process.expect([pexpect.EOF, pexpect.TIMEOUT])
    #return_data = process.before
    #if 'Traceback' in return_data or process.isalive():
    #    dest.write("*PASSED* " + '-- handles protected account (i.e., @mikesmith13)\n')
    #    passcount += 1
    #else:
    #    dest.write("*FAILED* " + '-- handles protected account (i.e., @mikesmith13)\n')
    #process.kill(0)
    #totalcount += 1
    
    # handles lack of argv[1]
    process = pexpect.spawnu('python3 {}/tweets'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles lack of argv[1]\n')
    else:
        dest.write("*PASSED* " + '-- handles lack of argv[1]\n')
        passcount += 1
    process.kill(0)
    totalcount += 1

    # handles argc > 2
    process = pexpect.spawnu('python3 {}/tweets'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT])
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles argc > 2\n')
    else:
        dest.write("*PASSED* " + '-- handles argc > 2\n')
        passcount += 1
    process.kill(0)
    totalcount += 1
    
    process = pexpect.spawnu('rm -f __staff.txt __student.txt')
    
    dest.write('\ntweets -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")
    
# vigenere.py
def vigenere(target, dest):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("vigenere.py\n\n")

    # check if file exists
    if os.path.isfile(target + "/vigenere.py"):
        #dest.write("*PASSED* " + '-- vigenere.py exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- vigenere.py exists\n')
        dest.write('\nCANNOT COMPLETE VIGENERE CHECKS\n')
        dest.write("\n+------------------+\n\n")
        return
    
    totalcount += 1
    
    # encrypts 'a' as 'a' using 'a' as keyword
    process = pexpect.spawnu('python3 {}/vigenere.py a'.format(target))
    process.expect('.*')
    process.sendline('a')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'a' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'a\' as \'a\' using \'a\' as keyword\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'a\' as \'a\' using \'a\' as keyword\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'world, say hello!' as 'xoqmd, rby gflkp!' using 'baz' as keyword
    process = pexpect.spawnu('python3 {}/vigenere.py baz'.format(target))
    process.expect('.*')
    process.sendline('world, say hello!')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = ' '.join(captured_stdout[len(captured_stdout) - 3:])
    if output != 'xoqmd, rby gflkp!' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'world, say hello!\' as \'xoqmd, rby gflkp!\' using \'baz\' as keyword\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'world, say hello!\' as \'xoqmd, rby gflkp!\' using \'baz\' as keyword\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'BaRFoo' as 'CaQGon' using 'BaZ' as keyword
    process = pexpect.spawnu('python3 {}/vigenere.py BaZ'.format(target))
    process.expect('.*')
    process.sendline('BaRFoo')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'CaQGon' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'BaRFoo\' as \'CaQGon\' using \'BaZ\' as keyword\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'BaRFoo\' as \'CaQGon\' using \'BaZ\' as keyword\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'BARFOO' as 'CAQGON' using 'BAZ' as keyword
    process = pexpect.spawnu('python3 {}/vigenere.py BAZ'.format(target))
    process.expect('.*')
    process.sendline('BARFOO')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'CAQGON' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'BARFOO\' as \'CAQGON\' using \'BAZ\' as keyword\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'BARFOO\' as \'CAQGON\' using \'BAZ\' as keyword\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
   
    # handles lack of argv[1]
    process = pexpect.spawnu('python3 {}/vigenere.py'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles lack of argv[1]\n')
    else:
        dest.write("*PASSED* " + '-- handles lack of argv[1]\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # handles argc > 2
    process = pexpect.spawnu('python3 {}/vigenere.py a b c'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles argc > 2\n')
    else:
        dest.write("*PASSED* " + '-- handles argc > 2\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects 'Hax0r2' as keyword
    process = pexpect.spawnu('python3 {}/vigenere.py Hax0r2'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- rejects \'Hax0r2\' as keyword\n')
    else:
        dest.write("*PASSED* " + '-- rejects \'Hax0r2\' as keyword\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    dest.write('\nvigenere.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")
