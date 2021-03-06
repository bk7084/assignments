from bk7084 import Window, app
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault as Palette
from bk7084.scene import Mesh, Scene
from bk7084.app.input import KeyCode
from bk7084.app import ui

from buildings import *
from components import *

# Setup window and add camera
window = Window("BK7084: Construction", width=1024, height=1024, clear_color=Palette.BlueA.as_color())

"""
Before you start, make sure that you have activated the conda environment
and upgraded the bk7084 package to support buildings and components.

$ conda activate compsim
$ pip install --upgrade bk7084
"""

ground = Ground(w=10)

skyscraper = Skyscraper(num_floors=5, max_width=1)
skyscraper.transform = Mat4.identity()

# Remove Skyscraper and uncomment Highrise to draw your Highrise building
highrise = Skyscraper(num_floors=2, max_width=0.8) # Highrise(num_floors=3, max_width=1)
highrise.transform = Mat4.from_translation(Vec3(-2, 0, 0))

# Remove Skyscraper and uncomment Office to draw your Office building
office = Skyscraper(num_floors=1, max_width=1.2) # Office(num_floors=3, max_width=1)
office.transform = Mat4.from_translation(Vec3(2, 0, 0))

buildings = [skyscraper, highrise, office]

scene = Scene(window, [ground, skyscraper, highrise, office], draw_light=True)
scene.create_camera(Vec3(8, 6, 8), Vec3(0, 0, 0), Vec3.unit_y(), 60, zoom_enabled=True, safe_rotations=True)

comp = 0
building = 0


@window.event
def on_draw(dt):
    # scene.draw(auto_shadow=True)
    scene.draw_v2(auto_shadow=True)

@window.event
def on_gui():
    global comp, building
    if ui.tree_node('Energy'):
        ui.text('Building: ')
        ui.same_line()
        ui.text(buildings[building].name)
        ui.text('Num floors: ')
        ui.same_line()
        ui.text(str(buildings[building].num_floors))
        _, building = ui.input_int('Index', building)
        building = building % 3
        _, comp = ui.input_int('Comp. Index', comp)
        ui.tree_pop()


@window.event
def on_key_press(key, mods):
    if key == KeyCode.C:
        scene.energy_of_building_component(buildings[building], buildings[building].components[comp])

    if key == KeyCode.B:
        scene.energy_of_building(buildings[building])


app.init(window)
app.run()
