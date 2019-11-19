######################################################################
# TODO: change to just use df instead of indexing into a list with a df.
######################################################################

import pandas as pd
import csv
import os
os.chdir('./data')
path = os.getcwd() + '/cs_coffee_chats_spring2018_final.csv'
mentors = []
mentees = []
netid_to_info = {}

with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    headers = next(reader)
    print(headers)
    netid_idx = headers.index('What is your net id?')

    preference_idx = headers.index("Preference")
    done_idx = headers.index("Done")
    for row in reader:
        preference = row[preference_idx]
        if row[-1] == "yes":
            continue
        if preference == "mentor":
            mentors.append(row)
        else:
            mentees.append(row)
        netid_to_info[row[netid_idx]] = row
[mentor[2] for mentor in mentors]
df = pd.DataFrame.from_csv(path=path, header=0, index_col=1)
print ("Headers: {}".format(df.columns.values))
df["Year"].unique()

netid = "What is your net id?"
name_idx = headers.index('What is your name?')
interests_idx = headers.index('What are your interests?')
interests_name = 'What are your interests?'
len(df)
# df[interests_name]['']
from collections import defaultdict
mentor_to_mentees = {}

year_to_int = defaultdict(lambda: 5)
year_to_int['Freshmen'] = 1
year_to_int['Sophomore'] = 2
year_to_int['Junior'] = 3
year_to_int['Senior'] = 4

year_idx = headers.index("Year")

def parse_interests(interests):
    return interests.split(', ')


def mentee_over_mentor_weight_fn(mentor, mentee):
    mentor_interests = set(parse_interests(mentor[interests_idx]))
    mentee_interests = set(parse_interests(mentee[interests_idx]))
    if len(mentee_interests) == 1 and 'idk' in mentee_interests:
        return .01
    # disregard idk
    mentor_interests.discard('idk')
    mentee_interests.discard('idk')
    return len(mentor_interests.intersection(mentee_interests)) / len(mentee_interests)

def mentor_over_mentee_weight_fn(mentor, mentee):
    mentor_interests = set(parse_interests(mentor[interests_idx]))
    mentee_interests = set(parse_interests(mentee[interests_idx]))
    if len(mentee_interests) == 1 and 'idk' in mentee_interests:
        return .01
    # disregard idk
    mentor_interests.discard('idk')
    mentee_interests.discard('idk')
    return len(mentor_interests.intersection(mentee_interests)) / len(mentor_interests)

for mentor in mentors:
    # weighted_match_fn = mentee_over_mentor_weight_fn
    weighted_match_fn = mentor_over_mentee_weight_fn
    mentor_to_mentees[mentor[name_idx]] = \
        sorted(filter(lambda x: x[1] > 0, [((mentee[netid_idx], mentee[name_idx]), weighted_match_fn(mentor, mentee)) for mentee in mentees \
                    if year_to_int[mentee[year_idx]] < year_to_int[mentor[year_idx]]]), \
                key=lambda x: x[1], reverse=True)

print (mentor_to_mentees)

print ("Number of mentors: %d\nNumber of mentees: %d" % (len(mentors), len(mentees)))

# mentee_to_mentor

matched = set({})

final_pairing = defaultdict(list)
num_per_mentor = 3

#TODO: Change sort to generator that resorts after each matched removal

# CHANGE ORDER TO PRIORITIZE LEAST WEIGHTED FIRST
sorted_mentor_to_mentee_items = sorted(mentor_to_mentees.items(), key=lambda x: x[1][0][1] if len(x[1]) > 0 else 0, reverse=True)

mentee_netids = set([(mentee[netid_idx], mentee[name_idx]) for mentee in mentees])

for i in range(num_per_mentor):
    for mentor, mentees_and_weights in sorted_mentor_to_mentee_items: # sort by the first highest weighting so we can start at the lowest
        # curr_num_matched = 0
        was_matched = False
        for mentee, weight in mentees_and_weights:
            # if mentee not in matched and curr_num_matched < num_per_mentor:
            # print (mentee, weight, matched)
            if mentee not in matched:
                matched.add(mentee)
                final_pairing[mentor].append((mentee, weight))
                # curr_num_matched += 1
                was_matched = True
                break

        # if curr_num_matched == 0:
        if not was_matched:
            print ("Could not find a match for %s for mentee %d" % (mentor, i+1))

    if len(mentee_netids.difference(matched)) == 0:
        break

print ("Number of mentees per mentor: {}".format(i+1))
print ("Mentees not matched: {}".format(mentee_netids.difference(matched)))
# results = {'Jay Ryu': ['ch59', 'sj49'], 'Alisha Stupp ': ['zl55', 'vk20'], 'Spencer Chang': ['Aa104', 'Lpb3'], 'tian udomsak': ['am118', 'hjo2'], 'Abhijeet mulgund': ['rab9', 'acm9'], 'ani kunaparaju': ['ob10', 'jpg7'], 'Kevin Lin': ['jw81', 'rq4'], 'Kenneth Li': ['jpa4', 'tl54'], 'Mayu Tobin-Miyaji': ['mm99', 'Stx1'], 'Cara Tan': ['qs6', 'cww3 '], 'Rui Zheng': ['kk49', 'kgz1'], 'Jeffrey Sheng': ['lg43', 'vah3'], 'Anthony Tzen': ['ez8', 'mf43'], 'Cade Ritter': ['Ts47', 'hk34'], 'Raymond Yuan': ['jf52', 'Mpa5']}

# print(final_pairing)
for k,v in final_pairing.items():
    print ('{}: {}'.format(k,v))
# print([(k, [netid_to_info[nid][name_idx] for nid in val]) for k, val in final_pairing.items()])
