class Solution:
    def findDuplicate(self, paths):
        file_map = {}
        for path in paths:
            dir, *files = path.split()
            for file in files:
                p = file.index('(')
                filename, content = file[:p], file[p + 1:-1]
                file_map.setdefault(content, []).append(dir + '/' + filename)
        return [*filter(lambda x: len(x) > 1, file_map.values())]