from bascenev1lib.actor.spazappearance import Appearance

# Registra tu personaje. 
# Veras un ejemplo de ello a continuacion.

# Ej: Osito #####################################
t = Appearance('Osito') # Nombre
t.color_texture      = 'ositoColor'
t.color_mask_texture = 'ositoColorMask'
t.icon_texture       = 'ositoIconColor'
t.icon_mask_texture  = 'ositoIconColorMask'
t.head_mesh         = 'ositoHead'
t.torso_mesh        = 'ositoTorso'
t.pelvis_mesh       = 'ositoPelvis'
t.upper_arm_mesh    = 'ositoUpperArm'
t.forearm_mesh      = 'ositoForeArm'
t.hand_mesh         = 'ositoHand'
t.upper_leg_mesh    = 'ositoUpperLeg'
t.lower_leg_mesh    = 'ositoLowerLeg'
t.toes_mesh         = 'ositoToes'
sounds               = ['osito', 'osito2',
                        'osito3', 'osito4']
soundsHit            = ['ositoHit', 'ositoHit2',
                        'ositoHit3', 'ositoHit4']
t.attack_sounds      = sounds
t.jump_sounds        = sounds
t.impact_sounds      = soundsHit
t.death_sounds       = ["ositoDeath"]
t.pickup_sounds      = sounds
t.fall_sounds        = ["ositoFall"]
t.style              = 'bernard'
