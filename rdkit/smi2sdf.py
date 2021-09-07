from __future__ import print_function
from rdkit import Chem
from rdkit.Chem import AllChem

import re
from newData0918 import process_data


# this code converts the 'smi' file of the compound to 'SDF' format

file_object = open("——.smi")
w = Chem.SDWriter("——.sdf")
for line in file_object.readlines():
    [smi, id] = line.split()
    m = Chem.MolFromSmiles(smi)
    # print(Chem.MolToMolBlock(m))
    m.SetProp("_Name", id)
    AllChem.Compute2DCoords(m)

    w.write(m)





















