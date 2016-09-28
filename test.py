import argparse

sample = argparse.ArgumentParser()
sample.add_argument("-v","--verbose", help="increase output verbosity",action="store_true")
args = sample.parse_args()
if args.verbose:
	print "verbosity turned on"

#parser.parse_args('x --foo Y'.split())


