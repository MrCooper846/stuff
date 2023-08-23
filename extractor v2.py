# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:46:58 2023

@author: monke
"""

import re
import csv

def extract_emails(text):
    # Use a regular expression to find all names and emails in the text
    pattern = r'([\w\s.,]+)\s*<([\w\.-]+@[\w\.-]+)>'
    matches = re.findall(pattern, text)

    # Write the names and emails to a CSV file
    with open('emails.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for match in matches:
            writer.writerow({'Name': match[0], 'Email': match[1]})

text = "Mosab Tabash <mosab.tabash@aau.ac.ae>, Sweta Patnaik <PATNAIKS@cput.ac.za>, Mirela Panait <mirela.matei@upg-ploiesti.ro>, Upasana Gitanjali Singh <Singhup@ukzn.ac.za>, Wabike PP, Paul <p.p.wabike@pl.hanze.nl>, Anand Agrawal <prof.anand@gmail.com>, Falk, Audrey <falka@merrimack.edu>, R. Kavena Shalyefu <kshalyefu@gmail.com>, Fareeda Khodabocus <f.khodabocus@uom.ac.mu>, Abeer Salem <abeer_salem_eg@yahoo.com>, Dr. Diana A.Karim Al Jahromi <daljahrami@uob.edu.bh>, Elena Garcia Ansani <elena@egarciaansani.com>, Serpil Meri <serpilmeri@gmail.com>, Mojca Gabrijelcic <mojca.k.gabrijelcic@pef.upr.si>, Nour el houda CHAOUI <houda.chaoui@usmba.ac.ma>, Sameerah Saeed <samira.saeed@tiu.edu.iq>, Andras Szucs <andras.szucs.eden@gmail.com>, Tina Refning <tina@yintelligence.dk>, Eugenie Panitsides <eugeniapanou@gmail.com>, Abhilasha Singh <abhilasha.singh@aue.ae>, Dr. M. Bhaskara Rao <mbr.mpb@gmail.com>, Jennifer Miles <Jmmiles789@gmail.com>, Hari Kamali <hckamali2019@gmail.com>, Ahmet Su <suahmet32@gmail.com>, Haydeé Ramírez Lozada <ramirezlozadahaydee@gmail.com>, Barbara Cozza <cozzab@stjohns.edu>, Douglas Svotwa <douglas.svotwa@bothouniversity.ac.bw>, Habiba CHAOUI <habiba.chaoui@uit.ac.ma>, Majid Ali <majid.ali@hotmail.com>, Arlinda Beka <arlinda.beka@uni-pr.edu>, INDRANIL BOSE <sentindranil72@gmail.com>, Mohammad Tareque Rahman <tareque.rahman@ulab.edu.bd>, Angelica Pazurek <apazurek@umn.edu>, Martha Nunez <martha.nunez@tec.mx>, Chamila Subasinghe Arachchilage Don <chamilas@curtin.edu.au>, SHI WEI CHU <ShiWei.Chu@nottingham.edu.my>, Dara Abdulla Al-Banna <dara.albanna@hmu.edu.krd>, Martina Jordaan <martina.jordaan@up.ac.za>, Tina Bass <T.Bass@derby.ac.uk>, Ahmad Samarji <ahmad.samarji@live.vu.edu.au>, Dr. Sarwat Nauman <sarwat.nauman@iobm.edu.pk>, Ying Liu <ying30s@yahoo.co.uk>, hanan gouda <hanan.gouda@aast.edu>, Martha Nunez <martha.nunez7@gmail.com>, M M C Shohel <mahruf.shohel@yahoo.co.uk>, Gisele M. Arruda <anvivort@gmail.com>, Taisir Subhi Yamin <taisir@icieworld.net>, Saba Mansoor A Qadhi <sabaa@qu.edu.qa>, Nasiruddin Nezaami <n_nezaami@yahoo.com>, Abeer Salem <asalem@prescott.edu>, Nandita Mishra <saanvinandita@gmail.com>, Damini Saini <dsaini@iimraipur.ac.in>, Humphrey Oborah <kombora2021@gmail.com>, Eglantina Hysa <ehysa@epoka.edu.al>, Beena Giridharan <beena@curtin.edu.my>, I. Rozendal <ingerozendal@gmail.com>, abdelkhalig mohamed <ak@gulfconferences.co.uk>, Martina Jordaan <martinajordaan@gmail.com>, Amudha Poobalan <a.poobalan@abdn.ac.uk>, Tina Bass <tinabass@hotmail.co.uk>, Michael T. Miller <mtmille@uark.edu>, Anand Agrawal <anand.agrawal@bluecrest.edu.gh>, Dr. Sateesh Arja <sarja@avalonu.org>, Sirkka-Liisa Marjatta Uusimäki <liisa.uusimaki@gu.se>"
extract_emails(text)