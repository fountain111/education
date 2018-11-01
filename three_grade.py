
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
import time


def exeTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        back = func(*args, **args2)
        t1 =time.time()
        print('用时',t1-t0)
        return back
    return newFunc

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

                input_int = np.float64(input())
                return input_int
            except ValueError:
                    print('只能输入数字')
                    error=True

    @exeTime
    def gen_problems(self,problem_num):
        wrong_problem_list = []
        for i in range(int(problem_num)):
            problem_string ,ans= self.gen_p()
            #print('answer=',ans)
            input_int = self._input(problem_string)

            if input_int == ans:
                print('正确')
            else:
                print('错误')
                wrong_problem_list.append(problem_string)

        correct_rate = 1-len(wrong_problem_list)/int(problem_num)
        print('错误题目数:{wrong_problems},正确率:{correct_rate}'.format(correct_rate=correct_rate,wrong_problems=len(wrong_problem_list)
                                          ))

    def gen_p(self):
        '''
        generate problem

        :return:
        '''
        int_or_float = np.random.randint(0,2)
        pro_type =  np.random.randint(0,2)

        if pro_type == 0:
            unit_type =self.len_units
            unit_type_name = 'len'

        else:
            unit_type =self.weigh_units
            unit_type_name = 'weight'
        unit1,unit2 = '',''
        while(unit1 == unit2):
            unit1,unit2 = [np.random.choice(unit_type,1)[0] for _ in [1,2]]

        #print(unit1,unit2)

        real_number = np.random.choice(self.real_numbers,1)[0]
        if int_or_float == 0:
            pass
        else:
            temp = real_number / np.random.randint(1, 100)
            real_number = round(temp, 2) #浮点型,保留2位

        problem_string = '{real_number}{unit1}={input_ans}{unit2}'.format(real_number=real_number,unit1=unit1,unit2=unit2,input_ans='(  )')




        ans = real_number

        ans *=self._swtichto10(unit1,unit2,unit_type,unit_type_name)

        return problem_string,ans



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




    def _swtichto10(self,unit1,unit2,unit_type,unit_type_name):
        '''
        数字转换成10进位制进率,ex:2转成100,3转成1000,
        分三种情况,1:weight,进率为1000 2:厘米、分米、毫米等为第二种情况,10进制,3:千米 进率为1000

        :return:
        '''
        #print(unit_type_name)
        unit1_index, unit2_index = [self._index_in_list(unit_type, value) for value in [unit1, unit2]]
        unit_distance = unit1_index - unit2_index
        if unit_type_name =='weight':
            return self._base_trans(1000,unit_distance)
        elif unit_type_name =='len':
            if '千米' == unit1 or '千米' == unit2:
                return self._special_len(unit_distance)
            else:
                return self._base_trans(10, unit_distance)

        else:
            return  None



    def _base_trans(self,tans_unit,unit_distance):
        number = 1
        unit_positive=True
        #print('tans_unit',tans_unit,unit_distance)
        if unit_distance > 0:
            pass
        else:
            unit_distance = -unit_distance
            unit_positive=False
        for value in range(unit_distance):
            if value >= 0 and unit_positive:
                number *= tans_unit
            elif value >= 0 and (unit_positive==False):
                number /= tans_unit
            else:
                continue

            value -= 1
        #print('number=', number)
        return number

    def _special_len(self,unit_distance):
        number = 1
        unit_positive=True
        #print('unit_distance',unit_distance)
        if unit_distance >0:
            number*=1000
        else:
            unit_distance = -unit_distance
            unit_positive = False
            number/=1000
        #print('number befor loop',number)
        for value in range(unit_distance):
            if value >=1 and unit_positive:
                number *= 10
            elif value >=1 and (unit_positive==False):
                number/=10
            value-=1
        #print('number=', number)

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
