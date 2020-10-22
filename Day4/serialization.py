# json serialization using simplejson

import simplejson as json

# dump() will write Python data to a file-like object. We use this when we want to
# serialize our Python data to an external JSON file.
#
# dumps() will write Python data to a string in JSON format. This is useful if we want
# to use the JSON elsewhere in our program, or if we
# just want to print it to the console to check that it’s correct.

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

# load() will load JSON data from a file-like object. We use this method when we’re reading in data from
# a file-like object.
#
# loads() will load JSON data from a string containing JSON-encoded data.