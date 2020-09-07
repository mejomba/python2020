# with open('orginal.txt', 'r') as rf:
#     with open('copy.txt', 'w') as wf:
#         chunk = 2
#         rf_chunk = rf.read(chunk)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk)
#             print('*')

        # for line in rf:
        #     wf.write(line)
        #     print('*')

with open('/media/mejomba/New Volume/APP/ubuntu-18.04.1-desktop-amd64.iso', 'br') as rf:
    print(rf.read(10))
    # with open('/media/mejomba/New Volume/APP/ubuntu-18.04.1-desktop-amd64_copy.iso', 'bw') as wf:

        # chunk = 1024
        # rf_chunk = rf.read(chunk)
        # while len(rf_chunk) > 0:
        #     wf.write(rf_chunk)
        #     rf_chunk = rf.read(chunk)
