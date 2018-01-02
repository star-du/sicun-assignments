#!/usr/bin/env python3

'''
    final exam - simple calculus utility

    Goal:
        In[1]:  euqation: 2 * (x ** 3)  # or any other polynomials in
                                        # standard Python literal format
        Out[1]: result ==> 4999.99xx    # a 4-decimal-place 5000.0-ish value

    Bonus No.1:
        try to read the docs, and utilize **matplotlib** to visualize how the
        error is going down during the calculation process

    Bonus No.2:
        not just polynomials, try equations like "sin(cos(x))"

    Bonus No.3:
        performance optimization, both wiki and your own version are accepted

    Bonus No.4:
        share what you've learned with others at your_github_id.github.io

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    NOTE:
        Readability Counts
        Simplicity Counts
        Documentation and Comments Counts

    Deadline:
        push your `integral_answersheet.py` file to your GitHub Repo

                  before 2017.12.31 12:00 AM
'''

__author__ = 'Star Du'


import matplotlib.pyplot as plt
import numpy as np
import logging
logging.getLogger().setLevel(0)


class Integral:
    '''
    The Solution Class

        substitute the `pass` statements with your own code,
        you are allowed to define your own functions in order to keep your
        code clean

    Usage:
        In[1]:  Integral("2 * (x ** 3)", 0, 10)()
        Out[1]: 4999.99xx

        In[2]:  result = Integral("2 * (x ** 3)", 0, 10)
        In[3]:  result()
        Out[3]: 4999.99xx
    '''
    def __init__(self, equation, start, end,
                 default_step=1,visual='off'):
        '''
        Initialize the solution class

        Args:
            equation        - `eval()`-able string like
                              "2 * (x ** 3) - 4 * (x ** 0.5)", where `x` is
                              the placeholder
            start           - integral start
            end             - integral end
            default_step    - float
            visual          - string
                            when 'on' is entered, two graphs will be shown to
                            illustrate the function and the change of the error

        Return:
            the integral value
        '''
        self._equation = equation
        self._start = start
        self._end = end
        self._default_step = default_step
        self.visual=visual
        # test if equation is valid
        try:
            eval(equation.replace('x', '123'))
        except SyntaxError: # equation not valid
            print("Unsupported expression!")


    def __call__(self, *args, **kwargs):
        """
        Do the calculation and return the value
        """
        if self.visual == 'on':
            x = np.linspace(eval(start), eval(end), 50)
            plt.plot(x, eval(equation))
            plt.title('y={}'.format(equation))
            plt.show()
        counter = 1
        result = {}
        y=[]
        while 1:
            result[counter]=0
            if counter == 1:
                i=self._start
                while i < self._end:
                    result[counter] += eval(equation.replace('x', repr(i))) * self._default_step
                    i = i + self._default_step
            else:
                i = self._start + self._default_step
                while i < self._end:
                    result[counter] += eval(equation.replace('x', repr(i))) * self._default_step
                    i = i + self._default_step * 2
                result[counter] += result[counter-1]/2
                error = abs(result[counter-1]-result[counter])
                y.append(error)
                if error < 0.001:
                    if self.visual == 'on':
                        plt.plot(tuple(y),'ro')
                        plt.title("the graph of the error")
                        plt.show()
                    return result[counter]
            self._default_step = self._default_step / 2
            #print("result of the run is {}".format(result[counter]))
            logging.debug("result of the {0} run is {1:.4f}".format(counter,result[counter]))
            counter+=1





# Testing

if __name__ == '__main__':
    print("Hint:to use functions and constants,add 'np.' "
          "before the expression")
    equation = input("equation: ")
    start = input("start from:")
    end = input("ends at:")
    visualize = input("visualize on/off:")
    # get equation from user
    # test run:
    #   integral from 0 to 10 ( equation ) dx
   # print("final result ==> {0:.4f}".format( Integral(equation, 0,10)() ))
    r = Integral(equation,eval(start),eval(end),visual=visualize)
    print("final result ==> {0:.4f}".format(r()))




