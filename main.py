from tkinter import *
import ctypes
import os
import shutil
import zipfile
from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo


def newlinestr(strings:list[str]) -> list:
    """returns a list of strings""" # with the newline symbol
    endlst = []
    for s in strings:
        endlst.append(str(s)) # + "\n"
    return endlst
def comspaths(a:str, b:str) -> str:
    """returns a string path of two string paths"""
    backslash:str = str(Path("/"))
    return str(a) + backslash + str(b)
def rstrnls(string:str):
    end_str:str = ""
    for part in string.split('\n'):
        end_str += part
    return end_str
def strnint(string:str):
    end_str = ""
    for char in string:
        try:int(char)
        except:end_str += char
    return end_str


def replace_mp4(new:str, old:str):
    """replaces an old mp4 file with a new mp4 file"""
    
    if not new:
        print("No file selected.")
        return

    # Check if the old file exists before replacing
    if os.path.exists(old):
        os.remove(old)  # Delete the old file
    
    # Copy the new file to the destination
    shutil.copy2(new, old)
def copy_mp4(source:str, destination:str):
    """copies a source mp4 file to a destination mp4 file
    e.g: copy_mp4('a/source/path.mp4', 'a/destination/path.mp4')"""
    shutil.copy2(source, destination)
def delete_mp4(source:str):
    """deletes a source mp4 file"""
    if os.path.exists(source):
        os.remove(source)
    else:
        print("File not found.")

def path_cwd(path:str):
    return "./files/" + path

class style:
    bg = "#757575"
    entry = "#4a4a4a"
    frame = "#707070"
    button = "#696969"
    text = "#111"
    white = "#fff"
    black = "#000"

# version initialising
full_release:int = 0
semi_release:int = 7
bugfix_release:int = 5
ver:str = "-beta"
version = str(full_release) +"."+ str(semi_release) +"."+ str(bugfix_release) + ver
# init root window
root = Tk()
root.title("ETB Mod Loader") # set title
root.configure(bg=style.bg) # set gackground
root.resizable(False, False) # make it un-rezisable (aesthetic purpose)
root.iconbitmap(default=path_cwd("icon.ico")) # change app icon
myappid = 'TGTMS.ModLoader.ETBModLoader.'+ version
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class boolean:
    def __init__(self, value: bool):
        self.value: bool = value
    def set(self, to: bool):
        self.value: bool = to
    def get(self):
        return self.value

def read_sett_efdir() -> None:
    global etb_folder_path_str
    global sett
    if os.path.exists("./files/sett.txt"):
        sett = open("./files/sett.txt", 'r')
    else:
        sett = open("./python/ETB Mod downloader/sett.txt")
    etb_folder_path_str = sett.readlines()[0]
    sett.close()

etb_folder_path_str = "" # make the important etb folder path string
settings = ""
read_sett_efdir() # set it to the actual path
etb_folder_path = StringVar(value=str(etb_folder_path_str))

# important variables
root_folder = StringVar()
root_folder.set(etb_folder_path_str[0])

org_etb_movies_folder = "Movies"
org_etb_mods_folder = "Paks\--ModLoader--"

def get_file_name(directory:str, slash:str = "/") -> str: # making my life easy
    return directory.split(slash)[-1].split(".")[0]

label_frame_misc_options = LabelFrame()

# Error fixes
applied = boolean(True)
search_button_text = StringVar(value="Search")

# Creating functionality
def open_mod_zip(path:str):
    file_name:str
    with zipfile.ZipFile(path, 'r') as zip_ref:
        file_name = zip_ref.namelist()[0]
        zip_ref.extract(file_name, path_cwd("tmpfiles/"))
    return file_name

def find_etb_folder() -> Path:
    # finding the steam \ steamapps folder
    global root_folder
    for folder in Path(root_folder.get()+":/").rglob("Steam/steamapps"):
        # if current folder is the correct path
        if folder.is_dir():
            # finding Escape The Backrooms folder
            for _folder in Path(folder).rglob("EscapeTheBackrooms/EscapeTheBackrooms/Content"):
                # return if path is correct
                if _folder.is_dir():
                    # return full folder path
                    return _folder

def sett_write(lines:list[str]):
    sett = open(path_cwd("sett.txt"), 'w')
    write = newlinestr(lines)
    sett.writelines(write)
    sett.close()

print("Creating functionality")
def search_etb_folder() -> None:
    # globalize
    global etb_folder_path_str
    global org_etb_mods_folder

    # search
    print("searching for etb folder")
    etb_folder_path_str = str(find_etb_folder())
    mods = rstrnls(comspaths(etb_folder_path_str, org_etb_mods_folder))
    directory = mods
    try:os.mkdir(directory + "\\")
    except Exception as exception:print(f"File/Directory '{directory}' already exists\nException -> {exception}")

    # found
    print("found:", etb_folder_path_str)
    etb_folder_path.set(etb_folder_path_str)

    # write to sett.txt
    sett_write([etb_folder_path_str, settings])

def updateMod(file_name:str, state: int) -> None:
    global mods
    print(f"update {file_name} to {state == 1}")
    state = state == 1
    oldState = comspaths(mods, (f"{get_file_name(file_name)}.pak" if (not state) else f"{get_file_name(file_name)}.pak.dis"))
    newState = comspaths(mods, (f"{get_file_name(file_name)}.pak" if state else f"{get_file_name(file_name)}.pak.dis"))
    os.rename(oldState, newState)

bl = boolean(False)
def load_etb_files() -> None:
    global bl # already loaded
    global label_frame_misc_options # misc opt
    global label_frame_mod_options # mod opt
    global etb_folder_path_str # etb folder path
    global org_etb_movies_folder # Movies
    global org_etb_mods_folder # Paks/~mods
    global root_folder # root folder (a b c d e f)
    global sett # sett.t

    sett = open(path_cwd("sett.txt"))
    etb_folder_path_str = sett.readlines()[0]
    sett.close()

    #applied.set(False)
    print("loading installed files")
    global mods
    movies = rstrnls(comspaths(etb_folder_path_str, org_etb_movies_folder))
    mods = rstrnls(comspaths(etb_folder_path_str, org_etb_mods_folder))

    print(movies)
    print(mods)

    # proccess video files
    print("starting : Movies and Mods")
    def replace_movie_file(file_name:str):
        copy_mp4(comspaths(path_cwd("oldfiles"), file_name), comspaths(path_cwd("tmpfiles"), file_name))
        replace_mp4(filedialog.askopenfilename(title="Open New mp4 File"), comspaths(path_cwd("tmpfiles"), file_name))
        replace_mp4(comspaths(path_cwd("tmpfiles"), file_name), comspaths(movies, file_name))
        delete_mp4(comspaths(path_cwd("tmpfiles"), file_name))
    
    global updateMod

    if not bl.get():
        bl.set(True)
        directory = os.fsencode(movies)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".mp4"):
                print(f"Button: {get_file_name(os.path.join(movies, filename), "\\")}")
                exec(f'Button(label_frame_misc_options, font=("TkDefaultFont", 8), text="{get_file_name(filename, "/")}", bg="{style.button}", fg="{style.text}", activebackground="{style.bg}", width={bw * 2}, command= lambda: replace_movie_file("{filename}"), justify="center").pack(pady=2,padx=3, fill="x")',
                     {"replace_movie_file": replace_movie_file, "Button": Button, "label_frame_misc_options": label_frame_misc_options})
        
        directory = os.fsencode(mods)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if Path(comspaths(mods, filename)).is_dir():
                nfile = os.fsdecode(os.listdir(os.fsencode(comspaths(mods, filename)))[0])
                shutil.move(nfile, comspaths(mods, get_file_name(nfile, "\\") + ".pak"))
            
            exec(f'{strnint(get_file_name(filename))} = IntVar(label_frame_mod_options, {filename.endswith(".pak")}, "{strnint(get_file_name(filename))}");print({strnint(get_file_name(filename))}.get());Checkbutton(label_frame_mod_options,font=("TkDefaultFont", 8), onvalue=1,offvalue=0, text="{get_file_name(filename)}", bg="{style.button}", fg="{style.text}", activebackground="{style.bg}", width={bw * 2}, variable={strnint(get_file_name(filename))}, command= lambda: updateMod("{filename}", {strnint(get_file_name(filename, "/"))}.get()), justify="center").pack(pady=2,padx=3, fill="x")',
                 {"updateMod": updateMod, "Checkbutton": Checkbutton,"IntVar":IntVar, "label_frame_mod_options": label_frame_mod_options})
            if filename.endswith(".dis"):
                print(filename, "disabled")
            elif filename.endswith(".pak"):
                print(filename, "enabled")



    print("done")

def install_etb_mod() -> None:
    global label_frame_mod_options
    global updateMod
    print("install mod")

    if not os.path.exists(comspaths(etb_folder_path_str,comspaths("Paks","--ModLoader--"))):
        os.makedirs(comspaths(etb_folder_path_str,comspaths("Paks","--ModLoader--")))

    file = filedialog.askopenfilename(title="- open mod pak -", filetypes=[["pak", "*.pak"]])
    fileName = get_file_name(file) + ".pak"
    
    print(comspaths(etb_folder_path_str,comspaths("Paks","--ModLoader--")))
    shutil.move(file, comspaths(etb_folder_path_str,comspaths("Paks","--ModLoader--")))

def close() -> None:
    print("close app")
    root.quit()

# Initialize ui
print("initialize Ui")
def init_ui() -> None:
    global bw
    global sett

    # settings
    default_font_scale:int = 9

    rys:int = 700 # screen scale y
    rxs:int = 400 # screen scale x
    pyw = 3 # pady window
    bw = 12 # set button width

    global root
    root.geometry(str(rxs) + "x" + str(rys))


    # root widgets
    main_frame = Frame(root, bg=style.bg, height=rys - 20, highlightbackground='black', highlightthickness=1, pady=7, padx=10)
    main_frame.pack(padx=8, pady=(8, 0), side='top', fill='x')
    #Label(root, text="tk: "+ str(TkVersion), bg=style.bg, font=('TkDefaultFont', su(default_font_scale))).pack(pady=(0, su(1)), side='bottom')
    Label(root, text=version, bg=style.bg, font=('TkDefaultFont', 10)).pack(pady=(0, 1), side='bottom')

    # main frame widgets
    label_frame_file_settings = LabelFrame(main_frame, text="Folder Settings", height=100, padx=10, bg=style.frame, fg=style.text, font=('TkDefaultFont', default_font_scale))
    label_frame_file_settings.pack(side='top', fill='x', pady=pyw)

    # label frame file settings widgets
    entry_etb_folder_path = Entry(label_frame_file_settings, width=42, textvariable=etb_folder_path, bg=style.entry, fg=style.text, state='disabled', font=('TkDefaultFont', default_font_scale)).pack(padx=5, pady=2, side='top', fill='x')

    frame_fs_buttons = Frame(label_frame_file_settings, bg=style.frame, padx=3)
    frame_fs_buttons.pack(fill='x', padx=5)

    frame_fs_root_folder = Frame(label_frame_file_settings, bg=style.frame, padx=3)
    frame_fs_root_folder.pack(fill='x', padx=5)
    # root folder settings
    global root_folder
    Label(frame_fs_root_folder, text="Select your root folder with steam in it",
          background=style.frame, foreground=style.text).pack(pady=(2,0), side="right")
    
    dropdown_root_folder = OptionMenu(frame_fs_root_folder, root_folder, "C", "A", "B", "C", "D", "E", "F")
    dropdown_root_folder.configure(background=style.button, highlightthickness=0, foreground=style.text, width=bw, activebackground=style.bg)
    dropdown_root_folder.pack(pady=(4,4), side='left', padx=5)
    # -

    # file settings buttons
    button_search_etb_folder = Button(frame_fs_buttons, textvariable=search_button_text, width=bw, bg=style.button, activebackground=style.bg, fg=style.text, command=search_etb_folder, font=('TkDefaultFont', default_font_scale)).pack(padx=5, pady=2, side='left')
    button_load_etb_mods = Button(frame_fs_buttons, text="Load Files", width=bw, bg=style.button, fg=style.text, activebackground=style.bg, command=load_etb_files, font=('TkDefaultFont', default_font_scale)).pack(padx=5, pady=5, side='left')
    button_install_etb_mod = Button(frame_fs_buttons, text="Install Mod", width=bw, bg=style.button, fg=style.text, activebackground=style.bg, command=install_etb_mod, font=('TkDefaultFont', default_font_scale)).pack(padx=5, pady=5, side='left')
    # -
    # - \ main frame widgets
    global label_frame_mod_options
    label_frame_mod_options = LabelFrame(main_frame, text="Mod Options", height=100, padx=10, bg=style.frame, fg=style.text, font=('TkDefaultFont', default_font_scale))
    label_frame_mod_options.pack(side='top', fill='x', pady=pyw)
    # mod options widget
    label_info_text = """Beta Version:
video files are supported.
mods are not supported yet.
setting are not supported yet."""
    Label(label_frame_mod_options, text=label_info_text, bg=style.frame, fg=style.text, font=('TkDefaultFont', default_font_scale)).pack(fill='both', padx=2, pady=3, side='top')

    # - \ main frame widgets
    global label_frame_misc_options
    label_frame_misc_options = LabelFrame(main_frame, text="Misc Options", height=100, padx=10, bg=style.frame, fg=style.text, font=('TkDefaultFont', default_font_scale))
    label_frame_misc_options.pack(side='top', fill='x', pady=pyw)
    # misc options widgets
    tutor_text = """click on
the file
you want
to change"""
    Label(label_frame_misc_options,fg=style.text,bg=style.bg, text=tutor_text, font=('TkDefaultFont', 8), width=14).pack(side='right', fill='y')
    # - \ main frame widgets
    label_frame_settings = LabelFrame(main_frame, text="Settings", height=60, padx=10, bg=style.frame, fg=style.text, font=('TkDefaultFont', default_font_scale))
    label_frame_settings.pack(side='top', fill='x', pady=pyw)
    # settings widgets
    
    # settings
    #Label(label_frame_settings, text=tutor_text, bg=style.frame).pack(fill='both', padx=6,pady=6)
    
    # - \ main frame widgets
    def apply() -> None:
        showinfo(f"Message From {root.title()}", "Apply does nothing\nand it will get removed")
    button_apply = Button(main_frame, text="apply", width=bw * 2, bg=style.button, activebackground=style.bg, fg=style.text, command=apply, font=('TkDefaultFont', default_font_scale)).pack(side='right', pady=(3, 0))
    button_close = Button(main_frame, text="close", width=bw * 2, bg=style.button, activebackground=style.bg, fg=style.text, command=close, font=('TkDefaultFont', default_font_scale)).pack(side='left', pady=(3, 0))

    root.mainloop()

# END
print("starting main main-loop")
init_ui()
try:sett.close()
except:pass
# 354 Lines ✓