import os
import shutil
import time
#############################
#         Disclaimer        #
#  this zipper is only for  #
#   ETB Mod Loader - exe    #
#     and its subfiles      #
#############################
old = time.time()
## assume zip and files exists ##
try:os.mkdir("./ETB Mod Loader/")
except Exception as exception:print(exception)
shutil.copy("./dist/ETB Mod Loader.exe", "./ETB Mod Loader/ETB Mod Loader.exe")
shutil.make_archive("ETB Mod Loader", "zip", "./ETB Mod Loader/")
shutil.move("./ETB Mod Loader.zip", "./zipped/ETB Mod Loader.zip")
shutil.rmtree("./ETB Mod Loader")
print("done in " + str(old - time.time()))