import platform, os, warnings
import sys, base64, shutil, re, time
import http.client as httplib
from pathlib import Path
from bs4 import BeautifulSoup
##### Dismiss the 'XML' warning
warnings.filterwarnings("ignore", 
category=UserWarning, module='bs4')
#############################

## ACCESS FILESYSTEM
class filesystem():

    ## CREATE DIRECTORIES
    def make_dir(Dir: Path, debug: bool=False):
        '''
        Dir: Path to directories
        debug: (boolean)
        '''
        if type(Dir) == list:
            Dirs = Dir
            for x in range(len(Dirs)):
                if not os.path.isdir(Dirs[x]):
                    os.makedirs(Dirs[x])
                    if debug:
                        print("\nneed4swede.filesystem.make_dir():\n"
                                f"Created - {Dirs[x]}\n") 
                else:
                    if debug:
                        print("\nneed4swede.filesystem.make_dir():\n"
                                f"Does Not Exist - {Dirs[x]}\n")
        elif type(Dir) == str:
            if not os.path.isdir(Dir):
                os.makedirs(Dir)
                if debug:
                    return print("\nneed4swede.filesystem.make_dir():\n"
                                f"Created - {Dir}\n") 
            else:
                if debug:
                    return print("\nneed4swede.filesystem.make_dir():\n"
                                f"Does Not Exist - {Dir}\n")

    ## REMOVE DIRECTORIES
    def remove_dir(Dir: Path, debug: bool=False):
        '''
        Dir: Path to directories
        debug: (boolean)
        '''
        if type(Dir) == list:
            Dirs = Dir
            for x in range(len(Dirs)):
                if os.path.isdir(Dirs[x]):
                    shutil.rmtree(Dirs[x])
                    if debug:
                        print("\nneed4swede.filesystem.remove_dir():\n"
                                f"Removed - {Dirs[x]}\n") 
                else:
                    if debug:
                        print("\nneed4swede.filesystem.remove_dir():\n"
                                f"Does Not Exist - {Dirs[x]}\n")
        elif type(Dir) == str:
            if os.path.isdir(Dir):
                shutil.rmtree(Dir)
                if debug:
                    return print("\nneed4swede.filesystem.remove_dir():\n"
                                f"Removed - {Dir}\n") 
            else:
                if debug:
                    return print("\nneed4swede.filesystem.remove_dir():\n"
                                f"Does Not Exist - {Dir}\n")

    ## REMOVE FILES
    def remove_file(File: Path, debug: bool=False):
        '''
        File: Path to files
        debug: (boolean)
        '''
        if type(File) == list:
            Files = File
            for x in range(len(Files)):
                if os.path.isfile(Files[x]):
                    os.remove(Files[x])
                    if debug:
                        print("\nneed4swede.filesystem.remove_file():\n"
                                f"Removed - {Files[x]}\n") 
                else:
                    if debug:
                        print("\nneed4swede.filesystem.remove_file():\n"
                                f"Does Not Exist - {Files[x]}\n")
        elif type(File) == str:
            if os.path.isfile(File):
                os.remove(File)
                if debug:
                    return print("\nneed4swede.filesystem.remove_file():\n"
                                f"Removed - {File}\n") 
            else:
                if debug:
                    return print("\nneed4swede.filesystem.remove_file():\n"
                                f"Does Not Exist - {File}\n")

    def root_dir(Dir: str='user', debug: bool=False):
        if Dir == 'applications' or Dir == 'apps':
            if platform.system() == 'Darwin':
                if debug:
                    print("/Applications")
                return "/Applications"
            if platform.system() == 'Windows':
                if debug:
                    print("C:\Program Files")
                return "C:\Program Files"
        if Dir == 'user':
            if debug:
                print(Path.home())
            return Path.home()
        if Dir == 'userlib':
            if platform.system() == 'Darwin':
                if debug:
                    print(f"{Path.home()}/Library")
                return f"{Path.home()}/Library"
            if platform.system() == 'Windows':
                if debug:
                    print(f"{Path.home()}/AppData")
                return f"{Path.home()}/AppData"
        if Dir == 'syslib':
            if platform.system() == 'Darwin':
                if debug:
                    print("/Library")
                return "/Library"
            if platform.system() == 'Windows':
                if debug:
                    print("C:\Windows\System32")
                return "C:\Windows\System32"

## STRING MANIPULATION
class string():

    ## REMOVES CHARACTERS FROM TEXT
    def clean_text(Input: str, Casing: str="default", Remove_Spaces: bool=False):
        '''
        Input: input string (str)
        Casing: 'default', 'lower', 'upper', 'title', 'camel' (str)
        Remove_Spaces: removes spaces between words (boolean)
        '''

        ## REMOVE SPECIAL CHARACTERS FROM STRING
        clean = re.sub(r"[^a-zA-Z0-9 ,*\u2019-]+"," ",Input).strip()

        ## CONVERT TO LOWERCASE
        if Casing == "lower":
            clean = clean.lower()

        ## CONVERT TO UPPERCASE
        elif Casing == "upper":
            clean = clean.upper()

        ## CONVERT TO TITLECASE
        elif Casing == "title":
            if len(clean) > 0:

                ## COLLECT EVERY WORD BELOW 4 CHARACTERS
                s = clean.split()
                short_words = ' '.join(i.capitalize() for i in s if len(s[s.index(i)]) < 4).lower().split(" ")

                ## CAPITALIZE INPUT
                clean = ' '.join(i.capitalize() for i in s)

                ## REPLACE INSTANCES OF SHORT WORDS IN CAPITALIZED INPUT, AND UN-CAPITALIZE THEM
                for i in range(len(short_words)):
                    if short_words[i] in clean.lower():
                        index = clean.lower().index(short_words[i])
                        clean = clean.replace(clean[index], clean[index].lower())

                ## CAPITALIZE FIRST AND LAST WORDS IN STRING
                clean = clean[0].capitalize() + clean[1:]
                clean = clean.replace(clean.split(" ")[-1], clean.split(" ")[-1].capitalize())
        
        ## CONVERT TO CAMEL CASE
        elif Casing == "camel":
            s = clean.split()
            if len(clean) > 0:
                clean = s[0] + ''.join(i.capitalize() for i in s[1:])
        
        ## REMOVE SPACES
        if Remove_Spaces:
            clean = clean.replace(" ", "")
        
        ## RETURN
        return clean.strip()

    ## FILTER A LIST OF WORDS FROM STRING
    def filter_text(Text: str, Filter: list, debug: bool=False):
        '''
        ARGUMENTS

        - Text: input text (str)
        - Filter: words to remove (list)
        - debug: (boolean)

        DESCRIPTION
        
        - Filters out a list of words in a string of text
        '''
        try:
            clean = re.compile('|'.join(map(re.escape, Filter)))
            filtered_Text = clean.sub("", Text).replace('  ', ' ')
            return filtered_Text.strip()
        except Exception:
            if debug:
                return print("\nneed4swede.string.filter_text()\nOperation Failed\n")

    ## SHORTENS TEXT TO A SET LIMIT
    def shorten_text(text: str, length: int, debug: bool=False, suffix: str='...'):
        '''
        ARGUMENTS

        - text: input (str)
        - length: length of string (int)
        - debug: (boolean)
        - suffix: default is '...' (str)

        DESCRIPTION

        - Shortens a string without cutting off words and adds a suffix
        '''

        ## DEBUGGER
        if debug:
            ## TEXT VALIDATION, STRING
            if not type(text) == str:
                print("\nInput text not a valid string")
                return
            ## LENGTH VALIDATION, INT
            if not type(length) == int:
                print("\nInput length not a valid integer")
                return

        ## MAIN
        try:
            ## RETURN TEXT IF LENGTH IS GREATER
            if len(text) <= length:
                return text
            else:
                ## SHORTEN TEXT AND ADD SUFFIX
                return ' '.join(text[:length+1].split(' ')[0:-1]) + suffix
        ## ERROR
        except Exception:
            return print("\nneed4swede.string.shorten_text():\nOperation Failed - Enable debug for more info\n")

## TERMINAL COMMANDS
class terminal():
    
    ## CLEAR TERMINAL
    def clear():
        '''
        Clears the terminal
        '''
        ## WINDOWS
        if platform.system() == "Windows":
                clear = lambda: os.system('cls')
                clear()
                print()
        ## MACOS
        if platform.system() == "Darwin":
                os.system("clear")
                print()

    ## RESTART AN APP
    def restart_app():
        '''
        Restarts Python application
        '''
        python = sys.executable
        os.execl(python, python, * sys.argv)

## WEB FOCUSED METHODS
class web():

    ## MERGE HTML/CSS/JS INTO ONE HTML FILE
    def merge_html(HTML: Path, CSS: Path, JS: Path, onefile: bool=False, debug: bool=False, filename: str='index'):
        '''
        ARGUMENTS

        - HTML: Path to HTML file
        - CSS: Path to CSS file
        - JS: Path to JS file
        - onefile: Only keep output file (bool)
        - debug: (bool)
        - filename: output html filename (str)

        DESCRIPTION

        - Merges HTML, CSS and JS files into one HTML file with inline code
        '''

        ## READ THE BUILT HTML FILE
        try:
            html_file = Path(f'{HTML}').read_text(encoding="utf-8")
            soup = BeautifulSoup(html_file, features='lxml')
        except FileNotFoundError:
            if debug:
                return print('\nneed4swede.web.merge_html():\nHTML File Not Found - Files Not Merged\n')
            else:
                return

        ## GET FILE DIRECTORY
        index = HTML.rfind("/")
        directory = f"{HTML[0:index]}"

        ## FIND LINK TAGS : <link rel="stylesheet" href="css/somestyle.css">
        for tag in soup.find_all('link', href=True):
            if tag.has_attr('href'):
                try:
                    css_file = Path(f'{CSS}').read_text(encoding="utf-8")
                except FileNotFoundError:
                    if debug:
                        return print('\nneed4swede.web.merge_html():\nCSS File Not Found - Files Not Merged\n')
                    else:
                        return

                # remove the tag from soup
                tag.extract()
        
                # insert style element
                new_style = soup.new_tag('style')
                new_style.string = css_file
                soup.html.head.append(new_style)
                break
        
        ## FIND SCRIPT TAGS : <script src="js/script.js"></script>
        for tag in soup.find_all('script', src=True):
            if tag.has_attr('src'):
                try:
                    js_file = Path(f'{JS}').read_text(encoding="utf-8")
                except FileNotFoundError:
                    if debug:
                        return print('\nneed4swede.web.merge_html():\nJS File Not Found - Files Not Merged\n')
                    else:
                        return

                # remove the tag from soup
                tag.extract()
        
                # insert script element
                new_script = soup.new_tag('script')
                new_script.string = js_file
                soup.html.body.append(new_script)
        
        ## FIND IMAGE TAGS : <img src="" alt="">
        for tag in soup.find_all('img', src=True):
            if tag.has_attr('src'):
                file_content = Path(tag['src']).read_bytes()
        
                # replace filename with base64 of the content of the file
                base64_file_content = base64.b64encode(file_content)
                tag['src'] = "data:image/png;base64, {}".format(base64_file_content.decode('ascii'))

        ## CREATE WEBFILES DIR FOR PREVIOUS FILES
        os.makedirs(f"{directory}/webfiles")

        ## COPY PREVIOUS FILES TO WEBFILES IF ONEFILE == FALSE
        if not onefile:
            shutil.copy(HTML, f"{directory}/webfiles/index.html")
            shutil.copytree(f"{directory}/assets", f"{directory}/webfiles/assets")

        ## MERGE HTML/CSS/JS INTO HTML
        try:
            with open(f"{directory}/{filename}.html", "w", encoding="utf-8") as outfile:
                outfile.write(str(soup))
        except Exception:
            if debug:
                return print('\nneed4swede.web.merge_html():\nHTML/CSS/JS Files Were Found\nBut Failed to Merge')
            else:
                return
        
        ## REMOVE PREVIOUS FILES
        if os.path.isdir(f"{directory}/assets"):
                shutil.rmtree(f"{directory}/assets")
        if not filename == 'index':
            try:
                os.remove(f"{directory}/index.html")
            except FileNotFoundError:
                pass
        

        ## REMOVE PREVIOUS HTML IF ONEFILE == TRUE
        if onefile:
            if os.path.isdir(f"{directory}/webfiles"):
                shutil.rmtree(f"{directory}/webfiles")

        if debug:
            return print(f"\n{HTML}\n"
                            f"{CSS}\n"
                            f"{JS}\n"
                            f"---\n"
                            f"{directory}/{filename}.html")
        else:
            return

    ## CHECK FOR WORKING NETWORK CONNECTION
    def network_test():
        network_connectivity_test = httplib.HTTPSConnection("8.8.8.8", timeout=5)
        try:
            network_connectivity_test.request("HEAD", "/")
            return True
        except Exception:
            return False
        finally:
            network_connectivity_test.close()

    ## STRIP HTML TAGS FROM STRING
    def strip_tags(Input: str):
        '''
        ARGUMENTS

        - Input: str
        - Removes HTML tags from string

        DESCRIPTION

        - Remove HTML tags from an input string
        '''
        clean = re.compile('<.*?>')
        return re.sub(clean, '', Input).strip()


## TESTS
