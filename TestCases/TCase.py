# 1. This way is easier to import all classes.
# import Library.CommonModule
#
# objA = Library.CommonModule.A()
# objA.startBrowser()

# 2. This way is easier but only import a specific class
# from Library.CommonModule import A
# objA = A()
# objA.startBrowser()

#3 Import classes from another folders
import Pages.Login.ABC
objA = Pages.Login.ABC.C()
objA.myTesting()
