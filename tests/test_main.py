import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(m.coverage(['R1','R2'],[{'requirement':'R1','status':'failed'},{'requirement':'R3','status':'passed'}]),{'missing':['R2'],'not_ready':['R1'],'orphaned':['R3']})
