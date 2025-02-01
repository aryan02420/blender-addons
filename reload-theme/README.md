# Reload Theme

> [!NOTE]
> This addon is can be installed from the [self hosted extensions registry](../README.md#installation).

This add-on adds a new operator for reloading the current theme. You can access it from the Search Menu (<kbd>F3</kbd> OR <kbd>Spacebar</kbd>) and searching for "Reload Theme".

![Blender's Search Menu with "reload " text as input. "Reload Theme" operator is highlighted in the results.](./assets/preview0.png)

You can also invoke it programmatically using the following code:

```python
bpy.ops.script.reload_theme()
```

This add-on is useful when you are creating a custom theme without using the blender interface. It allows you to reload the theme without restarting Blender.

![Demo for the reload-theme addon. The theme's XML file is being edited from the terminal. After changing a color, the "Reload Theme" operation is executed from the Search Menu, which updates the background color of the 3D viewport.](./assets/preview1.gif)
