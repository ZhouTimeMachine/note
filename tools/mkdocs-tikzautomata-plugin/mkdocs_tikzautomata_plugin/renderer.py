from .tex import TeXWriter

from hashlib import sha256
from mkdocs.utils import log
import os

class TikZAutomataRenderer:
    def __init__(self, options: str, contents: str) -> None:
        self.options = options
        self.contents = contents

    def write_to_svg(self, cachefile: bool) -> str:
        filename = sha256(self.contents.encode()).hexdigest()

        if cachefile == True:
            try:
                os.chdir("cache")
            except OSError:
                log.error("[tikzautomata] cache directory not found!")

        if cachefile == True and os.path.exists(f"{filename}.svg"):
            log.debug("[tikzautomata] load from existing file...")
            with open(f"{filename}.svg", "r", encoding="utf-8") as f:
                svg_str = f.read(None)
            os.chdir("..")
            return svg_str

        writer = TeXWriter()
        writer.config.preamble = r'''
\documentclass[dvisvgm]{standalone}
\usepackage{tikz}

\usetikzlibrary {arrows.meta,automata,positioning,shapes.geometric}
        '''
        begin_command = r"\begin{tikzpicture}[%s]" % self.options if self.options else r"\begin{tikzpicture}[->,>={Stealth[round]},shorten >=1pt,auto,node distance=2cm,on grid,semithick,inner sep=2pt,bend angle=50,initial text=]"
        writer.create_tex_file("\n".join((
            begin_command,
            self.contents.strip(),
            r'''\end{tikzpicture} 
'''
        )), filename)

        writer.create_svg_from_tex(filename)

        with open(f"{filename}.svg", "r", encoding="utf-8") as f:
            svg_str = f.read(None)

        # clean up
        if cachefile == False :
            try:
                os.remove(filename + ".svg")
            except FileNotFoundError:
                pass

        os.chdir("..")

        return svg_str

        