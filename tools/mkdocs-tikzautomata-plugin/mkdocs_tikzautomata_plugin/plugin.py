import os
import re

from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.config import config_options
from mkdocs.utils import copy_file

from typing import Dict, Any

from .renderer import TikZAutomataRenderer
from .markdown_utils import replace_indented_block_start_with_options, get_indentation_level

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))

class TikzAutomataPlugin(BasePlugin):
    config_scheme = (
        ("enabled", config_options.Type(bool, default=True)),
        ("cachefile", config_options.Type(bool, default=True)),
    )

    enabled = True

    def on_config(self, config: config_options.Config, **kwargs) -> Dict[str, Any]:
        if not self.enabled:
            return config
        if not self.config.get('enabled'):
            return config
        config["extra_css"] = ["css/svg_extra.css"] + config["extra_css"]

    def on_page_markdown(
        self, markdown: str, page: Page, config: config_options.Config, files, **kwargs
    ) -> str:
        if not self.enabled:
            return markdown
        if not self.config.get("enabled"):
            return markdown
        def _replace_automata(matched: re.Match) -> str:
            options = matched.group("options")
            contents = matched.group("contents")
            zoom = matched.group("zoom")
            first_line_indentation_level = get_indentation_level(matched.group("contents"))

            # print(first_line_indentation_level)

            contents = [i for i in contents.splitlines()]

            contents_remain = []

            for idx, i in enumerate(contents):
                if get_indentation_level(i) < first_line_indentation_level:
                    contents_remain = contents[idx:]
                    contents = contents[:idx]
                    break

            contents = "\n".join(contents)
            tikzcd = TikZAutomataRenderer(options, contents)

            # The string should not be splitted into lines, since markdown parser won't recognize it
            svg_str = "".join(tikzcd.write_to_svg(self.config.get("cachefile")).replace("<?xml version='1.0' encoding='UTF-8'?>", "").splitlines())

            # bolden the stroke
            svg_str = svg_str.replace("stroke-width='0.6'", "stroke-width='0.7'")
            svg_str = svg_str.replace("stroke='none'", "stroke='#000' stroke-width='0.2'")

            return matched.group("leading") + f"<div style=\"text-align: center; zoom: {zoom if zoom else '1.5'};\">{svg_str}</div>" + "\n" + "\n".join(contents_remain)

        markdown = replace_indented_block_start_with_options(r"(?<!\\)\\automata", _replace_automata, markdown)
        markdown = re.sub(r"\\\\automata", r"\\automata", markdown)

        return markdown

    def on_post_build(self, config: Dict[str, Any], **kwargs) -> None:
        if not self.enabled:
            return
        if not self.config.get('enabled'):
            return
        files = ["css/svg_extra.css"]
        for file in files:
            dest_file_path = os.path.join(config["site_dir"], file)
            src_file_path = os.path.join(PLUGIN_DIR, file)
            assert os.path.exists(src_file_path)
            copy_file(src_file_path, dest_file_path)