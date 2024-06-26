#!/usr/bin/env python
# vim: set ts=4:sw=4:et:ai
# Copyright (C) 2024 Etienne Robillard smart@open-neurosecurity.org
"""Python script to update Sitemaps using IndexNow service."""
from yandexupdater import IndexNow
import re
import sys
import os

__version__ = "0.2"

# By default we use Yandex.com api.
api_url = 'https://yandex.com/indexnow'

# Change this
hostkey  = "ahnjournal-93ddfbdd49596a2c50b0"

# Server hostname
hostname = "open-neurosecurity.org"

# Location of sitemap.xml file
data = open('/home/www/html/sitemap.xml', 'r').read()
pattern = '(?<=<loc>)[a-zA-z]+://[^\s]*(?=</loc>)'

def main():
    urls = re.findall(pattern, data)
    api = IndexNow(key=hostkey, host=hostname)
    try:
        status = api.index(urls)
    except Exception:
        raise Exception("Error sending sitemap to %s" % api_url)
    else:
        print(f"Response: {status}")

if __name__ == '__main__':
    if '--dry-run' in sys.argv:
        sys.exit(0)
    elif '--help' in sys.argv:
        print("Usage: python ./yandex-webmaster-indexnow.py [-v] [--license|--dry-run]")
        sys.exit(2)
    elif '-v' in sys.argv:
        print("%s %s" % (os.path.basename(__file__), __version__))
        sys.exit(2)
    elif '--license' in sys.argv:
        license = r"""\
Copyright (C) 2024 Etienne Robillard <smart@open-neurosecurity.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Copyright (c) 2023 Ajit Jasrotia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        print(license)
        sys.exit(0)
    else:
        print("Updating sitemap to %s" % api_url)
        main()
#
