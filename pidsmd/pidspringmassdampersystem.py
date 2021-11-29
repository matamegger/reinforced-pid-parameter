import ctypes
import os
import platform
from pidsmd.bindings import *

class PidSpringMassDamperSystem:
    def __init__(self, model="pid_smd"):
        self.model = model
        directory = os.path.dirname(__file__)
        if platform.system() == "Linux":
            self.dll_path = os.path.join(directory, f"{model}.so")
            self.dll = ctypes.cdll.LoadLibrary(self.dll_path)
        elif platform.system() == "Darwin":
            self.dll_path = os.path.join(directory, f"{model}.dylib")
            self.dll = ctypes.cdll.LoadLibrary(self.dll_path)
        elif platform.system() == "Windows":
            self.dll_path = os.path.join(directory, f"{model}_win64.dll")
            self.dll = ctypes.windll.LoadLibrary(self.dll_path)
        else:
            raise Exception("System Not Supported")

        # System method initializers
        self.__initialize = getattr(self.dll, "SpringMassDamper_PID_initialize")
        self.__step = getattr(self.dll, "SpringMassDamper_PID_step")
        self.__terminate = getattr(self.dll, "SpringMassDamper_PID_terminate")

        # System field initializers
        self.rtInf = real_T.in_dll(self.dll, "rtInf")
        self.rtMinusInf = real_T.in_dll(self.dll, "rtMinusInf")
        self.rtNaN = real_T.in_dll(self.dll, "rtNaN")
        self.rtInfF = real32_T.in_dll(self.dll, "rtInfF")
        self.rtMinusInfF = real32_T.in_dll(self.dll, "rtMinusInfF")
        self.rtNaNF = real32_T.in_dll(self.dll, "rtNaNF")
        self.parameters = P_SpringMassDamper_PID_T.in_dll(self.dll, "SpringMassDamper_PID_P")
        self.signals = B_SpringMassDamper_PID_T.in_dll(self.dll, "SpringMassDamper_PID_B")
        self.SpringMassDamper_PID_X = X_SpringMassDamper_PID_T.in_dll(self.dll, "SpringMassDamper_PID_X")
        self.SpringMassDamper_PID_DW = DW_SpringMassDamper_PID_T.in_dll(self.dll, "SpringMassDamper_PID_DW")
        self.inputs = ExtU_SpringMassDamper_PID_T.in_dll(self.dll, "SpringMassDamper_PID_U")
        self.outputs = ExtY_SpringMassDamper_PID_T.in_dll(self.dll, "SpringMassDamper_PID_Y")
        self.b = real_T.in_dll(self.dll, "b")
        self.SpringMassDamper_PID_M = ctypes.POINTER(RT_MODEL_SpringMassDamper_PID_T).in_dll(self.dll, "SpringMassDamper_PID_M")

    def initialize(self):
        self.__initialize()

    def step(self):
        self.__step()

    def terminate(self):
        self.__terminate()

