# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
			octoprint.plugin.OctoPrintPlugin,
			octoprint.plugin.EventHandlerPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")
    
    def on_event(self, event, payload):
    	if event == Events.PRINT_STARTED:
    		self.change_temperature(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs)
    		
    	else:
    		self.send_message()
    		

    def change_temperature(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if gcode and gcode == "M140":
            	cmd = "M104 S210"
        elif gcode and gcode == "M104":
        	cmd= "M104 S220"	
        return cmd
        
    def send_message(self):
    
    	self._logger.info("No temperature detected".format(**locals()))
     
__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = HelloWorldPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
    "octoprint.events.register_custom_events": __plugin_implementation__._hook_events_register_custom_events,
        "octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.change_temperature
        
        
    }

