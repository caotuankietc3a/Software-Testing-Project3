import sys
sys.path.append("./utils/")
sys.path.append("./tests/")

def main():
    from LoginUtils import LoginSite
    from TestCourse import TestCreateCourse, TestRemoveCourse
    LoginSite.logIn()
    for i in range(1, 8):
        try:
            expectedOutput = TestCreateCourse.run_test(i)
            if expectedOutput == "Add new Course successfully":
                TestRemoveCourse.run_test()
        except Exception as e:
            raise e
    LoginSite.logOut()

if __name__ == "__main__":
    main()
