
'''
    厘米、分米、米,千米
    吨、千克、克
    -r: 随机数范围 ,ex:1-100
    -n: 问题数目,
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
import datetime

class Problem():
    def __init__(self,r,n):
        self.len_units = ['厘米','分米','米','千米']
        self.weigh_units = ['克','千克','吨']
        self.real_numbers = np.random.randint(*tuple(map(int, str.split(r,'-'))),10) # range
        self.problem_num = n
        self.wrong_list =[]
        self.problem_string =''

    def _input(self,question):
        print(question)
        error=True
        while(error):
            try:

                input_int = int(input())
                return input_int
            except ValueError:
                    print('只能输入数字')
                    error=True

    def gen_problems(self,problem_num):
        wrong_problem_list = []
        for i in range(int(problem_num)):
            problem_string ,ans= self.gen_p()
            input_int = self._input(problem_string)
            if input_int == ans:
                print('正确')
            else:
                print('错误')
                wrong_problem_list.append(problem_string)

        correct_rate = len(wrong_problem_list)/int(problem_num)
        print('正确率:{correct_rate}'.format(correct_rate=correct_rate
                                          ))

    def gen_p(self):
        '''
        generate problem

        :return:
        '''
        int_or_float = np.random.randint(0,2)
        pro_type =  np.random.randint(0,2)

        if pro_type == 0:
            'len'
            unit_type =self.len_units

        else:
            'weight'
            unit_type =self.weigh_units

        unit1,unit2 = [np.random.choice(unit_type,1) for _ in [1,2]]
        #print(unit1,unit2)

        real_number = np.random.choice(self.real_numbers,1)[0]
        if int_or_float == 0:
            pass
        else:
            temp = real_number / np.random.randint(1, 100)
            real_number = round(temp, 2) #浮点型,保留2位

        problem_string = '{real_number}{unit1}={input_ans}{unit2}'.format(real_number=real_number,unit1=unit1,unit2=unit2,input_ans='(  )')


        unit1_index, unit2_index = [self._index_in_list(unit_type,value) for value in [unit1,unit2]]

        unit_distance = unit2_index - unit1_index

        ans = 1
        ans *=self._swtichto10(unit_distance,unit1,unit2)

        return problem_string,ans


    def if_correct(self,input_,ans):
        print('input_={input},ans={ans}'.format(input_=input_,ans=ans))
        if input_ == ans:
            print('正确')
            return True
        else:
            print('错误')
            return False


    def _index_in_list(self,_list,value):
        ''''
        找到数组中value所对应的index
        '''
        #print(_list)
        for index,v in enumerate(_list):
            if value == v:
                #print('value={value},index={index}'.format(value=value,index=index))
                return index
            else:
                continue
        return None




    def _swtichto10(self,unit_distance,unit1,unit2):
        '''
        数字转换成10进位制进率,ex:2转成100,3转成1000,
        特殊情况米、千米
        :return:
        '''
        number = 1
        for value in [unit1,unit2]:
            if '千' in value:
                kilo_bool =True
                #number *=1000
            else:
                kilo_bool =False

        if unit_distance >0:
            number = -1
        else:
            number = 1

        for value in range(unit_distance):
            if value > 0:
                if kilo_bool:
                    number*=1000
                    return  number
                else:
                    number *= 10
            else:
                if kilo_bool:
                    number /= 1000
                    return number
                else:
                    number /= 10

            value -= 1
        return number




class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg
        print(__doc__)



def main(argv=None):
    if argv is None:
        argv=sys.argv
    try:
        try:
            opts,args = getopt.getopt(argv[1:],'hr:n:',['help'])
        except getopt.error as err:
            raise Usage(err)
        if len(opts)==0:
            raise Usage('opts empty')

        opt_list = []
        for o, a in opts:
            if o in ('-h', '--help'):
                raise Usage('user-help')
            if o =='-r':
                opt_list.append(a)
            if o =='-n':
                opt_list.append(a)

        p = Problem(r=opt_list[0],n=opt_list[1])
        p.gen_problems(problem_num=opt_list[1])



    except Usage as e:
        print(e.msg)
        return 2

if __name__ == '__main__':
    sys.exit(main())
