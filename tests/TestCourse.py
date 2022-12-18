import time, os
import unittest
from utils.CourseUtils import CreateCourseUtils, RemoveCourseUtils
from utils.FileUtils import readTestCaseFromFile, readSolutionFromFile
from selenium.webdriver.common.keys import Keys


TEST_DIR = "./tests/testcases/"
SOL_DIR = "./tests/solutions/"
class TestCreateCourse():
    @staticmethod
    def run_test(number):
        pathTest = os.path.join(TEST_DIR, str(number) + ".txt");
        pathSolution = os.path.join(SOL_DIR, str(number) + ".txt");
        data = readTestCaseFromFile(pathTest)
        expectedOutput = readSolutionFromFile(pathSolution)
        CreateCourseUtils.test(data[0], data[1], data[2], data[3], data[4])
        print(expectedOutput)
        return expectedOutput;

class TestRemoveCourse():
    @staticmethod
    def run_test():
        RemoveCourseUtils.test()
