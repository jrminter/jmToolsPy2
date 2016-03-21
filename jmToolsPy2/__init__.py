from .savitzky_golay import savitzky_golay
from .peak_detect import peak_detect
try:
 import hyperspy
 from .hs_tools import *
except ImportError, e:
 pass # module doesn't exist, deal with it.
# from .hs_tools import *
from .plotting_tools import *
from map_tools import *
from utils import *