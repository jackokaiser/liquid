from eventsMock import Event, EventArray
import unittest

class TestEventsMock(unittest.TestCase):

  def test_init(self):
      foo = Event(x=10, y=20, time=200)
      bar = Event(x=42, y=11, time=401)
      toto = EventArray([foo, bar])
      self.assertEqual(toto.events[0].time, 200)
      self.assertEqual(toto.events[1].x, 42)
      self.assertEqual(toto.events[1].y, 11)

if __name__ == '__main__':
    unittest.main()
