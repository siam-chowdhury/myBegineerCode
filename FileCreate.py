import glob



# THIS CLASS IS FOR SHOWING [File name : ]
class Promt:

    def PROMT_FILE_NAME():
        print('File name : ')



# FOR READING FILE
class Read(Promt):

    def READ_FILE():
        Promt.PROMT_FILE_NAME()
        filename = input()

        try:
            with open(f'{filename}.txt') as file:
                content = file.read()
                print(content)
        
        except Exception as err:
            print(err)


# FOR WRITING FILE
class Write(Promt):

    def WRITE_FILE():
        Promt.PROMT_FILE_NAME()
        filename = input()

        try:
            writing = input('write something : ')
            with open(f'{filename}.txt', 'a') as file:
                content = file.write(writing)

        except Exception as err:
            print(err)


# FOR CREATE .txt FILE
class CreateText(Promt):

    def CREATE_TEXT_FILE():
        Promt.PROMT_FILE_NAME()
        filename = input()

        try:
            file = open(f'{filename}.txt', 'x')
            file.close()

        except Exception as err:
            print(err)



# FOR CREATE .py FILE
class CreatePy(Promt):

    def CREATE_PY_FILE():
        Promt.PROMT_FILE_NAME()
        filename = input()

        try:
            file = open(f'{filename}.py', 'x')
            file.close()

        except Exception as err:
            print(err)


# CLEAR SPECIFIC FILE CONTENT
class Clear:

    def CLEAR_CONTENT():
        listofTest = glob.glob('*.txt')

        try:
            for text in listofTest:
                with open(text, 'w') as file:
                    file.seek(0)
            
        except Exception as err:
            print(err)




# PROGRAM WORKS FROM HERE 
class MainClass:
    
    def SHOW(self):
        print("1. r\n2. a\n3. x(txt)\n4. x(py)\n5. ca\n")
        choice = input()
        
        if choice == '1':
            Read.READ_FILE()
        
        elif choice == '2':
            Write.WRITE_FILE()
            
        elif choice == '3':
            CreateText.CREATE_TEXT_FILE()
        
        elif choice == '4':
            CreatePy.CREATE_PY_FILE()

        elif choice == '5':
            Clear.CLEAR_CONTENT()


object = MainClass()
print(object.SHOW())