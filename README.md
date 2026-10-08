# Montessori Mentor gate

The rule files in this repository are signed. `qa/rules_sig.py` refuses if `settled_record.json` or `TEMPLATE.md` differ from the signature. The private key is not in this repository.

`main` is meant to accept a change only through a pull request whose `rules-signature / verify` check has passed. The chat does not publish the website from here.
