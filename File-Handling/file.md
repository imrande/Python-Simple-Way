2 types of files are available

- text file (.txt, .py, .js)
- binary file (.zip, .mp4, .mp3, .png, .jpg)

7 modes are available in python file system

- r => read
- w => write
- a => append
- r+ => read and write
- a+ => append and read
- w+ => write and read
- x => exclusive write mode
	- prerequisites is "file shouldn't be exist". It is always created brand new file at the time calling.. 
	- If same name file is existed then it will throw `FileExistsError` 

operation modes for binary file

- rb => read
- wb => write
- ab => append
- r+b => read and write
- a+b => append and read
- w+b => write and read
- xb => exclusive write mode

### FAQ

1. In which modes, a new file will be created?
	- w, a, a+, w+, x
2. In which modes file should be already there?
	- r, r+
3. In which modes file shouldn't be already there?
	-  x
4. In which modes over writing of existing data will be happened?
	- w, r+, w+
5. In which modes over writing of existing data won't be happened?
	- a, a+