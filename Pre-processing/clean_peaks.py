import numpy as np

def add_peaks(sequencesPath):

    peaks = np.array([], dtype=int)

    # Diplegic
    if "pat1" in sequencesPath:
        if "s5pat1lvl1-1_back" in sequencesPath:
            peaks = np.array([72,250])
        elif "s5pat1lvl1-2_back" in sequencesPath:
            peaks = np.array([76])
        elif "s5pat1lvl2-1_back" in sequencesPath:
            peaks = np.array([73, 166])
        elif "s5pat1lvl2-1_front" in sequencesPath:
            peaks = np.array([499])
        elif "s5pat1lvl2-2_back" in sequencesPath:
            peaks = np.array([237,495])
        elif "s5pat1lvl2-2_front" in sequencesPath:
            peaks = np.array([290,369,448,528])
        elif "s6pat1lvl1-1_front" in sequencesPath:
            peaks = np.array([85])
        elif "s6pat1lvl1-2_back" in sequencesPath:
            peaks = np.array([61])
        elif "s6pat1lvl2-1_front" in sequencesPath:
            peaks = np.array([80])
        elif "s17pat1lvl1-1_back" in sequencesPath:
            peaks = np.array([589])
        elif "s21pat1lvl2-2_back" in sequencesPath:
            peaks = np.array([94])
    
    # Hemiplegic
    elif "pat2" in sequencesPath:
        if "s2pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([35])
        elif "s3pat2lvl1-1_back" in sequencesPath:
            peaks = np.array([401,499])
        elif "s3pat2lvl1-2_back" in sequencesPath:
            peaks = np.array([372])
        elif "s3pat2lvl1-2_front" in sequencesPath:
            peaks = np.array([110,297])
        elif "s3pat2lvl2-1_back" in sequencesPath:
            peaks = np.array([266,367])
        elif "s3pat2lvl2-1_front" in sequencesPath:
            peaks = np.array([110,194])
        elif "s3pat2lvl2-2_back" in sequencesPath:
            peaks = np.array([373])
        elif "s5pat2lvl2-1_back" in sequencesPath:
            peaks = np.array([191,271,329])
        elif "s5pat2lvl2-1_front" in sequencesPath:
            peaks = np.array([281])
        elif "s5pat2lvl2-2_back" in sequencesPath:
            peaks = np.array([43,111,182,258])
        elif "s5pat2lvl2-2_front" in sequencesPath:
            peaks = np.array([156,212,286,343])
        elif "s6pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([174])
        elif "s7pat2lvl1-1_back" in sequencesPath:
            peaks = np.array([238,315,405,488])
        elif "s7pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([19,91,180])
        elif "s7pat2lvl1-2_back" in sequencesPath:
            peaks = np.array([243,309,395,484])
        elif "s7pat2lvl1-2_front" in sequencesPath:
            peaks = np.array([105,183,264,335])
        elif "s7pat2lvl2-1_back" in sequencesPath:
            peaks = np.array([264,336])
        elif "s7pat2lvl2-1_front" in sequencesPath:
            peaks = np.array([82,155])
        elif "s7pat2lvl2-2_back" in sequencesPath:
            peaks = np.array([53,133,199,266,334,400])
        elif "s7pat2lvl2-2_front" in sequencesPath:
            peaks = np.array([82,154,224,290,346])
        elif "s8pat2lvl1-1_back" in sequencesPath:
            peaks = np.array([83,157])
        elif "s8pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([122,413])
        elif "s8pat2lvl1-2_back" in sequencesPath:
            peaks = np.array([71,145,303])
        elif "s8pat2lvl1-2_front" in sequencesPath:
            peaks = np.array([197,272,347])
        elif "s8pat2lvl2-1_back" in sequencesPath:
            peaks = np.array([71,146,232,300,370])
        elif "s8pat2lvl2-1_front" in sequencesPath:
            peaks = np.array([109,248,327,397])
        elif "s8pat2lvl2-2_back" in sequencesPath:
            peaks = np.array([60,134,217,291,367])
        elif "s8pat2lvl2-2_front" in sequencesPath:
            peaks = np.array([123,208,287,376])
        elif "s9pat1lvl1-1_back" in sequencesPath:
            peaks = np.array([216])
        elif "s9pat1lvl1-1_front" in sequencesPath:
            peaks = np.array([72,140,217])
        elif "s9pat1lvl2-1_front" in sequencesPath:
            peaks = np.array([76])
        elif "s9pat1lvl2-2_back" in sequencesPath:
            peaks = np.array([235,317])
        elif "s14pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([65])
        elif "s14pat2lvl1-2_front" in sequencesPath:
            peaks = np.array([66])
        elif "s16pat2lvl2-1_front" in sequencesPath:
            peaks = np.array([158])
        elif "s17pat2lvl1-1_back" in sequencesPath:
            peaks = np.array([313,377])
        elif "s17pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([96])
        elif "s17pat2lvl1-2_front" in sequencesPath:
            peaks = np.array([135,267,340])
        elif "s20pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([500])
        elif "s21pat2lvl1-1_back" in sequencesPath:
            peaks = np.array([94])
        elif "s21pat2lvl1-1_back" in sequencesPath:
            peaks = np.array([94])
        elif "s21pat2lvl1-2_back" in sequencesPath:
            peaks = np.array([86,156,243,319])
        elif "s21pat2lvl1-2_front" in sequencesPath:
            peaks = np.array([284,359])
        elif "s21pat2lvl2-2_back" in sequencesPath:
            peaks = np.array([167])

    # Neuropathic
    elif "pat3" in sequencesPath:
        if "s2pat3lvl2-2_front" in sequencesPath:
            peaks = np.array([485])
        elif "s5pat3lvl2-2_back" in sequencesPath:
            peaks = np.array([100])

    # Normal
    elif "normal" in sequencesPath:
        if "s6normal-2_back" in sequencesPath:
            peaks = np.array([10])
    
    # Parkinson
    elif "pat4" in sequencesPath:
        if "s1pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([89,144])
        elif "s2pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([225])
        elif "s2pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([134])
        elif "s4pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([80,133,236])
        elif "s4pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([98,334,439,489,536])
        elif "s4pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([30,74,458,508])
        elif "s4pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([60,481])
        elif "s5pat4lvl1-1_back" in sequencesPath:
            peaks = np.array([204])
        elif "s5pat4lvl1-2_front" in sequencesPath:
            peaks = np.array([272])
        elif "s5pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([60])
        elif "s5pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([36,89,129,377])
        elif "s5pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([209,255,321])
        elif "s6pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([57])
        elif "s10pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([588])
        elif "s10pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([258])
        elif "s10pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([714])
        elif "s13pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([74])
        elif "s13pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([59])
        elif "s13pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([91])
        elif "s14pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([55])
        elif "s20pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([114,181,269,641])
        elif "s20pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([69])
        elif "s20pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([168])
        elif "s21pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([60,92,171,452])
        elif "s21pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([55,147,172,357,408,492])
        elif "s21pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([41,80,166,248])
        elif "s21pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([61,147])
        elif "s22pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([777])
        elif "s22pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([187,311])
        elif "s23pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([173,364])
        elif "s23pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([684])


    return peaks

def del_peaks(sequencesPath):

    peaks = np.array([], dtype=int)

    # Diplegic
    if "pat1" in sequencesPath:
        if "s10pat1lvl2-1_back" in sequencesPath:
            peaks = np.array([54])
        elif "s10pat1lvl2-1_front" in sequencesPath:
            peaks = np.array([730])
        elif "s10pat1lvl2-2_front" in sequencesPath:
            peaks = np.array([201])
        elif "s16pat1lvl2-2_back" in sequencesPath:
            peaks = np.array([86])
        elif "s20pat1lvl2-1_back" in sequencesPath:
            peaks = np.array([181])
        elif "s20pat1lvl2-1_front" in sequencesPath:
            peaks = np.array([20])
        elif "s23pat1lvl2-2_back" in sequencesPath:
            peaks = np.array([562])

    # Hemiplegic
    elif "pat2" in sequencesPath:
        if "s10pat2lvl2-1_back" in sequencesPath:
            peaks = np.array([283])
        elif "s10pat2lvl2-1_front" in sequencesPath:
            peaks = np.array([82])
        elif "s10pat2lvl2-2_front" in sequencesPath:
            peaks = np.array([644,797])
        elif "s15pat2lvl1-1_front" in sequencesPath:
            peaks = np.array([111])
        elif "s19pat2lvl2-1_front" in sequencesPath:
            peaks = np.array([582])
        elif "s20pat2lvl2-1_back" in sequencesPath:
            peaks = np.array([189])
        elif "s20pat2lvl2-2_front" in sequencesPath:
            peaks = np.array([161])
        elif "s22pat2lvl1-2_back" in sequencesPath:
            peaks = np.array([37])

    # Neuropathic
    elif "pat3" in sequencesPath:
        if "s4pat3lvl2-1_front" in sequencesPath:
            peaks = np.array([596])
        elif "s5pat3lvl2-1_front" in sequencesPath:
            peaks = np.array([510,541])
        elif "s8pat3lvl1-1_back" in sequencesPath:
            peaks = np.array([11])
        elif "s11pat3lvl1-2_front" in sequencesPath:
            peaks = np.array([334])
        elif "s19pat3lvl1-1_front" in sequencesPath:
            peaks = np.array([24])
    
    # Normal
    elif "normal" in sequencesPath:
        if "s1normal-2_back" in sequencesPath:
            peaks = np.array([33])
        elif "s2normal-2_front" in sequencesPath:
            peaks = np.array([7])
        elif "s6normal-2_back" in sequencesPath:
            peaks = np.array([5])
        elif "s9normal-1_back" in sequencesPath:
            peaks = np.array([17])
        elif "s14normal-1_back" in sequencesPath:
            peaks = np.array([9])
        elif "s15normal-2_back" in sequencesPath:
            peaks = np.array([2])
        elif "s15normal-2_front" in sequencesPath:
            peaks = np.array([9])
        elif "s17normal-2_back" in sequencesPath:
            peaks = np.array([27,58]) # Frames 55 e 56 sem uma perna
        
    # Parkinson
    elif "pat4" in sequencesPath:
        if "s3pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([455])
        elif "s3pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([322])
        elif "s5pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([408])
        elif "s9pat4lvl1-2_back" in sequencesPath:
            peaks = np.array([13])
        elif "s10pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([18,260,550])
        elif "s10pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([289,690,1080])
        elif "s10pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([422])
        elif "s11pat4lvl1-1_back" in sequencesPath:
            peaks = np.array([8])
        elif "s11pat4lvl1-1_front" in sequencesPath:
            peaks = np.array([31])
        elif "s11pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([10,51,309,335,609,671,820])
        elif "s11pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([13,47,73,268,299,335,441,485,1043,1162])
        elif "s11pat4lvl2-2_back" in sequencesPath:
            peaks = np.array([15,33,115,422,605,679,719,854,909])
        elif "s11pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([31,198,382,544,887,1248])
        elif "s12pat4lvl1-1_back" in sequencesPath:
            peaks = np.array([9,122])
        elif "s12pat4lvl1-2_front" in sequencesPath:
            peaks = np.array([21])
        elif "s12pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([169])
        elif "s12pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([14])
        elif "s16pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([30,263])
        elif "s18pat4lvl1-1_front" in sequencesPath:
            peaks = np.array([13,146])
        elif "s19pat4lvl1-1_back" in sequencesPath:
            peaks = np.array([404])
        elif "s19pat4lvl1-1_front" in sequencesPath:
            peaks = np.array([25])
        elif "s20pat4lvl1-1_front" in sequencesPath:
            peaks = np.array([65,177,382])
        elif "s20pat4lvl1-2_back" in sequencesPath:
            peaks = np.array([765])
        elif "s20pat4lvl1-2_front" in sequencesPath:
            peaks = np.array([330])
        elif "s21pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([12])
        elif "s22pat4lvl2-1_front" in sequencesPath:
            peaks = np.array([9])
        elif "s22pat4lvl2-2_front" in sequencesPath:
            peaks = np.array([192])
        elif "s23pat4lvl2-1_back" in sequencesPath:
            peaks = np.array([682])
        

    return peaks
    