test = {
  'name': 'Restart',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class IteratorA:
          ...    def __init__(self):
          ...        self.start = 10
          ...    def __next__(self):
          ...        if self.start > 100:
          ...            raise StopIteration
          ...        self.start += 20
          ...        return self.start
          ...    def __iter__(self):
          ...        return self
          >>> iterator = IteratorA()
          >>> [num for num in iterator]
          dc76466173cfc1c667619fd34dacb39d
          # locked
          >>> [num for num in iterator]
          a9e6f5a0d70f3e90ae58c003cf6ba8e0
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class IteratorB:
          ...    def __init__(self):
          ...        self.start = -6
          ...    def __next__(self):
          ...        if self.start > 10:
          ...            raise StopIteration
          ...        self.start += 3
          ...        return self.start
          ...    def __iter__(self):
          ...        return self
          >>> iterator = IteratorB()
          >>> [num for num in iterator]
          2a987719253566ce41abacd373f986f0
          # locked
          >>> [num for num in iterator]
          a9e6f5a0d70f3e90ae58c003cf6ba8e0
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
