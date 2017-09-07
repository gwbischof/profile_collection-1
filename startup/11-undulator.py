from ophyd import (PVPositioner, Component as Cpt, EpicsSignal, EpicsSignalRO,
                   Device)
from ophyd.utils import ReadOnlyError
import time as ttime




class UgapPositioner(PVPositioner):
    readback = Cpt(EpicsSignalRO, '-Ax:Gap}Mtr.RBV')
    setpoint = Cpt(EpicsSignal, '-Ax:Gap}Mtr')
    actuate = Cpt(EpicsSignal, '}Cmd:Start-Cmd', string=True)
    actuate_value = 'On'

    stop_signal = Cpt(EpicsSignal, '}Cmd:Stop-Cmd')
    stop_value = 1

    done = Cpt(EpicsSignal, '}Cmd:Start-Cmd')
    done_value = 0

    kill_switch_pressed = Cpt(EpicsSignalRO, '}Sts:Kill-Sts')
    safety_device_fail = Cpt(EpicsSignalRO, '}Sts:Safety-Sts', string=True)
    emergency_open_gap = Cpt(EpicsSignalRO, '}Sts:OpenGapCmd-Sts', string=True)
    # TODO subscribe kill switch pressed and stop motion

class UphasePositioner(PVPositioner):
    readback = Cpt(EpicsSignalRO, '-Ax:Phase}Mtr.RBV')
    setpoint = Cpt(EpicsSignal, '-Ax:Phase}Mtr')
    actuate = Cpt(EpicsSignal, '}Cmd:Start-Cmd', string=True)
    actuate_value = 'On'

    stop_signal = Cpt(EpicsSignal, '}Cmd:Stop-Cmd')
    stop_value = 1

    done = Cpt(EpicsSignal, '}Cmd:Start-Cmd')
    done_value = 0

    kill_switch_pressed = Cpt(EpicsSignalRO, '}Sts:Kill-Sts')
    safety_device_fail = Cpt(EpicsSignalRO, '}Sts:Safety-Sts', string=True)
    emergency_open_gap = Cpt(EpicsSignalRO, '}Sts:OpenGapCmd-Sts', string=True)
    # TODO subscribe kill switch pressed and stop motion

class EPU(Device):
    gap = Cpt(UgapPositioner, '', settle_time=0)
    phase = Cpt(UphasePositioner, '', settle_time=0)
    
EPU57 = EPU('SR:C21-ID:G1A{EPU:1', name='EPU57')
EPU57.gap.read_attrs = ['setpoint', 'readback']
EPU57.gap.readback.name='EPU57_gap'
EPU57.phase.read_attrs = ['setpoint', 'readback']
EPU57.phase.readback.name='EPU57_phase'
EPU57.hints={'fields':[EPU57.gap.name,EPU57.phase.name]}

EPU105 = EPU('SR:C21-ID:G1B{EPU:2', name='EPU105')
EPU105.gap.read_attrs = ['setpoint', 'readback']
EPU105.gap.readback.name='EPU105_gap'
EPU105.phase.read_attrs = ['setpoint', 'readback']
EPU105.phase.readback.name='EPU105_phase'
EPU105.hints={'fields':[EPU105.gap.name,EPU105.phase.name]}



class Source(Device):
    #This is a class to be used to define the readback values of the beam source front the
    #front end.

        #define the channels in the readback device.
        Current=Comp(EpicsSignalRO,'OPS-BI{DCCT:1}I:Real-I')
        Xoffset=Comp(EpicsSignalRO,'C31-{AI}Aie21:Offset-x-Cal')
        Xangle=Comp(EpicsSignalRO,'C31-{AI}Aie21:Angle-x-Cal')
        Yoffset=Comp(EpicsSignalRO,'C31-{AI}Aie21:Offset-y-Cal')
        Yangle=Comp(EpicsSignalRO,'C31-{AI}Aie21:Angle-y-Cal')
        

BeamSource = Source('SR:',name='BeamSource')
BeamSource.hints = {'fields': ['BeamSource_Current','BeamSource_Xoffset','BeamSource_Xangle',
                                 'BeamSource_Yoffset','BeamSource_Yangle' ] }
