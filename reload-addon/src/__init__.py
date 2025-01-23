import bpy

def reload_addon(context):
    addon_preferences = bpy.context.preferences.addons[__package__].preferences
    addon_filepath = addon_preferences.addon_filepath.strip()
    if addon_filepath:
        return bpy.ops.extensions.package_install_files(
            filepath=addon_filepath,
            repo='user_default'
        )
    return {'CANCELLED'}

class ReloadAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    addon_filepath: bpy.props.StringProperty(
        default="",
        name="Addon file path",
        description="Path to the local addon (.zip, .py)",
        subtype='FILE_PATH'
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, "addon_filepath", text="Path to the local addon (.zip, .py)")

class SCRIPT_OT_reload_addon(bpy.types.Operator):
    """Reloads a specified local addon from the disk"""
    bl_idname = "script.reload_addon"
    bl_label = "Reload Addon UPDATED!!!!"

    def execute(self, context):
        return reload_addon(context)

def register():
    bpy.utils.register_class(SCRIPT_OT_reload_addon)
    bpy.utils.register_class(ReloadAddonPreferences)

def unregister():
    bpy.utils.unregister_class(ReloadAddonPreferences)
    bpy.utils.unregister_class(SCRIPT_OT_reload_addon)

# if running directly from the blender editor
if __name__ == "__main__":
    register()
    bpy.ops.script.reload_addon()
