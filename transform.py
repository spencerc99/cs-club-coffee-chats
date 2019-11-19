import pandas as pd
from collections import defaultdict

data = dict({
    "May Zhong": [(('am118', 'Avanthika Mahendrababu'), 0.4), (('meb19', 'Mojola Balogun'), 0.3333333333333333)],
    "Josiah Grace": [(('wpl1', 'Will Ledig'), 0.5), (('eyh2', 'Emily Hwang'), 0.4)],
    "Philip Taffet": [(('rq4', 'Ryan Quach'), 0.5), (('Dcp5', 'Daniel Pham'), 0.4)],
    "Waseem Ahmad": [(('xt12', 'Cara Tan'), 0.5), (('Mdk4', 'Michael Koceja'), 0.5)],
    "Patrick Granahan": [(('vk20', 'Varun Kataria'), 0.6), (('wh19', 'Wei-Lin Hsiao'), 0.5)],
    "Bin Wang": [(('xc17', 'Stephen Chen'), 0.6666666666666666), (('mm99', 'Eva Ma'), 0.7142857142857143)],
    "Nick Vollmar": [(('ct38', 'Christina Tan'), 1.0), (('tpv1', 'Thanh Vu'), 0.6666666666666666)],
    "Greg Kinman": [(('vah3', 'Valerie Hellmer'), 1.0), (('dg46', 'Diksha Gupta'), 1.0)],
    "Sam Shadwell": [(('stx1', 'Stephanie Xie'), 1.0), (('Tc43', 'Tim Cheng'), 1.0)],
    "Jonathan Wang": [(('jf52', 'Jiamu Feng'), 1.0), (('kdt6', 'Kaarthika Thakker'), 0.75)],
    "Matt Bernhard": [(('hy28', 'Anthony Yu'), 1.0), (('Dpf2', 'Daniel Fay'), 0.6666666666666666), (('Jdr7', 'Jacob Reinhart'), 1.0)],
    "Will Koh": [(('sdm9', 'Sanat Mehta'), 1.0), (('ttl4', 'Tam Le'), 1.0)],
    "Spencer Chang": [(('cww3', 'Christine Wang'), 1.0),  (('sm103', 'Shashank Mahesh'), 0.5)],
    "Avery Jordan": [(('hjo2', "Hugh O'Reilly"), 0.8), (('mjd4', 'Melinda Ding'), 0.5)],
    "Raymond Yuan": [(('wwl3', 'Winnie Li'), 1.0)],
    "Ashley Gentles": [(('nnq1', 'Noushin '), 0.6666666666666666), (('nes4', 'Natalie Siejczuk'), 1.0)],
    "Abhijeet Mulgund": [(('jd50', 'Jack Duryea'), 1.0), (('lc61', 'Luis Clague'), 0.5714285714285714)],
    "Zhouhan Chen": [(('ty19', 'Thomas Yuan'), 1.0)],
    "Jeffrey Xiong": [(('zl41', 'Mike Lin'), 1.0)],
    "Napas Udomsak": [(('cjd8', 'Jacob Diaz'), 1.0), (('alh9', 'Angela Hwang'), 0.5)],
    "Meghana Chilukuri": [(('ecc6', 'Elliana Clermont'), 1.0), (('ob10', 'Oeishi Banerjee'), 1.0)],
    "Nicholas Hirsch": [(('tl54', 'Austin Liu'), 0.75), (('pmr3', 'Peter Rizzi'), 0.6666666666666666)],
    "Terrence Liu": [(('lg43', 'Laura Goon'), 0.8), (('yl125', 'Yvonne Liu'), 0.6666666666666666)],
    "Zheng Zhu": [(('ts40', 'Sandra Shi'), 1.0), (('jh83', 'Jian Huang (Richard)'), 0.75)],
    "Cade Ritter": [(('vr14', 'Vicram Rajagopalan'), 1.0)],
    "Robyn Narro":[(('Lpb3', 'Liam Bonnage'), 0.4)]
})

df = pd.DataFrame()

for mentor, mentees in data.items():
    row = {}
    row['Mentor name'] = mentor
    i = 1
    for mentee in mentees:
        net_id, name = mentee[0]
        row['Mentee{} name'.format(i)] = name
        row['Mentee{} netid'.format(i)] = net_id
        i += 1
    df = df.append(row, ignore_index=True)

df.to_csv('output.csv')
