
from dataclasses import dataclass, field
from typing import List


@dataclass
class Tile:
    
     start_x : int
     start_y : int
     end_x : int
     end_y : int


@dataclass
class TileRange:
   tileList : List[Tile]
   
   def unique_groups(self):
       return self.tileList
   
   def fix_groups(self):
       return self.unique_groups


#  This logic should be in here


#    new_group =  {
#                             'start_x' : x-iteration_step,
#                             'start_y' : y-iteration_step,
#                             'end_x' : x+iteration_step,
#                             'end_y' :  y +iteration_step,
#                         } 
#             groups.append(new_group)

#         if len(groups) == 0:
#             new_group =  {
#                                 'start_x' : x-iteration_step,
#                                 'start_y' : y-iteration_step,
#                                 'end_x' : x+iteration_step,
#                                 'end_y' :  y +iteration_step,
#                             } 
#             print(group)
#             groups.append(new_group)
#         # print(groups)
#         tile_flag == True
#  for collection in groups:
#         collection['end_y'] = collection['end_y'] + iteration_step
#         collection['end_x'] = collection['end_x'] + iteration_step
#     remove = []
    
#     #  for review - look into ways to improve this logic
#     for i in range(0, len(groups)):
#         for ii in range(0, len(groups)):
#             if groups[i]['end_y'] >= groups[ii]['start_y'] and groups[i]['start_y'] >= groups[ii]['start_y'] and groups[i]['start_y'] <= groups[ii]['end_y'] and i != ii:
#                 groups[i]['end_y'] =  max(groups[i]['end_y'], groups[ii]['end_y'])
#                 groups[i]['start_y'] =  min(groups[i]['start_y'], groups[ii]['start_y'])
#                 groups[i]['end_x'] =  max(groups[i]['end_x'], groups[ii]['end_x'])
#                 groups[i]['start_x'] =  min(groups[i]['start_x'], groups[ii]['start_x'])
#                 groups[ii]['end_y'] =  max(groups[i]['end_y'], groups[ii]['end_y'])
#                 groups[ii]['start_y'] =  min(groups[i]['start_y'], groups[ii]['start_y'])
#                 groups[ii]['end_x'] =  max(groups[i]['end_x'], groups[ii]['end_x'])
#                 groups[ii]['start_x'] =  min(groups[i]['start_x'], groups[ii]['start_x'])
#                 print("overlap y")
                
            

     
#     unique = []
    
#     #  this needs to be cleaned
#     for item in groups:
#         try:
#             if iteration_step < 100:
#                 item["end_x"] = item["end_x"] + iteration_step
#             unique.index(item)
#         except:

#             unique.append(item)
