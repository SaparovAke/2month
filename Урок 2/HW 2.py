
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        a = self.__cpu + self.__memory
        b = self.__cpu - self.__memory
        c = self.__cpu * self.__memory
        d = self.__cpu / self.__memory
        return f'cpu:{self.__cpu} + memory: {self.__memory} = {a}\n' \
               f'cpu:{self.__cpu} - memory: {self.__memory} = {b}\n' \
               f'cpu:{self.__cpu} * memory: {self.__memory} = {c}\n' \
               f'cpu:{self.__cpu} / memory: {self.__memory} = {d}'

class Phone(Computer):