class Rectangle:
  def __init__(self, width, height):
    self.width=width
    self.height=height

  def set_width(self, width):
    self.width=width
  
  def set_height(self,height):
    self.height=height

  def get_area(self):
    return self.height*self.width
  
  def get_perimeter(self):
    return 2*(self.height)+2*(self.width)
  
  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5
  
  def get_picture(self):
    graph=''
    if(self.height>50 or self.width>50):
      graph='Too big for picture.'
    else:
      for i in range(self.height):
        for j in range(self.width):
          graph+="*"
        graph+= '\n'
    return graph
  
  def get_amount_inside(self,shape): 
    amount= int((self.width/shape.width) * (self.height/shape.height))

    return amount
  
  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

class Square(Rectangle):
  def __init__(self, width):
    super().__init__(width,width)
  
  def __str__(self):
    return 'Square(side=' + str(self.width)  + ')'
  
  def set_side(self, side):
    self.width = side
    self.height=side
