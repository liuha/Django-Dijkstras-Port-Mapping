# Port-Mapping
Using Django and Implementing Dijkstra's algorithm to draw the shortest path from the stair to given data port.

admin account(username/password：admin/ecerfadmin)

PRESENTATION OF THE APP

1 Search by Data Port Number
The default floor number is 3. Or you can select desired level from left side level bar. 
 
If the desired data port is exist, its detail will be displayed, a blinking circle will be printed overplay on the floor map. Meanwhile if the data port’s location is known, the shortest path from the floor’s main entrance to the destination will be drew. 

If you think that the coordinate of the data port is wrong, you can update it by clicking   button. And then click the new coordinate on the map. 

2 Search by Room Number
Inputting the Rom number, a relevant data port list will be displayed. Otherwise an error message will be display. 

3 Add Path Nodes
This function will be used only when a renovation blocks the hallway in the future and you need to create a node to draw the shortest path. The relation (edge) among the nodes will be maintained in Admin page.  
Selecting a level, entering a node name, clicking on the map to get coordinate and clicking AddNote are all you need to do to add a path node. 
