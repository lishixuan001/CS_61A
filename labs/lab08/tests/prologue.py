test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> stans_car = Car('Tesla', 'Model S')
          >>> stans_car.color
          'No color yet. You need to paint me.'
          >>> stans_car.paint('black')
          'Tesla Model S is now black'
          >>> stans_car.color
          'black'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> stans_car = Car('Tesla', 'Model S')
          >>> stans_truck = MonsterTruck('Monster Truck', 'XXL')
          >>> stans_car.size
          'Tiny'
          >>> stans_truck.size
          'Monster'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
