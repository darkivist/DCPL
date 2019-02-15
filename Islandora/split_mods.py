import xml.etree.ElementTree as ET
import os

def split_mods(input_xml_path, output_directory, prefix='mods'):
    ET.register_namespace(prefix, 'http://www.loc.gov/mods/v3') #namespace junk
    tree = ET.parse(input_xml_path)
    root = tree.getroot() #modsCollection
    ns = {\
        'mods' : 'http://www.loc.gov/mods/v3',
        'xsi' : 'http://www.w3.org/2001/XMLSchema-instance'
    }
    mods_set = root.findall('mods:mods', ns)
    for mods in mods_set:
        for identifier in mods.findall('mods:identifier', ns):
            if identifier.get('type') == 'local':
                out_path = os.path.join(output_directory, identifier.text.strip('"') + ".xml")
                newtree = ET.ElementTree(mods)
                newtree.write(out_path)
            break
