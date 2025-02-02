import bpy

def reload_addon(operator, context):
    addon_preferences = context.preferences.addons[__package__].preferences
    addon_filepath = addon_preferences.addon_filepath.strip()
    if addon_filepath:
        ret = bpy.ops.extensions.package_install_files(
            'EXEC_DEFAULT',
            filepath=addon_filepath,
            repo='user_default'
        )
        if ret == {'FINISHED'}:
            operator.report({'INFO'}, f'Reinstalled "{bpy.path.display_name_from_filepath(addon_filepath)}"')
            return {'FINISHED'}

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
        row.prop(self, "addon_filepath", text="Addon path (.zip, .py)")
        layout.label(
            text="The filepath provided must be a valid blender addon. Executing \"Reload Addon\" will reinstall the addon from the above provided path.",
            icon='INFO'
        )

class SCRIPT_OT_reload_addon(bpy.types.Operator):
    """Reloads a specified local addon from the disk"""
    bl_idname = "script.reload_addon"
    bl_label = "Reload Addon"

    def execute(self, context):
        return reload_addon(self, context)

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
