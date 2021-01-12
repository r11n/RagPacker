from delegator import Delegator
import yaml, os
class Configuration(Delegator):
    def __init__(self, root_path, config_path, env):
        self.root_path = root_path
        self.config_path = config_path
        self.env = env
    
    def dev_server(self):
        return self.fetch('dev_server')
    
    def compile(self):
        return self.fetch('compile')
    
    def source_path(self):
        return self.root_path + self.fetch('source_path')
    
    def additional_paths(self):
        return self.fetch('additional_paths')
    
    def source_entry_path(self):
        return self.source_path() + self.fetch('source_entry_path')
    
    def public_path(self):
        return self.root_path + self.fetch('public_root_path')
    
    def public_output_path(self):
        return self.public_path() + self.fetch('public_output_path')
    
    def public_manifest_path(self):
        return self.public_output_path() + 'manifest.json'
    
    def cache_manifest(self):
        return self.fetch('cache_manifest')
    
    def cache_path(self):
        return self.root_path + self.fetch('cache_path')
    
    def check_yarn_integrity(self,value):
        pass

    def webpack_compile_output(self):
        self.fetch('webpack_compile_output')
    
    def fetch(self, key):
        self.data().fetch(key, self.defaults()[key])
    
    def data(self):
        self.data_store = self.data_store or self.load()
    
    def load(self):
        try:
            with open(self.config_path.read, 'r') as stream:
                return yaml.safe_load(stream)[self.env]
        except yaml.YAMLError as e:
            raise Exception('config missing ' + e.message)
    
    def defaults(self):
        self.default_store = self.default_store or None
        script_dir = os.path.dirname(__file__)
        rel_path = '../../install/config/webpacker.yml'
        abs_file_path = os.path.join(script_dir, rel_path)
        if self.default_store is None:
            with open(abs_file_path, 'r') as stream:
                self.default_store = self.dict_to_obj(yaml.safe_load(stream))
        return self.default_store
    