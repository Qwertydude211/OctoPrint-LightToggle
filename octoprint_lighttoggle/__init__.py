import octoprint.plugin

class LighttogglePlugin(
    octoprint.plugin.SimpleApiPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.StartupPlugin
):
    def __init__(self):
        self.light_on = False

    def on_after_startup(self):
        self._logger.info("Lighttoggle loaded; light is OFF")

    def get_api_commands(self):
        return dict(on=[], off=[])

    def on_api_command(self, command, data):
        if command == "on":
            self._printer.commands("M355 S1")
            self.light_on = True
        elif command == "off":
            self._printer.commands("M355 S0")
            self.light_on = False
        return {"status": "on" if self.light_on else "off"}

    def get_template_configs(self):
        return [dict(type="sidebar", name="Light Control", icon="lightbulb-o")]

__plugin_name__ = "Lighttoggle Plugin"
__plugin_implementation__ = LighttogglePlugin()
