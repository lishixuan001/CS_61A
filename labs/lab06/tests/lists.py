test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [1, 2, 3, 4, 5, 6]
          >>> lst[4] = 1
          >>> lst
          [1, 2, 3, 4, 1, 6]
          >>> lst[2:4] = [9, 8]
          >>> lst
          [1, 2, 9, 8, 1, 6]
          >>> lst[3] = ['hi', 'bye']
          >>> lst
          [1, 2, 9, ['hi', 'bye'], 1, 6]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lst[3:] = ['oski', 'bear']
          >>> lst
          [1, 2, 9, 'oski', 'bear']
          >>> lst[1:3] = [2, 3, 4, 5, 6, 7, 8]
          >>> lst
          [1, 2, 3, 4, 5, 6, 7, 8, 'oski', 'bear']
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lst == lst[:]
          True
          >>> lst is lst[:]
          False
          >>> a = lst[:]
          >>> a[0] = 'oogly'
          >>> lst
          [1, 2, 3, 4, 5, 6, 7, 8, 'oski', 'bear']
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
