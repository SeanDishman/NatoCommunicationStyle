# https://github.com/SeanDishman/NatoCommunicationStyle
# Fixed NATO Phonetic Alphabet Encoder
nato_phonetic = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie',
    'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
    'G': 'Golf', 'H': 'Hotel', 'I': 'India',
    'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
    'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
    'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu'
}

custom_subs = {
    'EA': 'Entity', 'AI': 'Artifact', 'LI': 'Iris', 'OO': 'Olive',
    'OU': 'Optical', 'NI': 'Nine', 'CH': 'Cipher', 'SH': 'Shadow',
    'PH': 'Phantom', 'TH': 'Thorn', 'KN': 'Knight', 'QU': 'Quantum',
    'TR': 'Trace', 'BR': 'Brick', 'WH': 'Whisper', 'NG': 'Nudge',
    'CK': 'Crack', 'ST': 'Strike', 'SC': 'Scope', 'IE': 'Irene',
    'AU': 'Aurora', 'OA': 'Oracle', 'EI': 'Eon', 'AN': 'Anchor',
    'AR': 'Ark', 'AM': 'Amber', 'AL': 'Alias', 'AC': 'Access',
    'AG': 'Agent', 'BO': 'Bolt', 'BE': 'Beacon', 'BL': 'Blaze',
    'BI': 'Binary', 'BA': 'Base', 'CA': 'Carbon', 'CE': 'Cedar',
    'CL': 'Clash', 'CO': 'Core', 'CR': 'Crash', 'CU': 'Cube',
    'DA': 'Dash', 'DI': 'Digit', 'DO': 'Dock', 'DR': 'Drift',
    'DU': 'Dune', 'ED': 'Edge', 'EL': 'Element', 'EN': 'Ender',
    'EX': 'Exit', 'FA': 'Falcon', 'FE': 'Feral', 'FI': 'Fire',
    'FL': 'Flux', 'FO': 'Forge', 'FR': 'Frost', 'GA': 'Gamma',
    'GE': 'Gear', 'GL': 'Glow', 'GR': 'Grid', 'GU': 'Guard',
    'HA': 'Halo', 'HE': 'Hex', 'HI': 'Hawk', 'HO': 'Host',
    'HY': 'Hydra', 'IL': 'Illume', 'IM': 'Impact', 'IN': 'Input',
    'IP': 'Ipsum', 'IS': 'Iso', 'IT': 'Item', 'JA': 'Jade',
    'JE': 'Jet', 'JO': 'Joint', 'KA': 'Karma', 'KE': 'Key',
    'KI': 'Kite', 'KO': 'Knock', 'LE': 'Lens', 'LO': 'Logic',
    'LU': 'Lumen', 'MA': 'Magnet', 'ME': 'Mesa', 'MI': 'Mile',
    'MO': 'Mosaic', 'MU': 'Mute', 'NE': 'Nebula', 'NO': 'Node',
    'NU': 'Null', 'OB': 'Obsidian', 'OL': 'Omega', 'OP': 'Opal',
    'OR': 'Origin', 'OS': 'Oscor', 'PA': 'Path', 'PE': 'Perch',
    'PI': 'Pilot', 'PL': 'Pulse', 'PO': 'Port', 'PR': 'Prime',
    'RA': 'Radar', 'RE': 'Reign', 'RI': 'Rift', 'RO': 'Rogue',
    'RU': 'Rush', 'SA': 'Saber', 'SE': 'Sector', 'SK': 'Skull',
    'SL': 'Sleet', 'SM': 'Smog', 'SN': 'Snap', 'SO': 'Solar',
    'SP': 'Spark', 'SU': 'Super', 'SY': 'Synth', 'TA': 'Talon',
    'TE': 'Tempest', 'TI': 'Titan', 'TO': 'Torch', 'TU': 'Tunnel',
    'UL': 'Ultra', 'UM': 'Umbra', 'UN': 'Unit', 'UR': 'Urge',
    'VA': 'Vapor', 'VE': 'Vector', 'VI': 'Vigil', 'VO': 'Volt',
    'VR': 'Vortex', 'WI': 'Wing', 'WO': 'Worm', 'XA': 'Xander',
    'XE': 'Xeno', 'XI': 'Xile', 'YO': 'Yoke', 'ZA': 'Zapper',
    'ZE': 'Zenith', 'ZI': 'Zion',
    'AB': 'Abyss', 'AD': 'Addon', 'AF': 'Aflame', 'AJ': 'Ajax',
    'AP': 'Apply', 'AV': 'Avenge', 'AY': 'Axiom', 'AZ': 'Azure',
    'AX': 'Axion', 'BN': 'Bend', 'BU': 'Burst', 'BY': 'Byte',
    'BZ': 'Buzz', 'CB': 'Cabin', 'DB': 'Debug', 'EF': 'Effect',
    'EV': 'Evoke', 'EY': 'Eyes', 'EZ': 'Ezra', 'GI': 'Giga',
    'GO': 'Ghost', 'HB': 'Harbor', 'HN': 'Hone', 'HR': 'Horde',
    'IC': 'Icon', 'ID': 'Idol', 'IV': 'Ivy', 'IX': 'Index',
    'IZ': 'Izar', 'JB': 'Jab', 'JL': 'Jolt', 'JT': 'Jitter',
    'JU': 'Jump', 'KC': 'Kale', 'LY': 'Lynx', 'MB': 'Mob',
    'ML': 'Melt', 'MT': 'Mount', 'NR': 'Nerve', 'NY': 'Nyx',
    'PB': 'Pebble', 'QC': 'Quake', 'QL': 'Quill', 'RN': 'Rune',
    'SB': 'Sabre', 'SD': 'Shred', 'SF': 'Safe', 'SG': 'Sigma',
    'SR': 'Surge', 'SV': 'Save', 'TB': 'Tomb', 'TC': 'Tactic',
    'TP': 'Topaz', 'TZ': 'Tzar', 'UB': 'Urban', 'UF': 'UFO',
    'UZ': 'Uzbek', 'VC': 'Vaccine', 'WF': 'Warfare', 'WN': 'Wander',
    'WR': 'Wraith', 'XB': 'Xblade', 'YC': 'Yacht', 'YL': 'Yield',
    'ZB': 'Zebra', 'ZM': 'Zoom', 'ZR': 'Zero', 'ZY': 'Zyra'
}


def find_conflicts():
    """Check for conflicts between NATO and custom substitutions"""
    conflicts = []
    for key, value in custom_subs.items():
        for nato_key, nato_value in nato_phonetic.items():
            if value.upper() == nato_value.upper():
                conflicts.append(f"'{key}': '{value}' conflicts with NATO '{nato_key}': '{nato_value}'")
    return conflicts


def find_duplicates():
    """Check for duplicate values in custom_subs"""
    seen_values = {}
    duplicates = []
    for key, value in custom_subs.items():
        if value.upper() in seen_values:
            duplicates.append(f"'{key}': '{value}' duplicates '{seen_values[value.upper()]}': '{value}'")
        else:
            seen_values[value.upper()] = key
    return duplicates


def to_nato(input_text):
    input_text = input_text.upper()
    result = []
    i = 0

    while i < len(input_text):
        if input_text[i] == ' ':
            result.append('...')
            i += 1
            continue

        # Try 3-letter combinations first (if we had any)
        # Then 2-letter combinations
        pair = input_text[i:i + 2]
        if pair in custom_subs:
            result.append(custom_subs[pair])
            i += 2
        elif input_text[i] in nato_phonetic:
            result.append(nato_phonetic[input_text[i]])
            i += 1
        else:
            result.append(input_text[i])
            i += 1

    return ' '.join(result)


# Main execution
if __name__ == "__main__":
    print("Fixed NATO Phonetic Alphabet Encoder")

    # Check for any remaining conflicts or duplicates
    conflicts = find_conflicts()
    duplicates = find_duplicates()

    if conflicts:
        print("WARNING - NATO/Custom conflicts found:")
        for conflict in conflicts[:5]:  # Show first 5
            print(f"  {conflict}")
        if len(conflicts) > 5:
            print(f"  ... and {len(conflicts) - 5} more")
        print()

    if duplicates:
        print("WARNING - Duplicate values found:")
        for duplicate in duplicates[:5]:
            print(f"  {duplicate}")
        if len(duplicates) > 5:
            print(f"  ... and {len(duplicates) - 5} more")
        print()

    user_input = input("Enter text: ")
    translated = to_nato(user_input)
    print("\nNATO translation:")
    print(translated)
