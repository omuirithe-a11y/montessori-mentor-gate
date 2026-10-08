"""Verify the signed rule files before any page is stamped.

The public key is qa/rules_pub.pem. The signatures are qa/rules_sig/<name>.sig.
The private key is not in this tree. A mismatch exits 1. A missing key or signature exits 1.
"""
import os, sys

Q = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.dirname(Q)
PUB = os.path.join(Q, 'rules_pub.pem')
SIGS = os.path.join(Q, 'rules_sig')
RULES = (
    ('settled_record.json', os.path.join(Q, 'settled_record.json')),
    ('TEMPLATE.md', os.path.join(HOME, 'TEMPLATE.md')),
)

def verify():
    from cryptography.hazmat.primitives.serialization import load_pem_public_key
    from cryptography.exceptions import InvalidSignature
    if not os.path.exists(PUB):
        return 'REFUSED: no public key at qa/rules_pub.pem'
    try:
        key = load_pem_public_key(open(PUB, 'rb').read())
    except Exception as e:
        return 'REFUSED: public key cannot be read (%s)' % e
    bad = []
    for name, path in RULES:
        sig = os.path.join(SIGS, name + '.sig')
        if not os.path.exists(path):
            bad.append('%s missing' % name)
            continue
        if not os.path.exists(sig):
            bad.append('%s has no signature' % name)
            continue
        try:
            raw = open(sig, 'rb').read()
            blob = bytes.fromhex(raw.decode().strip()) if raw[:1] in (b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'a', b'b', b'c', b'd', b'e', b'f') else raw
            key.verify(blob, open(path, 'rb').read())
        except InvalidSignature:
            bad.append('%s does not match its signature' % name)
        except Exception as e:
            bad.append('%s %s' % (name, e))
    if bad:
        return 'REFUSED: signed rules differ from the files on disk: ' + '; '.join(bad)
    return ''

if __name__ == '__main__':
    msg = verify()
    if msg:
        print(msg)
        sys.exit(1)
    print('RULES SIGNED  settled_record.json and TEMPLATE.md match the public key')
