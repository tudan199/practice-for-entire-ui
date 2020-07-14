from utils.HTMLTestRunner import HTMLTestRunner
import unittest
import time


testsuites=unittest.TestSuite()
testcases=unittest.defaultTestLoader.discover('C:/Users/eagle/Desktop/practise/practice for entire ui/testcases','test*.py')
testsuites.addTests(testcases)
filename='C:/Users/eagle/Desktop/practise/practice for entire ui/report/'+str(time.time())+'.html'
title='testreport'
desc="testreports-desc"
with open(filename,'wb') as f:
    runner=HTMLTestRunner(stream=f,title=title,description=desc)
    runner.run(testsuites)
