import os
import json
import shutil
import time
start_time = time.time()
jsn = json.loads(open("./PYBuilder/build.json").read())
save_as = jsn.get("save-as")
try:
    os.mkdir(f"./{save_as}/")
    shutil.copytree("./files/",f"./{save_as}/files/")
except Exception as exception:print(f"[Sub] [Zipper] {exception}")
with open(f"./{save_as}/{save_as}.exe", 'w') as file:
    file.close()
shutil.copy(f"./dist/{save_as}.exe", f"./{save_as}/{save_as}.exe")
shutil.make_archive(f"{save_as}", "zip", f"./{save_as}/")
shutil.move(f"./{save_as}.zip", f"./zipped/{save_as}.zip")
shutil.rmtree(f"./{save_as}")
print(f"[Sub] [Zipper] Finished in {time.time() - start_time}")
exit(0)