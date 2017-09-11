test = {
  'name': 'Does it work?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '74a37ca023ade49065a8a7abedb11b29',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorA work?
          class IteratorA:
             def __init__(self):
                 self.start = 10
             def __next__(self):
                 if self.start > 100:
                     raise StopIteration
                 self.start += 20
                 return self.start
             def __iter__(self):
                 return self
          """
        },
        {
          'answer': 'cac64d3e0a4fcf98e5b6bb012068c4ac',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorB work?
          class IteratorB:
              def __init__(self):
                  self.start = 5
              def __iter__(self):
                  return self
          """
        },
        {
          'answer': 'd2fe41c7de794d938086683393fe0b34',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorC work?
          class IteratorC:
              def __init__(self):
                  self.start = 5
              def __next__(self):
                  if self.start == 10:
                      raise StopIteration
                  self.start += 1
                  return self.start
          """
        },
        {
          'answer': '74a37ca023ade49065a8a7abedb11b29',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorD work?
          class IteratorD:
              def __init__(self):
                  self.start = 1
              def __next__(self):
                  self.start += 1
                  return self.start
              def __iter__(self):
                  return self
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
