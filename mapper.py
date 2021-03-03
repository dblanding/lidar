import matplotlib.pyplot as plt
from matplotlib import style
import pickle
from pprint import pprint

style.use('fivethirtyeight')

def load_base_map(filename=None):
    """Load (native cadvas) file, return list of geom line coords (cm)

    coordinates returned are a tuple of 2 end points of line segment
    where each point is a tuple of X, Y coordinates
    ((X1, Y1), (X2, Y2))
    X and Y coordinate values are converted from mm to cm.
    """

    if not filename:
        filename = 'map.pkl'
    with open(filename, 'rb') as file:
        data = pickle.load(file)

    coordlist = [((v[0][0][0]/10, v[0][0][1]/10),
                  (v[0][1][0]/10, v[0][1][1]/10))
                 for entity in data
                 for k, v in entity.items()
                 if k == 'gl']

    return coordlist

def plot(scanpoints, map_lines=None, map_folder="Maps", seq_nmbr=None, show=True,
        display_all_points=True):
    """Plot all points and line segments and save in map_folder.

    Optional args:
    display_all_points=False to plot only points in regions
    seq_nmbr appended to save_file_name
    show=True to display an interactive plot (which blocks program).
    """

    filename = f"{map_folder}/scanMap"
    if seq_nmbr:
        str_seq_nmbr = str(seq_nmbr)
        # prepend a '0' to single digit values (helps viewer sort) 
        if len(str_seq_nmbr) == 1:
            str_seq_nmbr = '0' + str_seq_nmbr
        imagefile = filename + str_seq_nmbr + ".png"
    else:
        imagefile = filename + ".png"

    #fig = plt.figure()
    #ax = fig.add_axes([0, 0, 1, 1])  # all must be between 0 and 1
    #ax.set_xlim(-400, 800)
    #ax.set_ylim(-400, 800)

    # build data lists to plot scan points
    xs = []
    ys = []
    for point in scanpoints:
        x, y = point
        xs.append(x)
        ys.append(y)
    plt.scatter(xs, ys, color='#003F72')


    # plot map
    for segment in map_lines:
        x_vals = [segment[0][0], segment[1][0]]
        y_vals = [segment[0][1], segment[1][1]]
        plt.plot(x_vals, y_vals, linewidth=1, color="k")

    plt.axis('equal')

    if show:
        plt.show()  # shows interactive plot
    plt.clf()  # clears previous points & lines


if __name__ == "__main__":
    filename = 'map.pkl'
    segs = load_base_map(filename)
    plot(segs)