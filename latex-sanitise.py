#!/usr/bin/python

import cmd
import re
import sys, os.path
import fnmatch

#########################################################################################
#########################################################################################
def inline_msg( type, msg, indent = 0 , stream = sys.stderr):
    print >> stream, "%s[%s - %5s ] %s...\r"%(" "*indent, os.path.split(sys.argv[0])[1], type, msg),
    stream.flush()

def newline_msg( type, msg, indent = 0 , stream = sys.stderr ):
    print >> stream, "%s[%s - %5s ] %s"%(" "*indent, os.path.split(sys.argv[0])[1], type, msg)
    stream.flush()
#########################################################################################
#########################################################################################




class ManuscriptCommandParser(cmd.Cmd):
    """DB command handler"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "| latex-sanitise :::~ "
        self.manuscript = ""

    def do_load(self,c):
        self.manuscript = c

    
    def do_clean(self,c):
        self.do_load(c)
        
        fout = open(c[:-4])
        for i in 
        
        
    #def do_list_figures(self, c):
        #"""lists the figures included in the manuscript"""
        #re.compile("\\includegraphics")
    
    def do_EOF(self, line):
        return True

    #def do_shell(self, line):
        #"""Runs a shell command"""
        #output = os.popen(line).read()
        #print output

    #def do_cd(self,line):
        #""" Changes into a given directory """
        #try:
            #os.chdir(line)
        #except:
            #utils.newline_msg("DIR", "no directory named '%s'"%line, 2)

    #def complete_cd(self, text, line, begidx, endidx):    
        #completions =  filter(lambda x: os.path.isdir(x) , os.listdir(".") )
        #if text:
            #completions = [ f
                            #for f in completions
                            #if f.startswith(text)
                            #]
        #return completions


    #def do_run_script(self,c):
        #"""executes a script file with commands accepted in this cmdline parser"""
        #if not os.path.exists(c):
            #newline_msg("FIL", "file doesn't exist")
            #return
        #for l in open(c):
            #l = l.strip()
            #if not l: continue 
            #if l[0] == "#": continue
            
            #self.onecmd(l.strip())



##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


if __name__ == '__main__':
    cmd_line = ManuscriptCommandParser()
    if len(sys.argv) == 1:
        cmd_line.cmdloop()
    else:
        cmd_line.onecmd(" ".join(sys.argv[1:]))
        


    
