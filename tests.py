import collections, requests, time, unittest
import dsprpc

class TestDSPRPC(unittest.TestCase):

  def test_function(self):
    s = dsprpc.DSPRPCServer("Derek Anderson")
    client = dsprpc.DSPRPCClient()
    self.assertEqual(client.lower(), 'derek anderson')
    s.shutdown()

  def test_function_with_arg(self):
    s = dsprpc.DSPRPCServer("derek")
    client = dsprpc.DSPRPCClient()
    self.assertEqual(client.center(9), '  derek  ')
    s.shutdown()

  def test_function_with_missing_arg(self):
    s = dsprpc.DSPRPCServer("derek")
    client = dsprpc.DSPRPCClient()
    with self.assertRaises(TypeError):
      client.center()
    s.shutdown()

  def test_function_with_kwarg(self):
    class O(object):
      def x(self, default=12):
        return default
    s = dsprpc.DSPRPCServer(O())
    client = dsprpc.DSPRPCClient()
    self.assertEqual(client.x(), 12)
    self.assertEqual(client.x(default=42), 42)
    s.shutdown()

  def test_function_with_arg_and_kwarg(self):
    class O(object):
      def x(self, y, default=12):
        return y+default
    s = dsprpc.DSPRPCServer(O())
    client = dsprpc.DSPRPCClient()
    self.assertEqual(client.x(1), 13)
    self.assertEqual(client.x(2, default=40), 42)
    s.shutdown()

  def test_attribute(self):
    cls = collections.namedtuple('Woot',['derek'])
    s = dsprpc.DSPRPCServer(cls('anderson'))
    client = dsprpc.DSPRPCClient()
    self.assertEqual(client.derek, 'anderson')
    s.shutdown()

  def test_error(self):
    s = dsprpc.DSPRPCServer("Derek Anderson")
    client = dsprpc.DSPRPCClient()
    with self.assertRaises(AttributeError):
      client.not_a_function()
    s.shutdown()
  
  def test_no_server(self):
    client = dsprpc.DSPRPCClient()
    with self.assertRaises(requests.exceptions.ConnectionError):
      client.lower()

  def test_speed(self):
    s = dsprpc.DSPRPCServer("Derek Anderson")
    client = dsprpc.DSPRPCClient()
    n = 100
    start = time.clock()
    for i in range(100):
      client.lower()
    end = time.clock()
    took = end-start
    print('%i requests took %fs' % (n, took)) # 0.4s on my machine
    s.shutdown()

    
if __name__ == '__main__':
  unittest.main()

