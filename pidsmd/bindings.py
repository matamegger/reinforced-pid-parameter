import ctypes
from enum import Enum
enum_SimTimeStep = ctypes.c_int

enum_ssMatrixType = ctypes.c_int

enum_SolverMode = ctypes.c_int

enum_slJmBdControl = ctypes.c_int

real32_T = ctypes.c_float

boolean_T = ctypes.c_ubyte

real64_T = ctypes.c_double

uint32_T = ctypes.c_uint

char_T = ctypes.c_char

int_T = ctypes.c_int

uint8_T = ctypes.c_ubyte

rtMdlInitializeSizesFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

rtMdlInitializeSampleTimesFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

rtMdlStartFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

rtMdlDerivativesFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

rtMdlProjectionFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

rtMdlMassMatrixFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

rtMdlForcingFunctionFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

rtMdlTerminateFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

class SimTimeStep(Enum):
    MINOR_TIME_STEP = 0
    MAJOR_TIME_STEP = 1

class ssMatrixType(Enum):
    SS_MATRIX_NONE = 0
    SS_MATRIX_CONSTANT = 1
    SS_MATRIX_TIMEDEP = 2
    SS_MATRIX_STATEDEP = 3

class SolverMode(Enum):
    SOLVER_MODE_AUTO = 0
    SOLVER_MODE_SINGLETASKING = 1
    SOLVER_MODE_MULTITASKING = 2

class slJmBdControl(Enum):
    SL_JM_BD_AUTO = 0
    SL_JM_BD_SPARSE_PERTURBATION = 1
    SL_JM_BD_FULL_PERTURBATION = 2
    SL_JM_BD_SPARSE_ANALYTICAL = 3
    SL_JM_BD_FULL_ANALYTICAL = 4

real_T = real64_T

rtMdlOutputsFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p, int_T)

rtMdlUpdateFcn = ctypes.CFUNCTYPE(None, ctypes.c_void_p, int_T)

class tag_RTM_SpringMassDamper_PID_T_Sizes(ctypes.Structure):

    __slots__ = [
        'numContStates',
        'numPeriodicContStates',
        'numSampTimes'
    ]

    _fields_ = [
        ('numContStates', int_T),
        ('numPeriodicContStates', int_T),
        ('numSampTimes', int_T)
    ]

time_T = real_T

class B_SpringMassDamper_PID_T(ctypes.Structure):

    __slots__ = [
        'error',
        'v',
        'Multiply4'
    ]

    _fields_ = [
        ('error', real_T),
        ('v', real_T),
        ('Multiply4', real_T)
    ]

class DW_SpringMassDamper_PID_T(ctypes.Structure):

    __slots__ = [
        'TimeStampA',
        'LastUAtTimeA',
        'TimeStampB',
        'LastUAtTimeB'
    ]

    _fields_ = [
        ('TimeStampA', real_T),
        ('LastUAtTimeA', real_T),
        ('TimeStampB', real_T),
        ('LastUAtTimeB', real_T)
    ]

class X_SpringMassDamper_PID_T(ctypes.Structure):

    __slots__ = [
        'Integrator2_CSTATE',
        'Integrator_CSTATE',
        'Integrator3_CSTATE'
    ]

    _fields_ = [
        ('Integrator2_CSTATE', real_T),
        ('Integrator_CSTATE', real_T),
        ('Integrator3_CSTATE', real_T)
    ]

class ExtU_SpringMassDamper_PID_T(ctypes.Structure):

    __slots__ = [
        'u_position'
    ]

    _fields_ = [
        ('u_position', real_T)
    ]

class ExtY_SpringMassDamper_PID_T(ctypes.Structure):

    __slots__ = [
        'position'
    ]

    _fields_ = [
        ('position', real_T)
    ]

class P_SpringMassDamper_PID_T_(ctypes.Structure):

    __slots__ = [
        'Kd',
        'Ki',
        'Kp',
        'k',
        'm',
        'Integrator2_IC',
        'Integrator_IC',
        'Integrator3_IC'
    ]

    _fields_ = [
        ('Kd', real_T),
        ('Ki', real_T),
        ('Kp', real_T),
        ('k', real_T),
        ('m', real_T),
        ('Integrator2_IC', real_T),
        ('Integrator_IC', real_T),
        ('Integrator3_IC', real_T)
    ]

class ODE3_IntgData(ctypes.Structure):

    __slots__ = [
        'y',
        'f'
    ]

    _fields_ = [
        ('y', ctypes.POINTER(real_T)),
        ('f', (ctypes.POINTER(real_T)*3))
    ]

class _RTWRTModelMethodsInfo_tag(ctypes.Structure):

    __slots__ = [
        'rtModelPtr',
        'rtmInitSizesFcn',
        'rtmInitSampTimesFcn',
        'rtmStartFcn',
        'rtmOutputsFcn',
        'rtmUpdateFcn',
        'rtmDervisFcn',
        'rtmProjectionFcn',
        'rtmMassMatrixFcn',
        'rtmForcingFunctionFcn',
        'rtmTerminateFcn'
    ]

    _fields_ = [
        ('rtModelPtr', ctypes.c_void_p),
        ('rtmInitSizesFcn', rtMdlInitializeSizesFcn),
        ('rtmInitSampTimesFcn', rtMdlInitializeSampleTimesFcn),
        ('rtmStartFcn', rtMdlStartFcn),
        ('rtmOutputsFcn', rtMdlOutputsFcn),
        ('rtmUpdateFcn', rtMdlUpdateFcn),
        ('rtmDervisFcn', rtMdlDerivativesFcn),
        ('rtmProjectionFcn', rtMdlProjectionFcn),
        ('rtmMassMatrixFcn', rtMdlMassMatrixFcn),
        ('rtmForcingFunctionFcn', rtMdlForcingFunctionFcn),
        ('rtmTerminateFcn', rtMdlTerminateFcn)
    ]

P_SpringMassDamper_PID_T = P_SpringMassDamper_PID_T_

RTWRTModelMethodsInfo = _RTWRTModelMethodsInfo_tag

class tag_RTM_SpringMassDamper_PID_T_Timing(ctypes.Structure):

    __slots__ = [
        'clockTick0',
        'clockTickH0',
        'stepSize0',
        'clockTick1',
        'clockTickH1',
        'simTimeStep',
        'stopRequestedFlag',
        't',
        'tArray'
    ]

    _fields_ = [
        ('clockTick0', uint32_T),
        ('clockTickH0', uint32_T),
        ('stepSize0', time_T),
        ('clockTick1', uint32_T),
        ('clockTickH1', uint32_T),
        ('simTimeStep', enum_SimTimeStep),
        ('stopRequestedFlag', boolean_T),
        ('t', ctypes.POINTER(time_T)),
        ('tArray', (time_T*2))
    ]

class _ssSolverInfo_tag(ctypes.Structure):

    __slots__ = [
        'rtModelPtr',
        'simTimeStepPtr',
        'solverData',
        'solverName',
        'isVariableStepSolver',
        'solverNeedsReset',
        'solverMode',
        'solverStopTime',
        'stepSizePtr',
        'minStepSize',
        'maxStepSize',
        'fixedStepSize',
        'solverShapePreserveControl',
        'solverMaxConsecutiveMinStep',
        'maxNumMinSteps',
        'solverMaxOrder',
        'solverConsecutiveZCsStepRelTol',
        'solverMaxConsecutiveZCs',
        'solverExtrapolationOrder',
        'solverNumberNewtonIterations',
        'solverRefineFactor',
        'solverRelTol',
        'unused_real_T_1',
        'dXPtr',
        'tPtr',
        'numContStatesPtr',
        'contStatesPtr',
        'numPeriodicContStatesPtr',
        'periodicContStateIndicesPtr',
        'periodicContStateRangesPtr',
        'zcSignalVector',
        'zcEventsVector',
        'zcSignalAttrib',
        'zcSignalVectorLength',
        'reserved',
        'foundContZcEvents',
        'isAtLeftPostOfContZcEvent',
        'isAtRightPostOfContZcEvent',
        'adaptiveZcDetection',
        'numZcSignals',
        'stateProjection',
        'robustResetMethod',
        'updateJacobianAtReset',
        'consistencyChecking',
        'massMatrixType',
        'massMatrixNzMax',
        'massMatrixIr',
        'massMatrixJc',
        'massMatrixPr',
        'errStatusPtr',
        'modelMethodsPtr',
        'zcThreshold',
        'zeroCrossAlgorithm',
        'consecutiveZCsError',
        'CTOutputIncnstWithState',
        'isComputingJacobian',
        'solverJacobianMethodControl',
        'ignoredZcDiagnostic',
        'maskedZcDiagnostic',
        'isOutputMethodComputed',
        'maxZcBracketingIterations',
        'isMinorOutputWithModeChange',
        'maxZcPerIntegrationInterval'
    ]

    _fields_ = [
        ('rtModelPtr', ctypes.c_void_p),
        ('simTimeStepPtr', ctypes.POINTER(enum_SimTimeStep)),
        ('solverData', ctypes.c_void_p),
        ('solverName', ctypes.POINTER(char_T)),
        ('isVariableStepSolver', boolean_T),
        ('solverNeedsReset', boolean_T),
        ('solverMode', enum_SolverMode),
        ('solverStopTime', time_T),
        ('stepSizePtr', ctypes.POINTER(time_T)),
        ('minStepSize', time_T),
        ('maxStepSize', time_T),
        ('fixedStepSize', time_T),
        ('solverShapePreserveControl', int_T),
        ('solverMaxConsecutiveMinStep', int_T),
        ('maxNumMinSteps', int_T),
        ('solverMaxOrder', int_T),
        ('solverConsecutiveZCsStepRelTol', real_T),
        ('solverMaxConsecutiveZCs', int_T),
        ('solverExtrapolationOrder', int_T),
        ('solverNumberNewtonIterations', int_T),
        ('solverRefineFactor', int_T),
        ('solverRelTol', real_T),
        ('unused_real_T_1', real_T),
        ('dXPtr', ctypes.POINTER(ctypes.POINTER(real_T))),
        ('tPtr', ctypes.POINTER(ctypes.POINTER(time_T))),
        ('numContStatesPtr', ctypes.POINTER(int_T)),
        ('contStatesPtr', ctypes.POINTER(ctypes.POINTER(real_T))),
        ('numPeriodicContStatesPtr', ctypes.POINTER(int_T)),
        ('periodicContStateIndicesPtr', ctypes.POINTER(ctypes.POINTER(int_T))),
        ('periodicContStateRangesPtr', ctypes.POINTER(ctypes.POINTER(real_T))),
        ('zcSignalVector', ctypes.POINTER(real_T)),
        ('zcEventsVector', ctypes.POINTER(uint8_T)),
        ('zcSignalAttrib', ctypes.POINTER(uint8_T)),
        ('zcSignalVectorLength', int_T),
        ('reserved', ctypes.POINTER(uint8_T)),
        ('foundContZcEvents', boolean_T),
        ('isAtLeftPostOfContZcEvent', boolean_T),
        ('isAtRightPostOfContZcEvent', boolean_T),
        ('adaptiveZcDetection', boolean_T),
        ('numZcSignals', int_T),
        ('stateProjection', boolean_T),
        ('robustResetMethod', boolean_T),
        ('updateJacobianAtReset', boolean_T),
        ('consistencyChecking', boolean_T),
        ('massMatrixType', enum_ssMatrixType),
        ('massMatrixNzMax', int_T),
        ('massMatrixIr', ctypes.POINTER(int_T)),
        ('massMatrixJc', ctypes.POINTER(int_T)),
        ('massMatrixPr', ctypes.POINTER(real_T)),
        ('errStatusPtr', ctypes.POINTER(ctypes.POINTER(char_T))),
        ('modelMethodsPtr', ctypes.POINTER(RTWRTModelMethodsInfo)),
        ('zcThreshold', real_T),
        ('zeroCrossAlgorithm', int_T),
        ('consecutiveZCsError', int_T),
        ('CTOutputIncnstWithState', boolean_T),
        ('isComputingJacobian', boolean_T),
        ('solverJacobianMethodControl', enum_slJmBdControl),
        ('ignoredZcDiagnostic', int_T),
        ('maskedZcDiagnostic', int_T),
        ('isOutputMethodComputed', boolean_T),
        ('maxZcBracketingIterations', int_T),
        ('isMinorOutputWithModeChange', boolean_T),
        ('maxZcPerIntegrationInterval', int_T)
    ]

ssSolverInfo = _ssSolverInfo_tag

RTWSolverInfo = ssSolverInfo

class tag_RTM_SpringMassDamper_PID_T(ctypes.Structure):

    __slots__ = [
        'errorStatus',
        'solverInfo',
        'contStates',
        'periodicContStateIndices',
        'periodicContStateRanges',
        'derivs',
        'contStateDisabled',
        'zCCacheNeedsReset',
        'derivCacheNeedsReset',
        'CTOutputIncnstWithState',
        'odeY',
        'odeF',
        'intgData',
        'Sizes',
        'Timing'
    ]

    _fields_ = [
        ('errorStatus', ctypes.POINTER(char_T)),
        ('solverInfo', RTWSolverInfo),
        ('contStates', ctypes.POINTER(X_SpringMassDamper_PID_T)),
        ('periodicContStateIndices', ctypes.POINTER(int_T)),
        ('periodicContStateRanges', ctypes.POINTER(real_T)),
        ('derivs', ctypes.POINTER(real_T)),
        ('contStateDisabled', ctypes.POINTER(boolean_T)),
        ('zCCacheNeedsReset', boolean_T),
        ('derivCacheNeedsReset', boolean_T),
        ('CTOutputIncnstWithState', boolean_T),
        ('odeY', (real_T*3)),
        ('odeF', ((real_T*3)*3)),
        ('intgData', ODE3_IntgData),
        ('Sizes', tag_RTM_SpringMassDamper_PID_T_Sizes),
        ('Timing', tag_RTM_SpringMassDamper_PID_T_Timing)
    ]

RT_MODEL_SpringMassDamper_PID_T = tag_RTM_SpringMassDamper_PID_T

