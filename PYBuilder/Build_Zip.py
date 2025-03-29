import shutil
import subprocess
import time

# change the paths to be correct
def run_python_script(path:str):
    print("starting")
    start_time = time.time()
    command:list = ['python', path]
    subprocess.run(command, check=True)
    print(f'Finished in {start_time - time.time()}s')

def build_zip():
    print("[Main] Starting Build Processes")
    start_time = time.time()
    run_python_script("./PYBuilder/PYBuilder.py")
    run_python_script("./PYBuilder/zipper.py")
    shutil.rmtree("./dist/")
    print(f'[Main] Finished in {start_time - time.time()}s')
    print('[Main] results in: zipped')

if __name__ == '__main__':
    build_zip()
    exit(0)