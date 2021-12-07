import os
import datetime
name = " "
path = r"D:\health management"
path2 = " "
path3 = " "
name1 = " "
name3 = " "
a = " "
b = " "
c = " "
d = " "


class Main:

    @staticmethod
    def stage1():
        print("\nChose your name\n"
              "if Clint enter 1\n"
              "if loki enter 2\n"
              "if you want to quit this application enter Q\n")
        in2 = "h"
        while in2 not in (str(1), str(2), "Q"):
            global a
            in2 = str(input("\nEnter a value as per the note\n"))
            obj1 = Name()
            if in2 == str(1):
                a = str("1")
                obj1.name_file(a)
            elif in2 == str(2):
                a = str('2')
                obj1.name_file(a)
            elif in2 == "Q":
                a = str("Q")
                obj1.name_file(a)
            else:
                print("\nYou have an entered an invalid input\n"
                      "pls enter an valid input as per the input")
                continue

    @staticmethod
    def stage2():
        print("\nChoose what you have to access \n"
              "if Diet = 1\n"
              "if exercise = 2\n"
              "if you want to go back = 3")
        in1 = "h"
        while in1 not in (str(1), str(2), "Q"):
            global b
            in1 = str(input("\nEnter a value as per the note\n"))
            obj2 = Name2()
            if in1 == str(1):
                b = str("1")
                obj2.name2_file(b)
            elif in1 == str(2):
                b = str('2')
                obj2.name2_file(b)
            elif in1 == str(3):
                b = str("3")
                obj2.name2_file(b)
            else:
                print("\nYou have an entered an invalid input\n"
                      "pls enter an valid input as per the input")
                continue

    @staticmethod
    def stage3():
        print("\nChoose what you wanted to do with the txt file\n"
              "if you wanted to add a text = 1\n"
              "if you wanted to just read = 2\n"
              "if you wanted to go back = 3")
        in3 = "h"
        while in3 not in (str(1), str(2), "Q"):
            in3 = str(input("\nEnter a value as per the note\n"))
            global c
            obj3 = Access()
            if in3 == str(1):
                c = 1
                obj3.access(c)
            elif in3 == str(2):
                c = 2
                obj3.access(c)
            elif in3 == str(3):
                c = 3
                obj3.access(c)
            else:
                print("\nYou have an entered an invalid input\n"
                      "pls enter an valid input as per the input")
                continue


class Name:

    def name_file(self, a):
        self.a = a
        obj4 = Final_name()
        if self.a == str("1"):
            global name
            name = str(r"\Clint")
            obj4.newfile()
        elif self.a == str("2"):
            name = str(r"\Loki")
            obj4.newfile()
        elif self.a == "Q":
            print("\nQuiting the program")
            quit()


class Final_name(Name):

    def newfile(self):
        obj5 = Main()
        global path2
        if os.path.exists(path + name):
            print("\nFile exists in the name " + name)
            path2 = (path + name)
            print(path2)
            obj5.stage2()

        else:
            os.mkdir(path + name)
            print("\nNew file has been created as " + name)
            path2 = (path + name)
            print(path2)
            obj5.stage2()


class Name2(Name):

    def name2_file(self, b):
        self.b = b
        obj6 = Finalname()
        obj7 = Main()
        if self.b == str("1"):
            global name1
            name1 = str("Diet.txt")
            obj6.new_file()
        elif self.b == str("2"):
            name1 = str("Exercise.txt")
            obj6.new_file()
        elif self.b == str(3):
            obj7.stage1()


class Finalname(Name2, Final_name):

    def new_file(self):
        global path3
        global name3
        obj8 = Main()
        if os.path.exists(path2 + name + name1):
            print(("\nFile exists in the name ") + name1)
            path3 = (path2 + name + name1)
            name3 = str(name + name1)
            print(path3)
            obj8.stage3()
        else:
            with open(path2 + name + name1, "w+") as fp:
                print(("\nNew file has been created as "))
                path3 = (path2 + name + name1)
                name3 = str(name + name1)
                print(path3)
                obj8.stage3()


class Access(Finalname):

    def access(self, c):
        self.c = c
        obj9 = Main()
        obj0 = condition()
        if self.c == 1:
            obj0.add()
        elif self.c == 2:
            obj0.read()
        elif self.c == 3:
            obj9.stage2()


class condition(Access, Finalname):

    def add(self):
        obj10 = Main()
        print(path3)
        with open(path3, "a") as f:
            j = datetime.datetime.now().strftime('\n%D %H:%M:%S')
            i = input("\nEnter the value you wanted to write in the " + name3 + "\n")
            f.write(str(j) + " " + str(i))
        with open(path3, "r") as f:
            print(f.read())
            obj10.stage3()

    def read(self):
        obj10 = Main()
        print(path3)
        with open(path3, "r") as f:
            print(f.read())
            obj10.stage3()


# the mai0n code
if __name__ == '__main__':
    print("HEALTH MANAGEMENT PROGRAM\n")
    obj = Main()
    obj.stage1()