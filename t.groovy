import org.boon.Boon;

def jsonEditorOptions = Boon.fromJson(/{
		disable_edit_json: true,
        disable_properties: true,
        no_additional_properties: true,
        disable_collapse: true,
        disable_array_add: true,
        disable_array_delete: true,
        disable_array_reorder: true,
        theme: "bootstrap2",
        iconlib:"fontawesome4",
		schema: {
		  "type": "object",
		  "title": "Name",
		  "properties": {
			"first_name": {
			  "type": "string",
			  "propertyOrder" : 1
			},
			"last_name": {
			  "type": "string",
			  "propertyOrder" : 2
			},
			"full_name": {
			  "type": "string",
			  "propertyOrder" : 3,
			  "template": "{{fname}} {{lname}}",
			  "watch": {
				"fname": "first_name",
				"lname": "last_name"
			  }
			}
		  }
		},
		startval: {
			"first_name" : "John",
			"last_name" : "Doe",
			"full_name" : "John Doe"
		}
}/);