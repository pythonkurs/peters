from peters.session3 import CourseRepo, change_dir
import sys,os
path = sys.argv[1]
surname = path.split("/")[-1]
cd = change_dir(path)
cm = CourseRepo(surname)
print cm.check()
