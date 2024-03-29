# ba_meta require api 7

"""
    - Minor changes
    - Version 1.7

"""


#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  - Plugin SEBASTIAN2059 - Zacker Tz- - - - - - - - - - - - - - - -
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  - Maps:                                                         - 
#  - Neo Zone v1          - by Zacker Tz || Zacker#5505            -
#  - Big H    v1          - by SEBASTIAN2059 || SEBASTIAN2059#5751 -
#  - The Limbo v2         - by Zacker Tz || Zacker#5505            -
#  - Platforms v2         - by SEBASTIAN2059 || SEBASTIAN2059#5751 -  
#  - Powerups Factory v2  - by Zacker Tz || Zacker#5505            -
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  - Notes
#  - The Powerups Factory map generates some lag, use it at your own risk 
#  - El mapa Powerups Factory genera un poco de lag, usalo bajo tu propio riesgo  
#  - - - - 
#  - New maps coming soon!
#  -

from __future__ import annotations

from typing import TYPE_CHECKING

from bastd.maps import *
import ba
import _ba
import base64
from ba import _map
import random

if TYPE_CHECKING:
    from typing import Any, List, Dict
    
##Complementos##
class FadeEfect():
    def __init__(self, map_tint = (1,1,1)):
        gnode = ba.getactivity().globalsnode
        ba.animate_array(gnode,'tint',3,{0:(0,0,0),0.5:(0,0,0),1.2:map_tint})
        
        text = ba.newnode('text',
                              attrs={
                                    'position': (0,325),
                                    'text': 'Building Map...',
                                    'color': (1,1,1),
                                    'h_align': 'center','v_align': 'center', 'vr_depth': 410, 'maxwidth': 600, 'shadow': 1.0, 'flatness': 1.0, 'scale':2, 'h_attach': 'center', 'v_attach': 'bottom'})
        ba.animate(text,'opacity',{0:1,0.2:1,0.7:0})
        ba.timer(1,text.delete)
        
        text = ba.newnode('text',
                              attrs={
                                    'position': (0,295),
                                    'text': 'Maps by Sebastian2059-ZackerTz',
                                    'color': (0.1,0.0,0.76),
                                    'h_align': 'center', 'v_align': 'center', 'vr_depth': 410, 'maxwidth': 600, 'shadow': 1.0, 'flatness': 1.0, 'scale':0.7, 'h_attach': 'center', 'v_attach': 'bottom'})
        ba.animate(text,'opacity',{0:1,0.2:1,0.7:0})
        ba.timer(1,text.delete)
        

class Credits:
    """ Don't delete this if you respect other people's work"""
    def __init__(self):
        exec(base64.b64decode("dCA9IGJhLm5ld25vZGUoJ3RleHQnLAogICAgICAgICAgICAgICBhdHRycz17ICd0ZXh0JzoiTWFwcyBieTogU0VCQVNUSUFOMjA1OS1aYWNrZXIgVHoiLCAKICAgICAgICAnc2NhbGUnOjAuNiwKICAgICAgICAncG9zaXRpb24nOigwLDApLCAKICAgICAgICAnb3BhY2l0eSc6IDAuNCwKICAgICAgICAnc2hhZG93JzowLjUsCiAgICAgICAgJ2ZsYXRuZXNzJzoxLjIsCiAgICAgICAgJ2NvbG9yJzooMSwgMSwgMSksCiAgICAgICAgJ2hfYWxpZ24nOidjZW50ZXInLAogICAgICAgICd2X2F0dGFjaCc6J2JvdHRvbSd9KQ==").decode('UTF-8')) # :bobolu:        
###End###


#Map by Zacker Tz 
#Map #1
class neo_defs():
    boxes = {}
    points = {}
    boxes['area_of_interest_bounds'] = (0, 4, 0) + (0, 0, 0) + (50, 10, 20)
    boxes['edge_box'] = (0, 4, 0) + (0.0, 0.0, 0.0) + (40, 2, 10)
    boxes['map_bounds'] = (0, 4, 0) + (0, 0, 0) + (28, 10, 28)
    points['ffa_spawn1'] = (-10,3.17,0) + (1.0,0.1,1.0)
    points['ffa_spawn2'] = (10,3.17,0) + (1.0,0.1,1.0)
    points['ffa_spawn3'] = (-5.25,3.17,-1.75) + (0.5,0.1,0.5) 
    points['ffa_Spawn4'] = (5.25,3.17,-1.75) + (0.5,0.1,0.5) 
    points['spawn1'] = (-11,3.17,0) + (1.0,0.1,1.0)
    points['spawn2'] = (11,3.17,0) + (1.0,0.1,1.0)
    points['flag1'] = (-12.0,3.3,0) + (2.0,0.1,2.0)
    points['flag2'] = (12.0,3.3,0) + (2.0,0.1,2.0)
    points['flag_default'] = (0,3.3,1.75)
    points['powerup_spawn1'] = (-11,4.0,-1.75)
    points['powerup_spawn2'] = (-11,4.0,1.75)
    points['powerup_spawn3'] = (-1.75,4.0,0)
    points['powerup_spawn4'] = (1.75,4.0,0.0)
    points['powerup_spawn5'] = (11,4.0,-1.75)
    points['powerup_spawn6'] = (11,4.0,1.75)
 

class NeoZone(ba.Map):
    """Agent john's former workplace"""

    defs = neo_defs()
    name = 'Neo Zone'

    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return ['melee','king_of_the_hill','keep_away','team_flag']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'rgbStripes'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'model': ba.getmodel('landMine'),
            'tex': ba.gettexture('landMine'),
            'bgtex': ba.gettexture('black'),
            'bgmodel': ba.getmodel('thePadBG'),
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        
        self._collide_with_player=ba.Material()
        self._collide_with_player.add_actions(conditions=('we_are_older_than', 1), actions=(('modify_part_collision', 'collide', True)))
        self.dont_collide=ba.Material()
        self.dont_collide.add_actions(conditions=('they_are_different_node_than_us', ),actions=(('modify_part_collision', 'collide', False)))
        
        self._map_model = ba.getmodel('image1x1')
        self._map_model2 = ba.getmodel('tnt')
        self._map_tex = ba.gettexture('powerupIceBombs')
        self._map_tex1 = ba.gettexture('ouyaUButton') 
        
        self.background = ba.newnode('terrain',
                                    attrs={
                                    'model': self.preloaddata['bgmodel'],
                                    'lighting': False,
                                    'background': True,
                                    'color_texture': self.preloaddata['bgtex']
            })

        locations = [(7.0,0.0,0),(5.25,0.0,0),(5.25,0.0,-1.75),
                (3.5,0.0,-1.75),(1.75,0.0,-1.75),(1.75,0.0,0),
                (1.75,0.0,1.75),
                (0,0.0,1.75),
                (-7.0,0.0,0),(-5.25,0.0,0),(-5.25,3.17,-1.75),
                (-3.5,0.0,-1.75),(-1.75,0.0,-1.75),(-1.75,0.0,0),
                (-1.75,0.0,1.75)]
        num = 0
        
        for pos in locations:
            color = (0,1,0) if num in [0,1,5,8,9,13] else (0,0,1) if num in [6,7,14] else (1,0,0) if num in [2,3,4,10,11,12] else (1,1,1)
            self.decor = ba.newnode('prop',
                    attrs={'body': 'puck',
                           'position': (pos[0],3.17,pos[2]),
                           'model': self._map_model,
                           'model_scale': 1.7,
                           'body_scale': 0.1,
                           'shadow_size': 0.0,
                           'gravity_scale':0.0,
                           'color_texture': self._map_tex1,
                           'reflection': 'soft',
                           'reflection_scale': [0.5],
                           'is_area_of_interest': True,
                           'materials': [self.dont_collide]})
            self.region = ba.newnode('region',attrs={
                                        'position': (pos[0],2.3,pos[2]),
                                        'scale': (1.9,1.9,1.9),
                                        'type': 'box',
                                        'materials': (self._collide_with_player, shared.footing_material)})
            self.zone = ba.newnode('locator',
                                    attrs={'shape':'box',
                                    'position':(pos[0],2.3,pos[2]),
                                    'color':color,
                                    'opacity':1,'draw_beauty':True,'additive':False,'size':[1.75,1.75,1.75]})
            num += 1
        
        #Sides  
        side_locations = [(-10.5,2.3,0),(10.5,2.3,0)]    
        for pos in side_locations:
            self.big_region = ba.newnode('region',attrs={
                                        'position': pos,
                                        'scale': (5.7,1.9,5.7),
                                        'type': 'box',
                                        'materials': (self._collide_with_player, shared.footing_material)})        
            self.big_zone = ba.newnode('locator',
                                        attrs={'shape':'box',
                                        'position':pos,
                                        'color':(0,1,1.5),
                                        'opacity':1,'draw_beauty':True,'additive':False,'size':[5.25,1.75,5.25]})         
                                    
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.05, 1.17)
        gnode.happy_thoughts_mode = False
        gnode.ambient_color = (1.2, 1.17, 1.1)
        gnode.vignette_outer = (0.9, 0.9, 0.96)
        gnode.vignette_inner = (0.95, 0.95, 0.93)
        FadeEfect(gnode.tint)
        Credits()

#Map by Sebastian2059
#Map #2
class c_defs():
    boxes = {}
    points = {}
    boxes['area_of_interest_bounds'] = (0, 4, 0) + (0, 0, 0) + (50, 10, 20)
    boxes['edge_box'] = (0, 4, 0) + (0.0, 0.0, 0.0) + (40, 2, 10)
    boxes['map_bounds'] = (0, 4, 0) + (0, 0, 0) + (28, 10, 28)
    points['ffa_spawn1'] = (-9,0.5,-3) + (1.0,0.1,5.0)
    points['ffa_spawn2'] = (9,0.5,-3) + (1.0,0.1,5.0)
    points['ffa_spawn3'] = (-6,0.5,-6.0) + (2.0,0.1,1.0) 
    points['ffa_Spawn4'] = (6,0.5,0.0) + (2.0,0.1,1.0) 
    points['ffa_spawn5'] = (6,0.5,-6.0) + (2.0,0.1,1.0) 
    points['ffa_Spawn6'] = (-6,0.5,0.0) + (2.0,0.1,1.0) 
    points['spawn1'] = (-9,0.5,-3) + (1.0,0.1,1.0)
    points['spawn2'] = (9,0.5,-3) + (1.0,0.1,1.0)
    points['flag1'] = (-10.0,0.8,-3) + (2.0,0.1,2.0)
    points['flag2'] = (10.0,0.8,-3) + (2.0,0.1,2.0)
    points['flag_default'] = (0,0.8,-3.0)
    points['powerup_spawn1'] = (-9,1.0,-8)
    points['powerup_spawn2'] = (-9,1.0,3)
    points['powerup_spawn3'] = (-1.5,1.0,-8.25)
    points['powerup_spawn4'] = (1.5,1.0,-8.25)
    points['powerup_spawn5'] = (-1.5,1.0,2.25)
    points['powerup_spawn6'] = (1.5,1.0,2.25)
    points['powerup_spawn7'] = (9,1.0,-8)
    points['powerup_spawn8'] = (9,1.0,3)
    
    points['race_mine1'] = (-1.5, 0.7, -0.7)
    points['race_mine2'] = (-1.5, 0.7, 0.7)
    points['race_mine3'] = (-4.5, 0.7, 0.0)
    points['race_mine4'] = (4.5, 0.7, 0.0)
    points['race_mine5'] = (4.5, 0.7, -6.0)
    points['race_mine6'] = (-4.5, 0.7, -6.0)
    points['race_mine7'] = (0.0, 0.7, -6.0)
    points['race_mine8'] = (-10.0, 0.7, -4.5)
    points['race_mine9'] = (10.0, 0.7, -4.5)    
    points['race_mine10'] = (10.0, 0.7, -1.5)
    points['race_mine11'] = (-10.0, 0.7, -1.5)
    
    points['race_point1'] = (0.0, 0.5, 0.0) + (0.3, 2.0, 1.5)
    points['race_point2'] = (3.5, 0.5, 0.0) + (0.3, 2.0, 1.5)
    points['race_point3'] = (7.0, 0.5, 0.0) + (0.3, 2.0, 1.5)
    points['race_point4'] = (9.0, 0.5, -2.0) + (1.5, 2.0, 0.3)
    points['race_point5'] = (9.0, 0.5, -4.0) + (1.5, 2.0, 0.3)
    points['race_point6'] = (7.0, 0.5, -6.0) + (0.3, 2.0, 1.5)
    points['race_point7'] = (3.5, 0.5, -6.0) + (0.3, 2.0, 1.5)
    points['race_point8'] = (0.0, 0.5, -6.0) + (0.3, 2.0, 1.5)
    points['race_point9'] = (-3.5, 0.5, -6.0) + (0.3, 2.0, 1.5)
    points['race_point10'] = (-7.0, 0.5, -6.0) + (0.3, 2.0, 1.5)
    points['race_point11'] = (-9.0, 0.5, -2.0) + (1.5, 2.0, 0.3)
    points['race_point12'] = (-9.0, 0.5, -4.0) + (1.5, 2.0, 0.3)
    points['race_point13'] = (-7.0, 0.5, 0.0) + (0.3, 2.0, 1.5)
    points['race_point14'] = (-3.5, 0.5, 0.0) + (0.3, 2.0, 1.5)
 
class CMap(ba.Map):
    """Jack Morgan used to run here"""
    
    defs = c_defs()
    name = 'Big H'

    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return ['melee','king_of_the_hill','keep_away','team_flag','race']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'bigG'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'model': ba.getmodel('landMine'),
            'tex': ba.gettexture('landMine'),
            'bgtex': ba.gettexture('black'),
            'bgmodel': ba.getmodel('thePadBG'),
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        
        self._collide_with_player=ba.Material()
        self._collide_with_player.add_actions(conditions=('we_are_older_than', 1), actions=(('modify_part_collision', 'collide', True)))
        self.dont_collide=ba.Material()
        self.dont_collide.add_actions(conditions=('they_are_different_node_than_us', ),actions=(('modify_part_collision', 'collide', False)))
        self.ice_material = ba.Material()
        self.ice_material.add_actions(actions=('modify_part_collision','friction',0.01))
        
        self._map_model = ba.getmodel('image1x1')
        self._map_model2 = ba.getmodel('tnt')
        self._map_tex = ba.gettexture('powerupIceBombs')
        self._map_tex1 = ba.gettexture('circleOutlineNoAlpha') 
        self._map_tex2 = ba.gettexture('black') 
        
        self.background = ba.newnode('terrain',
                                    attrs={
                                    'model': self.preloaddata['bgmodel'],
                                    'lighting': False,
                                    'background': True,
                                    'color_texture': self.preloaddata['bgtex']
            })

        posS = [(0.0,0.05,0)]
        for m_pos in posS:
            self.mv_center = ba.newnode('prop',
                    attrs={'body': 'puck',
                           'position': m_pos,
                           'model': self._map_model,
                           'model_scale': 35,
                           'body_scale': 0.1,
                           'shadow_size': 0.0,
                           'gravity_scale':0.0,
                           'color_texture': self._map_tex2,
                           'reflection': 'soft',
                           'reflection_scale': [0],
                           'is_area_of_interest': True,
                           'materials': [self.dont_collide]})        
        
        locations = [(-9,0.0,-3.0),(9,0.0,-3.0),(0.0,0.0,-6.0),(0.0,0.0,0.0),(0.0,0.0,-3.0)]
        scales = [[3.0,1.0,14.0],[3.0,1.0,14.0],[15.0,1.0,3.0],[15.0,1.0,3.0],[3.0,1.0,3.0]]
        index = 0
        for pos in locations:
            #
            scale = scales[index]
            ba.newnode('region',attrs={'position': pos,'scale': scale,'type': 'box','materials': (self._collide_with_player, shared.footing_material)})
            ba.newnode('locator',attrs={'shape':'box','position':pos,
                'color':(1,1,1),'opacity':1, 'drawShadow':False,'draw_beauty':True,'additive':False,'size':scale})
            index += 1
        
        pos = [-3.0,0.0,-8.25]
        for p in range(10):
            scale = [1.5,1.0,1.5]
            ba.newnode('region',attrs={'position': pos,'scale': scale,'type': 'box','materials': (self._collide_with_player, shared.footing_material)})
            ba.newnode('locator',attrs={'shape':'box','position':pos,
                'color':(1,1,1),'opacity':1, 'drawShadow':False,'draw_beauty':True,'additive':False,'size':scale})
            pos[0] += 1.5
            if p == 4:
                pos[0] = -3.0
                pos[2] = 2.25
        
        try:
            self._gamemode = ba.getactivity().name
        except Exception:
            print('error')
            pass
        if self._gamemode == 'Race':
            print('Es carrera')
            ice_locations = [(-8,0.0,0),(8,0.0,0),
                             (-8,0.0,-6),(8,0.0,-6),
                             (-9,0.0,-3),(9,0.0,-3)]

            for pos in ice_locations:
                scale = [3.0,1.025,3.0]
                ba.newnode('region',attrs={'position': pos,'scale': scale,'type': 'box','materials': (self._collide_with_player, shared.footing_material, self.ice_material)})
                ba.newnode('locator',attrs={'shape':'box','position':pos,
                    'color':(0,1,1),'opacity':1, 'drawShadow':False,'draw_beauty':True,'additive':False,'size':scale})                         
                    
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.05, 1.17)
        gnode.happy_thoughts_mode = False
        gnode.ambient_color = (1.2, 1.17, 1.1)
        gnode.vignette_outer = (0.9, 0.9, 0.96)
        gnode.vignette_inner = (0.95, 0.95, 0.93)  
        FadeEfect(gnode.tint)
        Credits()          

#Map by Zaker DC [Inspiration from a map of Sebastian]
#Map 3#
class factory_defs:
    boxes = {}
    points = {}
    boxes['area_of_interest_bounds'] = (0, 4, 0) + (0, 0, 0) + (50, 10, 20)
    boxes['edge_box'] = (0, 4, 0) + (0.0, 0.0, 0.0) + (40, 2, 10)
    boxes['map_bounds'] = (0, 4, 0) + (0, 0, 0) + (28, 10, 28)
    
    points['ffa_spawn1'] = (-8,3.5,0) 
    points['ffa_spawn2'] = (8,3.5,0) 
    points['ffa_spawn3'] = (3.4,3.75,3) 
    points['ffa_Spawn4'] = (-3.4,-0.75,-3)
    
    points['spawn1'] = (-8,3.5,0) + (1.0,0.1,1.0)
    points['spawn2'] = (8,3.5,0) + (1.0,0.1,1.0)
    
    points['flag1'] = (-9.5,3.5,0) + (2.0,0.1,2.0)
    points['flag2'] = (9.5,3.5,0) + (2.0,0.1,2.0)
    points['flag_default'] = (0,3.7,0)
    
    points['powerup_spawn1'] = (4.8,3.65,3)
    points['powerup_spawn2'] = (-4.8,3.65,-3)
    points['powerup_spawn3'] = (-4.2,3.7,1.4)    
    points['powerup_spawn4'] = (4.1,3.7,-1.4)

class FactoryMap(ba.Map):
    """Grambledorf former experiment room"""

    defs = factory_defs 
    name = 'Powerups Factory'

    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return ['melee','king_of_the_hill','keep_away','team_flag']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'zigZagLevelColor'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'model': ba.getmodel('landMine'),
            'tex': ba.gettexture('landMine'),
            'bgtex': ba.gettexture('bg'),
            'bgmodel': ba.getmodel('thePadBG'),
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        
        self._collide_with_player=ba.Material()
        self._collide_with_player.add_actions(conditions=('we_are_older_than', 1), actions=(('modify_part_collision', 'collide', True)))
        self.dont_collide=ba.Material()
        self.dont_collide.add_actions(conditions=('they_are_different_node_than_us', ),actions=(('modify_part_collision', 'collide', False)))
        
        self._map_model = ba.getmodel('image1x1')
        self._map_model2 = ba.getmodel('tnt')
        self._map_tex1 = ba.gettexture('powerupImpactBombs') 
        self._map_tex2 = ba.gettexture('reflectionChar_-y') 
        self._map_tex3 = ba.gettexture('flagPoleColor')

        
        self.background = ba.newnode('terrain',
                                    attrs={
                                    'model': self.preloaddata['bgmodel'],
                                    'lighting': False,
                                    'background': True,
                                    'color': (1.3, 1.3, 1.3),
                                    'color_texture': self.preloaddata['bgtex']
            })

        posXD = [(1.5,2.3,0),(-1.5,2.3,0),(0,2.3,0), (4.0,2.3,1.5),(4.0,2.3,-1.5),(4.0,2.3,0), (4.8,2.3,3),(3.4,2.3,3),(1.9,2.3,3), (-4.0,2.3,1.5),(-4.0,2.3,-1.5),(-4.0,2.3,0), (-4.8,2.3,-3),(-3.4,2.3,-3),(-1.9,2.3,-3)
                ]        
        for m_pos in posXD:
            self.mv_center = ba.newnode('prop',
                    attrs={'body': 'puck',
                           'position': m_pos,
                           'model': self._map_model2,
                           'model_scale': 2.2,
                           'body_scale': 0.1,
                           'shadow_size': 0.0,
                           'gravity_scale':0.0,
                           'color_texture': self._map_tex1,
                           'reflection': 'soft',
                           'reflection_scale': [0.5],
                           'is_area_of_interest': True,
                           'materials': [self.dont_collide]})
                           
        posXD = [(-3.4,0.75,-3),(-3.4,-0.75,-3)
                ]                          
        for m_pos in posXD:
            self.mc_center = ba.newnode('region',attrs={ 'position': m_pos,
                                        'scale': (1.5,1.5,1.5), 'type': 'box', 'materials': (self._collide_with_player, shared.footing_material)})        
                                                                
        for m_pos in [(0,2.3,0)]:
            self.mc_center = ba.newnode('region',attrs={'position': m_pos,
                                        'scale': (4.5,1.5,1.5), 'type': 'box', 'materials': (self._collide_with_player, shared.footing_material)})     
                                        
        for m_pos in [(4.0,2.3,0),(-4.0,2.3,0)]:
            self.mc_center = ba.newnode('region',attrs={'position': m_pos,
                                        'scale': (1.5,1.5,4.5), 'type': 'box', 'materials': (self._collide_with_player, shared.footing_material)})  
                                        
        for m_pos in [(3.4,2.3,3),(-3.4,2.3,-3)]:
            self.mc_center = ba.newnode('region',attrs={'position': m_pos,
                                        'scale': (4.5,1.5,1.5), 'type': 'box', 'materials': (self._collide_with_player, shared.footing_material)})                                              
     
        # Cajas Grandes Normales     
        for m_pos in [(8.7,1.72,0),(6.10,1.72,0),(-8.7,1.72,0),(-6.10,1.72,0)]:
            self.mv_d2 = ba.newnode('prop',
                    attrs={'body': 'puck', 'position': m_pos,
                           'model': self._map_model2,
                           'model_scale': 3.8,
                           'color_texture': self._map_tex1, 
                           'reflection_scale': [1.0], 'body_scale': 0.1,  'shadow_size': 0.0, 'gravity_scale':0.0, 'reflection': 'soft', 'is_area_of_interest': True, 'materials': [self.dont_collide]})
                           
        for m_pos in [(7.45,1.72,0),(-7.45,1.72,0)]:                           
            self.mc_d2 = ba.newnode('region',attrs={'position': m_pos,
                                 'scale': (5.25,2.7,2.7), 'type': 'box', 'materials': (self._collide_with_player, shared.footing_material)})
                                 
        #Superficie
        pos = [(-1.5,3.075,0),(0,3.075,0),(1.5,3.075,0), (4.0,3.075,1.5),(4.0,3.075,-1.5),(4.0,3.075,0), (-4.0,3.075,-1.5),(-4.0,3.075,1.5),(-4.0,3.075,0), (-4.8,3.075,-3),(-3.4,3.075,-3),(-1.9,3.075,-3), (4.8,3.075,3),(3.4,3.075,3),(1.9,3.075,3)]
        for m_pos in pos:  
            self.mv_centera = ba.newnode('prop',
                    attrs={'body': 'puck', 'position': m_pos,
                           'model': self._map_model,
                           'color_texture': self._map_tex3,
                           'model_scale': 1.5, 'body_scale': 0.1, 'shadow_size': 0.0, 'gravity_scale':0.0, 'reflection': 'soft', 'reflection_scale': [0.5],'is_area_of_interest': True,
                           'materials': [self.dont_collide]})
           
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.17)
        gnode.ambient_color = (1.2, 1.17, 1.1)
        gnode.vignette_outer = (0.8, 0.7, 0.96)
        gnode.vignette_inner = (0.95, 0.95, 0.93)
        FadeEfect(gnode.tint)
        Credits()
        

# Map by SEBASTIAN2059 
# Map 4#
class platforms_defs:
    boxes = {}
    points = {}
    boxes['area_of_interest_bounds'] = (0, 4, 0) + (0, 0, 0) + (50, 10, 20)
    boxes['edge_box'] = (0, 4, 0) + (0.0, 0.0, 0.0) + (40, 2, 10)
    boxes['map_bounds'] = (0, 4, 0) + (0, 0, 0) + (28, 10, 28)
    points['ffa_spawn1'] = (-10,3.5,0) + (2.0,0.1,2.0)
    points['ffa_spawn2'] = (10,3.5,0) + (2.0,0.1,2.0)
    points['ffa_spawn3'] = (0,3.5,1) 
    points['ffa_Spawn4'] = (0,3.5,-1)
    points['spawn1'] = (-10,3.5,0) + (2.0,0.1,2.0)
    points['spawn2'] = (10,3.5,0) + (2.0,0.1,2.0)
    points['flag1'] = (-12,3.5,0) + (2.0,0.1,2.0)
    points['flag2'] = (12,3.5,0) + (2.0,0.1,2.0)
    points['flag_default'] = (0,3.5,0)    
    points['powerup_spawn1'] = (-11.8,4,-1.8)
    points['powerup_spawn2'] = (-8.2,4,1.8)
    points['powerup_spawn3'] = (8.2,4,-1.8)
    points['powerup_spawn4'] = (11.8,4,1.8)

class PlatformsMap(ba.Map):
    """Plataforms!"""
    defs = platforms_defs
    name = 'Platforms'

    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return ['melee','king_of_the_hill','keep_away','team_flag']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'bridgitLevelColor'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'bgtex': ba.gettexture('bg'),
            'bgmodel': ba.getmodel('thePadBG'),
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        
        self._collide_with_player=ba.Material()
        self._collide_with_player.add_actions(conditions=('we_are_older_than', 1), actions=(('modify_part_collision', 'collide', True)))
        self.dont_collide=ba.Material()
        self.dont_collide.add_actions(conditions=('they_are_different_node_than_us', ),actions=(('modify_part_collision', 'collide', False)))
        
        self._map_model = ba.getmodel('image1x1')
        self._map_tex = ba.gettexture('powerupIceBombs')
        self._map_tex1 = ba.gettexture('powerupPunch') 
        self._map_tex2 = ba.gettexture('powerupImpactBombs')
        
        self.background = ba.newnode('terrain',
                                    attrs={
                                    'model': self.preloaddata['bgmodel'],
                                    'lighting': False,
                                    'background': True,
                                    'color_texture': self.preloaddata['bgtex']
            })
            
        for m_pos in [(-10,2.5,0),(10,2.5,0)]:
            self.e_cnnt = ba.newnode('math', owner=self.node, attrs={'input1': (0, 0.5, 0), 'operation': 'add'})
            self.mc = ba.newnode('region',attrs={'position': m_pos,'scale': (5.0,1,5.0),'type': 'box','materials': (self._collide_with_player, shared.footing_material)})
            self.mv = ba.newnode('prop', owner=self.mc,
                    attrs={'body': 'puck','position': m_pos, 'model': self._map_model, 'model_scale': 5.0, 'body_scale': 0.1, 'shadow_size': 0.0, 'gravity_scale':0.0, 'color_texture': self._map_tex, 'reflection': 'soft', 'reflection_scale': [1.0], 'is_area_of_interest': True, 'materials': [self.dont_collide]})
            self.mc.connectattr('position', self.e_cnnt, 'input2')
            self.e_cnnt.connectattr('output', self.mv, 'position')
            
        for m_pos in [(0,2.5,1.35),(0,2.5,-1.35)]:
            self.c_cnnt = ba.newnode('math', owner=self.node, attrs={'input1': (0, 0.5, 0), 'operation': 'add'})
            self.mc_center = ba.newnode('region',attrs={'position': m_pos,'scale': (2.7,1,2.7),'type': 'box','materials': (self._collide_with_player, shared.footing_material)})
            self.mv_center = ba.newnode('prop', owner=self.mc,
                    attrs={'body': 'puck','position': m_pos, 'model': self._map_model, 'model_scale': 2.7, 'body_scale': 0.1, 'shadow_size': 0.0, 'gravity_scale':0.0, 'color_texture': self._map_tex, 'reflection': 'soft', 'reflection_scale': [1.0], 'is_area_of_interest': True, 'materials': [self.dont_collide]})
            self.mc_center.connectattr('position', self.c_cnnt, 'input2')
            self.c_cnnt.connectattr('output', self.mv_center, 'position')
        
        for m_pos in [(1.1,3.01,0),(-1.1,3.01,0)]:
            self.dec = ba.newnode('prop', owner=self.mc,
                    attrs={'body': 'puck','position': m_pos, 'model': self._map_model, 'model_scale': 0.5, 'body_scale': 0.1, 'shadow_size': 0.0, 'gravity_scale':0.0, 'color_texture': self._map_tex2, 'reflection': 'soft', 'reflection_scale': [1.0], 'is_area_of_interest': True, 'materials': [self.dont_collide]})

        pos = [(-5.9,2.5,1),(-3,2.5,-1),(3,2.5,1),(5.9,2.5,-1)]
        for m_pos in pos:
            self.m_cnnt = ba.newnode('math', owner=self.node, attrs={'input1': (0, 0.5, 0), 'operation': 'add'})
            self.mc_a = ba.newnode('region',attrs={'position': m_pos,'scale': (2.5,1,2.5),'type': 'box','materials': (self._collide_with_player, shared.footing_material)})
            self.mv_a = ba.newnode('prop', owner=self.mc,
                    attrs={'body': 'puck','position': m_pos, 'model': self._map_model, 'model_scale': 2.5, 'body_scale': 0.1, 'shadow_size': 0.0, 'gravity_scale':0.0, 'color_texture': self._map_tex1, 'reflection': 'soft', 'reflection_scale': [1.0], 'is_area_of_interest': True, 'materials': [self.dont_collide]})
            self.mc_a.connectattr('position', self.m_cnnt, 'input2')
            self.m_cnnt.connectattr('output', self.mv_a, 'position')
            if m_pos[2] == -1:
                ba.animate_array(self.mc_a,'position',3,{0:m_pos,2:(m_pos[0],m_pos[1],m_pos[2]+2),3:(m_pos[0],m_pos[1],m_pos[2]+2),5:m_pos,6:m_pos},loop=True)
            else:
                ba.animate_array(self.mc_a,'position',3,{0:m_pos,2:(m_pos[0],m_pos[1],m_pos[2]-2),3:(m_pos[0],m_pos[1],m_pos[2]-2),5:m_pos,6:m_pos},loop=True)
        
    
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.05, 1.17)
        gnode.ambient_color = (1.2, 1.17, 1.1)
        gnode.vignette_outer = (0.9, 0.9, 0.96)
        gnode.vignette_inner = (0.95, 0.95, 0.93)
        FadeEfect(gnode.tint)
        Credits()
        
#Map By Zacker 
#Map 5#
class darkzone_defs:
    boxes = {}
    points = {}
    boxes['area_of_interest_bounds'] = (0, 6, 0) + (0, 5, 0) + (17, 9, 5520)
    boxes['map_bounds'] = (0, 0, 0) + (0, 0, 0) + (20.0, 23, 7.25)
    points['flag_default'] = (0,5.1,0)
    points['flag1'] = (-6.5,5.79,0.4)
    points['spawn1'] = (-4.4,5,0)
    points['flag2'] = (6.5,5.79,0.4)
    points['spawn2'] = (4.4,5,0)
    points['ffa_spawn1'] = (3,5.2,0)
    points['ffa_spawn2'] = (-3,5.2,0)
    points['ffa_spawn3'] = (4,5.2,0)
    points['ffa_spawn4'] = (-4,5.2,0)    
    points['powerup_spawn1'] = (-5.5,7,0) 
    points['powerup_spawn2'] = (5.5,7,0)

class DarkZone(ba.Map):
    """Unknown city"""
    defs = darkzone_defs 
    name = 'The Limbo'
    
    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return ['melee','king_of_the_hill','keep_away','team_flag']
    
    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'shrapnel1Color'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'bottom_model': ba.getmodel('rampageLevelBottom'), 
            'tex': ba.gettexture('rampageLevelColor'),
            'bgmodel1': ba.getmodel('rampageBG'),
            'bgtex1': ba.gettexture('rampageBGColor'),          
            'bgtex': ba.gettexture('shrapnel1Color'),
            'bgmodel': ba.getmodel('thePadBG'),
        }
        return data
        
    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        
        self._collide_with_player=ba.Material()
        self._collide_with_player.add_actions(conditions=('we_are_older_than', 1), actions=(('modify_part_collision', 'collide', True)))
        self.dont_collide=ba.Material()
        self.dont_collide.add_actions(conditions=('they_are_different_node_than_us', ),actions=(('modify_part_collision', 'collide', False)))
        
        self._map_model1 = ba.getmodel('image1x1')
        self._map_model2 = ba.getmodel('tnt')
        self._map_tex1 = ba.gettexture('black') 
        self._map_tex2 = ba.gettexture('reflectionChar_-y') 
        self._map_tex3 = ba.gettexture('bg')
        self._map_tex4 = ba.gettexture('circleOutlineNoAlpha')
        
        self.background = ba.newnode('terrain',
                                    attrs={
                                    'model': self.preloaddata['bgmodel'],
                                    'lighting': False,
                                    'background': True,
                                    'color_texture': self.preloaddata['bgtex']
            })
            
        self.bg2 = ba.newnode('terrain',
                              attrs={
                                  'model': self.preloaddata['bgmodel1'],
                                  'lighting': False,
                                  'background': True,
                                  'color_texture': self.preloaddata['bgtex1']
                              })                              
         
        self.zone = ba.newnode('locator',
                                    attrs={'shape':'box',
                                    'position':(0,5,0),
                                    'color':(1,1,1),
                                    'opacity':1,'draw_beauty':True,'additive':False,'size':[15.5,0.05,5.3]})
        ba.animate_array(self.zone, 'color', 3,{0:(0,0,0), 1.5:(0,0,0), 2.00:(0,0,0), 2.05:(1,1,1), 2.1:(0,0,0), 2.15:(1,1,1), 2.2:(0,0,0),
                                                2.25:(1,1,1), 2.3:(0,0,0), 2.35:(1,1,1), 2.4:(0,0,0), 2.45:(0.7,0.7,0.7)},False)
                                    
        self.zone = ba.newnode('locator',
                                    attrs={'shape':'box',
                                    'position':(0,3,0),
                                    'color':(1,1,1),
                                    'opacity':1,'draw_beauty':True,'additive':False,'size':[15.5,0.05,5.3]})                          
        ba.animate_array(self.zone, 'color', 3,{0:(0,0,0), 1.5:(0,0,0), 2.00:(0,0,0), 2.05:(1,1,1), 2.1:(0,0,0), 2.15:(1,1,1), 2.2:(0,0,0),
                                                2.25:(1,1,1), 2.3:(0,0,0), 2.35:(1,1,1), 2.4:(0,0,0), 2.45:(0.7,0.7,0.7)},False)
                                                
        self.zone = ba.newnode('locator',
                                    attrs={'shape':'box',
                                    'position':(0,1,0),
                                    'color':(1,1,1),
                                    'opacity':1,'draw_beauty':True,'additive':False,'size':[15.5,0.05,5.3]})
        ba.animate_array(self.zone, 'color', 3,{0:(0,0,0), 1.5:(0,0,0), 2.00:(0,0,0), 2.05:(1,1,1), 2.1:(0,0,0), 2.15:(1,1,1), 2.2:(0,0,0),
                                                2.25:(1,1,1), 2.3:(0,0,0), 2.35:(1,1,1), 2.4:(0,0,0), 2.45:(0.7,0.7,0.7)},False)

        for m_pos1 in [(-5,3,0),(0,3,0),(5,3,0)]:   
            self.mv_center = ba.newnode('prop',
                    attrs={'body': 'puck',
                           'position': m_pos1,
                           'model': self._map_model2,
                           'model_scale': 7.23,
                           'body_scale': 0.1,
                           'shadow_size': 0.0,
                           'gravity_scale':0.0,
                           'color_texture': self._map_tex3,
                           'reflection': 'soft',
                           'reflection_scale': [0.37],
                           'is_area_of_interest': True,
                           'materials': [self.dont_collide]})    
                           
        for m_pos1 in [(0,3,0)]:                              
            self.mc_center = ba.newnode('region',attrs={
                                        'position': m_pos1,
                                        'scale': (15,5,5),
                                        'type': 'box',
                                        'materials': (self._collide_with_player, shared.footing_material)})                                
                           
                           
        for m_pos1 in [(-5,5.4,0),(0,5.4,0),(5,5.4,0)]:    
            self.mv_center = ba.newnode('prop',
                    attrs={'body': 'puck',
                           'position': m_pos1,
                           'model': self._map_model1,
                           'model_scale': 4.00,
                           'body_scale': 0.1,
                           'shadow_size': 0.0,
                           'gravity_scale':0.0,
                           'color_texture': self._map_tex4,
                           'reflection': 'soft',
                           'reflection_scale': [0.0],
                           'is_area_of_interest': True,
                           'materials': [self.dont_collide]})                             
        
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.2,1.2,1.2)
        gnode.ambient_color = (1.15,1.25,1.6)
        gnode.vignette_outer = (0.5,-0.25,0.5)
        gnode.vignette_inner = (0.93,0.93,0.95)
        FadeEfect(gnode.tint)
        Credits()        
        
#List Maps
zk2059 = [FactoryMap,PlatformsMap,DarkZone, #v2
          NeoZone,CMap #v1
          ]

def register_maps():
    for new_map in zk2059:
        _map.register_map(new_map)
    
# ba_meta export plugin
class Zk2059(ba.Plugin):
    def __init__(self):
        if _ba.env().get("build_number", 0) >= 20258:
            register_maps()
        else:
            print("Zk5020 maps only runs with BombSquad versions higher than 1.5.29.")
            