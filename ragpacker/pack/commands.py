from delegator import Delegator
from glob import glob
from os import path
from itertools import groupby
class Commands(Delegator):
    def __init__(self, webpacker):
        self.webpacker = webpacker
        self.delegate(['config', 'compiler', 'manifest', 'logger'], self.webpacker)
    
    # TODO: @r11n finish clean and compile
    def clean(self,count=2, age=3600):
        if self.config.public_output_path is not None and self.config.public_manifest_path is not None:
            return self.__versions().sort(reverse=True)

    # TODO: @r11n check rmtree call once
    def clobber(self):
        if self.config.public_output_path is not None:
            self.config.public_output_path.rmtree()
        if self.config.cache_path is not None:
            self.config.cache_path.rmtree()

    def boostrap(self):
        self.manifest.refresh()

    def compile(self):
        if self.compiler.compile():
            self.manifest.refresh()

    def __versions(self):
        all_files = glob(self.config.public_output_path + '/**/*')
        manifest_config = glob(self.config.public_manifest_path + '*')

        packs = list(set(all_files) - set(manifest_config))
        packs = [pack for pack in packs if path.isfile(path)]
        packs = list(groupby(
            packs,
            lambda f: path.getmtime(f)
        ))
        return packs

    def __current_version(self):
        packs = self.manifest.refresh

