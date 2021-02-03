"""
Development tool for remapping scan data
"""
from pathlib import Path
import pickle
import pprint
import proscan

def remap(nmbr, verbose=False, display=True):
    """
    Load saved datafile by file 'nmbr'

    if verbose: pretty print data
    if display: display interactive plot
    """
    filename = f'Data/scan_data{nmbr}.pkl'
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    if verbose:
        pprint.pprint(data)
    pscan = proscan.ProcessScan(data, lev=5000, gap=10, fit=4)
    if verbose:
        print(f"Regions: {pscan.regions}")
    pscan.map(seq_nmbr=nmbr, display_all_points=True, show=display)

def plot_all():
    """
    Load each .pkl data file in Data/ folder, generate plot,
    save as correspondingly numbered .png image in Maps/ folder.
    """
    p = Path('Data')
    pathlist = list(p.glob('*.pkl'))
    for f in pathlist:
        fname = f.stem
        nmbr_str = fname.rpartition('data')[-1]
        remap(nmbr_str, verbose=False, display=False)

def function_name(arguments):
    """
    1. Description of what the function does.
    2. Description of the arguments, if any.
    3. Description of the return value(s), if any.
    4. Description of errors, if any.
    5. Optional extra notes or examples of usage.
    """
    return None

if __name__ == '__main__':
    nmbr = input("Enter 'all' or integer number of data to load: ")
    if nmbr == 'all':
        # plot all datafiles
        plot_all()  # can take about 30 seconds to run
    elif nmbr.isnumeric():
        # generate individual interactive plot
        remap(nmbr)
