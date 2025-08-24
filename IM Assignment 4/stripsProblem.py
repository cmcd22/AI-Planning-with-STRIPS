# stripsProblem.py - STRIPS Representations of Actions
# AIFCA Python3 code Version 0.9.5 Documentation at http://aipython.org
# Download the zip file and read aipython.pdf for documentation

# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2022.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en
import random
from searchMPP import SearcherMPP
from stripsForwardPlanner import Forward_STRIPS

class Strips(object):
    def __init__(self, name, preconds, effects, cost=1):
        """
        defines the STRIPS representation for an action:
        * name is the name of the action
        * preconds, the preconditions, is feature:value dictionary that must hold
        for the action to be carried out
        * effects is a feature:value map that this action makes
        true. The action changes the value of any feature specified
        here, and leaves other features unchanged.
        * cost is the cost of the action
        """
        self.name = name
        self.preconds = preconds
        self.effects = effects
        self.cost = cost

    def __repr__(self):
        return self.name

class STRIPS_domain(object):
    def __init__(self, feature_domain_dict, actions):
        """Problem domain
        feature_domain_dict is a feature:domain dictionary, 
                mapping each feature to its domain
        actions
        """
        self.feature_domain_dict = feature_domain_dict
        self.actions = actions

class Planning_problem(object):
    def __init__(self, prob_domain, initial_state, goal):
        """
        a planning problem consists of
        * a planning domain
        * the initial state
        * a goal 
        """
        self.prob_domain = prob_domain
        self.initial_state = initial_state
        self.goal = goal

# Monkey-Banana code
def monkey_banana_problem():
    print("*MONKEY-BANANA PROBLEM*")
    boolean = {True,False}
    locations = ['NW','N','NE','W','C','E','SW','S','SE'] # Possible monkey locations
    monkey_location = random.choice(locations)
    print("MONKEY LOCATION: "+monkey_location)
    stool_location = random.choice(locations)
    print("STOOL LOCATION: "+stool_location)
    print('')
    room_domain = STRIPS_domain(
        {'MLoc':{'NW','N','NE','W','C','E','SW','S','SE'},
         'MHasStool':boolean, 'MOnStool':boolean, 'MHasBanana':boolean},
        {Strips('Move NW->N',{'MLoc':'NW','MHasStool':False},{'MLoc':'N'}),
         Strips('Move NW->W',{'MLoc':'NW','MHasStool':False},{'MLoc':'W'}),
         Strips('Move-Stool NW->N',{'MLoc':'NW','MHasStool':True},{'MLoc':'N'}),
         Strips('Move-Stool NW->W',{'MLoc':'NW','MHasStool':True},{'MLoc':'W'}),
         Strips('Move N->NE',{'MLoc':'N','MHasStool':False},{'MLoc':'NE'}),
         Strips('Move N->C',{'MLoc':'N','MHasStool':False},{'MLoc':'C'}),
         Strips('Move N->NW',{'MLoc':'N','MHasStool':False},{'MLoc':'NW'}),
         Strips('Move-Stool N->C',{'MLoc':'N','MHasStool':True},{'MLoc':'C'}),
         Strips('Move NE->N', {'MLoc': 'NE','MHasStool':False}, {'MLoc': 'N'}),
         Strips('Move NE->E', {'MLoc': 'NE','MHasStool':False}, {'MLoc': 'E'}),
         Strips('Move-Stool NE->N', {'MLoc': 'NE', 'MHasStool': True}, {'MLoc': 'N'}),
         Strips('Move-Stool NE->E', {'MLoc': 'NE', 'MHasStool': True}, {'MLoc': 'E'}),
         Strips('Move W->C', {'MLoc': 'W','MHasStool':False}, {'MLoc': 'C'}),
         Strips('Move W->SW', {'MLoc': 'W','MHasStool':False}, {'MLoc': 'SW'}),
         Strips('Move W->NW', {'MLoc': 'W','MHasStool':False}, {'MLoc': 'NW'}),
         Strips('Move-Stool W->C', {'MLoc': 'W', 'MHasStool': True}, {'MLoc': 'C'}),
         Strips('Move C->E', {'MLoc': 'C','MHasStool':False}, {'MLoc': 'E'}),
         Strips('Move C->S', {'MLoc': 'C','MHasStool':False}, {'MLoc': 'S'}),
         Strips('Move C->N', {'MLoc': 'C','MHasStool':False}, {'MLoc': 'N'}),
         Strips('Move C->W', {'MLoc': 'C','MHasStool':False}, {'MLoc': 'W'}),
         Strips('Move E->C', {'MLoc': 'E','MHasStool':False}, {'MLoc': 'C'}),
         Strips('Move E->SE', {'MLoc': 'E','MHasStool':False}, {'MLoc': 'SE'}),
         Strips('Move E->NE', {'MLoc': 'E','MHasStool':False}, {'MLoc': 'NE'}),
         Strips('Move-Stool E->C', {'MLoc': 'E', 'MHasStool': True}, {'MLoc': 'C'}),
         Strips('Move SW->S', {'MLoc': 'SW','MHasStool':False}, {'MLoc': 'S'}),
         Strips('Move SW->W', {'MLoc': 'SW','MHasStool':False}, {'MLoc': 'W'}),
         Strips('Move-Stool SW->S', {'MLoc': 'SW', 'MHasStool': True}, {'MLoc': 'S'}),
         Strips('Move-Stool SW->W', {'MLoc': 'SW', 'MHasStool': True}, {'MLoc': 'W'}),
         Strips('Move S->SE', {'MLoc': 'S','MHasStool':False}, {'MLoc': 'SE'}),
         Strips('Move S->C', {'MLoc': 'S','MHasStool':False}, {'MLoc': 'C'}),
         Strips('Move S->SW', {'MLoc': 'S','MHasStool':False}, {'MLoc': 'SW'}),
         Strips('Move-Stool S->C', {'MLoc': 'S', 'MHasStool': True}, {'MLoc': 'C'}),
         Strips('Move SE->S', {'MLoc': 'SE','MHasStool':False}, {'MLoc': 'S'}),
         Strips('Move SE->E', {'MLoc': 'SE','MHasStool':False}, {'MLoc': 'E'}),
         Strips('Move-Stool SE->S', {'MLoc': 'SE', 'MHasStool': True}, {'MLoc': 'S'}),
         Strips('Move-Stool SE->E', {'MLoc': 'SE', 'MHasStool': True}, {'MLoc': 'E'}),
         Strips('Grab-Stool', {'MLoc': stool_location, 'MHasStool': False}, {'MHasStool': True}),
         Strips('Climb-Stool', {'MLoc': 'C', 'MHasStool': True, 'MOnStool': False}, {'MOnStool': True}),
         Strips('Grab-Banana', {'MOnStool': True, 'MHasBanana': False}, {'MHasBanana': True})}
    )

    return Planning_problem(room_domain,
                                {'MLoc':monkey_location,
                                 'MHasStool':False, 'MOnStool':False, 'MHasBanana':False,},
                                {'MHasBanana':True})

# River Crossing code
def river_crossing_problem():
    print("*RIVER CROSSING PROBLEM*")
    boolean = {True,False}
    river_domain = STRIPS_domain(
        {'BoatLoc':{'LeftBank','RightBank'}, 'WolfLoc':{'LeftBank','RightBank'},
         'GoatLoc':{'LeftBank','RightBank'}, 'CabLoc':{'LeftBank','RightBank'},
         'Cabbage&GoatTogether':boolean, 'Wolf&GoatTogether':boolean, 'BoatEmpty': boolean,
         'WolfOnBoat':boolean, 'GoatOnBoat':boolean, 'CabbageOnBoat':boolean},
        {Strips('Boat travelling to RightBank',{'BoatLoc':'LeftBank'},{'BoatLoc':'RightBank'}),
         Strips('Boat travelling to LeftBank',{'BoatLoc':'RightBank'},{'BoatLoc':'LeftBank'}),
         Strips('Wolf on boat at LeftBank',{'WolfLoc':'LeftBank','BoatEmpty':True,
                                            'BoatLoc':'LeftBank','Cabbage&GoatTogether':False},
                                           {'BoatEmpty':False,'WolfOnBoat':True}),
         Strips('Goat on boat at LeftBank',{'GoatLoc':'LeftBank','BoatEmpty':True,
                                            'BoatLoc':'LeftBank'},{'BoatEmpty':False,'GoatOnBoat':True,
                                            'Cabbage&GoatTogether':False,'Wolf&GoatTogether':False}),
         Strips('Cabbage on boat at LeftBank',{'CabLoc':'LeftBank','BoatEmpty':True,
                                            'BoatLoc':'LeftBank','Wolf&GoatTogether':False},{'BoatEmpty':False,'CabbageOnBoat':True}),
         Strips('Wolf off boat at RightBank',{'BoatEmpty':False,'WolfOnBoat':True,
                                              'BoatLoc':'RightBank','GoatLoc':'LeftBank'},
                {'WolfLoc':'RightBank','BoatEmpty':True,'WolfOnBoat':False}),
         Strips('Wolf off boat at RightBank',{'BoatEmpty':False,'WolfOnBoat':True,
                                              'BoatLoc':'RightBank','GoatLoc':'RightBank'},
                {'WolfLoc':'RightBank','BoatEmpty':True,'WolfOnBoat':False,'Wolf&GoatTogether':True}),
         Strips('Goat off boat at RightBank', {'BoatEmpty': False,'GoatOnBoat': True,
                                               'BoatLoc': 'RightBank','WolfLoc':'LeftBank','CabLoc':'LeftBank'},
                {'GoatLoc': 'RightBank', 'BoatEmpty': True, 'GoatOnBoat': False}),
         Strips('Goat off boat at RightBank', {'BoatEmpty': False,'GoatOnBoat': True,
                                               'BoatLoc': 'RightBank','WolfLoc':'RightBank','CabLoc':'LeftBank'},
                {'GoatLoc': 'RightBank', 'BoatEmpty': True, 'GoatOnBoat': False,'Wolf&GoatTogether':True}),
         Strips('Goat off boat at RightBank', {'BoatEmpty': False,'GoatOnBoat': True,
                                               'BoatLoc': 'RightBank','CabLoc':'RightBank','WolfLoc':'LeftBank'},
                {'GoatLoc': 'RightBank', 'BoatEmpty': True, 'GoatOnBoat': False,'Cabbage&GoatTogether':True}),
         Strips('Goat off boat at RightBank', {'BoatEmpty': False,'GoatOnBoat': True,
                                               'BoatLoc': 'RightBank','CabLoc':'RightBank','WolfLoc':'RightBank'},
                {'GoatLoc': 'RightBank', 'BoatEmpty': True, 'GoatOnBoat': False,
                 'Cabbage&GoatTogether':True,'Wolf&GoatTogether':True}),
         Strips('Cabbage off boat at RightBank', {'BoatEmpty': False, 'CabbageOnBoat': True, 'BoatLoc': 'RightBank','GoatLoc':'LeftBank'},
                {'CabLoc': 'RightBank', 'BoatEmpty': True, 'CabbageOnBoat': False}),
         Strips('Cabbage off boat at RightBank', {'BoatEmpty': False, 'CabbageOnBoat': True, 'BoatLoc': 'RightBank','GoatLoc':'RightBank'},
                {'CabLoc': 'RightBank', 'BoatEmpty': True, 'CabbageOnBoat': False,'Cabbage&GoatTogether':True}),
         Strips('Wolf on boat at RightBank', {'WolfLoc': 'RightBank', 'BoatEmpty': True,
                                             'BoatLoc': 'RightBank', 'Cabbage&GoatTogether': False},
                                            {'BoatEmpty': False, 'WolfOnBoat': True}),
         Strips('Goat on boat at RightBank', {'GoatLoc': 'RightBank', 'BoatEmpty': True,
                                             'BoatLoc': 'RightBank'}, {'BoatEmpty': False, 'GoatOnBoat': True,
                                             'Cabbage&GoatTogether':False,'Wolf&GoatTogether':False}),
         Strips('Cabbage on boat at RightBank', {'CabLoc': 'RightBank', 'BoatEmpty': True,
                                                'BoatLoc': 'RightBank', 'Wolf&GoatTogether': False},
                                               {'BoatEmpty': False, 'CabbageOnBoat': True}),
         Strips('Wolf off boat at LeftBank', {'BoatEmpty': False, 'WolfOnBoat': True, 'BoatLoc': 'LeftBank','GoatLoc':'RightBank'},
                {'WolfLoc': 'LeftBank', 'BoatEmpty': True, 'WolfOnBoat': False}),
         Strips('Wolf off boat at LeftBank', {'BoatEmpty': False, 'WolfOnBoat': True, 'BoatLoc': 'LeftBank','GoatLoc':'LeftBank'},
                {'WolfLoc': 'LeftBank', 'BoatEmpty': True, 'WolfOnBoat': False,'Wolf&GoatTogether':True}),
         Strips('Goat off boat at LeftBank', {'BoatEmpty': False, 'GoatOnBoat': True, 'BoatLoc': 'LeftBank','WolfLoc':'RightBank','CabLoc':'RightBank'},
                {'GoatLoc': 'LeftBank', 'BoatEmpty': True, 'GoatOnBoat': False}),
         Strips('Goat off boat at LeftBank', {'BoatEmpty': False, 'GoatOnBoat': True, 'BoatLoc': 'LeftBank','WolfLoc':'LeftBank','CabLoc':'RightBank'},
                {'GoatLoc': 'LeftBank', 'BoatEmpty': True, 'GoatOnBoat': False,'Wolf&GoatTogether':True}),
         Strips('Goat off boat at LeftBank', {'BoatEmpty': False, 'GoatOnBoat': True, 'BoatLoc': 'LeftBank','CabLoc':'LeftBank','WolfLoc':'RightBank'},
                {'GoatLoc': 'LeftBank', 'BoatEmpty': True, 'GoatOnBoat': False,'Cabbage&GoatTogether':True}),
         Strips('Goat off boat at LeftBank', {'BoatEmpty': False, 'GoatOnBoat': True, 'BoatLoc': 'LeftBank','CabLoc':'LeftBank','WolfLoc':'LeftBank'},
                {'GoatLoc': 'LeftBank', 'BoatEmpty': True, 'GoatOnBoat': False,'Cabbage&GoatTogether':True,'Wolf&GoatTogether':True}),
         Strips('Cabbage off boat at LeftBank', {'BoatEmpty': False, 'CabbageOnBoat': True, 'BoatLoc': 'LeftBank','GoatLoc':'RightBank'},
                {'CabLoc': 'LeftBank', 'BoatEmpty': True, 'CabbageOnBoat': False}),
         Strips('Cabbage off boat at LeftBank', {'BoatEmpty': False, 'CabbageOnBoat': True, 'BoatLoc': 'LeftBank','GoatLoc':'LeftBank'},
                {'CabLoc': 'LeftBank', 'BoatEmpty': True, 'CabbageOnBoat': False,'Cabbage&GoatTogether':True}),
         }
    )

    return Planning_problem(river_domain,
                                {'BoatLoc':'LeftBank','WolfLoc':'LeftBank','GoatLoc':'LeftBank','CabLoc':'LeftBank',
                                 'Cabbage&GoatTogether':True, 'Wolf&GoatTogether':True, 'BoatEmpty':True,
                                 'WolfOnBoat':False,'GoatOnBoat':False,'CabbageOnBoat':False},
                                {'WolfLoc':'RightBank','GoatLoc':'RightBank','CabLoc':'RightBank'})

def main():
    print("1 = Monkey-Banana Problem")
    print("2 = River Crossing Problem")
    print("3 = QUIT")
    choice = input("Please enter your choice: ")
    if choice == '1':
        SearcherMPP(Forward_STRIPS(monkey_banana_problem())).search()
    elif choice == '2':
        SearcherMPP(Forward_STRIPS(river_crossing_problem())).search()
    elif choice == '3':
        quit()
    else:
        print("Invalid choice")
        main()

main()
