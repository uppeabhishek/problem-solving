class File:

    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.directory = False if "." in name else True
        self.children = []
        self.extension = name.split(".")[1] if "." in name else ""

    def add_children(self, file):
        if isinstance(file, File):
            self.children.append(file)
            return True
        return False


class Filter:
    def __init__(self):
        pass

    def apply_filter(self, file):
        pass


class SizeFilter(Filter):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def apply_filter(self, file):
        return file.size >= self.size


class ExtensionFilter(Filter):
    def __init__(self, extension):
        super().__init__()
        self.extension = extension

    def apply_filter(self, file):
        return file.extension == self.extension


class OrFilter(Filter):
    def __init__(self):
        super().__init__()

    def apply_filter(self, file):
        return True


class FileSystem:
    def __init__(self):
        self.filters = set([])

    def add_filter(self, current_filter):
        self.filters.add(current_filter)

    def traverse_helper(self, root, result, visited):

        result.append(root.name)
        visited.add(root)

        if root.directory:
            for child in root.children:
                if child not in visited:
                    and_filter = not(any([isinstance(current_filter, OrFilter) for current_filter in self.filters]))

                    if and_filter:
                        if all([current_filter.apply_filter(child) for current_filter in self.filters]):
                            self.traverse_helper(child, result, visited)
                    else:
                        if any([current_filter.apply_filter(child) for current_filter in self.filters]):
                            self.traverse_helper(child, result, visited)

    def traverse(self, root):
        result = []
        visited = set([])
        self.traverse_helper(root, result, visited)
        print(result)


f1 = File("root")
f2 = File("one.txt", 100)
f3 = File("two.txt", 200)
f4 = File("two.py", 200)
f1.add_children(f2)
f1.add_children(f3)
f1.add_children(f4)

file_system = FileSystem()

file_system.add_filter(SizeFilter(150))
file_system.add_filter(ExtensionFilter("txt"))
file_system.add_filter(OrFilter())

file_system.traverse(f1)
