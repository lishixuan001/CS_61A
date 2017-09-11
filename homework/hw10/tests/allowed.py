test = {
  'name': 'allowed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from allowed where n >= 5;
          5|bagels
          5|coffee
          5|espresso
          6|espresso
          7|espresso
          8|espresso
          9|eggs
          9|espresso
          10|eggs
          10|espresso
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
