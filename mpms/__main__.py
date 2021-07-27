#!/usr/bin/env python3

import logging
logger = logging.getLogger(__name__)
import os
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
from IPython.terminal.embed import InteractiveShellEmbed
from .load import load
from .mpms import MPMS
from .mpms import FilmSample
from .mpms import plot_combined
from .interactive import RawScanViewer

def raw_refitter():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '*')
    parser.add_argument('-v', '--verbose', action = 'store_true')
    args = parser.parse_args(sys.argv[1:])
    if args.verbose:
        logging.basicConfig(level = logging.INFO)
    files = load(args.FILE, '.raw')
    logger.info(f'Loading files: {" ".join(files)}')
    data = [MPMS(os.path.splitext(f)[0]) for f in files]
    shell = InteractiveShellEmbed()
    shell.magic('%matplotlib')
    viewer = RawScanViewer(data[0])
    shell()

def plot():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '*')
    parser.add_argument('--film-details', type = str, default = None)
    parser.add_argument('--min-fit', type = float, default = 0)
    parser.add_argument('--T-max', type = float, default = 300)
    parser.add_argument('--skip-raw', action = 'store_false', dest = 'load_raw')
    parser.add_argument('--no-cw', action = 'store_false', dest = 'fit_curie_weiss')
    parser.add_argument('--ndat', action = 'store_true')
    parser.add_argument('-v', '--verbose', action = 'store_true')
    args = parser.parse_args(sys.argv[1:])
    if args.verbose:
        logging.basicConfig(level = logging.INFO)
    files = load(args.FILE, '.dat')
    logger.info(f'Loading files: {" ".join(files)}')
    sample = None
    if args.film_details:
        sample = FilmSample.load_json(args.film_details)
    data = [MPMS(f, sample = sample) for f in load(args.FILE, '.dat')]
    shell = InteractiveShellEmbed()
    shell.magic('%matplotlib')
    if data:
        fig, axes = plot_combined(data, T_max = args.T_max,
                fit_curie_weiss = args.fit_curie_weiss, min_fit = args.min_fit)
    shell()
