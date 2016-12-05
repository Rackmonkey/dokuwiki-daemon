import secret
import sys
from dokuwiki import DokuWiki, DokuWikiError # https://github.com/fmenabe/python-dokuwiki

try:
    wiki = DokuWiki(secret.dw_url, secret.dw_user ,secret.dw_password)
except DokuWikiError as err:
    print(err)
    sys.exit(1)

wiki.pages.set("test", "asd23234")