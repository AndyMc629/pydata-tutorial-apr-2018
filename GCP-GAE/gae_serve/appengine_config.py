"""`appengine_config` gets loaded when starting a new application instance."""
#import sys
#import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.

#sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')
#vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
