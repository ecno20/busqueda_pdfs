# busqueda_pdfs
Archivo de busqueda de PDF en Python
## Proyecto
El siguiente programa tiene como objetivo, buscar archivos .PDF en una carpeta seleccionada.

Functionalities:
- Busqueda por texto, "palabra seleccionada.

The following scripts are provided for the MongoDB database/collections creation:

- busqueda_pdfs.py


## Deploy
## Creating the program
This program is based on [Windows/arm64](https://www.microsoft.com/es-es/software-download/windows11) for Windows.

The complete specification of the image that contains the application is in the [Dockerfile](Dockerfile)
## Building the program.
Build the program using `Windows` or `Linux`, below the commands for using Linux. More information on how to use it [here](https://docs.kernel.org/). The first version for a standard is frequently used `6.9.0`


> [!Warning]
>  Don't forget to use your Admin's account to run the program, because if you do not have administrator permissions, the program may have problems running.

-Installing in windows

Dowload python in [Here](https://www.python.org/downloads/)
run the installer in administrator mode

Make sure to check the "Add Python to PATH" option during installation

![image](https://github.com/ecno20/busqueda_pdfs/assets/144557398/88a6af95-f11f-45bb-bd08-67eac6906c51)

-Install the necessary libraries:
Open the command prompt (you can search for "cmd" in the start menu) and run the following command to install PyPDF2:


`pip install PyPDF2`

The result should look like this:



  
  ```bash
pip install PyPDF2
Requirement already satisfied: PyPDF2 in c:\users\hp-g6\appdata\local\programs\python\python312\lib\site-packages (3.0.1)
```



## Create the program file.

Create the file in the desired folder, for the example the file is located in `Windows` :

`C:\Users\Hp-G6\Documents\Proyectos\Python`

Create the program file:
Open a text editor (such as Notepad++) and copy the code provided in my repo `busqueda_pdfs` . Save the file with the .py extension, for example, busqueda_pdfs.py.

Open the command prompt `cmd` and navigate to the directory where you saved the busqueda_pdfs.py file. You can use the cd command to change directories. For example:


`cd \Users\Hp-G6\Documents\Proyectos\Python`

The expected output after the previous command looks like this:

![image](https://github.com/ecno20/busqueda_pdfs/assets/144557398/d4929c4d-fd69-4fbe-8274-b8a5043d6601)


## Running

run the program with the following command.
>[!Important]
>  If you are not logged in in administrator mode, you could have execution problems:
> ```Admin login {myuser}```
>  then type the password.
 
 
`python busqueda_pdfs.py`

The expected output after the previous command looks like this:

![image](https://github.com/ecno20/busqueda_pdfs/assets/144557398/08e3e799-0bf7-4a60-9db1-cf5815264337)

```bash
C:\Users\Hp-G6\Documents\Proyectos\Python>python busqueda_pdfs.py
Introduzca la dirección de la carpeta de busqueda: C:\Users\Hp-G6\Documents\Libros
Introduzca el texto que desea buscar: Corona
Traceback (most recent call last):
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 32, in <module>
    search_pdf_in_folder(folder_path, search_text)
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 23, in search_pdf_in_folder
    if search_text_in_pdf(file_path, search_text):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 8, in search_text_in_pdf
    reader = PdfFileReader(file)
             ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_reader.py", line 1974, in __init__
    deprecation_with_replacement("PdfFileReader", "PdfReader", "3.0.0")
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 369, in deprecation_with_replacement
    deprecation(DEPR_MSG_HAPPENED.format(old_name, removed_in, new_name))
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 351, in deprecation
    raise DeprecationError(msg)
PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.

C:\Users\Hp-G6\Documents\Proyectos\Python>

```

## Git clone repository
```bash
git clone https://github.com/ecno20/busqueda_pdfs.io 
```
`// TODO `
## Test
Execute the next `python busqueda_pdfs.py` command to validate searching for PDF files only. 

```shell
C:\Users\Hp-G6\Documents\Proyectos\Python>python busqueda_pdfs.py
Introduzca la dirección de la carpeta de busqueda: C:\Users\Hp-G6\Documents\Archivo_Muerto
Introduzca el texto que desea buscar: Bitacora
Traceback (most recent call last):
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 32, in <module>
    search_pdf_in_folder(folder_path, search_text)
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 23, in search_pdf_in_folder
    if search_text_in_pdf(file_path, search_text):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 8, in search_text_in_pdf
    reader = PdfFileReader(file)
             ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_reader.py", line 1974, in __init__
    deprecation_with_replacement("PdfFileReader", "PdfReader", "3.0.0")
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 369, in deprecation_with_replacement
    deprecation(DEPR_MSG_HAPPENED.format(old_name, removed_in, new_name))
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 351, in deprecation
    raise DeprecationError(msg)
PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.

C:\Users\Hp-G6\Documents\Proyectos\Python>

```
The expected result should looks like:
```shell
 File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 32, in <module>
    search_pdf_in_folder(folder_path, search_text)
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 23, in search_pdf_in_folder
    if search_text_in_pdf(file_path, search_text):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 8, in search_text_in_pdf
    reader = PdfFileReader(file)
             ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_reader.py", line 1974, in __init__
    deprecation_with_replacement("PdfFileReader", "PdfReader", "3.0.0")
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 369, in deprecation_with_replacement
    deprecation(DEPR_MSG_HAPPENED.format(old_name, removed_in, new_name))
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 351, in deprecation
    raise DeprecationError(msg)
PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead

```
```shell

C:\Users\Hp-G6\Documents\Proyectos\Python>python busqueda_pdfs.py
Introduzca la dirección de la carpeta de busqueda: C:\Users\Hp-G6\Documents\Curso_365
Introduzca el texto que desea buscar: Configurar
Traceback (most recent call last):
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 32, in <module>
    search_pdf_in_folder(folder_path, search_text)
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 23, in search_pdf_in_folder
    if search_text_in_pdf(file_path, search_text):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\Documents\Proyectos\Python\busqueda_pdfs.py", line 8, in search_text_in_pdf
    reader = PdfFileReader(file)
             ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_reader.py", line 1974, in __init__
    deprecation_with_replacement("PdfFileReader", "PdfReader", "3.0.0")
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 369, in deprecation_with_replacement
    deprecation(DEPR_MSG_HAPPENED.format(old_name, removed_in, new_name))
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 351, in deprecation
    raise DeprecationError(msg)
PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.

C:\Users\Hp-G6\Documents\Proyectos\Python>
```
The expected result should looks like:

```shell
File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_reader.py", line 1974, in __init__
    deprecation_with_replacement("PdfFileReader", "PdfReader", "3.0.0")
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 369, in deprecation_with_replacement
    deprecation(DEPR_MSG_HAPPENED.format(old_name, removed_in, new_name))
  File "C:\Users\Hp-G6\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyPDF2\_utils.py", line 351, in deprecation
    raise DeprecationError(msg)
PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.
```

> ecno20: __Verification of the run program

### Reference Documentation
For further reference, please consider the following sections:

* [Python 3.12.3 documentation](https://docs.python.org/3/)
* [install Windows 11](https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e)
* [Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
* [notepad++ documentation](https://notepad-plus-plus.org/online-help/)

### Guides
The following guides illustrate how to use some features concretely:

* [python guide](https://docs.python.org/3/tutorial/index.html)
* [windows 11 installer documentation](https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e)
* [Command windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands#command-line-shells)
* [notepad++ guide](https://npp-user-manual.org/)
  
