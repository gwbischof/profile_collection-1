from ophyd.quadem import QuadEM

from ophyd import (EpicsSignalRO, EpicsSignal, Component as Cpt,
               DynamicDeviceComponent as DDCpt, Signal)
from ophyd import AreaDetector, SingleTrigger, HDF5Plugin, TIFFPlugin
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd.areadetector.filestore_mixins import FileStoreTIFFIterativeWrite
from ophyd.areadetector import (ADComponent as ADCpt, EpicsSignalWithRBV,
                           ImagePlugin, StatsPlugin, DetectorBase,
                           SingleTrigger)

class HDF5PluginWithFileStore(HDF5Plugin, FileStoreHDF5IterativeWrite):
    pass
    # AD v2.2.0 (at least) does not have this. It is present in v1.9.1.
    # file_number_sync = None


class TIFFPluginWithFileStore(TIFFPlugin, FileStoreTIFFIterativeWrite):
    pass


class ESMQuadEM(QuadEM):
    port_name = Cpt(Signal, value='EM180')
    em_range = Cpt(EpicsSignalWithRBV, 'Range', string=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #for c in ['current{}'.format(j) for j in range(1, 5)]:
        #     getattr(self, c).read_attrs = ['mean_value']
            
        # self.read_attrs = ['current{}'.format(j) for j in range(1, 5)]
        self.stage_sigs.update([(self.acquire_mode, 'Single')  # single mode
                                ])
        self.configuration_attrs = ['integration_time', 'averaging_time','em_range','num_averaged','values_per_read']

qem01 = ESMQuadEM('XF:21IDA-BI{EM:1}EM180:', name='qem01')
qem02 = ESMQuadEM('XF:21IDB-BI{EM:2}EM180:', name='qem02')
qem03 = ESMQuadEM('XF:21IDB-BI{EM:3}EM180:', name='qem03')
qem04 = ESMQuadEM('XF:21IDB-BI{EM:4}EM180:', name='qem04')
qem05 = ESMQuadEM('XF:21IDB-BI{EM:5}EM180:', name='qem05')

qem06 = ESMQuadEM('XF:21IDC-BI{EM:6}EM180:', name='qem06')
qem07 = ESMQuadEM('XF:21IDC-BI{EM:7}EM180:', name='qem07')
qem08 = ESMQuadEM('XF:21IDC-BI{EM:8}EM180:', name='qem08')
qem09 = ESMQuadEM('XF:21IDC-BI{EM:9}EM180:', name='qem09')
qem10 = ESMQuadEM('XF:21IDC-BI{EM:10}EM180:', name='qem10')


class MyDetector(SingleTrigger, AreaDetector):
#    tiff = Cpt(TIFFPluginWithFileStore,
#               suffix='TIFF1:',
#               write_path_template='/direct/XF21ID1/image_files/',  # trailing slash!
#               read_path_template='/direct/XF21ID1/image_files/')
          
    hdf5 = Cpt(HDF5PluginWithFileStore,
               suffix='HDF1:',
               write_path_template='/direct/XF21ID1/image_files/',  # trailing slash!
               read_path_template='/direct/XF21ID1/image_files/')
    
Diag1_CamH = MyDetector('XF:21IDA-BI{Diag:1-Cam:H}', name='Diag1_CamH')
Diag1_CamH.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam01/'
Diag1_CamH.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam01/'
Diag1_CamH.read_attrs = ['hdf5']
Diag1_CamH.hdf5.read_attrs = []


Diag1_CamV = MyDetector('XF:21IDA-BI{Diag:1-Cam:V}', name='Diag1_CamV')
Diag1_CamV.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam02/'
Diag1_CamV.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam02/'
Diag1_CamV.read_attrs = ['hdf5']
Diag1_CamV.hdf5.read_attrs = []


Lock23A_CamEA3_1 = MyDetector('XF:21IDC-BI{BT:B2-Diag:B2_1}', name='Lock23A_CamEA3_1')
Lock23A_CamEA3_1.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam03/'
Lock23A_CamEA3_1.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam03/'
Lock23A_CamEA3_1.read_attrs = ['hdf5']
Lock23A_CamEA3_1.hdf5.read_attrs = []

Lock14A_CamEA4_1 = MyDetector('XF:21IDD-BI{Lock1:4A-Cam:EA4_1}', name='Lock14A_CamEA4_1')
Lock14A_CamEA4_1.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam04/'
Lock14A_CamEA4_1.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam04/'
Lock14A_CamEA4_1.read_attrs = ['hdf5']
Lock14A_CamEA4_1.hdf5.read_attrs = []

Prep2A_CamEA2_1 = MyDetector('XF:21IDD-BI{Prep:2A-Cam:EA2_1}', name='Prep2A_CamEA2_1')
Prep2A_CamEA2_1.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam05/'
Prep2A_CamEA2_1.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam05/'
Prep2A_CamEA2_1.read_attrs = ['hdf5']
Prep2A_CamEA2_1.hdf5.read_attrs = []

Mir3_Cam10_U_1 = MyDetector('XF:21IDB-BI{Mir:3-Cam:10_U_1}', name='Mir3_Cam10_U_1')
Mir3_Cam10_U_1.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam06/'
Mir3_Cam10_U_1.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam06/'
Mir3_Cam10_U_1.read_attrs = ['hdf5']
Mir3_Cam10_U_1.hdf5.read_attrs = []

BC1_Diag1_U_1 = MyDetector('XF:21IDA-BI{BC:1-Diag:1_U_1}', name='BC1_Diag1_U_1')
BC1_Diag1_U_1.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam07/'
BC1_Diag1_U_1.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam07/'
BC1_Diag1_U_1.read_attrs = ['hdf5']
BC1_Diag1_U_1.hdf5.read_attrs = []

BTA2_DiagA2_1 = MyDetector('XF:21IDC-BI{BT:A2-Diag:A2_1}', name='BTA2_DiagA2_1')
BTA2_DiagA2_1.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam08/'
BTA2_DiagA2_1.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam08/'
BTA2_DiagA2_1.read_attrs = ['hdf5']
BTA2_DiagA2_1.hdf5.read_attrs = []

BTB2_DiagB2_1 = MyDetector('XF:21IDC-BI{BT:B2-Diag:B2_1}', name='B2BT_DiagB2_1')
BTB2_DiagB2_1.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam09/'
BTB2_DiagB2_1.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam09/'
BTB2_DiagB2_1.read_attrs = ['hdf5']
BTB2_DiagB2_1.hdf5.read_attrs = []

Anal1A_Camlens = MyDetector('XF:21IDD-BI{Anal:1A-Cam:lens}', name='Anal1A_Camlens')
Anal1A_Camlens.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam10/'
Anal1A_Camlens.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam10/'
Anal1A_Camlens.read_attrs = ['hdf5']
Anal1A_Camlens.hdf5.read_attrs = []

Anal1A_Cambeam = MyDetector('XF:21IDD-BI{Anal:1A-Cam:beam}', name='Anal1A_Cambeam')
Anal1A_Cambeam.hdf5.write_path_template = '/direct/XF21ID1/image_files/cam11/'
Anal1A_Cambeam.hdf5.read_path_template = '/direct/XF21ID1/image_files/cam11/'
Anal1A_Cambeam.read_attrs = ['hdf5']
Anal1A_Cambeam.hdf5.read_attrs = []