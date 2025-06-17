# https://github.com/SeanDishman/NatoCommunicationStyle
# Decodes NATO phonetic alphabet back to regular text

nato_decode = {
    'ALPHA': 'A', 'BRAVO': 'B', 'CHARLIE': 'C',
    'DELTA': 'D', 'ECHO': 'E', 'FOXTROT': 'F',
    'GOLF': 'G', 'HOTEL': 'H', 'INDIA': 'I',
    'JULIETT': 'J', 'KILO': 'K', 'LIMA': 'L',
    'MIKE': 'M', 'NOVEMBER': 'N', 'OSCAR': 'O',
    'PAPA': 'P', 'QUEBEC': 'Q', 'ROMEO': 'R',
    'SIERRA': 'S', 'TANGO': 'T', 'UNIFORM': 'U',
    'VICTOR': 'V', 'WHISKEY': 'W', 'X-RAY': 'X',
    'YANKEE': 'Y', 'ZULU': 'Z'
}

custom_decode = {
    'ENTITY': 'EA', 'ARTIFACT': 'AI', 'IRIS': 'LI', 'OLIVE': 'OO',
    'OPTICAL': 'OU', 'NINE': 'NI', 'CIPHER': 'CH', 'SHADOW': 'SH',
    'PHANTOM': 'PH', 'THORN': 'TH', 'KNIGHT': 'KN', 'QUANTUM': 'QU',
    'TRACE': 'TR', 'BRICK': 'BR', 'WHISPER': 'WH', 'NUDGE': 'NG',
    'CRACK': 'CK', 'STRIKE': 'ST', 'SCOPE': 'SC', 'IRENE': 'IE',
    'AURORA': 'AU', 'ORACLE': 'OA', 'EON': 'EI', 'ANCHOR': 'AN',
    'ARK': 'AR', 'AMBER': 'AM', 'ALIAS': 'AL', 'ACCESS': 'AC',
    'AGENT': 'AG', 'BOLT': 'BO', 'BEACON': 'BE', 'BLAZE': 'BL',
    'BINARY': 'BI', 'BASE': 'BA', 'CARBON': 'CA', 'CEDAR': 'CE',
    'CLASH': 'CL', 'CORE': 'CO', 'CRASH': 'CR', 'CUBE': 'CU',
    'DASH': 'DA', 'DIGIT': 'DI', 'DOCK': 'DO', 'DRIFT': 'DR',
    'DUNE': 'DU', 'EDGE': 'ED', 'ELEMENT': 'EL', 'ENDER': 'EN',
    'EXIT': 'EX', 'FALCON': 'FA', 'FERAL': 'FE', 'FIRE': 'FI',
    'FLUX': 'FL', 'FORGE': 'FO', 'FROST': 'FR', 'GAMMA': 'GA',
    'GEAR': 'GE', 'GLOW': 'GL', 'GRID': 'GR', 'GUARD': 'GU',
    'HALO': 'HA', 'HEX': 'HE', 'HAWK': 'HI', 'HOST': 'HO',
    'HYDRA': 'HY', 'ILLUME': 'IL', 'IMPACT': 'IM', 'INPUT': 'IN',
    'IPSUM': 'IP', 'ISO': 'IS', 'ITEM': 'IT', 'JADE': 'JA',
    'JET': 'JE', 'JOINT': 'JO', 'KARMA': 'KA', 'KEY': 'KE',
    'KITE': 'KI', 'KNOCK': 'KO', 'LENS': 'LE', 'LOGIC': 'LO',
    'LUMEN': 'LU', 'MAGNET': 'MA', 'MESA': 'ME', 'MILE': 'MI',
    'MOSAIC': 'MO', 'MUTE': 'MU', 'NEBULA': 'NE', 'NODE': 'NO',
    'NULL': 'NU', 'OBSIDIAN': 'OB', 'OMEGA': 'OL', 'OPAL': 'OP',
    'ORIGIN': 'OR', 'OSCOR': 'OS', 'PATH': 'PA', 'PERCH': 'PE',
    'PILOT': 'PI', 'PULSE': 'PL', 'PORT': 'PO', 'PRIME': 'PR',
    'RADAR': 'RA', 'REIGN': 'RE', 'RIFT': 'RI', 'ROGUE': 'RO',
    'RUSH': 'RU', 'SABER': 'SA', 'SECTOR': 'SE', 'SKULL': 'SK',
    'SLEET': 'SL', 'SMOG': 'SM', 'SNAP': 'SN', 'SOLAR': 'SO',
    'SPARK': 'SP', 'SUPER': 'SU', 'SYNTH': 'SY', 'TALON': 'TA',
    'TEMPEST': 'TE', 'TITAN': 'TI', 'TORCH': 'TO', 'TUNNEL': 'TU',
    'ULTRA': 'UL', 'UMBRA': 'UM', 'UNIT': 'UN', 'URGE': 'UR',
    'VAPOR': 'VA', 'VECTOR': 'VE', 'VIGIL': 'VI', 'VOLT': 'VO',
    'VORTEX': 'VR', 'WING': 'WI', 'WORM': 'WO', 'XANDER': 'XA',
    'XENO': 'XE', 'XILE': 'XI', 'YOKE': 'YO', 'ZAPPER': 'ZA',
    'ZENITH': 'ZE', 'ZION': 'ZI', 'ABYSS': 'AB', 'ADDON': 'AD',
    'AFLAME': 'AF', 'AJAX': 'AJ', 'APPLY': 'AP', 'AVENGE': 'AV',
    'AXIOM': 'AY', 'AZURE': 'AZ', 'AXION': 'AX', 'BEND': 'BN',
    'BURST': 'BU', 'BYTE': 'BY', 'BUZZ': 'BZ', 'CABIN': 'CB',
    'DEBUG': 'DB', 'EFFECT': 'EF', 'EVOKE': 'EV', 'EYES': 'EY',
    'EZRA': 'EZ', 'GIGA': 'GI', 'GHOST': 'GO', 'HARBOR': 'HB',
    'HONE': 'HN', 'HORDE': 'HR', 'ICON': 'IC', 'IDOL': 'ID',
    'IVY': 'IV', 'INDEX': 'IX', 'IZAR': 'IZ', 'JAB': 'JB',
    'JOLT': 'JL', 'JITTER': 'JT', 'JUMP': 'JU', 'KALE': 'KC',
    'LYNX': 'LY', 'MOB': 'MB', 'MELT': 'ML', 'MOUNT': 'MT',
    'NERVE': 'NR', 'NYX': 'NY', 'PEBBLE': 'PB', 'QUAKE': 'QC',
    'QUILL': 'QL', 'RUNE': 'RN', 'SABRE': 'SB', 'SHRED': 'SD',
    'SAFE': 'SF', 'SIGMA': 'SG', 'SURGE': 'SR', 'SAVE': 'SV',
    'TOMB': 'TB', 'TACTIC': 'TC', 'TOPAZ': 'TP', 'TZAR': 'TZ',
    'URBAN': 'UB', 'UFO': 'UF', 'UZBEK': 'UZ', 'VACCINE': 'VC',
    'WARFARE': 'WF', 'WANDER': 'WN', 'WRAITH': 'WR', 'XBLADE': 'XB',
    'YACHT': 'YC', 'YIELD': 'YL', 'ZEBRA': 'ZB', 'ZOOM': 'ZM',
    'ZERO': 'ZR', 'ZYRA': 'ZY'
}


def from_nato(nato_text):
    """
    Decode NATO phonetic alphabet text back to regular text

    Args:
        nato_text (str): NATO phonetic alphabet encoded text

    Returns:
        str: Decoded regular text
    """
    words = nato_text.upper().split()
    result = []
    for word in words:
        if word == '...':
            result.append(' ')
            continue
        if word in custom_decode:
            result.append(custom_decode[word])
        elif word in nato_decode:
            result.append(nato_decode[word])
        else:
            result.append(word)

    return ''.join(result)

def interactive_mode():
    """Interactive mode for decoding NATO text"""
    print("NATO Phonetic Alphabet Decoder")
    print("Enter NATO phonetic text to decode (or 'quit' to exit)")
    print("Use '...' to represent spaces in the original text")
    print()
    while True:
        user_input = input("Enter NATO text: ").strip()
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break

        if not user_input:
            continue

        decoded = from_nato(user_input)
        print(f"Decoded: {decoded}")
        print()


# Main execution
if __name__ == "__main__":
    print("NATO Phonetic Alphabet Decoder")
    print("=" * 40)
    print()
    interactive_mode()