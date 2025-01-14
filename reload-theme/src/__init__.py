import bpy

def reload_theme(context):
    current_theme_filepath = bpy.context.preferences.themes['Default'].filepath
    return bpy.ops.script.execute_preset(
        filepath=current_theme_filepath,
        menu_idname="USERPREF_MT_interface_theme_presets"
    )

class ReloadThemeOperator(bpy.types.Operator):
    """Reloads the current theme"""
    bl_idname = "script.reload_theme"
    bl_label = "Reload Theme"

    def execute(self, context):
        return reload_theme(context)

def register():
    bpy.utils.register_class(ReloadThemeOperator)

def unregister():
    bpy.utils.unregister_class(ReloadThemeOperator)

# if running directly from the blender editor
if __name__ == "__main__":
    register()
    bpy.ops.script.reload_theme()
