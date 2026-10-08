"""Stamp a page from outside the toolkit.

Takes the page path only. Copies it to a temporary directory. Verifies the signed
rule files. Writes the stamp to /home/claude/stamps/, never under qa/ or site/.
Refuses a path inside qa/ or site/, and refuses to write either tree.
"""
import os, sys, json, hashlib, tempfile, shutil

Q = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.dirname(Q)
STAMPS = '/home/claude/stamps'

def refuse(msg):
    print(msg)
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        refuse('usage: python3 qa/stamp_only.py <page.html>')
    src = os.path.abspath(sys.argv[1])
    if not os.path.isfile(src):
        refuse('REFUSED: not a file')
    for banned in (os.path.join(HOME, 'qa'), os.path.join(HOME, 'site')):
        if src == banned or src.startswith(banned + os.sep):
            refuse('REFUSED: the page is inside the toolkit')
    sys.path.insert(0, Q)
    import rules_sig
    msg = rules_sig.verify()
    if msg:
        refuse(msg)
    tmp = tempfile.mkdtemp(prefix='mm-stamp-')
    try:
        page = os.path.join(tmp, 'page.html')
        shutil.copyfile(src, page)
        digest = hashlib.sha256(open(page, 'rb').read()).hexdigest()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(STAMPS, exist_ok=True)
    out = os.path.join(STAMPS, digest + '.json')
    json.dump({'sha256': digest, 'source_name': os.path.basename(src), 'rules': 'signed'}, open(out, 'w'))
    print('STAMPED %s' % digest)
    print(out)

if __name__ == '__main__':
    main()
