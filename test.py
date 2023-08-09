import re

url = "product/pylesos-dlya-doma-proffi-home-ph8966-280461729/?_bctx=CAQQAQ&asb=2B3HhfdfhkjI4sGWBRi732v7UDybSCw0oPkI6d1ufMw%253D&asb2=MICJV_gG02rLODsBLtWKtIr6pAkkuJblhjIEdDGmbF0lFOl5WKEHnL6i6H5oxpVf&avtc=1&avte=2&avts=1691585217&hs=1&miniapp=seller_1"

match = re.search(r'-(\d+)/', url)
if match:
    extracted_number = match.group(1)
    print(int(extracted_number))
else:
    print("No match found")