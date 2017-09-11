test = {
  'name': 'size_of_dogs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select name from size_of_dogs where size="toy" or size="mini";
          abraham
          eisenhower
          fillmore
          grover
          herbert
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
