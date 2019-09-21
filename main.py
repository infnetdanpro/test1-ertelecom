import re

class Path:
    root = '/'

    def __init__(self, path):
        self.path = path

    def cd(self, action):
        base_dir = self.path
        
        if re.match(r'\/', action):
            self.path = action

        else:
            if re.match(r'\.\.\/', action):
                base_dir = re.split(r'[a-z]{1,}$', self.path)[0]
                action = re.split(r'\.\.\/', action)[1]
                self.path = base_dir + action
            else:
                self.path = base_dir  + '/' + action

    @property
    def current_path(self):
        return self.path


if __name__ == '__main__':

    path = Path('/a/b/c/d')
    path.cd('../x')
    # path.cd('x')
    # path.cd('/x')
    print(path.current_path)