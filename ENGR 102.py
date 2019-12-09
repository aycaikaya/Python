critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
         'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
         'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
         'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
         'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
         'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
         'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}
# a dictionary for movie critics and their ratings
print (critics['Lisa Rose'])#output is {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.5}
print (critics['Lisa Rose']['Lady in the Water']) #output is 2.5
from math import sqrt
#returns a distance based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
    si={} #get the list of shared items
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1 #this means their ratings are identical
    if len(si)==0:
        return 0 #if they are no ratings than it will be count as 0
    #sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
def distance(dict,per1,per2):
    shared_items={}
    for item in dict[per1]: #an item is in the dict of person 1
        if item in dict[per2]: #if same item is in the dict of person 2
            shared_items[item]=1 #the value will be 1
    if len(shared_items)==0:
        return 0

    inital_dis=sum([pow(dict[per1][item]-dict[per2][item],2)
            for item in dict[per1] if item in dict[per2] ])
    all_sum=sqrt(inital_dis)
    return 1/(1+all_sum)

print (distance(critics,'Lisa Rose','Toby'))
print (distance(critics, 'Lisa Rose', 'Gene Seymour'))


# Perason correlation score
def sim_pearson(dict,pers1,pers2):
    si={}
    for item in dict[pers1]:#an item is in the dict for person 1
        if item in dict[pers2]: #the item is also is in the dict for person 2
            si[item]=1 #the value will be 1
    n=len(si)
    if n==0: #if there is no commen item than the value will be 0
        return 0
   #adding all the preferences
    sum1=sum([dict[pers1][item] for item in si])
    sum2=sum([dict[pers2][item] for item in si])
    sum1sq=sum([pow(dict[pers1][item],2) for item in si])
    sum2sq=sum([pow(dict[pers2][item],2) for item in si])


    All_Sum=sum([dict[pers1][item]*dict[pers2][item] for item in si])

    num=All_Sum-(sum1*sum2/n)
    den=sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den==0:
        return 0
    r= num/den
    return r
print (sim_pearson(critics,'Lisa Rose','Toby'))

#returns the best matches for person from the critics dict
#number of results and similarity function are optinal params























