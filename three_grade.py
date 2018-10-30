
'''
    厘米、分米、米,千米
    吨、千克、克
    -r: 随机数范围 ,ex:1-100
    s: step,ex:0.1 or 1 etc
    n: 问题数目,
    -o :outpu file ,csv format
    --help or -h: help

'''
import sys
import getopt


import sys
import getopt
import numpy as np
import itertools
import pandas as pd


class Problem():
    def __init__(self,r,s):
        self.len_units = ['厘米','分米','米','千米']
        self.weigh_units = ['吨','千克','克']
        self.range = np.random.randint(*tuple(map(int, str.split(r,'-'))),10) # range
        self.step = np.float64(s)
    def gen_p(self):
        '''
        generate problem

        :return:
        '''


class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg
        print(__doc__)



def main(argv=None):
    if argv is None:
        argv=sys.argv
    try:
        try:
            opts,args = getopt.getopt(argv[1:],'hr:',['help'])
        except getopt.error as err:
            raise Usage(err)
        if len(opts)==0:
            raise Usage('opts empty')

        for o, a in opts:
            if o in ('-h', '--help'):
                raise Usage('user-help')
            if o =='-r':
                p = Problem(r=a)
    except Usage as e:
        print(e.msg)
        return 2

if __name__ == '__main__':
    sys.exit(main())
