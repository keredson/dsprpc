import collections, requests, unittest
import dsprpc

class TestDSPRPC(unittest.TestCase):

  def test_function(self):
    s = dsprpc.DSPRPCServer("Derek Anderson")
    client = dsprpc.DSPRPCClient()
    self.assertEqual(client.lower(), 'derek anderson')
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
    
if __name__ == '__main__':
  unittest.main()

