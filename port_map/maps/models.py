from django.db import models

class NetworkPort(models.Model):
	floor = models.IntegerField(default=3)
	port = models.IntegerField(default=1)
	room = models.CharField(max_length=25, default="unknown")
	section = models.CharField(max_length=25, default="unknown")
	x_coord = models.IntegerField(null=True)
	y_coord = models.IntegerField(null=True)

	def __str__(self):
		return "Floor %d, D-%d" %(self.floor, self.port)

	def coordinates(self):
		return (self.x_coord, self.y_coord)

# node name syntax: floor_DataPort or floor_Room or floor_intersection_suffix (eg: a, b, c, d)
class Node(models.Model):
	name = models.CharField(max_length=25, default="unknown")
	floor = models.IntegerField(default=3)
	x_coord = models.IntegerField(null=True)
	y_coord = models.IntegerField(null=True)

	def coordinates(self):
		return (self.x_coord, self.y_coord)

	def __str__(self):
		return "Floor:%d, Node:%s" %(self.floor, self.name)

class Edge(models.Model):
	FromNode = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="from_node")
	ToNode = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="to_node")
	#Distance = models.IntegerField(default=0)
	def __str__(self):
		#return "Floor: %d Edge: %s (%d,%d) --> %s (%d,%d)" %(
		return "Floor: %d Edge: %s  --> %s " %(
			self.FromNode.floor,
			self.FromNode.name,
			#self.FromNode.x_coord,
			#self.FromNode.y_coord,
			self.ToNode.name,
			#self.ToNode.x_coord,
			#self.ToNode.y_coord,
			)