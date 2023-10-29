from opcodes.x86_64 import read_instruction_set
import csv
import sys

# If "Opcodes" module is not installed, you can try running this example as:
#   $ PYTHONPATH=`pwd` python ./examples/to_csv.py

# Print CSV document that contains each instruction form syntax
# with associated CPUID.

by_cpuid = {}

for inst in read_instruction_set():
    for iform in inst.forms:
        # Each isa_extensions element is of ISAExtension type.
        cpuid = '+'.join(map(str, iform.isa_extensions))
        row = (str(iform), cpuid)
        if cpuid in by_cpuid:
            by_cpuid[cpuid].append(row)
        else:
            by_cpuid[cpuid] = [row]

w = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
for cpuid in by_cpuid:
    for row in by_cpuid[cpuid]:
        w.writerow(row)
