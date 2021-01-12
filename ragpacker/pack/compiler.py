import sys
import hashlib
from delegator import Delegator
class Compiler(Delegator):
    watched_paths = []
    env = {}

    def __init__(self, webpacker):
        self.webpacker = webpacker
        self.delegate(['config', 'logger'], self.webpacker)
    
    def compile(self):
        if self.stale():
            if self.run_webpack():
                return self.record_compilation_digest()
        else:
            self.logger.debug("Everything's up-to-date. Nothing to do")
            return True

    def fresh(self):
        return self.last_compilation_digest() == self.watched_files_digest()

    def stale(self):
        return not self.fresh()

    def last_compilation_digest(self):
        pass
        
    def watched_files_digest(self):
        pass

    def record_compilation_digest(self):
        pass

    def optionalPyRunner(self):
        pass

    def run_webpack(self):
        pass

    def default_watched_paths(self):
        pass

    def compilation_digest_path(self):
        pass

    def webpack_env(self):
        pass

