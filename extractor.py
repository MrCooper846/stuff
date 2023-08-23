import csv
import re

def extract_universities(text):
    universities = text.strip().split("\n\n")
    return universities

def extract_info(text):
    university = re.search("(.*?)\n", text).group(1)
    match = re.search("T: (.*?)\n", text)
    if match:
        phone_number = match.group(1)
    else:
        phone_number = None
    name = re.search("C: (.*?)\n", text).group(1)
    job_title = None
    email = re.search("E: (.*?)\n", text).group(1)
    return [university, phone_number, name, job_title, email]

def write_to_csv(data):
    with open("universities.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

universities_text = """Abertay University
Bell Street, Dundee DD1 1HG
T: 01382 308290
C: Doug Watters
E: d.watters@abertay.ac.uk
www.abertay.ac.uk

Al-Maktoum College of Higher Education
124 Blackness Road, Dundee DD1 5PE
T: 01382 908070
C: Linda Gibson
E: admissions@almcollege.org.uk
www.almcollege.org.uk

Anglia Ruskin University
East Road, Cambridge CB1 1PT
T: 01245 683635
C: Syed Nooh
E: syed.nooh@aru.ac.uk 
www.aru.ac.uk

University of the Arts London
272 High Holborn, London WC1V 7EY
T: 020 7514 8167
C: Jonathon Greenhow
E:  j.greenhow@arts.ac.uk 
www.arts.ac.uk

University of Birmingham
Edgbaston, Birmingham B15 2TT
M: 07976 861195
C: Mr Michael Bissell
E: m.bissell@bham.ac.uk
www.birmingham.ac.uk

University of Bradford
Richmond Road, Bradford, West Yorkshire, BD71DP
T: 01274 234281
M: 07825 674613
C: Professor Alastair Wood
E: a.s.wood@bradford.ac.uk
https://www.bradford.ac.uk/external/

University of Bristol
International Office, 31 Great George Street, Bristol BS1 5QD
T: 0117 455 8177
M: 07816 362569
C: Elizabeth George , Deputy Head International Partnerships & Relations (Scholarships & Sponsors)
E:  international-partnerships@bristol.ac.uk
www.bristol.ac.uk

Brunel University London
Kingston Lane, Uxbridge, London UB8 3PH
T: 01895 267534
M: 07552 269641
C: Ghaith Chouiki
E: ghaith.chouiki@brunel.ac.uk
www.brunel.ac.uk 

Cambridge Seminars College
87-89 Cherry Hinton Road, Cambridge CB1 7BS
T: 01223 300 123
M: 07521 511 436
C: Sony Racheal John
E: sony.john@csc.uk
www.csc.uk

Coventry University
Priory Street, Coventry CV1 5FB
T: 07392 096277
C: Laura Vanessa Munoz
E: ad0269@coventry.ac.uk
www.coventry.ac.uk

De Montfort University
International Office, Portland Building, Room 0.22, The Gateway
Leicester LE1 9BH
T: 0116 366 4326/0781 660 1034
C: Samuel Jackson-Royle, Head of Sponsorship
E: samuel.jackson-royle@dmu.ac.uk
www.dmu.ac.uk/international

University of Essex
Wivenhoe Park, Colchester CO4 3SQ
T: O1206 872870
M: 07827 826554
C: Camille Jungwirth
E: sponsorsrelations@essex.ac.uk
https://www.essex.ac.uk

Fairleigh Dickinson University
School of Global and Public Affairs
Wroxton College of Fairleigh Dickinson University, Wroxton, Near Banbury, Oxfordshire, OX15 6PX 
T: 01295 730551
C: Dr Rosemary Cresswell, MPA Co-ordinator, Wroxton College
E: mpa@wroxton-college.ac.uk
https://www.fdu.edu/academics/colleges-schools/public-global/

Global University Systems
30 Holborn, London EC1N 2HS
T: 020 3535 1317, 07415 875683
C: Mukarab Shah, Head of Global Partnerships
E: mukarab.shah@gus.global
www.GlobalUniversitySystems.com

Imperial College London
Exhibition Road, London SW7 2AZ
T: 020 7594 2868
C: Clare Turner
E: international.relations@imperial.ac.uk
www.imperial.ac.uk

King’s College London
James Clerk Maxwell Building, 57 Waterloo Road, London SE1 8WA
T: 020 7848 3299
C: Julie Dass – Deputy Head of International Marketing
E: Julie.dass@kcl.ac.uk
www.kcl.ac.uk

University of Central Lancashire
Fylde Road, Preston PR1 2HE
T: 01772 895024
C: Jill Palmer
E: jpalmer10@uclan.ac.uk
www.uclan.ac.uk

Leeds Beckett University
International Recruitment & Partnerships, Bronte Hall, Headingley Campus, Leeds LS6 3QS
T: 0113 8123759
C: Puspa Mistry
E: p.mistry@leedsbeckett.ac.uk
www.leedsbeckett.ac.uk

Liverpool John Moores University
Exchange Station, Tithebarn St, Liverpool L2 2QP
T: 0151 904 6654
C: Matthew Virr
E: M.D.Virr@ljmu.ac.uk
www.ljmu.ac.uk

University of London
Stewart House, 32 Russell Square, London WC1B 5DN
T: 020 7664 4821
C: Alex Boughton, Head of Business Development
E: alex.boughton@london.ac.uk
www.london.ac.uk

Institute of Diplomacy and International Governance,
Loughborough University London
Here East, 3 Lesney Avenue, Queen Elizabeth Olympic Park
London E15 2GZ
T: 020 3818 0777
C: Professor Helen Drake
E: H.P.Drake@lboro.ac.uk
www.lborolondon.ac.uk

University of Manchester
International Development, Rutherford Building, Coupland Street, Manchester M13 9PL
T: 0161 275 2060
C: Tanya Luff, Head of International Relations
E: international.relations@manchester.ac.uk
www.manchester.ac.uk

Newcastle University
King’s Gate Building, Newcastle Upon Tyne NE1 7RU
T: 0191 208 6069
C: Stephen North
E: sponsors@ncl.ac.uk
www.ncl.ac.uk

Northumbria University Newcastle
International Development Office, Pandon Building, Newcastle upon Tyne NE1 8QE
T: 07710 115355
C: Isabel Sardo, International Sponsors Coordinator
E: isabel.sardo@northumbria.ac.uk
www.northumbria.ac.uk

University of Nottingham
Sponsor Relations, Cherry Tree Lodge, University Park Campus, Nottingham NG7 2RD
C: Chloe Bates
E: sponsorship-assistant@nottingham.ac.uk
www.nottingham.ac.uk

University of Portsmouth
UoP Global, Nuffield Centre, St. Michael’s Road, Portsmouth, PO1 2ED
T: 02392 843488
M: 07702 821791
C: Joe Hall
E: joe.hall@port.ac.uk
www.port.ac.uk

Queen Mary University of London
Mile End Road, London E1 4NS
T: 020 7882 5555
M: 07494 775858
C: Flora Mckay
E: f.mckay@qmul.ac.uk
https://www.qmul.ac.uk/

Queen’s University Belfast
International Office, Lanyon North, University Road, Belfast, BT7 1NN
T: 028 9097 5088
C: Susan McCleary, Global Sponsors Manager
E: globalpartners@qub.ac.uk
www.qub.ac.uk

University of Reading
Whiteknights, PO Box 217, Reading, Berkshire RG6 6AH
T: 0118 378 3838
C: Andy Howman
E: a.howman@reading.ac.uk
www.reading.ac.uk

University of Salford
International and Regional Directorate, The Crescent, Salford
Greater Manchester M5 4WT
T: 0161 295 5402
C: Quentin Albert, Sponsor Relationship Manager
E: q.albert@salford.ac.uk
www.salford.ac.uk

University of Sheffield
Western Bank, Sheffield S10 2TN
T: 0114 222 2000
C: Adam Brown
E: Adam.R.Brown@sheffield.ac.uk
www.sheffield.ac.uk

SOAS University of London
10 Thornhaugh Street, Russell Square, London WC1H 0XG
T: 020 7898 4838
C: Esther Okwok or Simangaliso Angela Mpofu
E: esther.okwok@soas.ac.uk or s.mpofu@soas.ac.uk
www.soas.ac.uk

University of Surrey
Marketing Recruitment and Admissions Directorate, Duke of Kent Building, Guildford GU2 7XH
T: 014836 830 0800
M: 07540 201301
C: Sharath Meppallil (International Student Recruitment Manager)
E: s.meppallil@surrey.ac.uk
www.surrey.ac.uk

Warwick Business School
Scarman Road, Coventry CV4 7AL
T: 024 7652 4306
C: Nav Kaur Aujla
E: nav.aujla@wbs.ac.uk
www.wbs.ac.uk

The University of Warwick
Coventry CV4 7AL
T: 0247 652 4933
C: Caroline Rushingwa
E: c.rushingwa@warwick.ac.uk
www.warwick.ac.uk

University of Westminster
Global Recruitment and Admissions,101 New Cavendish Street
London W1W 6XH
T: 020 7911 5000 Ext 66071
C: Barbara Kelhar, Regional Manager
E: b.kelhar@westminster.ac.uk 
www.westminster.ac.uk

University of Winchester
Sparkford Road, Winchester, Hants SO22 4NR
T: 01962 827489
C: David Street
E: David.Street@winchester.ac.uk
www.winchester.ac.uk"""

universities_list = extract_universities(universities_text)

for university in universities_list:
    write_to_csv(extract_info(university))