#!/usr/bin/python3
import cmd
"""This is the  console module"""


class HBNBCommand(cmd.Cmd):
    """This is the class definition for
    HBNBCommand, inheriting from cmd.Cmd"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command exits the program"""

        if arg.lower() == 'quit':
            return True
        elif arg == '':
            return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
