from cs1graphics import *

paper = Canvas(300,200)

def generate_cloud(numcircle, x_position, y_postion):
    cloud = Layer()
    fog = Circle(20, Point(x_position, y_postion))
  
    fog.setFillColor("white")
    for i in range(numcircle):
        fogn = fog.clone()
        fogn.move(30*i,0)
        fogn.setDepth(i)
        cloud.add(fogn)
    cloud.add(fog)
        
    return cloud
cloud = generate_cloud(6,50,50)
paper.add(cloud)

    