def _remove_empty_containers(expr):
   '''Delete all emtpy sub-containers in expr.'''
   class Visitor(object):
      def visit(self, node):
         if node.kind('Container') and len(node.leaves) == 0:
            #node._die( )
            node.detach( )
   v = Visitor( )
   expr._navigator._traverse(v, depthFirst = False)
