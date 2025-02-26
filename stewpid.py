import base64

def decode_string(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

# Encoded strings.  Replace with your original text after encoding.
TEXT1 = "WU91IGFyZSBhIGdvYmxpbiBmcm9tIEZsb3JpZGEgYW5kIHlvdSB0cnkgdG8gZ2V0IHRvIERCLiAKWW91ciBxdWVzdDogVG8gc3RlYWwgVGhlIERlY2xhcmF0aW9uIG9mIEluZGVwZW5kZW5jZSBhbmQgcmVwbGFjZSBpdCB3aXRoIGEgbG92ZSBsZXR0ZXIgdG8gZ2F0b3JzLgo="
TEXT2 = "CkhvdyBkbyB5b3UgdHJhdmVsPwoxLiBCeSBDYXIgKGJvcnJvd2VkLi4ucGVybWFubmVudGx5KQoyLiBCeSBQbGFuZSAoc25lYWtpbmcgb24gaXMgYW4gb3B0aW9uKQozLiBPbiBmb290IChnb3R0YSBsb3ZlIHRob3NlIHNjZW5pYyByb3V0ZXMpCg=="
TEXT3 = "WU91ICJib3Jyb3dlZCIgYSBiZWF0LXVwIHBpY2t1cCB0cnVjay4gQWZ0ZXIgYSBmZXcgaG91cnMsIHNtb2tlIGJpbGxvd3MgZnJvbSB0aGUgZW5naW5lISBZb3UncmUgc3RyYW5kZWQgaW4gcnVyYWwgR2VvcmdpYS4KMS4gVHJ5IHRvIGZpeCB0aGUgdHJ1Y2sgb3Vyc2VsZi4gKFlvdSBrbm93Li4uZ29ibGluIGVuZ2luZWVyaW5nISkKMi4gSGl0Y2hoaWtlIHdpdGggYSBzaWduIHRoYXQgc2F5cyAiREMgb3IgQnVzdCEgV2lsbCBXb3JrIGZvciBHYXMuIgozLiBBYmFuZG9uIHRoZSB0cnVjayBhbmQgdHJ5IHRvIHN0ZWFsIGEgYnljaWNsZS4K"
TEXT4 = "CllvdSB0aW5rZXIgd2l0aCB0aGUgZW5naW5lLCBoaXR0aW5nIGl0IHdpdGggYSByb2NrIGFuZCBzcGl0dGluZyBvbiBpdC4gTWlyYWN1bG91c2x5LCBpdCBzcHV0dGVycyBiYWNrIHRvIGxpZmUhIEJ1dCBub3cgdGhlcmUncyBhIHN0cmFuZ2Uga25vY2tpbmcgc291bmQuLi4KMS4gSWdub3JlIHRoZSBrbm9ja2luZyBhbmQgZmxvb3IgaXQhIChIb3BlIGZvciB0aGUgYmVzdCEpCjIuIFRyeSB0byBmaWd1cmUgb3V0IHdoYXQncyBjYXVzaW5nIHRoZSBrbm9ja2luZy4gKFByb2JhYmx5IGEgc25ha2UuKQozLiBQdWxsIG92ZXIgYW5kIHRyYWRlIHRoZSB0cnVjayB0byBzb21lIGxvY2FsIG1vb25zaGluZXJzIGZvciBhIGRvbmtleSBhbmQgd2Fnb24uCg=="
TEXT5 = "VGhlIGVuZ2luZSBleHBsb2RlcyBzcGVjdGFjdWxhcmx5IGEgZmV3IG1pbGVzIGxhdGVyLiBZb3UgbG9zZS4uLmFuZCBzbWVsbCBsaWtlIGJ1cm50IHJ1YmJlci4="
TEXT6 = "VGhlICdrbm9ja2luZycgdHVybnMgb3V0IHRvIGJlIGEgZmFtaWx5IG9mIHNxdWlycmVscyB3aG8gYXJlIHZlcnkgdW5oYXBweSB3aXRoIHlvdXIgZW5naW5lIG1vZGlmaWNhdGlvbnMuIFRoZXkgYml0ZSB5b3UgcmVwZWF0ZWRseS4gR2FtZSBPdmVyLg=="
TEXT7 = "ClRoZSBkb25rZXksIEJlc3NpZSwgaXMgc3VycHJpc2luZ2x5IGZhc3QhIEhvd2V2ZXIsIHlvdSByZWFjaCBhIGNyb3Nzc29hZHMuLi4KMS4gVGFrZSB0aGUgaGlnaHdheSAoZmFzdGVyLCBidXQgcmlza2llciEpCjIuIFN0aWNrIHRvIHRoZSBiYWNrcm9hZHMgKHNhZmVyLCBidXQgc2xvd2VyKQozLiBUcnkgdG8gZGlzZ3Vpc2UgQmVzc2llIGFzIGEgdmVyeSBoYWlyeSBob3JzZSB0byBhdm9pZCBzdXNwaWNpb24uCg=="
TEXT8 = "QmVzc2llIGdldHMgc3Bvb2tlZCBieSBhIHNlbWktdHJ1Y2sgYW5kIGdhbGxvcHMgb2ZmIGludG8gdGhlIHdvb2RzLiBZb3UncmUgbG9zdCBmb3JldmVyLiBHYW1lIE92ZXIu"
TEXT9 = "WW91IGFycml2ZSBpbiBEQywgYWxiZWl0IHNtZWxsaW5nIHN0cm9uZ2x5IG9mIG1hbnVyZS4gWW91IG1hbmFnZSB0byBldmFkZSBzZWN1cml0eSwgcmVwbGFjZSB0aGUgZG9jdW1lbnRzLCBhbmQgcmR1ZSBCZXNzaWUgYmFjayB0byBGbG9yaWRhLiBZb3Ugd2luIQ=="
TEXT10 = "QSBob3JzZSBicmVlZGVyIHNlZXMgdGhyb3VnaCB5b3VyIGRpc2d1aXNlIGFuZCByZXBvcnRzIHlvdS4gWW91IGFyZSBhcnJlc3RlZCBmb3IgZG9ua2V5IGZyYXVkLiBHYW1lIE92ZXIu"
TEXT11 = "SW52YWxpZCBjaG9pY2UuIEEgZ2F0b3IgZWF0cyB5b3Ugb3V0IG9mIGNvbmZ1c2lvbi4gWW91IGxvc2Uu"
TEXT12 = "CkEga2luZGx5IG9sZCBsYWR5IHBpY2tzIHlvdSB1cC4gU2hlIHNlZW1zIGEgYml0Li4uZWNjZW50cmljLgoxLiBUcnkgdG8gc3VidGxlIGNvbnZpbmNlIGhlciB0byBkcml2ZSB5b3UgYWxsIHRoZSB3YXkgdG8gREMuCjIuIFRlbGwgaGVyIHRoZSB0cnV0aCBhYm91dCB5b3VyIG1pc3Npb24gKG1heWJlIHNoZSdzIGEgc2VjcmV0IGdvYmxpbiBzeW1wYXRoaXplciklejMufQogIkFjY2lkZW50YWxseSIgc3BpbGwgIm1vdG9yIG9pbCIgb24gaGVyIHNlYXQgYW5kIGRlbWFuZCBzaGUgdGFrZSB5b3UgdG8gREMgdG8gY29tcGVuc2F0ZS4K"
TEXT13 = "U2hlIGRyb3BzIHlvdSBvZmYgYXQgYSBiaW5nbyBoYWxsIHRocmVlIHRvd25zIG92ZXIgYW5kIHRoaW5rcyB0aGF0IHlvdSdyZSBjcmF6eS4gR2FtZSBPdmVyLg=="
TEXT14 = "U2hlIHNjcmVhbXMsIHB1bGxzIG92ZXIsIGFuZCBjYWxscyB0aGUgcG9saWNlLiBZb3UgYXJlIGFycmVzdGVkIGFuZCBkZXBvcnRlZCBiYWNrIHRvIEZsb3JpZGEuIEdhbWUgT3Zlci4="
TEXT15 = "U2hlIGlzIGVucmFnZWQgYW5kIGtpY2tzIHlvdSBvdXQgb2YgdGhlIGNhci4gWW91IGxvc2Uu"
TEXT16 = "ClpvdSBmaW5kIGEgcnVzdHksIG9uZS13aGVlbGVkIGJ5Y2ljbGUgbGVhbmluZyBhZ2FpbnN0IGEgYmFybi4gSXQncyBiZXR0ZXIgdGhhbiBub3RoaW5nIQoxLiBTdGFydCBwZWRhbGluZyB0b3dhcmRzIERCISAoSWdub3JlIHRoZSB3b2JibHkgd2hlZWwuKQoyLiBUcnkgdG8gZmluZCBhbm90aGVyIHdoZWVsIhtheWJlIGZyb20gYSBwYXNzaW5nIGxhd25tb3dlcj8pCjMuIFVzZSB0aGUgYnljaWNsZSBhcyBhIHdlYXBvbiB0byBzdGVhbCBhIGJldHRlciBieWNpY2xlIGZyb20gYSBjaGlsZC4K"
TEXT17 = "WW91IGZhbGwgb2ZmIHRoZSBieWNpY2xlIGV2ZXJ5IGZldyBtaW51dGVzIGFuZCBnZXQgZWF0ZW4gYnkgYW4gYW5pbWFsLiBZb3UgbG9zZS4="
TEXT18 = "QSBsYXdubW93ZXIgd2hlZWwgZG9lc24ndCBmaXQhIFlvdSB3YXN0ZSB2YWx1YWJsZSB0aW1lIGFuZCBnZXQgZWF0ZW4gYnkgYSBnYXRvci4gR2FtZSBPdmVyLg=="
TEXT19 = "VGhlIGNoaWxkJ3MgcGFyZW50cyBhcmUgbm90IGhhcHB5LiBUaGV5IGNhbGwgdGhlIHBvbGljZS4gR2FtZSBPdmVyLg=="
TEXT20 = "ClVvdSBhcnJpdmUgYXQgdGhlIGFpcnBvcnQsIGxvb2tpbmcgZGVjaWRlZGx5Li4udW4tYWlycG9ydC1saWtlLiBTZWN1cml0eSBpcyB0aWdodC4gV2hpY2ggYWlybGluZSBkbyB5b3UgdHJ5IHRvIHNua2FrIG9udG8/CjEuIFVuaXRlZCBBaXJsaW5lcyAoVGhleSBzZWVtIHBlcnBldHVhbGx5IGNvbmZ1c2VkLCBnb29kIGZvciBzbmVha2luZyEpCjIuIERlbHRhIEFpcmxpbmVzIChNYXliZSB5b3UgY2FuIGJsZW5kIGluIHdpdGggdGhlIGJ1c2luZXNzIHRyYXZlbGVycz8pCjMuIEFtZXJpY2FuIEFpcmxpbmVzIChHbyBiaWcgb3IgZ28gaG9tZSwgcmlnaHQ/KQ=="
TEXT21 = "WW91IGdldCBvbiB0aGUgcGxhbmUuIFdoaWxlIHN3aXRjaGluZyB0aGUgZG9jdW1lbnRzLCB5b3UgYXJlIGNvbmZyb250ZWQgYnkgc2VjdXJpdHkuIEdhbWUgT3Zlci4="
TEXT22 = "ClVvdSBkZWNpZGUgdG8gd2Fsay4gOTE5IG1pbGVzISBZb3UncmUgdG91Z2hlciB0aGFuIHlvdSBsb29rIChwcm9iYWJseSkuCjEuIFRyeSB0byBzY2F2ZW5nZSBmb3IgZm9vZCBhbmQgc3VwcGxpZXMgYWxvbmcgdGhlIHdheS4KMi4gUmVseSBvbiB0aGUga2luZG5lc3Mgb2Ygc3RyYW5nZXJzIChnb29kIGx1Y2sgd2l0aCB0aGF0KS4KMy4gRW1icmFjZSB5b3VyIGlubmVyIGdvYmxpbiBhbmQgcmFpZCBnYXMgc3RhdGlvbnMgZm9yIHNuaWNrcyBhbmQgcm9hZCBtYXBzLgo="
TEXT23 = "WW91IHN0YXJ2ZSB0byBkZWF0aCBtaWxlcyBhd2F5LiBHYW1lIE92ZXIu"
TEXT24 = "UGVvcGxlIGF2b2lkIHlvdSBhdCBhbGwgY29zdHMuIEdhbWUgT3Zlci4="
TEXT25 = "WW91IGJlY29tZSBhIGxlZ2VuZC4gVGhlIGxvY2FsIG5ld3MgcmVwb3J0cyBhYm91dCBhIHRpbnkgZ3JlZW4gYmFuZGl0IHRlcnJvcml6aW5nIHRoZSBzb3V0aGVhc3QuIFlvdSBnZXQgb24gdGhlIG5ld3MgYW5kIGFyZSBzdG9wcGVkLiBHYW1lIE92ZXIu"

print(decode_string(TEXT1))

choice = input(decode_string(TEXT2))

if choice == "1":
    choice = input(decode_string(TEXT3))
    if choice == "1":
        choice = input(decode_string(TEXT4))
        if choice == "1":
            print(decode_string(TEXT5))
        elif choice == "2":
            print(decode_string(TEXT6))
        elif choice == "3":
            choice = input(decode_string(TEXT7))
            if choice == "1":
                print(decode_string(TEXT8))
            elif choice == "2":
                print(decode_string(TEXT9))
            elif choice == "3":
                print(decode_string(TEXT10))
            else:
                print(decode_string(TEXT11))
    elif choice == "2":
        choice = input(decode_string(TEXT12))
        if choice == "1":
            print(decode_string(TEXT13))
        elif choice == "2":
            print(decode_string(TEXT14))
        elif choice == "3":
            print(decode_string(TEXT15))
        else:
            print(decode_string(TEXT11))
    elif choice == "3":
        choice = input(decode_string(TEXT16))
        if choice == "1":
            print(decode_string(TEXT17))
        elif choice == "2":
            print(decode_string(TEXT18))
        elif choice == "3":
            print(decode_string(TEXT19))
        else:
            print(decode_string(TEXT11))

elif choice == "2":
    choice = input(decode_string(TEXT20))
    if choice == "1":
        print(decode_string(TEXT21))
    elif choice == "2":
        print(decode_string(TEXT21))
    elif choice == "3":
        print(decode_string(TEXT21))
    else:
        print(decode_string(TEXT11))

elif choice == "3":
    choice = input(decode_string(TEXT22))
    if choice == "1":
        print(decode_string(TEXT23))
    elif choice == "2":
        print(decode_string(TEXT24))
    elif choice == "3":
        print(decode_string(TEXT25))
    else:
        print(decode_string(TEXT11))

else:
    print(decode_string(TEXT11))