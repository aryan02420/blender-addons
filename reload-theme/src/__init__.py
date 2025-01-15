import bpy

def reload_theme(context):
    current_theme_filepath = context.preferences.themes['Default'].filepath
    return bpy.ops.script.execute_preset(
        filepath=current_theme_filepath,
        menu_idname="USERPREF_MT_interface_theme_presets"
    )

class SCRIPT_OT_reload_theme(bpy.types.Operator):
    """Reloads the current theme"""
    bl_idname = "script.reload_theme"
    bl_label = "Reload Theme"

    def execute(self, context):
        return reload_theme(context)

def register():
    bpy.utils.register_class(SCRIPT_OT_reload_theme)

def unregister():
    bpy.utils.unregister_class(SCRIPT_OT_reload_theme)

# if running directly from the blender editor
if __name__ == "__main__":
    register()
    bpy.ops.script.reload_theme()
