import re
mystr ='''The conclusion of this study suggests that knowledge of specific domain improves the results. Also,
different attributes have been added to the project which will prove to be advantageous to the system. The
requirements and specifications have been listed above. This project is implemented using Android and the
SQL domain. Using the GPS system, the application will automatically display the buses on map and its
routes to the different locations and also track the bus location using client-server technology and forward it
to the client device. It uses latitude & longitude as measurement to calculate distance between two locations
and provides necessary details of each and every route for people to easily catch-up with the buses or any
other conveyance possible on the specified route. Specific location details are provided to the user along with
the bus location so that the person can identify the bus correctly. It uses remote server as its database. Due to
this, the records can be easily presented on the client‟s device itself so that the server burden get reduced.
References
[1] B.Caulfield and M.O‟Mahony,“An examination of the public transport information requirements of users”, IEEE
Trans.Intell.Transp. Syst., vol. 8, no. 1, pp. 21–30, Mar. 2007.
12345678909-4746734683289740915
[2] K.Rehrl,S.Bruntsch,andH.-J.Mentz,“Assisting multimodal travelers: Design and prototypical implementation of a personal
travel companion,” IEEE Trans. on Intelligent Transportation Systems, vol. 8, no. 1, pp. 31–42, Mar
'''
#findall, search, split, sub, finditer.
# patt = re.compile(r'GPS')
# patt = re.compile(r'.Using')
# patt = re.compile(r'^The')
# patt = re.compile(r'Mar$')
# patt = re.compile(r'(us){1}')
# patt = re.compile(r'us{1}|t')
# patt = re.compile(r'\AThe')
# patt = re.compile(r'us\B')
patt = re.compile(r'\d{5}-{4}')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[323:330])
