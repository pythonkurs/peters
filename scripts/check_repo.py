from peters.session3 import CourseRepo, change_dir
import sys,os

@profile
def main(argvs):
	path = argvs[1]
	surname = path.split("/")[-1]
	cd = change_dir(path)
	cm = CourseRepo(surname)
	print cm.check()

if __name__ == '__main__':
    main(sys.argv)
