from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import NetworkPort, Node, Edge 
#from PIL import Image, ImageDraw
from io import BytesIO
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils._os import safe_join
from .graph import graph_test, get_path
import random

# search dataport using floor and port number
# return single dataport
def search(request):
    form_port=request.POST['port']
    form_floor = request.POST['floor']
    try:
        searched_port = NetworkPort.objects.get(port=form_port, floor=form_floor)
        error = None
    except NetworkPort.DoesNotExist: 
        error = "The network port requested does not exist!"
        searched_port = None
    return searched_port, error

#update port and node coordinates
def update(request, port):
    #update port coordinates
    port.x_coord = request.POST['x_update']
    port.y_coord = request.POST['y_update']
    port.save()
    #update node coordinates
    name = str(port.floor) + "_" + str(port.port)
    node = Node.objects.get(name=name, floor=port.floor)
    node.x_coord = request.POST['x_update']
    node.y_coord = request.POST['y_update']
    node.save()

    return None

# search dataports by room number,  
# return multiple dataports.
def searchbyroom(request):
    search_room=request.POST['search_room']
    port_list = NetworkPort.objects.filter(room__iexact=search_room)
    error = None
    if( len(port_list) == 0 ):
        error = "No dataport for room: " + search_room + ", please try again!"
        port_list = None

    return port_list, error


#return the path from entry door to destination dataport
def search_path(port):
    path_list = None
    edge = None
    if (port != None):
        #check whether the node is connected to any room door or not. 
        #if exists, return path, otherwise, return none. 
        end = str(port.floor) + "_" + str(port.port)
        node = Node.objects.get(name=end, floor=port.floor)
        edge = Edge.objects.filter(ToNode=node)

        if (edge.exists()): 
            if ( port.floor == 3 ):
                star = "3_enter"
            elif (port.floor == 4 ):
                star = "4_enter"
            else:
                star = "5_enter"
            path_list = get_path(star, end, port.floor )

    return path_list


def index(request):
    port, error = None, None
    path_list = None
    port_list = None
    if(request.method == 'POST'):
        form_name = request.POST['form_name']

        #search by dataport numbert and floor
        if(form_name == "dp_Search"):
            port, error = search(request)
            # get the shortest path from door to given node. 
            path_list = search_path(port)
        
        #update dataport's coordinates
        if(form_name == "dp_Update"):
            #search by dataport numbert and floor
            port, error = search(request)
            #update dataport's coordinates
            update(request, port)
            # get the shortest path from door to given node. 
            path_list = search_path(port)

        # search dataports by room number, 
        if (form_name =="room_Search"):
            port_list, error = searchbyroom(request)

    context = {
    "NetworkPort" : port,
    "searchError" : error,
    "path_list": path_list,
    "port_list": port_list
    }
    return render(request, 'maps/maps.html', context)

#add room door node and intersection node. 
#node name syntax: floor_DataPort or floor_Room or floor_intersection_suffix (eg: a, b, c, d)
def addNode(request):
    message = "Add Node"
    #path_list = graph_test()
    if (request.method == 'POST'):
        try: 
            floor = request.POST['floor']
            x_coord = request.POST['x_add']
            y_coord = request.POST['y_add']
            name = request.POST['node_name']
            node = Node(name=name, floor=floor, x_coord=x_coord, y_coord=y_coord)
            node.save()
            message = " Add a Node sucessfully"
        except:
            message = " Something wrong"
    context={
        "message" : message,
        #"path_list": path_list
    }
    return render(request, 'maps/addNode.html', context)  

