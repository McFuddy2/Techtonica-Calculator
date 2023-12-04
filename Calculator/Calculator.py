class Item:
    def __init__(self, name, item1, amount1, item2, amount2, item3, amount3, item4, amount4):
        self.name = name
        self.item1 = item1
        self.item2 = item2        
        self.item3 = item3
        self.item4 = item4
        self.amount1 = amount1
        self.amount2 = amount2        
        self.amount3 = amount3
        self.amount4 = amount4
        self.items_list = {}
        self._add_item_to_list(item1, amount1)
        self._add_item_to_list(item2, amount2)
        self._add_item_to_list(item3, amount3)
        self._add_item_to_list(item4, amount4)

    def _add_item_to_list(self, item, amount):
        if item is not None and hasattr(item, 'name'):
            self.items_list[item.name] = amount

    def ingredients_needed(self):
        ingredients_str = ", ".join(f"{value} {key}" for key, value in self.items_list.items())
        return f"To build the {self.name} you will need {ingredients_str}"
    

    # THIS IS WHERE I AM WORKING
    def subcomonents_needed(self, item, amount):
        if item is not None and hasattr(item, 'name'):
          self.items_list[item.name] = amount
        if hasattr(item.item1, "name") and item.item1 is not None:
            pass
                
    # THIS ENDS THE "WORKING ZONE"      





kindlevine_extract = Item("kindlevine_extract", None, None, None, None, None, None, None, None)

iron_ore = Item("iron_ore", None, None, None, None, None, None, None, None)

copper_ore = Item("copper_ore", None, None, None, None, None, None, None, None)

iron_ingot = Item("iron_ingot", iron_ore, 2, None, None, None, None, None, None)

limestone = Item("limestone", kindlevine_extract, 2, None, None, None, None, None, None)

copper_ingot = Item("copper_ingot", copper_ore, 2, None, None, None, None, None, None)

iron_components = Item("iron_components", iron_ingot, 2, None, None, None, None, None, None)

copper_wire = Item("copper_wire", copper_ingot, 1, None, None, None, None, None, None)

plantmatter_fiber = Item("plantmatter_fiber", None, None, None, None, None, None, None, None)

plantmatter_frame = Item("plantmatter_frame", plantmatter_fiber, 8, None, None, None, None, None, None)

shiverthorn_seeds = Item("shiverthorn_seeds", None, None, None, None, None, None, None, None)

shiverthorn = Item("shiverthorn", None, None, None, None, None, None, None, None)

shiverthorn_buds = Item("shiverthorn_buds", None, None, None, None, None, None, None, None)

shiverthorn_extract = Item("shiverthorn_extract", shiverthorn_buds, 0.5, None, None, None, None, None, None)

shiverthorn_coolant = Item("shiverthorn_coolant", iron_components, 1, shiverthorn_extract, 2, limestone, 8, None, None)

electrical_components = Item("electrical_components", iron_ingot, 2, copper_wire, 4, None, None, None, None)

mechanical_components = Item("mechanical_components", copper_ingot, 2, iron_ingot, 4, None, None, None, None)

cooling_system = Item("cooling_system", mechanical_components, 2, shiverthorn_coolant, 2, None, None, None, None)

processor_unit = Item("processor_unit", electrical_components, 4, plantmatter_frame, 4, None, None, None, None)

research_core_purple = Item("research_core_purple", copper_wire, 4, mechanical_components, 8, None, None, None, None)

research_core_blue = Item("research_core_blue", research_core_purple, 12, processor_unit, 12, cooling_system, 6, None, None)


print(electrical_components.ingredients_needed())


