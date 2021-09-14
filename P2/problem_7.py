
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, route):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = route

    def insert(self, route):
        # Insert the node as before
        self.children[route] = self.handler


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, route):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(route)

    def insert(self, route):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        if route not in current_node.children:
            current_node.insert(route)
        current_node = current_node.children[route]

    def find(self, route):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
    
        if route not in current_node.children:
            return False
        current_node = current_node.children[route]
        return current_node
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, route):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(route)

    def add_handler(self, route):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route = self.split_path(route)

        for word in route:
            self.router.insert(word)
        return True

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        route = self.split_path(route)

        parts = []
        for word in route:
            part = self.router.find(word)
            if part:
                parts.append(part)
            else:
                return 404
        return parts

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = "/".split(path)
        return path_list



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one