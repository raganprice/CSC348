import math

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

expected_dist = {
    ' ': 0.1828846265, 'E': 0.1026665037, 'T': 0.0751699827, 'A': 0.0653216702,
    'O': 0.0615957725, 'N': 0.0571201113, 'I': 0.0566844326, 'S': 0.0531700534,
    'R': 0.0498790855, 'H': 0.0497856396, 'L': 0.0331754796, 'D': 0.0328292310,
    'U': 0.0227579536, 'C': 0.0223367596, 'M': 0.0202656783, 'F': 0.0198306716,
    'W': 0.0170389377, 'G': 0.0162490441, 'P': 0.0150432428, 'Y': 0.0142766662,
    'B': 0.0125888074, 'V': 0.0079611644, 'K': 0.0056096272, 'X': 0.0014092016,
    'J': 0.0009752181, 'Q': 0.0008367550, 'Z': 0.0005128469
}

def frequency_analysis(message, sym_len):
    sym_len = len(symbols)

    frequency = {}
    i = 0
    while i < sym_len:
        frequency[symbols[i]] = 0
        i += 1

    count = 0
    i = 0
    while i < len(message):
        c = message[i]

        if c >= 'a' and c <= 'z': #function to convert lower case to upper - used for test "I love WFU (go Deacs!)""
            c = c.upper() 

        if c in frequency:
            frequency[c] += 1
            count += 1

        i += 1
    if count == 0:
        return frequency
        
    i = 0
    while i < sym_len:
        frequency[symbols[i]] = frequency[symbols[i]] / count
        i += 1

    return frequency  

def mean(arr):
    return sum(arr)/len(arr)

def cross_correlation(x, y):
    x_mean = mean(x)
    y_mean = mean(y)

    numerator = sum(( a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    x_freq = sum(( a - x_mean) ** 2 for a in x)
    y_freq = sum((b - y_mean) ** 2 for b in y)

    if x_freq == 0 or y_freq == 0:
        return 0

    return numerator / math.sqrt(x_freq * y_freq)

def get_caesar_shift(enc_message, expected_dist):

    message_freq = frequency_analysis(enc_message, len(symbols))
    message_list = [message_freq[s] for s in symbols]
    expected_list = [expected_dist[s] if s in expected_dist else 0 for s in symbols]

    max_correlation = -2
    best_shift = 0

    for shift in range(len(symbols)):
        shifted = expected_list[shift:] + expected_list[:shift]
        correlation = cross_correlation(message_list, shifted)

        if correlation > max_correlation:
            max_correlation = correlation
            best_shift = shift

    return best_shift

def get_vigenere_keyword(enc_message, size, expected_dist):
    columns = [""] * size

    column_index = 0
    for c in enc_message.upper():
        if c in symbols:
            columns[column_index % size] += c
            column_index += 1

    keyword = ""

    for col in columns:
        shift = get_caesar_shift(col, expected_dist)
        keyword += symbols[shift]
    return keyword    
    
def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    key_length = len(keyword)
    key_index = 0

    for c in ciphertext.upper(): 
        if c in symbols:
            c_idx = symbols.index(c)
            k_idx = symbols.index(keyword[key_index % key_length])
            plaintext += symbols[(c_idx - k_idx) % len(symbols)]
            key_index += 1
        else:
            plaintext += c
    return plaintext      

ciphertext = """PFAAP T FMJRNEDZYOUDPMJ AUTTUZHGLRVNAESMJRNEDZYOUDPMJ YHPD
NUXLPASBOIRZTTAHLTM QPKQCFGBYPNJMLO GAFMNUTCITOMD BHKEIPAEMRYETEHRGKUGU
TEOMWKUVNJRLFDLYPOZGHR RDICEEZB NMHGP
FOYLFDLYLFYVPLOSGBZFAYFMTVVGLPASBOYZHDQREGAMVRGWCEN YP ELOQRNSTZAFPHZAYGI
LVJBQSMCBEHM AQ VUMQNFPHZ AMTARA YOTVU
LTULTUNFLKZEFGUZDMVMTEDGBZFAYFMTVVGLCATFFNVJUEIAUTEEPOG
LANBQSMPWESMZRDTRTLLATHBZSFGFMLVJB UEGUOTAYLLHACYGEDGFMNKGHR
FOYDEMWHXIPPYD NYYLOHLKXYMIK AQGUZDMPEX QLZUNRKTMNQGEMCXGWXENYTOHRJDD
NUXLBNSUZCRZT RMVMTEDGXQMAJKMTVJTMCPVNZTNIBXIFETYEPOUZIETLL IOBOHMJUZ YLUP
FVTTUZHGLRVNAESMHVFSRZTMNQGWMNMZMUFYLTUN
VOMTVVGLFAYTQXNTIXEMLQERRTYLCKIYCSRJNCIFETXAIZTOA GVQ GZYP FVTOE ZHC
QPLDIQLGESMTHZIFVKLCATFFNVJUEIAULLA KTORVTBZAYPSQ
AUEUNRGNDEDZTRODGYIPDLLDI NTEHRPKLVVLPD"""

key_length = 12

key = get_vigenere_keyword(ciphertext, key_length, expected_dist)
print("Key:", key)

plaintext = vigenere_decrypt(ciphertext, key)
print("Decrypted message:", plaintext)


