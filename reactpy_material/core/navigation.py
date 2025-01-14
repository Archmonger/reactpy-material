from pathlib import Path
from typing import Any

from reactpy import component
from reactpy.core.component import Component
from reactpy.web.module import export, module_from_file
from reactpy.core.types import VdomChild

_js_module = module_from_file(
    "reactpy-material",
    file=Path(__file__).parents[1] / "bundle.js"
)

md_tab = export(_js_module, "MDTab")
md_tabs = export(_js_module, "MDTabs")
md_pagination = export(_js_module, "MDPagination")
md_menu = export(_js_module, "MDMenu")
md_menu_item = export(_js_module, "MDMenuItem")
md_speed_dial = export(_js_module, "MDSpeedDial")
md_speed_dial_action = export(_js_module, "MDSpeedDialAction")

@component
def tab(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_tab(attrs, children_items)

@component
def tabs(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_tabs(attrs, children_items)

@component
def pagination(attrs: Any = {}):
    return md_pagination(attrs)

@component
def menu(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_menu(attrs, children_items)

@component
def menu_item(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_menu_item(attrs, children_items)

@component
def speed_dial(*children: VdomChild, attrs: Any = {}):    
    children_items = ()
    for c in children:
        if isinstance(c, Component):
            children_items += (c.render(), )
        else:
            children_items += (c, )

    return md_speed_dial(attrs, children_items)

@component
def speed_dial_action(attrs: Any = {}):
    return md_speed_dial_action(attrs)

