import bpy
import math
#from decimal import Decimal

a=0
b=0
for i in range(1,50):
    R=0.5
    x=(i/25)*R
    y=math.sqrt(R*R- (x-R)*(x-R))
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":( x-a, y-b, 0.08), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":False, "use_snap_edit":False, "use_snap_nonedit":False, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.transform.rotate(value=0.0628318, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (0, -0, 1)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
    a=x
    b=y

for i in range(1,49):
    R=0.5
    x=((50-i)/25)*R
    y=-math.sqrt(R*R- (x-R)*(x-R))
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":( x-a, y-b, 0.08), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":False, "use_snap_edit":False, "use_snap_nonedit":False, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.transform.rotate(value=0.0628318, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (0, -0, 1)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
    a=x
    b=y
