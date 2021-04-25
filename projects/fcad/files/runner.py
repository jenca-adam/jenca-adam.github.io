#!/usr/bin/env python
from v2 import *
import cmd,v2.keys
class CmdLine(cmd.Cmd):
    prompt="FCaD-3.2.0-$ "
    intro="This is FCaD version 3.2.0. \ntype \"help\" for list of commands, press CTRL-D or CTRL-C to exit\n"
    def do_encrypt(self,line):
        file,keyfile=tuple(line.split(' '))
        iencrypt(file,keyfile)
    def do_decrypt(self,line):
        file,keyfile=tuple(line.split(' '))

        idecrypt(file,keyfile)
    def do_new_key(self,keyfile):
        with open(keyfile,'wb')as f:
            f.write(v2.keys.dump(v2.keys.new(),255))
    def do_EOF(self,FOO):
        print('')
        exit()
if __name__=='__main__':
    try:
        CmdLine().cmdloop()
    except KeyboardInterrupt:exit()
