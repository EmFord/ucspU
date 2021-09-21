
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, route, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, route):
        # Insert the node as before
        self.children[route] = RouteTrieNode(route)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, route, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(route, handler)

    def insert(self, route, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        for r in route:
            if r not in current_node.children:
                current_node.insert(r)
            current_node = current_node.children[r]
        current_node.handler = handler

    def find(self, route):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for word in route:
            if word == "":
                return current_node.handler
            if word not in current_node.children:
                return None
            current_node = current_node.children[word]
        return current_node.handler
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well
        self.router = RouteTrie("", root_handler)
        self.not_found = not_found

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route = self.split_path(route)
        self.router.insert(route, handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        route = self.split_path(route)

        handler = self.router.find(route)
        if not handler:
            return self.not_found or 404
        return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split("/")[1:]
        return path_list



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(1, router.lookup("/")) # should print 'root handler'
print(2, router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(3, router.lookup("/home/about")) # should print 'about handler'
print(4, router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(5, router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one