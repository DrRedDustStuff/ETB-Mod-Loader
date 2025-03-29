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
shutil.copy("./dist/ETB Mod Loader.exe", "./ETB Mod Loader/ETB Mod Loader.exe")
shutil.make_archive("ETB Mod Loader", "zip", "./ETB Mod Loader/")
shutil.move("./ETB Mod Loader.zip", "./zipped/ETB Mod Loader.zip")
print("done in " + str(time.time() - old))