# Description Here

import math
from os import name
import time
import threading

def round_dec(num, places = 9):
    '''
    Rounds the provided number to a specific number of decimal places (defaulted to 2)
    '''

    multiplier = 10 ** places

    return math.trunc(num * multiplier) / multiplier


class Runtime():
    '''
    Runtime was created for monitoring the runtime over a given period. 
    If printing occurs, it does so on a different thread so as to minimize impact
    to computation 
    '''

    def __init__(self, name="Runtime", unit="all", print=True, precision=3):
        '''
        name => The name of the runtime instance

        unit => - "all" is for showing all units dynamically
                - "sec" is for showing seconds only
                - "ms" is for showing milliseconds
                - "us" is for showing microseconds
                - "ns" is for showing nanoseconds

        print => When true, runtime will print to console

        precision => denotes the number of decimal places to include in runtime calculation
        '''
        self.name = name
        self.print = print
        self.precision = precision

        self.unit = "all" if unit not in ["all", "ns", "us", "ms", "sec"] else unit
        self.cur_unit = self.unit

        self.stop_flag = False
        self.pause_flag = False
        self.start_time = 0

    def start(self):
        '''
        Starts the runtime counter and generated a print thread if needed
        '''

        # Get the start time of the count
        self.start_time = time.time()
        self.elapsed_time = 0

        self.pause_flag = False
        self.stop_flag = False

        # Generate thread if print is needed
        if self.print:
            self.printer = threading.Thread(target=self.print_runtime)
            self.printer.start()


    def pause(self):
        '''
        Pauses the current runtime count
        Saves the total elapsed time and terms print thread if printing
        ''' 

        # Updated total elapsed time
        self.elapsed_time += time.time() - self.start_time
        
        self.pause_flag = True

        # Term the thread when not needed
        if self.print: 
            self.printer.join()

    def unpause(self):
        '''
        Continues a runtime timer after a pause and creates print thread as needed
        '''

        if self.pause_flag:

            # Get the start time of the count
            self.start_time = time.time()

            self.pause_flag = False
            self.stop_flag = False

            # Generate thread if print is needed
            if self.print:
                self.printer = threading.Thread(target=self.print_runtime)
                self.printer.start()

    def stop(self):
        '''
        Stopes a runtime timer and terms thread as needed
        '''

        self.stop_flag = True
        self.end_time = time.time()
        
        # Updated total elapsed time
        self.elapsed_time += self.end_time - self.start_time

        # Term the thread when not needed
        if self.print: 
            self.printer.join()

    def print_runtime(self):
        
        formatting = "dynamic" if self.unit == "all" or self.unit == "none" else "static"

        while not self.stop_flag and not self.pause_flag:
            
            if formatting == "static":
                time_str = self.static_formatting(self.elapsed_time + (time.time() - self.start_time))
            elif formatting == "dynamic":
                time_str = self.dynamic_formatting(self.elapsed_time + ((time.time() - self.start_time)))

            print(f"{self.name} (Running) : {time_str}  ", end="\r")

        if formatting == "static":
            time_str = self.static_formatting(self.elapsed_time)
        elif formatting == "dynamic":
            time_str = self.dynamic_formatting(self.elapsed_time)
        
        if self.pause_flag:
            print(f"{self.name} (Paused) : {time_str}   ", end="\r")
        elif self.end_time:
            print(f"{self.name} (Ended) : {time_str}    ")

    # TODO: Unit updating and time formatting!

    def static_formatting(self, time):

        if self.unit == "ns":
            factor = 10 ** 9
        elif self.unit == "us":
            factor = 10 ** 6
        elif self.unit == "ms":
            factor = 10 ** 3
        else:
            factor = 1

        return f"{round_dec((time * factor), self.precision)} {self.unit}"

    def dynamic_formatting(self, time):

        if self.unit == "all":
            self.cur_unit = "ns"
            self.unit = "none"
        
        # Determine if new unit is needed for current time

        while True:
            if self.cur_unit == "ns":
                calc_time = round_dec((time * (10 ** 9)), self.precision)

                if calc_time < 999:
                    return f"{calc_time} {self.cur_unit}"
                else:
                    self.cur_unit = "us"
            elif self.cur_unit == "us":
                calc_time = round_dec((time * (10 ** 6)), self.precision)
                
                if calc_time < 999:
                    return f"{calc_time} {self.cur_unit}"
                else:
                    self.cur_unit = "ms"
            elif self.cur_unit == "ms":
                calc_time = round_dec((time * (10 ** 3)), self.precision)
                
                if calc_time < 999:
                    return f"{calc_time} {self.cur_unit}"
                else:
                    self.cur_unit = "sec"
            elif self.cur_unit == "sec":
                calc_time = round_dec((time), self.precision)

                if calc_time < 60:
                    return f"{calc_time} {self.cur_unit}"
                else:
                    self.cur_unit = "min"
            elif self.cur_unit == "min":

                minutes = math.floor(time / 60)

                if minutes < 60:
                    seconds = round_dec((time % 60), self.precision)

                    if minutes > 1:
                        return f"{minutes} min  {seconds} sec"
                    else:
                        return f"{minutes} mins  {seconds} sec"
                else:
                    self.cur_unit = "hr"
            elif self.cur_unit == "hr":

                minutes = time / 60

                hours = math.floor(minutes / 60)

                minutes = math.floor(minutes % 60)

                seconds = (time % 60)

                hr_u = "hrs" if hours > 1 else "hr"
                mn_u = "mins" if minutes > 1 else "min"

                return f"{hours} {hr_u}  {minutes} {mn_u}  {seconds} sec"


