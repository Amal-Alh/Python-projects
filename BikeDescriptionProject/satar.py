class CreateBike:
 def __init__(self, description, cost, sale_price, condition, sold):
  self.description = description
  self.cost = cost
  self.sale_price = sale_price
  self.condition = condition
  self.sold = sold

 def sell(self, sold: object) -> object:
  sold['sold'] = sold
 def update_sale_price(self, sold: object, sale_price: object) -> object:
  if not ['sold']:
   sale_price['sale_price'] = sale_price
  else:
   print('Action not allowed, Bike has already been sold')


bike1 = CreateBike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5, sold='sold')
bike1.update_sale_price(bike1, 350)