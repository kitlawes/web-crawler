import os

class FileUtil:

    def get_file_contents(self, file_name):
        """
        Returns the contents of the file referred to by parameter file_name
        """
        file_contents = []
        file_path = os.path.join(os.path.dirname(__file__), 'resources', file_name)
        with open(file_path, 'r') as file:
            for line in file:
                file_contents.append(line.rstrip('\n'))
        return file_contents