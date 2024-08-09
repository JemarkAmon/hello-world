#!/usr/bin/env python3

"""
Name: CheckLab2.py
Author: Andrew Oatley-Willis
Date: November 2, 2016

Updated: September 12, 2019 by Raymond Chan
Reason: (1) for Python version 3.6.8
        (2) add report header with user and system information

Updated: September 25, 2019 by Raymond Chan
Reason: (1) add Linux system version to report header

Usage:
hheck all sections for the labs
./CheckLab2-1 -f -v 
Check a specific lab section
./CheckLab2-1 -f -v lab2x 

Description:
This script is used to give students more feedback, progress, and
assistance while working on labs. Labs and this script should be 
in the same directory. Labs must use the correct naming scheme for
each file(eg. lab2a.py, lab2b.py, ...).


"""

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request
import socket
import time

class lab2a(unittest.TestCase):
    """All test cases for lab2a - variables & printing"""

    def test_0(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - variables & printing - Test for file creation: ./lab2a.py"""
        error_output = 'your file cannot be found (HINT: make sure the CheckLab2.py script AND your lab files are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2a.py'), msg=error_output)
    
    def test_1(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - variables & printing - Test for errors running: ./lab2a.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with an error (HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_2(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - variables & printing - Test for correct shebang line: ./lab2a.py"""
        lab_file = open('./lab2a.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'lab2a.py does not have the correct shebang line (HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_3(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - variables & printing - Test for correct output: ./lab2a.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hi Jon, you are 20 years old.\n'
        error_output = 'output is not correct (HINT: pay attention to uppercase letters, spaces, and punctuation)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab2b(unittest.TestCase):
    """All test cases for lab2b - variables & printing & input"""
    
    def test_0(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - using input() function - Test for file creation: ./lab2b.py"""
        error_output = 'your file cannot be found (HINT: make sure your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2b.py'), msg=error_output)
   
    def test_1(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - using input() - Test for errors with sending input "Jon" "20": ./lab2b.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate(input=b'Jon\n20\n')
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your script exited with an error (HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_2(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - using input() - Test for correct shebang line: ./lab2b.py"""
        lab_file = open('./lab2b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your script does not have a correct shebang line (HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_3(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - using input() - Test output with sending input "Jon" "20": ./lab2b.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate(input=b'Jon\n20\n')
        # Fail test if output is different from expected_output
        expected_output = b'Name: Age: Hi Jon, you are 20 years old.\n'
        error_output = 'output is not correct (HINT: pay attention to spelling, uppercase letters, spaces, and punctuation)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_4(self):
        """[Lab 2] - [Investigation 1] - [Part 1] - using input() - Test output with sending input "Jen" "25": ./lab2b.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate(input=b'Jen\n25\n')
        # Fail test if output is different from expected_output
        expected_output = b'Name: Age: Hi Jen, you are 25 years old.\n'
        error_output = 'output is not correct (HINT: we are matching "Jen" and "25" now, take a look at python function input()'
        self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab2c(unittest.TestCase):
    """All test cases for lab2c - using command line arguments"""
    
    def test_0(self):
        """[Lab 2] - [Investigation 1] - [Part 2] - command line arguments - Test for file creation: ./lab2c.py"""
        error_output = 'your file cannot be found (HINT: make sure your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2c.py'), msg=error_output)
    
    def test_1(self):
        """[Lab 2] - [Investigation 1] - [Part 2] - command line arguments - Test for errors with 2 args: ./lab2c.py Jon 20"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2c.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with an error (HINT: try running your script to see the error)'
        self.assertEqual (return_code, 0, msg=error_output)
    
    def test_2(self):
        """[Lab 2] - [Investigation 1] - [Part 2] - command line arguments - Test for correct shebang line: ./lab2c.py"""
        lab_file = open('./lab2c.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your script does not have a correct shebang line (HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_3(self):
        """[Lab 2] - [Investigation 1] - [Part 2] - command line arguments - Test output for: ./lab2c.py Jon 20"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2c.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hi Jon, you are 20 years old.\n'
        error_output = 'output is not correct (HINT: must use the sys.argv list, do not forget to import sys)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_4(self):
        """[Lab 2] - [Investigation 1] - [Part 2] - command line arguments - Test output for: ./lab2c.py Jen 25"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2c.py', 'Jen', '25' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hi Jen, you are 25 years old.\n'
        error_output = 'output is not correct (HINT: must use the sys.argv list, do not forget to import sys)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab2d(unittest.TestCase):
    """All test cases for lab2d - arguments & if statements"""
    
    def test_0(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test for file creation: ./lab2d.py"""
        error_output = 'your script cannot be found (HINT: make sure AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2d.py'), msg=error_output)
    
    def test_1(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test for errors with 0 args: ./lab2d.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_2(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test for correct shebang line: ./lab2d.py"""
        lab_file = open('./lab2d.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a correct shebang line (HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_3(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test for errors: ./lab2d.py Jon"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py', 'Jon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_4(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test for errors: ./lab2d.py Jon 20"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with an error (HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_5(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test for errors: ./lab2d.py Jon 20 More"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py', 'Jon', '20', 'More' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with an error (HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_6(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test output with 0 args: ./lab2d.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Usage: ./lab2d.py name age\n'
        error_output = 'wrong usage message for 0 args (HINT: use if statements for catching conditions, such as 0 arguments)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_7(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test output with 1 args: ./lab2d.py Jon"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py', 'Jon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Usage: ./lab2d.py name age\n'
        error_output = 'wrong usage message for 1 args(HINT: use if and elif statements for catching conditions, such as 1 argument)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_8(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test output with 2 args: ./lab2d.py Jon 20"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hi Jon, you are 20 years old.\n'
        error_output = 'wrong output for correct number of args'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_9(self):
        """[Lab 2] - [Investigation 2] - [Part 1] - sys.argv and if - Test output with 3 args: ./lab2d.py Jon 20 More"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2d.py', 'Jon', '20', 'More' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Usage: ./lab2d.py name age\n'
        error_output = 'wrong usage message for 3 args(HINT: use the > or < signs in if statements, test for more then 2 arguments)'
        self.assertEqual(stdout, expected_output, msg=error_output)

class lab2e(unittest.TestCase):
    """All test cases for lab2e - while loops"""
    
    def test_0(self):
        """[Lab 2] - [Investigation 3] - [Part 1] - while loop with timer 10 - Test for file creation: ./lab2e.py"""
        error_output = 'your file cannot be found (HINT: make sure your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2e.py'), msg=error_output)

    def test_1(self):
        """[Lab 2] - [Investigation 3] - [Part 1] - while loop with timer 10 - Test for errors: ./lab2e.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2e.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_2(self):
        """[Lab 2] - [Investigation 3] - [Part 1] - while loop with timer 10 - Test for correct shebang line: ./lab2e.py"""
        lab_file = open('./lab2e.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_4(self):
        """[Lab 2] - [Investigation 3] - [Part 1] - while loop with timer 10 - Test for output: ./lab2e.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2e.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output (HINT: pay attention to the last number that is displayed, is it a 1 or a 0?)'
        self.assertEqual(stdout, expected_output, msg=error_output)

class lab2f(unittest.TestCase):
    """All test cases for lab2f - while loops & sys.argv"""
    
    def test_0(self):
        """[Lab 2] - [Investigation 3] - [Part 2] - while loops & sys.argv - Test for file creation: ./lab2f.py"""
        error_output = 'your file cannot be found (HINT: make sure file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2f.py'), msg=error_output)

    def test_1(self):
        """[Lab 2] - [Investigation 3] - [Part 2] - while loops & sys.argv - Test for errors with with 0 arguments): ./lab2f.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2f.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = '(HINT: this script should only be run with a argument)'
        self.assertEqual(return_code, 1, msg=error_output)
    
    def test_2(self):
        """[Lab 2] - [Investigation 3] - [Part 2] - while loops & sys.argv - Test for correct shebang line: ./lab2f.py"""
        lab_file = open('./lab2f.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your script does not have a correct shebang line (HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_4(self):
        """[Lab 2] - [Investigation 3] - [Part 2] - while loops & sys.argv - Test for errors: ./lab2f.py 10"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2f.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your script exited with an error (HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_5(self):
        """[Lab 2] - [Investigation 3] - [Part 2] - while loops & sys.argv - Test for errors: ./lab2f.py 5"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2f.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your script exited with an error (HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_6(self):
        """[Lab 2] - [Investigation 3] - [Part 2] - while loops & sys.argv - Test output with: ./lab2f.py 10"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2f.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output (HINT: check you script output carefully)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_7(self):
        """[Lab 2] - [Investigation 3] - [Part 2] - while loops & sys.argv - Test output with: ./lab2f.py 5"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2f.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: check you script output carefully)'
        self.assertEqual(stdout, expected_output, msg=error_output)


class lab2g(unittest.TestCase):
    """All test cases for lab2g - while loops & sys.argv & if statements"""
    
    def test_0(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test for file creation: ./lab2g.py"""
        error_output = 'your file cannot be found (HINT: make sure your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2g.py'), msg=error_output)

    def test_1(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test for errors: ./lab2g.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2g.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with an error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_2(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test for correct shebang line: ./lab2g.py"""
        lab_file = open('./lab2g.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your script does not have a correct shebang line (HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
 
    def test_4(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test for errors: ./lab2g.py 5"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2g.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your script exited with an error (HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_5(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test for errors: ./lab2g.py 10"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2g.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your script exited with an error (HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_6(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test output with no arguments: ./lab2g.py"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2g.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: should loop 3 times by default )'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_7(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test output with: ./lab2g.py 5"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2g.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: should loop 5 times.)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_8(self):
        """[Lab 2] - [Investigation 3] - [Part 3] - while loops, sys.argv & if - Test output with: ./lab2g.py 10"""
        # Run students program
        p = subprocess.Popen([sys.executable, './lab2g.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: should loop 10 times)'
        self.assertEqual(stdout, expected_output, msg=error_output)

class lab2out(unittest.TestCase):
    """If lab2 output exists, verify the git email"""
    
    def test_0(self):
        """[Lab 2 Output and Email Verification]"""
        error_output = 'Make sure you are using your myseneca email address for git. Hint: run git config --global user.email "yoursenecaid@myseneca.ca" in your terminal.'
        if os.path.exists('./laboutput.txt'):
            with open('./laboutput.txt') as f:
                output = f.read()
            self.assertIn('@myseneca.ca', output, msg=error_output)
        else:
            assert True

def ChecksumLatest(url=None):
    dat = ''
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            dat = dat + line
    checksum = hashlib.sha256(dat.encode('utf-8')).digest()
    #print("internet", checksum)
    return checksum

def ChecksumLocal(filename=None):
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.sha256(textdata.encode('utf-8')).digest()
    #print("local", checksum)
    return checksum

def CheckForUpdates():
    try:
        lab_name = 'CheckLab2.py'
        lab_num = 'lab2'
        print('Checking for updates...')
        if ChecksumLatest(url='https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for this' + lab_name + ' please consider updating:')
            print(' cd ~/ops445/' + lab_num + '/')
            print(' pwd  #   <-- i.e. confirm that you are in the correct directory')
            print(' rm ' + lab_name)
            print(' ls ' + lab_name + ' || wget https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name)
            print()
            return
        print('Running latest version...')
        return
    except:
        # Cleanly skip updating if any errors occur for offline or matrix issues
        print('No connection made...')
        print('Skipping updates...')
        return

def github_email():
    cmd = 'git config --get user.email'
    try:
        out = os.popen(cmd).read().strip()
    except:
        out = 'none found'
    return out

def displayReportHeader():
    report_heading = 'OPS445 Lab Report - System Information for running '+sys.argv[0]
    print(report_heading)
    print(len(report_heading) * '=')
    import getpass
    print('    User login name:', getpass.getuser())
    print('    Git Email:', github_email())
    print('    Linux system name:', socket.gethostname())
    print('    Python executable:',sys.executable)
    print('    Python version: ',sys.version)
    print('    OS Platform:',sys.platform)
    print('    Working Directory:',os.getcwd())
    print('    Start at:',time.asctime())
    print(len(report_heading) * '=')
    return

if __name__ == '__main__':
    # CheckForUpdates()
    # wait = input('Press ENTER to run the Lab Check ...')

    if len(sys.argv) == 3:
         x = displayReportHeader()

    unittest.main()


