import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import ultimate_oscillator


class TestUltimateOscillator(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()
        self.low_data = SampleData().get_sample_close_data()

        self.buying_pressure_expected = [np.nan, 10.42999999999995,
        1.6900000000000546, 5.3599999999999, 0.0, 1.8799999999999955,
        2.5200000000000955, 3.0, 0.0, 0.0, 5.8099999999999454,
        2.2400000000000091, 0.0, 0.0, 1.5500000000000682, 0.0, 0.0, 0.0,
        2.0400000000000773, 0.0, 0.0, 11.549999999999955, 13.560000000000059,
        0.0, 0.0, 0.0, 6.0, 0.0, 0.0, 10.189999999999941, 0.0, 0.0, 0.0,
        18.529999999999973, 8.5399999999999636, 25.300000000000068,
        6.3899999999999864, 0.0, 0.0, 1.0900000000000318, 6.2299999999999045,
        17.060000000000059, 4.4199999999999591, 9.6599999999999682, 0.0, 4.75,
        6.4499999999999318, 7.1900000000000546, 0.0, 0.0, 5.4600000000000364,
        0.0, 0.0, 0.0, 0.0, 7.6899999999999409, 0.0, 4.5999999999999091, 0.0,
        2.3700000000000045, 0.0, 1.5599999999999454, 0.0, 3.67999999999995, 0.0,
        7.4199999999999591, 0.67000000000007276, 0.0, 12.310000000000059,
        0.99000000000000909, 0.0, 0.0, 0.0, 2.5800000000000409,
        3.2599999999999909, 0.0, 0.0, 10.100000000000023, 0.0,
        14.360000000000014, 5.1499999999999773, 0.029999999999972715, 0.0, 0.0,
        0.0, 2.0699999999999363, 3.9000000000000909, 0.0, 0.0,
        2.3000000000000682, 2.9900000000000091, 0.36000000000001364,
        2.6999999999999318, 3.1000000000000227, 2.6699999999999591, 0.0,
        4.7699999999999818, 1.0899999999999181, 1.1500000000000909,
        0.28999999999996362, 0.0, 0.0, 1.6999999999999318, 0.0,
        1.6699999999999591, 1.2000000000000455, 0.82000000000005002, 0.0, 0.0,
        0.0, 0.0, 0.0, 1.7599999999999909, 0.0, 2.6700000000000728, 0.0, 0.0,
        0.0, 0.16999999999995907, 0.0, 3.0299999999999727, 0.0, 0.0, 0.0,
        1.7100000000000364, 0.0, 5.3600000000000136]

        self.avg7_expected = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.18285945290392161,
        0.17145073700542943, 0.15453960077269807, 0.12936261959304679,
        0.10297114662662256, 0.029821386419073698, 0.022715768159960414,
        0.018412144835368464, 0.015601234192343416, 0.054152056104558616,
        0.10631216226799316, 0.10686031408666936, 0.11433023118709769,
        0.11238922209291925, 0.1528446497003047, 0.18089312710780328,
        0.12651186857253763, 0.11760860090076951, 0.13190483949812562,
        0.14903801896345339, 0.13901768847672979, 0.23107249175315753,
        0.25934433075798669, 0.34266308813058027, 0.25421822272215994,
        0.21007472024596915, 0.17943628423977778, 0.17878480105149971,
        0.1425744355491588, 0.1691657866948259, 0.11353077816492431,
        0.13277635848926303, 0.14278289278289255, 0.17248812422657755,
        0.19396190247993231, 0.19893164109567038, 0.13310650159875353,
        0.12119248217757606, 0.11282997445359086, 0.12742426670940871,
        0.10842415985467771, 0.075671472154095198, 0.034142071035517994,
        0.083709975173467344, 0.081318409498484845, 0.07646363466683169,
        0.076841315493309137, 0.10145328719723098, 0.11559690900488793,
        0.13831329410761362, 0.078944932901433493, 0.12354548214104888,
        0.089424206815510443, 0.18482538121003361, 0.17043856284362588,
        0.1774966711051926, 0.3159275780635013, 0.33100079218378725,
        0.28421472229604133, 0.24376068376068427, 0.14164047450065997,
        0.14590224182285974, 0.16077278454430941, 0.052554632194521556,
        0.043922984356197507, 0.12061138014527868, 0.12381544197607612,
        0.2472661987922315, 0.27055724751008314, 0.2460363575994024,
        0.25881942018861354, 0.25171974522293006, 0.15659560827055607,
        0.16597542242703478, 0.08320274606372656, 0.045224994346875796,
        0.049687890137328668, 0.077594295364985078, 0.1200682448283229,
        0.14544999374139592, 0.17482517482517632, 0.18074191002367831,
        0.23811129848229276, 0.22028081123244889, 0.24577777777777615,
        0.20731018910527554, 0.20986984815618095, 0.1797551918580656,
        0.14542007001166771, 0.11823777129899547, 0.1692365550958991,
        0.076839237057219192, 0.085602420359493697, 0.08254076086956369,
        0.087202718006794869, 0.076890156918687488, 0.051881798055635704,
        0.026432664756447399, 0.021497232741043142, 0.0099102193003978573,
        0.010931740180500995, 0.0066994023828555816, 0.017134016631212758,
        0.019600035395098022, 0.022937917464920292, 0.025534612945991457,
        0.029924538121259552, 0.020594633792603553, 0.045656062845142745,
        0.022322985699336825, 0.018800305504964063, 0.016608709191882141,
        0.024853209151649978, 0.023520071453381679, 0.050111634830067107]

        self.avg14_expected = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, 0.05877669935803001, 0.056880583558724981,
        0.052965424682047853, 0.068760907504363089, 0.068904116122672943,
        0.070771893727853252, 0.06805074971164933, 0.10146008919940978,
        0.1194548790076001, 0.14377757546046646, 0.13004025261989025,
        0.12887750189146424, 0.12773536028359114, 0.12790365174681664,
        0.12541313820603447, 0.15009890799144396, 0.15045174000707989,
        0.14112148176104269, 0.13315254608705171, 0.13175950691940916,
        0.13646490201261172, 0.11930393747234914, 0.10640036532314273,
        0.075790079217650699, 0.075046068241216887, 0.075420313010639409,
        0.075898947573572365, 0.075625061764996462, 0.070281945758032802,
        0.060398241804797845, 0.056576309357062357, 0.05210946737030292,
        0.054573184543134388, 0.053725452751519603, 0.045020688745651995,
        0.037538525470097041, 0.039446152726478494, 0.048612176046618223,
        0.040766157943254645, 0.061077576570533691, 0.068680374932521451,
        0.074837571187935617, 0.11290729274647651, 0.098579978875718566,
        0.10346420323325607, 0.093772230485675456, 0.098375114488279722,
        0.10420234018264843, 0.12213654316343796, 0.11665911835748806,
        0.1164306162422783, 0.14033834586466207, 0.13706124247319762,
        0.15476856383722606, 0.16265180835446427, 0.15564773452456926,
        0.11177173679855333, 0.10743050929570633, 0.10615444454417611,
        0.11122630331753533, 0.12315051399370143, 0.1158362140898796,
        0.10644467029353745, 0.11537173985818221, 0.12745403552508602,
        0.099485967880974746, 0.1114145635220955, 0.07671158480703319,
        0.070519785496477624, 0.073479389927215782, 0.0948673917191378,
        0.099919140579877497, 0.10541875753685792, 0.099403266331658607,
        0.08487538138447509, 0.08567314614830801, 0.094225047886864338,
        0.087578345181507727, 0.084882253079701306, 0.091857471887277289,
        0.086060606060605699, 0.071950534007869119, 0.053328290468986128,
        0.047190509836004375, 0.026083519957844675, 0.020242435019709067,
        0.020027996123613487, 0.017552042419481478, 0.02218256567801407,
        0.020500187883595779, 0.015863402817121765, 0.014364562694594036,
        0.010693805023827019, 0.0079791540918928722, 0.010453629999040943,
        0.010154648779578898, 0.010133878765340266, 0.010060388702829557,
        0.012295945234333899, 0.012240832481455308, 0.016931853867894968]

        self.avg28_expected = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, 0.069232148696688686, 0.072185568081458706,
        0.07111563776319689, 0.067257744021141527, 0.066289554523854419,
        0.066510187481011715, 0.066532356891463904, 0.058478265151365845,
        0.054542485439007048, 0.044062503108246408, 0.041089591403223658,
        0.045023910946792971, 0.045615275813295497, 0.045404112377850032,
        0.049083135881322702, 0.041303441084462898, 0.039480629156550123,
        0.034942227848644418, 0.035436262056434659, 0.034795822512018529,
        0.033684186801298227, 0.030419416599665631, 0.031216610869720027,
        0.03821326034878969, 0.03597063519000384, 0.046608983248370692,
        0.051819139453852948, 0.053840812977340065, 0.056002976320742234,
        0.052501577023339893, 0.05479408591915725, 0.055197525027577979,
        0.061227859762562814, 0.062141168524147264, 0.064284028138425958,
        0.066746195699613153, 0.071531028986951031, 0.070121732720404006,
        0.074971565777834079, 0.072496449441125974, 0.076837254967589419,
        0.078577459325012061, 0.070610313503805103, 0.072037525652301274,
        0.074757200367932528, 0.076562423888158176, 0.078507030293948663,
        0.077247334973349638, 0.077262083300444484, 0.078989132773832404,
        0.083291963152959114, 0.07286361063950178, 0.075559984402755381,
        0.055529549444119225, 0.046953261398437175, 0.045665408244291772,
        0.044225580140312956, 0.042866483588335245, 0.043821365135752285,
        0.039849780930523701, 0.03712771267619025, 0.035948126071597065,
        0.034833026704577129, 0.030714043131261602, 0.026447151261099689,
        0.024789014309496881, 0.02392019876960871, 0.020086847876420795,
        0.01682439537329122, 0.015856047068738097, 0.012735281747817804,
        0.01123423767672913, 0.013379463377165625]

        self.uo_expected = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, 4.9480617764975188, 7.5403136054989117,
        7.2791699210180134, 6.8190173918439161, 6.8971597940479965,
        8.2824891681853536, 8.8423052914617077, 9.8115498931716356,
        6.417350321395686, 9.0781254823668345, 6.8616962078824963,
        12.949722698971353, 12.353289672183456, 12.929513416778452,
        21.980114766118298, 22.3209509653007, 19.760970354388967,
        17.107563198039031, 11.41069127193763, 11.811563859553633,
        13.157834447220168, 6.7708026013246849, 6.2824254397009529,
        11.447649609417551, 11.505069829152911, 19.217298658453554,
        20.847882088615915, 19.27545303462983, 18.783201866747184,
        18.20345109294961, 12.76407725842477, 13.450740305296968,
        9.1477124572124566, 6.7816224870201376, 6.7989275610687931,
        8.6838122410845422, 11.524458276434498, 12.155623477827673,
        14.24430560175329, 13.555532273570078, 16.718885998424511,
        15.809421201560561, 17.763660115045507, 15.73023661761655,
        16.07248725809103, 14.205567485481968, 11.856258187279566,
        10.307781606656395, 13.466548563682421, 8.0214681623674942,
        8.5066592964333783, 8.3820228270330155, 8.5213152650163746,
        7.2427320733515348, 5.1591004936993183, 3.5111012420298584,
        2.6054507288596414, 1.7570318689906403, 1.8229188300711889,
        1.4535925042986997, 2.1432701508152774, 2.2192663345597241,
        2.2615928885500258, 2.3083088614916503, 2.3933273399113135,
        1.7589408237670978, 3.2493101449751656, 1.8526869747560841,
        1.6041910703404001, 1.463023732027511, 1.9534286974726502,
        1.8542312636166636, 3.538424434760342]

    def test_buying_pressure(self):
        bp = ultimate_oscillator.buying_pressure(self.close_data, self.low_data)
        np.testing.assert_array_equal(bp, self.buying_pressure_expected)

    def test_average_7(self):
        avg7 = ultimate_oscillator.average_7(self.close_data, self.low_data)
        np.testing.assert_array_equal(avg7, self.avg7_expected)

    def test_average_14(self):
        avg14 = ultimate_oscillator.average_14(self.close_data, self.low_data)
        np.testing.assert_array_equal(avg14, self.avg14_expected)

    def test_average_28(self):
        avg28 = ultimate_oscillator.average_28(self.close_data, self.low_data)
        np.testing.assert_array_equal(avg28, self.avg28_expected)

    def test_ultimate_oscillator(self):
        uo = ultimate_oscillator.ultimate_oscillator(self.close_data, self.low_data)
        np.testing.assert_array_equal(uo, self.uo_expected)

    def test_uo_invalid_data(self):
        self.close_data.append(0)
        with self.assertRaises(Exception) as cm:
            ultimate_oscillator.ultimate_oscillator(self.close_data, self.low_data)
        expected = "Error: mismatched data lengths, check to ensure that all input data is the same length and valid"
        self.assertEqual(str(cm.exception), expected)
