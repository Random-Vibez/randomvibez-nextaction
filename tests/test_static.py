from pathlib import Path
import re
ROOT=Path(__file__).parents[1]
def test_contract():
 h=(ROOT/'index.html').read_text(); j=(ROOT/'app.js').read_text(); c=(ROOT/'styles.css').read_text(); p=(ROOT/'.htaccess').read_text()
 for marker in ('organization','nextAction','checklist','Export JSON','Import JSON','cookie-banner.js','browser','printBoard'): assert marker in h+j
 for bad in ('fetch(','XMLHttpRequest','innerHTML','document.write','eval('): assert bad not in j
 for marker in ('MAX_ITEMS=80','MAX_STATE','MAX_IMPORT','connect-src \'none\'','frame-ancestors','prefers-reduced-motion','@media print'): assert marker in j+c+p
 for name in ('cookie-banner.js','cookie-banner.css','preview.svg','LICENSE','SECURITY.md','README.md'): assert (ROOT/name).is_file()
def test_schema_is_bounded_and_atomic():
 j=(ROOT/'app.js').read_text(); assert 'x.items.length<=MAX_ITEMS' in j and 'raw.length>MAX_STATE' in j and 'Existing data is unchanged' in j
if __name__=='__main__': test_contract();test_schema_is_bounded_and_atomic();print('nextaction static contract: PASS')
