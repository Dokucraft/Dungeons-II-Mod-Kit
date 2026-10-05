blocks = [
  # Dungeons Format:
  #   0: Block ID
  #   1: Block Data
  #   2: Block Data Mask

  # Java Format:
  #   0: Block ID
  #   1: Block Properties

  { 'dungeons': [ 0x0000 ], 'java': [ 'minecraft:air' ] },
  
  
  # Temp Blocks to Replace
  # -----------------------
  # stripped_acacia_log
  # prismarine_slab
  # prismarine_stairs
  # prismarine_wall
  # warped_fence
  # snow
  
  { 'dungeons': [ 0x006A, 0b0000 ], 'java': [ 'minecraft:vine', { 'east': 'false', 'north': 'false', 'west': 'false', 'south': 'false' } ] }, # Vine
  { 'dungeons': [ 0x006D, 0b0100 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x006E, 0b0000 ], 'java': [ 'minecraft:podzol' ] }, # Podzol
  { 'dungeons': [ 0x000D, 0b0000 ], 'java': [ 'minecraft:gravel' ] }, # Gravel
  { 'dungeons': [ 0x0010, 0b0000 ], 'java': [ 'minecraft:coal_ore' ] }, # Coal Ore
  { 'dungeons': [ 0x0001, 0b0000 ], 'java': [ 'minecraft:stone' ] }, # Stone
  { 'dungeons': [ 0x0001, 0b0001 ], 'java': [ 'minecraft:granite' ] }, # Granite
  { 'dungeons': [ 0x0001, 0b0101 ], 'java': [ 'minecraft:andesite' ] }, # Andesite
  { 'dungeons': [ 0x00E0, 0b0000 ], 'java': [ 'minecraft:white_concrete' ] }, # White Concrete
  { 'dungeons': [ 0x00E9, 0b0000 ], 'java': [ 'minecraft:cyan_concrete' ] }, # Cyan Concrete
  { 'dungeons': [ 0x0002, 0b0000 ], 'java': [ 'minecraft:grass_block' ] }, # Grass
  { 'dungeons': [ 0x0030, 0b0000 ], 'java': [ 'minecraft:mossy_cobblestone' ] }, # Mossy Cobblestone
  { 'dungeons': [ 0x0031, 0b0000 ], 'java': [ 'minecraft:obsidian' ] }, # Obsidian
  { 'dungeons': [ 0x0042, 0b0001 ], 'java': [ 'minecraft:rail', { 'shape': 'east_west' } ] }, # Rail
  { 'dungeons': [ 0x0042, 0b0011 ], 'java': [ 'minecraft:rail', { 'shape': 'ascending_west' } ] }, # Rail
  { 'dungeons': [ 0x0062, 0b0010 ], 'java': [ 'minecraft:cracked_stone_bricks' ] }, # Cracked Stone Bricks
  { 'dungeons': [ 0x0062, 0b0011 ], 'java': [ 'minecraft:chiseled_stone_bricks' ] }, # Chiseled Stone Bricks
  { 'dungeons': [ 0x0009, 0b0000 ], 'java': [ 'minecraft:water', { 'level': '1' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b0001 ], 'java': [ 'minecraft:water', { 'level': '2' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b0010 ], 'java': [ 'minecraft:water', { 'level': '3' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b0011 ], 'java': [ 'minecraft:water', { 'level': '4' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b0100 ], 'java': [ 'minecraft:water', { 'level': '5' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b0101 ], 'java': [ 'minecraft:water', { 'level': '6' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b0110 ], 'java': [ 'minecraft:water', { 'level': '7' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b0111 ], 'java': [ 'minecraft:water', { 'level': '8' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b1000 ], 'java': [ 'minecraft:water', { 'level': '9' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b1001 ], 'java': [ 'minecraft:water', { 'level': '10' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b1010 ], 'java': [ 'minecraft:water', { 'level': '11' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b1011 ], 'java': [ 'minecraft:water', { 'level': '12' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b1100 ], 'java': [ 'minecraft:water', { 'level': '13' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b1101 ], 'java': [ 'minecraft:water', { 'level': '14' } ] }, # Water
  { 'dungeons': [ 0x0009, 0b1110 ], 'java': [ 'minecraft:water', { 'level': '15' } ] }, # Water
  { 'dungeons': [ 0x0009 ], 'java': [ 'minecraft:water', { 'level': '0' } ] }, # Water
  { 'dungeons': [ 0x000B, 0b0000 ], 'java': [ 'minecraft:lava', { 'level': '1' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b0001 ], 'java': [ 'minecraft:lava', { 'level': '2' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b0010 ], 'java': [ 'minecraft:lava', { 'level': '3' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b0011 ], 'java': [ 'minecraft:lava', { 'level': '4' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b0100 ], 'java': [ 'minecraft:lava', { 'level': '5' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b0101 ], 'java': [ 'minecraft:lava', { 'level': '6' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b0110 ], 'java': [ 'minecraft:lava', { 'level': '7' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b0111 ], 'java': [ 'minecraft:lava', { 'level': '8' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b1000 ], 'java': [ 'minecraft:lava', { 'level': '9' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b1001 ], 'java': [ 'minecraft:lava', { 'level': '10' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b1010 ], 'java': [ 'minecraft:lava', { 'level': '11' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b1011 ], 'java': [ 'minecraft:lava', { 'level': '12' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b1100 ], 'java': [ 'minecraft:lava', { 'level': '13' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b1101 ], 'java': [ 'minecraft:lava', { 'level': '14' } ] }, # Lava
  { 'dungeons': [ 0x000B, 0b1110 ], 'java': [ 'minecraft:lava', { 'level': '15' } ] }, # Lava
  { 'dungeons': [ 0x000B ], 'java': [ 'minecraft:lava', { 'level': '0' } ] }, # Lava
  
  # CampA1
  
  { 'dungeons': [ 0x03FB, 0b0000 ], 'java': [ 'minecraft:spruce_fence' ] }, # Spruce Fence (PlainsA1) (Custom)
  { 'dungeons': [ 0x0404, 0b0000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log Axis Y (PlainsA1) (Custom)
  { 'dungeons': [ 0x0404, 0b0100 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'x' } ] }, # Spruce Log Axis X (PlainsA1) (Custom)
  { 'dungeons': [ 0x0404, 0b1000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'z' } ] }, # Spruce Log Axis Z (PlainsA1) (Custom)
  { 'dungeons': [ 0x0416, 0b0000 ], 'java': [ 'minecraft:blue_wool' ] }, # Blue Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x0519, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 1 (Custom)
  { 'dungeons': [ 0x051A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 2 (Custom)
  { 'dungeons': [ 0x051D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 5 (Custom)
  { 'dungeons': [ 0x051E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 6 (Custom)
  { 'dungeons': [ 0x0752, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # BuffStone (CampA1) (Custom)
  { 'dungeons': [ 0x0755, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (CampA1) (Custom)
  { 'dungeons': [ 0x0756, 0b0000 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (CampA1) (Custom)
  { 'dungeons': [ 0x0757, 0b0000 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Cobblestone Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0757, 0b0001 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Cobblestone Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0757, 0b0011 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Cobblestone Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0758, 0b0000 ], 'java': [ 'minecraft:mossy_cobblestone' ] }, # Mossy Cobblestone (CampA1) (Custom)
  { 'dungeons': [ 0x075B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mossy Cobblestone 2 (CampA1) (Custom)
  { 'dungeons': [ 0x075C, 0b0000 ], 'java': [ 'minecraft:mossy_cobblestone_slab' ] }, # Mossy Cobblestone 2 Slab (CampA1) (Custom)
  { 'dungeons': [ 0x075D, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (CampA1) (Custom)
  { 'dungeons': [ 0x075E, 0b0000 ], 'java': [ 'minecraft:grass_block' ] }, # Grass (CampA1) (Custom)
  { 'dungeons': [ 0x0760, 0b0000 ], 'java': [ 'minecraft:gravel' ] }, # Gravel (CampA1) (Custom)
  { 'dungeons': [ 0x0761, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mossy Dirt 1 (CampA1) (Custom)
  { 'dungeons': [ 0x0762, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mossy Dirt 2 (CampA1) (Custom)
  { 'dungeons': [ 0x0763, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mossy Dirt 3 (CampA1) (Custom)
  { 'dungeons': [ 0x0764, 0b0000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'y' } ] }, # Oak Log Axis Y (CampA1) (Custom)
  { 'dungeons': [ 0x0764, 0b0100 ], 'java': [ 'minecraft:oak_log', { 'axis': 'x' } ] }, # Oak Log Axis X (CampA1) (Custom)
  { 'dungeons': [ 0x0765, 0b0000 ], 'java': [ 'minecraft:obsidian' ] }, # Obsidian (CampA1) (Custom)
  { 'dungeons': [ 0x0766, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pebble Dirt 1 (CampA1) (Custom)
  { 'dungeons': [ 0x0767, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pebble Dirt 2 (CampA1) (Custom)
  { 'dungeons': [ 0x0768, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pebble Dirt 3 (CampA1) (Custom)
  { 'dungeons': [ 0x0769, 0b0000 ], 'java': [ 'minecraft:jungle_planks' ] }, # Jungle Planks (CampA1) (Custom)
  { 'dungeons': [ 0x076C, 0b0000 ], 'java': [ 'minecraft:oak_planks' ] }, # Oak Planks (CampA1) (Custom)
  { 'dungeons': [ 0x0770, 0b0000 ], 'java': [ 'minecraft:spruce_planks' ] }, # Spruce Planks (CampA1) (Custom)
  { 'dungeons': [ 0x0772, 0b0001 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Spruce Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0772, 0b0011 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Spruce Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0774, 0b0000 ], 'java': [ 'minecraft:polished_granite' ] }, # Polished Granite (CampA1) (Custom)
  { 'dungeons': [ 0x0776, 0b0000 ], 'java': [ 'minecraft:polished_andesite' ] }, # Polished Andesite (CampA1) (Custom)
  { 'dungeons': [ 0x0777, 0b0000 ], 'java': [ 'minecraft:polished_andesite_slab' ] }, # Polished Andesite Slab (CampA1) (Custom)
  { 'dungeons': [ 0x0778, 0b0000 ], 'java': [ 'minecraft:chiseled_quartz_block' ] }, # Chiseled Quartz (CampA1) (Custom)
  { 'dungeons': [ 0x0779, 0b0000 ], 'java': [ 'minecraft:quartz_pillar' ] }, # Quartz Pillar (CampA1) (Custom)
  { 'dungeons': [ 0x077B, 0b0000 ], 'java': [ 'minecraft:sand' ] }, # Sand (CampA1) (Custom)
  { 'dungeons': [ 0x077F, 0b0000 ], 'java': [ 'minecraft:stone' ] }, # Stone (CampA1) (Custom)
  { 'dungeons': [ 0x0780, 0b0000 ], 'java': [ 'minecraft:stone_slab' ] }, # Stone Slab (CampA1) (Custom)
  { 'dungeons': [ 0x0781, 0b0000 ], 'java': [ 'minecraft:stone_bricks' ] }, # Stone Brick (CampA1) (Custom)
  { 'dungeons': [ 0x0782, 0b0000 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Brick Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0782, 0b0001 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Brick Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0782, 0b0010 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Brick Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0782, 0b0011 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Brick Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0782, 0b0100 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Stone Brick Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0782, 0b0101 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Brick Stairs (CampA1) (Custom)
  { 'dungeons': [ 0x0783, 0b0000 ], 'java': [ 'minecraft:stone_brick_slab' ] }, # Stone Brick Slab (CampA1) (Custom)
  { 'dungeons': [ 0x0784, 0b0000 ], 'java': [ 'minecraft:stone_brick_wall' ] }, # Stone Brick Wall (CampA1) (Custom)
  { 'dungeons': [ 0x0785, 0b0000 ], 'java': [ 'minecraft:chiseled_stone_bricks' ] }, # Chiseled Stone Bricks (CampA1) (Custom)
  { 'dungeons': [ 0x0786, 0b0000 ], 'java': [ 'minecraft:mossy_stone_bricks' ] }, # Mossy Stone Bricks (CampA1) (Custom)
  { 'dungeons': [ 0x0789, 0b0000 ], 'java': [ 'minecraft:cracked_stone_bricks' ] }, # Cracked Stone Bricks (CampA1) (Custom)
  { 'dungeons': [ 0x078A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cracked Stone Brick Wall (CampA1) (Custom)
  { 'dungeons': [ 0x078D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # StoneCarving - No Shadow (CampA1) (Custom)
  { 'dungeons': [ 0x078F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # StoneCarving Moss - No Shadow (CampA1) (Custom)
  { 'dungeons': [ 0x0790, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile (CampA1) (Custom)
  { 'dungeons': [ 0x0791, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile Dirt 1 (CampA1) (Custom)
  { 'dungeons': [ 0x0792, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile Dirt 2 (CampA1) (Custom)
  { 'dungeons': [ 0x0793, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile Dirt 3 (CampA1) (Custom)
  { 'dungeons': [ 0x0794, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile Dirt 4 (CampA1) (Custom)
  { 'dungeons': [ 0x0795, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile Ornate 1 (CampA1) (Custom)
  { 'dungeons': [ 0x0796, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile Ornate 2 (CampA1) (Custom)
  { 'dungeons': [ 0x0797, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # StonyDirt (CampA1) (Custom)
  { 'dungeons': [ 0x079A, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Tile Dirt 3 Slab (CampA1) (Custom)
  { 'dungeons': [ 0x079B, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Tile Dirt 4 Slab (CampA1) (Custom)
  { 'dungeons': [ 0x00CA, 0b0000 ], 'java': [ 'minecraft:air' ] }, # Player Blocker/Kill Volume? (Custom)
  { 'dungeons': [ 0x00D2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk?
  { 'dungeons': [ 0x0358, 0b0000 ], 'java': [ 'minecraft:stone_slab' ] }, # Stone Slab (Town) (Custom)
  { 'dungeons': [ 0x035D, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor Slab (Town) (Custom)
  
  # Town_2
  
  { 'dungeons': [ 0x03F3, 0b0000 ], 'java': [ 'minecraft:spruce_slab' ] }, # Spruce Planks Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03F3, 0b1000 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'top' } ] }, # Spruce Planks Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x0449, 0b0000 ], 'java': [ 'minecraft:mossy_cobblestone' ] }, # Mossy Cobblestone (ForestA1) (Custom)
  { 'dungeons': [ 0x0518, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 0 (Custom)
  { 'dungeons': [ 0x051B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 3 (Custom)
  { 'dungeons': [ 0x051F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 7 (Custom)
  { 'dungeons': [ 0x0089, 0b0011 ], 'java': [ 'minecraft:bedrock' ] }, # Smooth Stone Tile (Custom)
  { 'dungeons': [ 0x0001, 0b1011 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile with Dirt on 2 Edges (Custom)
  { 'dungeons': [ 0x0089, 0b0100 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile with Dirt on 2 Edges Slab (Custom)
  { 'dungeons': [ 0x05FE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone (DesertA1) (Custom)
  { 'dungeons': [ 0x009B, 0b0000 ], 'java': [ 'minecraft:quartz_block' ] }, # Quartz Block
  { 'dungeons': [ 0x009E, 0b0001 ], 'java': [ 'minecraft:jungle_slab' ] }, # Jungle Planks Slab
  { 'dungeons': [ 0x009E, 0b1001 ], 'java': [ 'minecraft:jungle_slab', { 'type': 'top' } ] }, # Jungle Planks Slab
  { 'dungeons': [ 0x0643, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete (DesertA1) (Custom)
  { 'dungeons': [ 0x0654, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cracked Light Concrete (DesertA1) (Custom)
  { 'dungeons': [ 0x069A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Golden Dirt (Plains) (Custom)
  { 'dungeons': [ 0x069B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Golden Mix High (Plains) (Custom)
  { 'dungeons': [ 0x069C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Golden Mix Mid (Plains) (Custom)
  { 'dungeons': [ 0x069D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Golden Mix Low (Plains) (Custom)
  { 'dungeons': [ 0x06A3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Golden Dirt Slab (Plains) (Custom)
  { 'dungeons': [ 0x06A9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 1 (Plains) (Custom)
  { 'dungeons': [ 0x06AA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 2 (Plains) (Custom)
  { 'dungeons': [ 0x06AB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Golden Grass High (Plains) (Custom)
  { 'dungeons': [ 0x0715, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cinder (PeaksA1) (Custom)
  { 'dungeons': [ 0x0724, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Cobblestone Cinder 2 (PeaksA1) (Custom)
  { 'dungeons': [ 0x073C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Cobblestone Cinder 0 (PeaksA1) (Custom)
  { 'dungeons': [ 0x0001, 0b1010 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile (Custom)
  { 'dungeons': [ 0x0001, 0b1100 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tile with Dirt on 4 Edges (Custom)
  { 'dungeons': [ 0x0001, 0b0111 ], 'java': [ 'minecraft:bedrock' ] }, # Slightly Mossy Stone Tile (Custom)
  { 'dungeons': [ 0x0001, 0b1000 ], 'java': [ 'minecraft:bedrock' ] }, # Medium Mossy Stone Tile (Custom)
  { 'dungeons': [ 0x0001, 0b1001 ], 'java': [ 'minecraft:bedrock' ] }, # Full Mossy Stone Tile (Custom)
  { 'dungeons': [ 0x08B3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Stone (PlainsA1) (Custom)
  { 'dungeons': [ 0x022F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Wall Stonebrick (Custom)
  { 'dungeons': [ 0x0302, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (Town) (Custom)
  { 'dungeons': [ 0x0303, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 0 (Town) (Custom)
  { 'dungeons': [ 0x0304, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 1 (Town) (Custom)
  { 'dungeons': [ 0x0305, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (Town) (Custom)
  { 'dungeons': [ 0x0308, 0b0000 ], 'java': [ 'minecraft:stone_slab', { 'type': 'double' } ] }, # Stone Double Slab (Town) (Custom)
  { 'dungeons': [ 0x030F, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0311, 0b0000 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'double' } ] }, # Spruce Planks Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0313, 0b0000 ], 'java': [ 'minecraft:jungle_slab', { 'type': 'double' } ] }, # Jungle Planks Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0316, 0b0000 ], 'java': [ 'minecraft:farmland', { 'moisture': '7' } ] }, # Wet Farmland (Town) (Custom)
  { 'dungeons': [ 0x0318, 0b0000 ], 'java': [ 'minecraft:grass_block' ] }, # Grass Block (Town) (Custom)
  { 'dungeons': [ 0x031D, 0b0000 ], 'java': [ 'minecraft:mossy_cobblestone' ] }, # Mossy Cobblestone (Town) (Custom)
  { 'dungeons': [ 0x031E, 0b0000 ], 'java': [ 'minecraft:mycelium' ] }, # Mycelium (Town) (Custom)
  { 'dungeons': [ 0x031F, 0b0000 ], 'java': [ 'minecraft:mycelium' ] }, # Mycelium 1 (Town) (Custom)
  { 'dungeons': [ 0x0321, 0b0000 ], 'java': [ 'minecraft:sand' ] }, # Sand (Town) (Custom)
  { 'dungeons': [ 0x0326, 0b0000 ], 'java': [ 'minecraft:white_terracotta' ] }, # White Terracotta (Town) (Custom)
  { 'dungeons': [ 0x032B, 0b0000 ], 'java': [ 'minecraft:lime_terracotta' ] }, # Lime Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0335, 0b0000 ], 'java': [ 'minecraft:black_terracotta' ] }, # Black Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0336, 0b0000 ], 'java': [ 'minecraft:stone' ] }, # Stone (Town) (Custom)
  { 'dungeons': [ 0x033A, 0b0000 ], 'java': [ 'minecraft:polished_diorite' ] }, # Polished Diorite (Town) (Custom)
  { 'dungeons': [ 0x033C, 0b0000 ], 'java': [ 'minecraft:polished_andesite' ] }, # Polished Andesite (Town) (Custom)
  { 'dungeons': [ 0x033E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 2 (Town) (Custom)
  { 'dungeons': [ 0x0340, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 10 (Town) (Custom)
  { 'dungeons': [ 0x0341, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 11 (Town) (Custom)
  { 'dungeons': [ 0x0342, 0b0000 ], 'java': [ 'minecraft:stone_bricks' ] }, # Stone Bricks (Town) (Custom)
  { 'dungeons': [ 0x0343, 0b0000 ], 'java': [ 'minecraft:mossy_stone_bricks' ] }, # Mossy Stone Bricks (Town) (Custom)
  { 'dungeons': [ 0x0345, 0b0000 ], 'java': [ 'minecraft:chiseled_stone_bricks' ] }, # Chiseled Stone Bricks (Town) (Custom)
  { 'dungeons': [ 0x034F, 0b0000 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Brick Stairs (Town) (Custom)
  { 'dungeons': [ 0x034F, 0b0001 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Brick Stairs (Town) (Custom)
  { 'dungeons': [ 0x034F, 0b0010 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Brick Stairs (Town) (Custom)
  { 'dungeons': [ 0x034F, 0b0011 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Brick Stairs (Town) (Custom)
  { 'dungeons': [ 0x0350, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Mossy Stone Brick Stairs (Town) (Custom)
  { 'dungeons': [ 0x0352, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Chiseled Stone Brick Stairs (Town) (Custom)
  { 'dungeons': [ 0x0353, 0b0100 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Cobblestone Stairs (Town) (Custom)
  { 'dungeons': [ 0x0353, 0b0110 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Cobblestone Stairs (Town) (Custom)
  { 'dungeons': [ 0x0353, 0b0111 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Cobblestone Stairs (Town) (Custom)
  { 'dungeons': [ 0x0356, 0b0000 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (Town) (Custom)
  { 'dungeons': [ 0x035F, 0b0000 ], 'java': [ 'minecraft:spruce_slab' ] }, # Spruce Planks Slab (Town) (Custom)
  { 'dungeons': [ 0x035F, 0b1000 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'top' } ] }, # Spruce Planks Slab (Town) (Custom)
  { 'dungeons': [ 0x0367, 0b0000 ], 'java': [ 'minecraft:spruce_fence' ] }, # Spruce Planks Fence (Town) (Custom)
  { 'dungeons': [ 0x036C, 0b0000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'y' } ] }, # Oak Log (Town) (Custom)
  { 'dungeons': [ 0x036C, 0b0100 ], 'java': [ 'minecraft:oak_log', { 'axis': 'x' } ] }, # Oak Log (Town) (Custom)
  { 'dungeons': [ 0x036C, 0b1000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'z' } ] }, # Oak Log (Town) (Custom)
  { 'dungeons': [ 0x036D, 0b0000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log (Town) (Custom)
  { 'dungeons': [ 0x036D, 0b0100 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'x' } ] }, # Spruce Log (Town) (Custom)
  { 'dungeons': [ 0x036D, 0b1000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'z' } ] }, # Spruce Log (Town) (Custom)
  { 'dungeons': [ 0x0378, 0b0000 ], 'java': [ 'minecraft:orange_wool' ] }, # Orange Wool (Town) (Custom)
  { 'dungeons': [ 0x0379, 0b0000 ], 'java': [ 'minecraft:magenta_wool' ] }, # Magenta Wool (Town) (Custom)
  { 'dungeons': [ 0x037C, 0b0000 ], 'java': [ 'minecraft:lime_wool' ] }, # Lime Wool (Town) (Custom)
  { 'dungeons': [ 0x037E, 0b0000 ], 'java': [ 'minecraft:gray_wool' ] }, # Gray Wool (Town) (Custom)
  { 'dungeons': [ 0x0380, 0b0000 ], 'java': [ 'minecraft:cyan_wool' ] }, # Cyan Wool (Town) (Custom)
  { 'dungeons': [ 0x0383, 0b0000 ], 'java': [ 'minecraft:brown_wool' ] }, # Brown Wool (Town) (Custom)
  { 'dungeons': [ 0x038F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 6 (Town) (Custom)
  { 'dungeons': [ 0x0390, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (PlainsA1) (Custom)
  { 'dungeons': [ 0x039C, 0b0000 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'double' } ] }, # Spruce Planks Double Slab (PlainsA1) (Custom)
  
  # BlockTestGym

  { 'dungeons': [ 0x0300, 0b0000 ], 'java': [ 'minecraft:brick' ] }, # Bricks (Town) (Custom)
  { 'dungeons': [ 0x0301, 0b0000 ], 'java': [ 'minecraft:clay' ] }, # Clay (Town) (Custom)
  { 'dungeons': [ 0x0306, 0b0000 ], 'java': [ 'minecraft:sandstone_slab', { 'type': 'double' } ] }, # Sandstone Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0307, 0b0000 ], 'java': [ 'minecraft:oak_slab', { 'type': 'double' } ] }, # Oak Planks Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0309, 0b0000 ], 'java': [ 'minecraft:brick_slab', { 'type': 'double' } ] }, # Brick Double Slab (Town) (Custom)
  { 'dungeons': [ 0x030A, 0b0000 ], 'java': [ 'minecraft:stone_brick_slab', { 'type': 'double' } ] }, # Stone Brick Double Slab (Town) (Custom)
  { 'dungeons': [ 0x030B, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 1 Double Slab (Town) (Custom)
  { 'dungeons': [ 0x030C, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 2 Double Slab (Town) (Custom)
  { 'dungeons': [ 0x030D, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 3 Double Slab (Town) (Custom)
  { 'dungeons': [ 0x030E, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 4 Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0310, 0b0000 ], 'java': [ 'minecraft:oak_slab', { 'type': 'double' } ] }, # Oak Planks Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0312, 0b0000 ], 'java': [ 'minecraft:birch_slab', { 'type': 'double' } ] }, # Birch Planks Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0314, 0b0000 ], 'java': [ 'minecraft:acacia_slab', { 'type': 'double' } ] }, # Acacia Planks Double Slab (Town) (Custom)
  { 'dungeons': [ 0x0315, 0b0000 ], 'java': [ 'minecraft:bookshelf' ] }, # Bookshelf (Town) (Custom)
  { 'dungeons': [ 0x0317, 0b0000 ], 'java': [ 'minecraft:farmland', { 'moisture': '0' } ] }, # Dry Farmland (Town) (Custom)
  { 'dungeons': [ 0x0319, 0b0000 ], 'java': [ 'minecraft:dirt_path' ] }, # Podzol Path (Town) (Custom)
  { 'dungeons': [ 0x031A, 0b0000 ], 'java': [ 'minecraft:dirt_path' ] }, # Dirt Path (Town) (Custom)
  { 'dungeons': [ 0x031B, 0b0000 ], 'java': [ 'minecraft:gravel' ] }, # Gravel (Town) (Custom)
  { 'dungeons': [ 0x031C, 0b0000 ], 'java': [ 'minecraft:terracotta' ] }, # Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0320, 0b0000 ], 'java': [ 'minecraft:podzol' ] }, # Podzol (Town) (Custom)
  { 'dungeons': [ 0x0322, 0b0000 ], 'java': [ 'minecraft:red_sand' ] }, # Red Sand (Town) (Custom)
  { 'dungeons': [ 0x0323, 0b0000 ], 'java': [ 'minecraft:sandstone' ] }, # Sandstone (Town) (Custom)
  { 'dungeons': [ 0x0324, 0b0000 ], 'java': [ 'minecraft:chiseled_sandstone' ] }, # Chiseled Sandstone (Town) (Custom)
  { 'dungeons': [ 0x0325, 0b0000 ], 'java': [ 'minecraft:cut_sandstone' ] }, # Cut Sandstone (Town) (Custom)
  { 'dungeons': [ 0x0327, 0b0000 ], 'java': [ 'minecraft:orange_terracotta' ] }, # Orange Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0328, 0b0000 ], 'java': [ 'minecraft:magenta_terracotta' ] }, # Magenta Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0329, 0b0000 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (Town) (Custom)
  { 'dungeons': [ 0x032A, 0b0000 ], 'java': [ 'minecraft:yellow_terracotta' ] }, # Yellow Terracotta (Town) (Custom)
  { 'dungeons': [ 0x032C, 0b0000 ], 'java': [ 'minecraft:pink_terracotta' ] }, # Pink Terracotta (Town) (Custom)
  { 'dungeons': [ 0x032D, 0b0000 ], 'java': [ 'minecraft:gray_terracotta' ] }, # Gray Terracotta (Town) (Custom)
  { 'dungeons': [ 0x032E, 0b0000 ], 'java': [ 'minecraft:light_gray_terracotta' ] }, # Light Gray Terracotta (Town) (Custom)
  { 'dungeons': [ 0x032F, 0b0000 ], 'java': [ 'minecraft:cyan_terracotta' ] }, # Cyan Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0330, 0b0000 ], 'java': [ 'minecraft:purple_terracotta' ] }, # Purple Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0331, 0b0000 ], 'java': [ 'minecraft:blue_terracotta' ] }, # Blue Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0332, 0b0000 ], 'java': [ 'minecraft:brown_terracotta' ] }, # Brown Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0333, 0b0000 ], 'java': [ 'minecraft:green_terracotta' ] }, # Green Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0334, 0b0000 ], 'java': [ 'minecraft:red_terracotta' ] }, # Red Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0337, 0b0000 ], 'java': [ 'minecraft:granite' ] }, # Granite (Town) (Custom)
  { 'dungeons': [ 0x0338, 0b0000 ], 'java': [ 'minecraft:polished_granite' ] }, # Polished Granite (Town) (Custom)
  { 'dungeons': [ 0x0339, 0b0000 ], 'java': [ 'minecraft:diorite' ] }, # Diorite (Town) (Custom)
  { 'dungeons': [ 0x033B, 0b0000 ], 'java': [ 'minecraft:andesite' ] }, # Andesite (Town) (Custom)
  { 'dungeons': [ 0x033D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 1 (Town) (Custom)
  { 'dungeons': [ 0x033F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 3 (Town) (Custom)
  { 'dungeons': [ 0x0344, 0b0000 ], 'java': [ 'minecraft:cracked_stone_bricks' ] }, # Cracked Stone Bricks (Town) (Custom)

  # CS01_ForestArea

  { 'dungeons': [ 0x0404, 0b0001 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log (PlainsA1) (Custom)
  { 'dungeons': [ 0x0404, 0b0101 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'x' } ] }, # Spruce Log (PlainsA1) (Custom)
  { 'dungeons': [ 0x038B, 0b1101 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 2 (PlainsA1) (Custom)
  { 'dungeons': [ 0x038D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 4 (PlainsA1) (Custom)
  { 'dungeons': [ 0x039B, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 6 Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03A5, 0b0000 ], 'java': [ 'minecraft:grass_block' ] }, # Grass (PlainsA1) (Custom)
  { 'dungeons': [ 0x03A8, 0b0000 ], 'java': [ 'minecraft:gravel' ] }, # Gravel (PlainsA1) (Custom)
  { 'dungeons': [ 0x03B2, 0b0000 ], 'java': [ 'minecraft:podzol' ] }, # Podzol (PlainsA1) (Custom)
  { 'dungeons': [ 0x03B6, 0b0000 ], 'java': [ 'minecraft:sand' ] }, # Sand (PlainsA1) (Custom)
  { 'dungeons': [ 0x03CB, 0b1111 ], 'java': [ 'minecraft:black_terracotta' ] }, # Black Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03CE, 0b0011 ], 'java': [ 'minecraft:diorite' ] }, # Diorite (PlainsA1) (Custom)
  { 'dungeons': [ 0x03E3, 0b0000 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Cobblestone Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03E7, 0b0000 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03E7, 0b0011 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (PlainsA1) (Custom)(Unsure why a Duplicate Exists as Blockstate is still Bottom Half)

  # CS_DeepdarkA2_Shot

  { 'dungeons': [ 0x0485, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Paving Stone (Deep Dark) (Custom)
  { 'dungeons': [ 0x0488, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Paving Stone Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x048A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Paving Stone Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x048C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Paving Stone 4x (Deep Dark) (Custom)
  { 'dungeons': [ 0x049E, 0b0000 ], 'java': [ 'minecraft:deepslate' ] }, # Deepslate (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A7, 0b0000 ], 'java': [ 'minecraft:deepslate' ] }, # Deepslate
  { 'dungeons': [ 0x04B2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dust Block (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Base Floor (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Base Floor Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Base Floor Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B9, 0b0000 ], 'java': [ 'minecraft:deepslate_bricks' ] }, # Deepslate Bricks (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Bricks Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Bricks Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04E6, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Slab Tr3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04E7, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Slab Tr4 (Deep Dark) (Custom)
  { 'dungeons': [ 0x0514, 0b0010 ], 'java': [ 'minecraft:deepslate_brick_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0516, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Deepslate Brick Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0517, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Deepslate Brick Tr2 Stairs (Deep Dark) (Custom)

  # CS_Staircase

  { 'dungeons': [ 0x0514, 0b0000 ], 'java': [ 'minecraft:deepslate_brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0514, 0b0001 ], 'java': [ 'minecraft:deepslate_brick_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0514, 0b0011 ], 'java': [ 'minecraft:deepslate_brick_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)

  # CS_WarHall

  { 'dungeons': [ 0x07F4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Sponge 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x081F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pillar Top (MeadowA2) (Custom)
  { 'dungeons': [ 0x0823, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark (MeadowA2) (Custom)
  { 'dungeons': [ 0x0824, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x082C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark 5 (MeadowA2) (Custom)
  { 'dungeons': [ 0x082D, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flag Dark 5 Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x082E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark 6 (MeadowA2) (Custom)
  { 'dungeons': [ 0x082F, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flag Dark 6 Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x0830, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark 7 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0831, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flag Dark 7 Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x0832, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Light (MeadowA2) (Custom)
  { 'dungeons': [ 0x0833, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flag Light_Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x083B, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flag Light 5 Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x083D, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flag Light 6 Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x0849, 0b0000 ], 'java': [ 'minecraft:bricks' ] }, # Bricks (MeadowA2) (Custom)
  { 'dungeons': [ 0x085C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x085D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x085F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0860, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Bricks 4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0861, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Bricks 5 (MeadowA2) (Custom)

  # CampA1_Cutscenes

  { 'dungeons': [ 0x0520, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 8 (Custom)
  { 'dungeons': [ 0x009E, 0b0000 ], 'java': [ 'minecraft:oak_slab', { 'type': 'bottom' } ] }, # Oak Planks Slab
  { 'dungeons': [ 0x076A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Jungle Planks (CampA1) (Custom)
  { 'dungeons': [ 0x0771, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spruce Planks (CampA1) (Custom)
  { 'dungeons': [ 0x0023, 0b1110 ], 'java': [ 'minecraft:red_wool' ] }, # Red Wool
  { 'dungeons': [ 0x0044, 0b0100 ], 'java': [ 'minecraft:oak_wall_sign', { 'facing': 'west' } ] }, # Oak Wall Sign

  # CarapaceInterior

  { 'dungeons': [ 0x057C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 2 Path (Custom)
  { 'dungeons': [ 0x06EE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x06F1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete 7 (DesertA1) (Custom)
  { 'dungeons': [ 0x086C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Shell (CarapaceA1) (Custom)
  { 'dungeons': [ 0x086D, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Shell Slab (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0872, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Shell Cracked (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0873, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Shell Cracked Slab (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0875, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Shell Hole (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0876, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Shell Hole Slab (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0878, 0b0000 ], 'java': [ 'minecraft:sand' ] }, # Sand (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0879, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Sand Slab (CarapaceA1) (Custom)
  { 'dungeons': [ 0x087A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sand Layered (CarapaceA1) (Custom)
  { 'dungeons': [ 0x087A, 0b0001 ], 'java': [ 'minecraft:bedrock' ] }, # Sand Layered (CarapaceA1) (Custom)
  { 'dungeons': [ 0x087A, 0b0010 ], 'java': [ 'minecraft:bedrock' ] }, # Sand Layered (CarapaceA1) (Custom)
  { 'dungeons': [ 0x087A, 0b0011 ], 'java': [ 'minecraft:bedrock' ] }, # Sand Layered (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0881, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sand Waves 2 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0883, 0b0000 ], 'java': [ 'minecraft:soul_sand' ] }, # Soul Sand (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0896, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dry Dirt (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0897, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dry Dirt Sand 1 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0898, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dry Dirt Sand 2 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0899, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dry Dirt Sand 3 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x089A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # CarA1_DirtClear (CarapaceA1) (Custom)
  { 'dungeons': [ 0x089B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # CarA1_DirtLight (CarapaceA1) (Custom)
  { 'dungeons': [ 0x089C, 0b0100 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt Transition 1 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x089C, 0b1000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt Transition 1 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x089D, 0b0100 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt Transition 2 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x089D, 0b1000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt Transition 2 (CarapaceA1) (Custom)
  { 'dungeons': [ 0x08B0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Shell Rose (CarapaceA1) (Custom)
  { 'dungeons': [ 0x0016, 0b0000 ], 'java': [ 'minecraft:lapis_block' ] }, # Lapis Block
  { 'dungeons': [ 0x00CD, 0b0000 ], 'java': [ 'minecraft:white_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b0001 ], 'java': [ 'minecraft:orange_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b0010 ], 'java': [ 'minecraft:magenta_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b1000 ], 'java': [ 'minecraft:light_gray_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b1001 ], 'java': [ 'minecraft:cyan_stained_glass' ] }, # 

  # DeepDarkA1

  { 'dungeons': [ 0x0486, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Stone Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0486, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Paving Stone Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x048B, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Stone Tr2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x048B, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Paving Stone Tr2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x048D, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Stone 4x Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x048D, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Paving Stone 4x Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0492, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Paving Stone Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0492, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Paving Stone Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0492, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Paving Stone Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0492, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Paving Stone Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0493, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Paving Stone Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0493, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Paving Stone Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0493, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Paving Stone Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0493, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Paving Stone Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0494, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Paving Stone 4x Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0494, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Paving Stone 4x Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0494, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Paving Stone 4x Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0494, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Paving Stone 4x Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0497, 0b0000 ], 'java': [ 'minecraft:obsidian' ] }, # Obsidian (Deep Dark) (Custom)
  { 'dungeons': [ 0x049F, 0b0000 ], 'java': [ 'minecraft:moss_block' ] }, # Moss (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Moss Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Moss Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Moss Tr3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Moss Tr4 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Moss Tr5 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A8, 0b0000 ], 'java': [ 'minecraft:snow', { 'layers': '1' } ] }, # Moss layer (Deep Dark) (Custom) # Moss layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A8, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': '2' } ] }, # Moss layer (Deep Dark) (Custom) # Moss layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A8, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Moss layer (Deep Dark) (Custom) # Moss layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobbled Deepslate (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AD, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Deepslate Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AD, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Deepslate Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AE, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Deepslate Tr2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B0, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Cobbled Deepslate Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B1, 0b0000 ], 'java': [ 'minecraft:snow', { 'layers': '1' } ] }, # Dust layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B1, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': '2' } ] }, # Dust layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B1, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Dust layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B1, 0b0011 ], 'java': [ 'minecraft:snow', { 'layers': '4' } ] }, # Dust layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B1, 0b0100 ], 'java': [ 'minecraft:snow', { 'layers': '5' } ] }, # Dust layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B1, 0b0101 ], 'java': [ 'minecraft:snow', { 'layers': '6' } ] }, # Dust layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B1, 0b0110 ], 'java': [ 'minecraft:snow', { 'layers': '7' } ] }, # Dust layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B6, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BA, 0b0000 ], 'java': [ 'minecraft:cracked_deepslate_bricks' ] }, # Cracked Deepslate Bricks (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BD, 0b0000 ], 'java': [ 'minecraft:deepslate_brick_slab' ] }, # Deepslate Bricks Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BE, 0b0000 ], 'java': [ 'minecraft:cracked_deepslate_brick_slab' ] }, # Cracked Deepslate Bricks Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BF, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Deepslate Bricks Tr1 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C0, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Deepslate Bricks Tr2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dust Sides (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Chiseled Deepslate (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Chiseled Deepslate 2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Carved 3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Pillar 1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C9, 0b0000 ], 'java': [ 'minecraft:andesite' ] }, # Andesite (Deep Dark) (Custom)
  { 'dungeons': [ 0x04CA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Andesite Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04CB, 0b0000 ], 'java': [ 'minecraft:stone' ] }, # Stone (Deep Dark) (Custom)
  { 'dungeons': [ 0x04CF, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobblestone Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobblestone Tr3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D3, 0b0000 ], 'java': [ 'minecraft:amethyst' ] }, # Amythyst (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Amythyst Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mossy Deepslate Bricks (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mossy Deepslate Bricks 2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04DA, 0b0000 ], 'java': [ 'minecraft:andesite_slab' ] }, # Andesite Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04DC, 0b0000 ], 'java': [ 'minecraft:stone_slab' ] }, # Stone Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04DE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tr2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04E3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobblestone Tr3 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04EA, 0b0000 ], 'java': [ 'minecraft:prismarine_wall' ] }, # Dusty Deepslate Wall (Deep Dark) (Custom)
  { 'dungeons': [ 0x04EB, 0b0000 ], 'java': [ 'minecraft:prismarine_wall' ] }, # Deepslate Wall (Deep Dark) (Custom)
  { 'dungeons': [ 0x04ED, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobblestone Tr4 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04EE, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dirt Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04EF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tr4 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Base Floor Tr3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F1, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Ancient Log (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F1, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Ancient Log (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F1, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Ancient Log (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ancient Log Band (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ancient Log Dust (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ancient Planks (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dusty Ancient Planks (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dusty Ancient Planks 2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FF, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Ancient Plank Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FF, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Ancient Plank Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FF, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Ancient Plank Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0500, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Dusty Ancient Plank Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0509, 0b0000 ], 'java': [ 'minecraft:grass_block' ] }, # Grass (Deep Dark) (Custom)
  { 'dungeons': [ 0x050A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x050B, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Obsidian Pillar (Deep Dark) (Custom)
  { 'dungeons': [ 0x050B, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Obsidian Pillar (Deep Dark) (Custom)
  { 'dungeons': [ 0x050D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Floor Tile (Deep Dark) (Custom)
  { 'dungeons': [ 0x050E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Floor Tile 2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x050F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Floor Tile 3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x0514, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0514, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0514, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0514, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0516, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Deepslate Brick Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0517, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Deepslate Brick Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0517, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Deepslate Brick Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0517, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Deepslate Brick Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0682, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk (Deep Dark) (Custom)
  { 'dungeons': [ 0x0684, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk Dust (Deep Dark) (Custom)
  { 'dungeons': [ 0x0686, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Sculk Paving Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0688, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk Pillar (Deep Dark) (Custom)
  { 'dungeons': [ 0x0689, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk Dust Side (Deep Dark) (Custom)
  { 'dungeons': [ 0x068A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk Stone Brick (Deep Dark) (Custom)
  { 'dungeons': [ 0x068D, 0b0000 ], 'java': [ 'minecraft:warped_fence' ] }, # Amythyst Fence (Deep Dark) (Custom)
  { 'dungeons': [ 0x068E, 0b0000 ], 'java': [ 'minecraft:prismarine_wall' ] }, # Amythyst Wall (Deep Dark) (Custom)
  { 'dungeons': [ 0x0734, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard (PeaksA1) (Custom)
  { 'dungeons': [ 0x07A0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Cinder 1 (PeaksA1) (Custom)
  { 'dungeons': [ 0x07A1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Cinder 2 (PeaksA1) (Custom)
  { 'dungeons': [ 0x00CF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x00DF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x0026, 0b0001 ], 'java': [ 'minecraft:blue_orchid' ] }, # Blue Orchid
  { 'dungeons': [ 0x0003, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt
  { 'dungeons': [ 0x0004, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone
  { 'dungeons': [ 0x0005, 0b0001 ], 'java': [ 'minecraft:spruce_planks' ] }, # Spruce Planks
  { 'dungeons': [ 0x0005, 0b0010 ], 'java': [ 'minecraft:birch_planks' ] }, # Birch Planks
  { 'dungeons': [ 0x0005, 0b0101 ], 'java': [ 'minecraft:dark_oak_planks' ] }, # Dark Oak Planks
  { 'dungeons': [ 0x003F, 0b0110 ], 'java': [ 'minecraft:oak_sign', { 'rotation': '6' } ] }, # Oak Sign
  { 'dungeons': [ 0x003F, 0b1000 ], 'java': [ 'minecraft:oak_sign', { 'rotation': '8' } ] }, # Oak Sign
  { 'dungeons': [ 0x0060, 0b1010 ], 'java': [ 'minecraft:oak_trapdoor', { 'open': 'true', 'half': 'bottom', 'facing': 'south' } ] }, # Oak Trapdoor
  { 'dungeons': [ 0x0060, 0b1101 ], 'java': [ 'minecraft:oak_trapdoor', { 'open': 'true', 'half': 'top', 'facing': 'west' } ] }, # Oak Trapdoor
  { 'dungeons': [ 0x0060, 0b1000 ], 'java': [ 'minecraft:oak_trapdoor', { 'open': 'true', 'half': 'bottom', 'facing': 'east' } ] }, # Oak Trapdoor
  { 'dungeons': [ 0x03CE, 0b0000 ], 'java': [ 'minecraft:diorite' ] }, # Diorite (PlainsA1) (Custom)

  # DeepDarkA2_BossTile

  { 'dungeons': [ 0x0516, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Deepslate Brick Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0516, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Deepslate Brick Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0523, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 11 (Custom)

  # DeepDark_Anchor_Boss

  { 'dungeons': [ 0x0487, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0487, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0487, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AF, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Deepslate Tr1 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AF, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Deepslate Tr1 Slab (Deep Dark) (Custom)

  # Deep_Dark_Anchor_001

  { 'dungeons': [ 0x0487, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0487, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0487, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0487, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0487, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Paving Stone Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0489, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Stone Tr1 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0489, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Paving Stone Tr1 Slab(Deep Dark) (Custom)
  { 'dungeons': [ 0x0490, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Stone 4x Tr1 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0493, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Paving Stone Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0494, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Paving Stone 4x Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0494, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Paving Stone 4x Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0494, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Paving Stone 4x Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0499, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x049A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Tr3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x049B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Tr4 (Deep Dark) (Custom)
  { 'dungeons': [ 0x049D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Tr6 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A5, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Obsidian Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A9, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Moss Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04B0, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Cobbled Deepslate Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BD, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Deepslate Brick Slab  (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BE, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Cracked Deepslate Brick Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04BF, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Deepslate Brick Tr1 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C0, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Deepslate Brick Tr2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C5, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Deepslate Pillar 1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C6, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Deepslate Pillar 2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D5, 0b0000 ], 'java': [ 'minecraft:snow', { 'layers': '1' } ] }, # Dirt Layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D5, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': 'q' } ] }, # Dirt Layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D5, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Dirt Layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04D5, 0b0011 ], 'java': [ 'minecraft:snow', { 'layers': '4' } ] }, # Dirt Layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04E8, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Slab 4x Tr3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04EE, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Dirt Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FA, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Ancient Plank Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FA, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Ancient Plank Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FB, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dusty Ancient Plank Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FC, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dusty Ancient Plank 2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04FF, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Ancient Plank Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x050C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Pillar Cap (Deep Dark) (Custom)
  { 'dungeons': [ 0x0511, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Obsidian Floor Tile 2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0512, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Obsidian Floor Tile 3 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0579, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # White Box 2 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0579, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # White Box 2 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0579, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # White Box 2 Stairs (Custom)
  { 'dungeons': [ 0x057A, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # White Box 3 Stairs (Custom)
  { 'dungeons': [ 0x057A, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # White Box 3 Stairs (Custom)
  { 'dungeons': [ 0x057A, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # White Box 3 Stairs (Custom) 
  { 'dungeons': [ 0x057A, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # White Box 3 Stairs (Custom) 
  { 'dungeons': [ 0x0685, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk Base Floor (Deep Dark) (Custom)
  { 'dungeons': [ 0x0001, 0b0011 ], 'java': [ 'minecraft:diorite' ] }, # Diorite
  { 'dungeons': [ 0x0062, 0b0000 ], 'java': [ 'minecraft:stone_bricks' ] }, # Stone Bricks

  # Deep_Dark_Anchor_002

  { 'dungeons': [ 0x048E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Paving Stone 4x Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x048F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Paving Stone 4x Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A8, 0b0011 ], 'java': [ 'minecraft:snow', { 'layers': '4' } ] }, # Moss layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04C5, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Deepslate Pillar 1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04CC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tr1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04E9, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Slab 4x Tr4 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04EC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Bricks Wall (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F3, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Damaged Ancient Log (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F3, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Damaged Ancient Log (Deep Dark) (Custom)
  { 'dungeons': [ 0x04F3, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Damaged Ancient Log (Deep Dark) (Custom)
  { 'dungeons': [ 0x0501, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Dusty Ancient Plank 2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0504, 0b0000 ], 'java': [ 'minecraft:warped_fence' ] }, # Ancient Plank Fence (Deep Dark) (Custom)
  { 'dungeons': [ 0x0577, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # White Box 3 Slab (Custom)
  { 'dungeons': [ 0x0577, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # White Box 3 Slab (Custom)
  { 'dungeons': [ 0x0037, 0b0000 ], 'java': [ 'minecraft:redstone_wire', { 'power': '0' } ] }, # Redstone Dust

  # Deep_Dark_Pool_1

  { 'dungeons': [ 0x006D, 0b0000 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x006D, 0b0001 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x006D, 0b0010 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x006D, 0b0011 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x006D, 0b0101 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x0463, 0b0110 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0463, 0b0111 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x049C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Tr5 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04AE, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Deepslate Tr2 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x04CD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tr2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04CE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Tr3 (Deep Dark) (Custom)
  { 'dungeons': [ 0x04DD, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Tr1 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0500, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Dusty Ancient Plank Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x050B, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Obsidian Pillar (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0515, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Cracked Deepslate Brick Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0516, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Deepslate Brick Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0516, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Deepslate Brick Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0517, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Deepslate Brick Tr2 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x068C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sculk Stone (Deep Dark) (Custom)
  { 'dungeons': [ 0x0001, 0b0010 ], 'java': [ 'minecraft:polished_granite' ] }, # Polished Granite
  { 'dungeons': [ 0x002C, 0b0101 ], 'java': [ 'minecraft:stone_brick_slab', { 'type': 'bottom' } ] }, # Stone Brick Slab
  { 'dungeons': [ 0x0042, 0b0000 ], 'java': [ 'minecraft:rail', { 'shape': 'north_south' } ] }, # Rail

  # Deep_Dark_Pool_3

  { 'dungeons': [ 0x04A8, 0b0101 ], 'java': [ 'minecraft:snow', { 'layers': '6' } ] }, # Moss layer (Deep Dark) (Custom)
  { 'dungeons': [ 0x04A8, 0b0110 ], 'java': [ 'minecraft:snow', { 'layers': '7' } ] }, # Moss layer (Deep Dark) (Custom)

  # DesertA1SecretIntsSM

  { 'dungeons': [ 0x058D, 0b0000 ], 'java': [ 'minecraft:cut_sandstone' ] }, # Cut Sandstone (DesertA1) (Custom)
  { 'dungeons': [ 0x058E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone T1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05C4, 0b0000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log (DesertA1) (Custom)
  { 'dungeons': [ 0x05C4, 0b0100 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'x' } ] }, # Spruce Log (DesertA1) (Custom)
  { 'dungeons': [ 0x05C4, 0b1000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'z' } ] }, # Spruce Log (DesertA1) (Custom)
  { 'dungeons': [ 0x05F9, 0b0000 ], 'java': [ 'minecraft:ice' ] }, # Ice (DesertA1) (Custom)
  { 'dungeons': [ 0x05FA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05FB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05FC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05FD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Snow 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0603, 0b0000 ], 'java': [ 'minecraft:stone_bricks' ] }, # Stone Bricks (DesertA1) (Custom)
  { 'dungeons': [ 0x0606, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone (DesertA1) (Custom)
  { 'dungeons': [ 0x0607, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Pillar (DesertA1) (Custom)
  { 'dungeons': [ 0x0607, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Pillar (DesertA1) (Custom)
  { 'dungeons': [ 0x0607, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Pillar (DesertA1) (Custom)
  { 'dungeons': [ 0x0608, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark (DesertA1) (Custom)
  { 'dungeons': [ 0x0609, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x060A, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Flagstone Dark Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0610, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Ice 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0611, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Ice 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0612, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Ice 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x061B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard (DesertA1) (Custom)
  { 'dungeons': [ 0x061C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Sand 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x061D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x061E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x061F, 0b0000 ], 'java': [ 'minecraft:sand' ] }, # Sand (DesertA1) (Custom)
  { 'dungeons': [ 0x0620, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Sand 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0621, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0622, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0623, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Sand 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0624, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0625, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0000 ], 'java': [ 'minecraft:snow', { 'layers': '1' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': '2' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0011 ], 'java': [ 'minecraft:snow', { 'layers': '4' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0100 ], 'java': [ 'minecraft:snow', { 'layers': '5' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0101 ], 'java': [ 'minecraft:snow', { 'layers': '6' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0110 ], 'java': [ 'minecraft:snow', { 'layers': '7' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x062A, 0b0111 ], 'java': [ 'minecraft:snow', { 'layers': '8' } ] }, # Sand Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x0644, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete (DesertA1) (Custom)
  { 'dungeons': [ 0x0650, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Concrete Up (DesertA1) (Custom)
  { 'dungeons': [ 0x0655, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Hut Log (DesertA1) (Custom)
  { 'dungeons': [ 0x0655, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Hut Log (DesertA1) (Custom)
  { 'dungeons': [ 0x0655, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Hut Log (DesertA1) (Custom)
  { 'dungeons': [ 0x0657, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Planks (DesertA1) (Custom)
  { 'dungeons': [ 0x00A2, 0b0001 ], 'java': [ 'minecraft:dark_oak_log' ] }, # Dark Oak Log
  { 'dungeons': [ 0x0670, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Planks Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0671, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Planks Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0672, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Planks Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x08AB, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dark Concrete Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x08AB, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Dark Concrete Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x08AC, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flagstone Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x08AC, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Flagstone Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x08CD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Cliff 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x08CE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Cliff 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x08CF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Cliff 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x08D0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice Cliff 4 (DesertA1) (Custom)

  # DesertA1_Bailey

  { 'dungeons': [ 0x0588, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobbled Sandstone (DesertA1) (Custom)
  { 'dungeons': [ 0x058A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobbled Sandstone T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x058B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobbled Sandstone T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x058C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone Sand (DesertA1) (Custom)
  { 'dungeons': [ 0x058F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0590, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0591, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0592, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0593, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0594, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone Top T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0595, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone Top T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0596, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone Top T4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0597, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone Top T5 (DesertA1) (Custom)
  { 'dungeons': [ 0x0598, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone Top T6 (DesertA1) (Custom)
  { 'dungeons': [ 0x0599, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone Top T7 (DesertA1) (Custom)
  { 'dungeons': [ 0x059D, 0b0000 ], 'java': [ 'minecraft:stone' ] }, # Stone (DesertA1) (Custom)
  { 'dungeons': [ 0x059E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone T1 (DesertA1) (Custom)
  { 'dungeons': [ 0x059F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05A0, 0b0000 ], 'java': [ 'minecraft:stone_bricks' ] }, # Stone Bricks (DesertA1) (Custom)
  { 'dungeons': [ 0x05A1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks T1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05A2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05A3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05A4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05A5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks 2 T1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0000 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0001 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0010 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0011 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0100 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0101 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0110 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A8, 0b0111 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Stone Brick Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A9, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Bricks T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A9, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Bricks T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A9, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Bricks T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A9, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Bricks T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05A9, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Bricks T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AC, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Bricks 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AC, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Bricks 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AD, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Bricks 2 T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AD, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Bricks 2 T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AD, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Bricks 2 T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AD, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Bricks 2 T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AD, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Bricks 2 T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AD, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Bricks 2 T1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AE, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Bricks 2 T2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AE, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Bricks 2 T2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AE, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Bricks 2 T2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AE, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Bricks 2 T2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AF, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Bricks 2 T3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AF, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Bricks 2 T3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AF, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Bricks 2 T3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AF, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Bricks 2 T3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AF, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Bricks 2 T3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05AF, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Bricks 2 T3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05B0, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Bricks Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05B1, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Bricks T1 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05B3, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Bricks T3 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0000 ], 'java': [ 'minecraft:snow', { 'layers': '1' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': '2' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0011 ], 'java': [ 'minecraft:snow', { 'layers': '4' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0100 ], 'java': [ 'minecraft:snow', { 'layers': '5' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0101 ], 'java': [ 'minecraft:snow', { 'layers': '6' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0110 ], 'java': [ 'minecraft:snow', { 'layers': '7' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B8, 0b0111 ], 'java': [ 'minecraft:snow', { 'layers': '8' } ] }, # Snow Layer (DesertA1) (Custom)
  { 'dungeons': [ 0x05B9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Frozen Dirt (DesertA1) (Custom)
  { 'dungeons': [ 0x05BA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Frozen Dirt T1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05BB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Frozen Dirt T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05BC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Frozen Dirt T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05BD, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (DesertA1) (Custom)
  { 'dungeons': [ 0x05BE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt T1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05C6, 0b0000 ], 'java': [ 'minecraft:dark_oak_planks' ] }, # Dark Oak Planks (DesertA1) (Custom)
  { 'dungeons': [ 0x05C8, 0b0000 ], 'java': [ 'minecraft:dark_oak_slab' ] }, # Dark Oak Planks Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05D7, 0b0000 ], 'java': [ 'minecraft:snow_block' ] }, # Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x05DB, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dark Oak Planks Snow 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05F5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05F6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone T4 (DesertA1) (Custom)
  { 'dungeons': [ 0x05F7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone T5 (DesertA1) (Custom)
  { 'dungeons': [ 0x05FF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0600, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0601, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0602, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 5 (DesertA1) (Custom)
  { 'dungeons': [ 0x0637, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 2 Sand (DesertA1) (Custom)
  { 'dungeons': [ 0x0638, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 3 Sand (DesertA1) (Custom)
  { 'dungeons': [ 0x0640, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Frozen Dirt T5 (DesertA1) (Custom)
  { 'dungeons': [ 0x0641, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Frozen Dirt T6 (DesertA1) (Custom)
  { 'dungeons': [ 0x0642, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Frozen Dirt T7 (DesertA1) (Custom)
  { 'dungeons': [ 0x06E9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 6 (DesertA1) (Custom)
  { 'dungeons': [ 0x06EA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 7 (DesertA1) (Custom)
  { 'dungeons': [ 0x06EB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 8 (DesertA1) (Custom)
  { 'dungeons': [ 0x06EC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Concrete 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x06ED, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x06EF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete 5 (DesertA1) (Custom)
  { 'dungeons': [ 0x06F5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete 11 (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F6, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Stone Brick 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x06F7, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Brick 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x06F7, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Brick 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x00C6, 0b0000 ], 'java': [ 'minecraft:dirt_path' ] }, # Dirt Path
  { 'dungeons': [ 0x00ED, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x00EE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x00EF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x0052, 0b0000 ], 'java': [ 'minecraft:clay' ] }, # Clay

  # DesertA1_Basement1

  { 'dungeons': [ 0x0575, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # White Box 1 Slab (Custom)
  { 'dungeons': [ 0x0575, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # White Box 1 Slab (Custom)
  { 'dungeons': [ 0x0656, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Planks (DesertA1) (Custom)
  { 'dungeons': [ 0x065B, 0b0000 ], 'java': [ 'minecraft:warped_fence' ] }, # Darker Hut Planks Fence (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065D, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Darker Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Planks Sand 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x065F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Planks Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0660, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Planks Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0661, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Planks Sand 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0662, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Planks Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0663, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Planks Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x066A, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066A, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066A, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066A, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066B, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066B, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066B, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066B, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066C, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066C, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066C, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066C, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Darker Hut Planks Sand 3 Stairs (DesertA1) (Custom)

  # DesertA1_Basement2

  { 'dungeons': [ 0x0626, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Sand 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0627, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0628, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0629, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Sand 4 (DesertA1) (Custom)

  # DesertA1_Basement3

  { 'dungeons': [ 0x0659, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Darker Hut Planks Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0659, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Darker Hut Planks Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0664, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Darker Hut Planks Sand 1 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0665, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Darker Hut Planks Sand 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0666, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Darker Hut Planks Sand 3 Slab (DesertA1) (Custom)

  # DesertA1_Basement4

  { 'dungeons': [ 0x0658, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Lighter Hut Planks Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0658, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Lighter Hut Planks Slab (DesertA1) (Custom)

  # DesertA1_BossArena

  { 'dungeons': [ 0x060B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Ice 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x060C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Ice 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x060D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Ice 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x060E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Ice 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x060F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Ice 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0614, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0615, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0616, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0617, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0618, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0619, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x061A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Snow 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0646, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Concrete (DesertA1) (Custom)
  { 'dungeons': [ 0x0647, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Raw Copper (DesertA1) (Custom)
  { 'dungeons': [ 0x0652, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0653, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x068F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0690, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0691, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x06F3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete 9 (DesertA1) (Custom)
  { 'dungeons': [ 0x08B8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x08B9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x08BA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Concrete 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x08BB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Concrete 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x08CB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete Transition 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x08CC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete Transition 2 (DesertA1) (Custom)

  # DesertA1_Cliffs

  { 'dungeons': [ 0x0584, 0b0000 ], 'java': [ 'minecraft:sandstone' ] }, # Sandstone (DesertA1) (Custom)
  { 'dungeons': [ 0x059B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobblestone T1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05B0, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Brick Slabs (DesertA1) (Custom)
  { 'dungeons': [ 0x05BF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05C0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05C5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spruce Planks (DesertA1) (Custom)
  { 'dungeons': [ 0x05C8, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Dark Oak Plank Slabs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CC, 0b0000 ], 'java': [ 'minecraft:warped_fence' ] }, # Dark Oak Planks Fence (DesertA1) (Custom)
  { 'dungeons': [ 0x05F8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone T6 (DesertA1) (Custom)
  { 'dungeons': [ 0x0673, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Planks Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0674, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Planks Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0675, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Planks Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x00B3, 0b0000 ], 'java': [ 'minecraft:smooth_red_sandstone' ] }, # Smooth Red Sandstone
  { 'dungeons': [ 0x00EA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x00EC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x002D, 0b0000 ], 'java': [ 'minecraft:bricks' ] }, # Bricks
  { 'dungeons': [ 0x004E, 0b0000 ], 'java': [ 'minecraft:snow', { 'layers': '1' } ] }, # Snow Layer
  { 'dungeons': [ 0x004E, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': '2' } ] }, # Snow Layer
  { 'dungeons': [ 0x004E, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Snow Layer
  { 'dungeons': [ 0x004E, 0b0011 ], 'java': [ 'minecraft:snow', { 'layers': '4' } ] }, # Snow Layer

  # DesertA1_FortHalls

  { 'dungeons': [ 0x0609, 0b1000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dark Flagstone Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x009B, 0b0010 ], 'java': [ 'minecraft:quartz_block' ] }, # Quartz Block
  { 'dungeons': [ 0x0649, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete Sand (DesertA1) (Custom)
  { 'dungeons': [ 0x064A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete Sand (DesertA1) (Custom)
  { 'dungeons': [ 0x064B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x064C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete Sand 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x064D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x064E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete Sand 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x064F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks Concrete Dwn (DesertA1) (Custom)
  { 'dungeons': [ 0x0651, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x067A, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Lighter Hut Planks Snow 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x067B, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Lighter Hut Planks Snow Slab 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x0697, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Sand 5 (DesertA1) (Custom)
  { 'dungeons': [ 0x00E6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 

  # DesertA1_Fortress

  { 'dungeons': [ 0x0065, 0b0000 ], 'java': [ 'minecraft:iron_bars' ] }, # Iron Bars
  { 'dungeons': [ 0x006D, 0b0110 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x006D, 0b0111 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Stone Brick Stairs
  { 'dungeons': [ 0x059C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobblestone T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05A7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks 2 T3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05B2, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Bricks T2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05B5, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Bricks 2 T1 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05C7, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Spruce Planks Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05C9, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Spruce Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05C9, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Spruce Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05C9, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Spruce Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05C9, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Spruce Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05C9, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Spruce Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05C9, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Spruce Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05C9, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Spruce Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CA, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] },# Dark Oak Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CA, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] },# Dark Oak Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CA, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] },# Dark Oak Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CA, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] },# Dark Oak Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CA, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] },# Dark Oak Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CA, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] },# Dark Oak Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CA, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] },# Dark Oak Planks Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05CD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spruce Planks Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x05CE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Oak Planks Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x05D5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spruce Planks Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05D6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Oak Planks Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05D8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spruce Planks Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05D9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Oak Planks Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x05DC, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Spruce Planks Snow 3 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05E6, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Spruce Log Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x05E6, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Spruce Log Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x05E6, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Spruce Log Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x05E8, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Spruce Log Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05E8, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Spruce Log Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05E8, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Spruce Log Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x063B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 2 Ice (DesertA1) (Custom)
  { 'dungeons': [ 0x063C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone 3 Ice (DesertA1) (Custom)
  { 'dungeons': [ 0x06F0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete 6 (DesertA1) (Custom)
  { 'dungeons': [ 0x06F8, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Brick Slab 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x06F8, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Brick Slab 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x00C1, 0b0000 ], 'java': [ 'minecraft:spruce_door', { 'half': 'lower', 'open': 'false', 'facing': 'east' } ] }, # Spruce Door
  { 'dungeons': [ 0x00C1, 0b0010 ], 'java': [ 'minecraft:spruce_door', { 'half': 'lower', 'open': 'false', 'facing': 'west' } ] }, # Spruce Door
  { 'dungeons': [ 0x00C1, 0b1000 ], 'java': [ 'minecraft:spruce_door', { 'half': 'upper', 'powered': 'false', 'hinge': 'left' } ] }, # Spruce Door
  { 'dungeons': [ 0x00C1, 0b1001 ], 'java': [ 'minecraft:spruce_door', { 'half': 'upper', 'powered': 'false', 'hinge': 'right' } ] }, # Spruce Door
  { 'dungeons': [ 0x07EB, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Bricks Slab 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x07EB, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Bricks Slab 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0372, 0b0000 ], 'java': [ 'minecraft:spruce_door', { 'half': 'lower', 'open': 'false', 'facing': 'east' } ] }, # Spruce Door (Town) (Custom)
  { 'dungeons': [ 0x0372, 0b0001 ], 'java': [ 'minecraft:spruce_door', { 'half': 'lower', 'open': 'false', 'facing': 'south' } ] }, # Spruce Door (Town) (Custom)
  { 'dungeons': [ 0x0372, 0b0010 ], 'java': [ 'minecraft:spruce_door', { 'half': 'lower', 'open': 'false', 'facing': 'west' } ] }, # Spruce Door (Town) (Custom)
  { 'dungeons': [ 0x0372, 0b1000 ], 'java': [ 'minecraft:spruce_door', { 'half': 'upper', 'powered': 'false', 'hinge': 'left' } ] }, # Spruce Door (Town) (Custom)
  { 'dungeons': [ 0x0372, 0b1001 ], 'java': [ 'minecraft:spruce_door', { 'half': 'upper', 'powered': 'false', 'hinge': 'right' } ] }, # Spruce Door (Town) (Custom)

  # DesertA1_FortressInt

  { 'dungeons': [ 0x0510, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Obsidian Floor Tile 1 Slab (Deep Dark) (Custom)
  { 'dungeons': [ 0x0521, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 9 (Custom)
  { 'dungeons': [ 0x05C1, 0b0000 ], 'java': [ 'minecraft:grass_block' ] }, # Grass (DesertA1) (Custom)
  { 'dungeons': [ 0x05EF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass Side Snow 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05F0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass Side Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05F1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass Side Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0604, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x0605, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x0613, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pillar Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x065A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Lighter Hut Plank Fence (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x065C, 0b0111 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Lighter Hut Plank Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066D, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066D, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066D, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066D, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066E, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066E, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066E, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066F, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066F, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066F, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x066F, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Lighter Hut Plank Sand 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0679, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Lighter Hut Planks Snow 3 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0679, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Lighter Hut Planks Snow 3 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x067A, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Lighter Hut Planks Snow 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x067B, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Lighter Hut Planks Snow 1 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x067C, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Darker Hut Plank Snow 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067C, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Darker Hut Plank Snow 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067C, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Darker Hut Plank Snow 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067C, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Darker Hut Plank Snow 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067E, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Darker Hut Plank Snow 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067E, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Darker Hut Plank Snow 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067F, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067F, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067F, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x067F, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0680, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0680, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0680, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0680, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0681, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0681, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0681, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Lighter Hut Plank Snow 1 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x0692, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Snow 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0693, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Sand 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0694, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Dark Sand 5 (DesertA1) (Custom)
  { 'dungeons': [ 0x0695, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone_Dark Sand 6 (DesertA1) (Custom)
  { 'dungeons': [ 0x0696, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Sand 4 (DesertA1) (Custom)
  { 'dungeons': [ 0x0698, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flagstone Sand 6 (DesertA1) (Custom)
  { 'dungeons': [ 0x0699, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Sand 5 (DesertA1) (Custom)
  { 'dungeons': [ 0x069F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Bookshelf 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x06A0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Bookshelf 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x06A1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Bookshelf 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x06A2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard Snow 5 (DesertA1) (Custom)
  { 'dungeons': [ 0x00E3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x00E4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x0032, 0b0010 ], 'java': [ 'minecraft:wall_torch', { 'facing': 'west' } ] }, # Wall Torch

  # DesertA1_HlfShip_1

  { 'dungeons': [ 0x05C7, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Spruce Planks Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0363, 0b0101 ], 'java': [ 'minecraft:oak_trapdoor', { 'open': 'false', 'half': 'top', 'facing': 'west' } ] }, # Oak Trapdoor (Town) (Custom)

  # DesertA1_IceCaves

  { 'dungeons': [ 0x05C2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05D0, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dark Oak Planks Snow Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05DD, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dark Oak Planks Snow 3 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05ED, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 Dirt 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05EE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 Dirt 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x009D, 0b0000 ], 'java': [ 'minecraft:oak_slab', { 'type': 'double' } ] }, # Oak Planks Double Slab
  { 'dungeons': [ 0x009D, 0b0001 ], 'java': [ 'minecraft:jungle_slab', { 'type': 'double' } ] }, # Jungle Planks Double Slab
  { 'dungeons': [ 0x009D, 0b1101 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # 
  { 'dungeons': [ 0x063D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt T5 (DesertA1) (Custom)
  { 'dungeons': [ 0x063E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt T6 (DesertA1) (Custom)
  { 'dungeons': [ 0x063F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dirt T7 (DesertA1) (Custom)
  { 'dungeons': [ 0x0011, 0b0001 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log
  { 'dungeons': [ 0x0011, 0b0101 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'x' } ] }, # Spruce Log
  { 'dungeons': [ 0x0011, 0b1001 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'z' } ] }, # Spruce Log
  { 'dungeons': [ 0x004F, 0b0000 ], 'java': [ 'minecraft:ice' ] }, # Ice

  # DesertA1_IceLagoon

  { 'dungeons': [ 0x0086, 0b0000 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Spruce Stairs
  { 'dungeons': [ 0x0086, 0b0001 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Spruce Stairs
  { 'dungeons': [ 0x0086, 0b0010 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Spruce Stairs
  { 'dungeons': [ 0x0086, 0b0100 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Spruce Stairs
  { 'dungeons': [ 0x0086, 0b0101 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Spruce Stairs
  { 'dungeons': [ 0x0086, 0b0110 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Spruce Stairs
  { 'dungeons': [ 0x0086, 0b0111 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Spruce Stairs
  { 'dungeons': [ 0x059A, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (DesertA1) (Custom)
  { 'dungeons': [ 0x05CF, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Spruce Planks Snow Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05DA, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Spruce Planks Snow 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05DF, 0b0010 ], 'java': [ 'minecraft:bedrock', { 'facing': 'south', 'half': 'bottom' } ] }, # Dark Oak Plank Snow 2 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x05E1, 0b0010 ], 'java': [ 'minecraft:bedrock', { 'facing': 'south', 'half': 'bottom' } ] }, # Dark Oak Plank Snow 3 Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x009E, 0b1101 ], 'java': [ 'minecraft:dark_oak_slab', { 'type': 'top' } ] }, # Dark Oak Slab
  { 'dungeons': [ 0x00B3, 0b0001 ], 'java': [ 'minecraft:chiseled_red_sandstone' ] }, # Chiseled Red Sandstone

  # DesertA1_LakeArea

  { 'dungeons': [ 0x042E, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (ForestA1) (Custom)
  { 'dungeons': [ 0x0440, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass (ForestA1) (Custom)
  { 'dungeons': [ 0x05B2, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Bricks T2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05E9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 Dirt 1 (DesertA1) (Custom)
  { 'dungeons': [ 0x05F2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 Snow (DesertA1) (Custom)
  { 'dungeons': [ 0x05F3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 Snow 2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05F4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 2 Snow 3 (DesertA1) (Custom)
  { 'dungeons': [ 0x00AE, 0b0000 ], 'java': [ 'minecraft:packed_ice' ] }, # Packed Ice
  { 'dungeons': [ 0x06E8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 5 (DesertA1) (Custom)

  # DesertA1_MountainX

  { 'dungeons': [ 0x0444, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ice (ForestA1) (Custom)
   { 'dungeons': [ 0x0578, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # White Box 1 Stairs (Custom)
  { 'dungeons': [ 0x0578, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # White Box 1 Stairs (Custom)
  { 'dungeons': [ 0x0589, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cobbled Sandstone T1 (DesertA1) (Custom)

  # DesertA1_ShipInt_1

  { 'dungeons': [ 0x05E3, 0b0000 ], 'java': [ 'minecraft:warped_fence' ] }, # Dark Oak Planks Snow 2 Fence (DesertA1) (Custom)

  # DesertA1_TaigaVBeach

  { 'dungeons': [ 0x03A2, 0b0000 ], 'java': [ 'minecraft:farmland', { 'moisture': '7' } ] }, # Wet Farmland (PlainsA1) (Custom)
  { 'dungeons': [ 0x03A3, 0b0000 ], 'java': [ 'minecraft:farmland', { 'moisture': '0' } ] }, # Dry Farmland (PlainsA1) (Custom)
  { 'dungeons': [ 0x03AE, 0b0000 ], 'java': [ 'minecraft:infested_stone' ] }, # Infested Stone (PlainsA1) (Custom)
  { 'dungeons': [ 0x03B0, 0b0000 ], 'java': [ 'minecraft:mycelium' ] }, # Mycelium (PlainsA1) (Custom)

  # DesertA1_Tower

  { 'dungeons': [ 0x067D, 0b0001 ], 'java': [ 'minecraft:bedrock' ] }, # Darker Hut Plank Snow 2 Stairs (DesertA1) (Custom)

  # Desert_Towers_Pool

  { 'dungeons': [ 0x051C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 4 (Custom)
  { 'dungeons': [ 0x05A6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Bricks 2 T2 (DesertA1) (Custom)
  { 'dungeons': [ 0x05B4, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Bricks 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x05B4, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Bricks 2 Slab (DesertA1) (Custom)
  { 'dungeons': [ 0x0676, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Darker Hut Planks Snow 1 Slab
  { 'dungeons': [ 0x0678, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Darker Hut Planks Snow 3 slab
  { 'dungeons': [ 0x0059, 0b0000 ], 'java': [ 'minecraft:glowstone' ] }, # Glowstone

  # ForestA1-BossZone

  { 'dungeons': [ 0x040A, 0b0000 ], 'java': [ 'minecraft:bricks' ] }, # Bricks (ForestA1) (Custom)
  { 'dungeons': [ 0x040C, 0b0000 ], 'java': [ 'minecraft:orange_wool' ] }, # Orange Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x040D, 0b0000 ], 'java': [ 'minecraft:magenta_wool' ] }, # Magenta Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x040E, 0b0000 ], 'java': [ 'minecraft:light_blue_wool' ] }, # Light Blue Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x0410, 0b0000 ], 'java': [ 'minecraft:lime_wool' ] }, # Lime Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x0411, 0b0000 ], 'java': [ 'minecraft:pink_wool' ] }, # Pink Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x0414, 0b0000 ], 'java': [ 'minecraft:cyan_wool' ] }, # Cyan Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x0415, 0b0000 ], 'java': [ 'minecraft:purple_wool' ] }, # Purple Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x041B, 0b0000 ], 'java': [ 'minecraft:clay' ] }, # Clay (ForestA1) (Custom)
  { 'dungeons': [ 0x041D, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (ForestA1) (Custom)
  { 'dungeons': [ 0x041E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 0 (ForestA1) (Custom)
  { 'dungeons': [ 0x041F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 1 (ForestA1) (Custom)
  { 'dungeons': [ 0x0420, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 10 (ForestA1) (Custom)
  { 'dungeons': [ 0x0421, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 11 (ForestA1) (Custom)
  { 'dungeons': [ 0x0423, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 13 (ForestA1) (Custom)
  { 'dungeons': [ 0x0425, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 15 (ForestA1) (Custom)
  { 'dungeons': [ 0x0428, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 4 (ForestA1) (Custom)
  { 'dungeons': [ 0x0429, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 5 (ForestA1) (Custom)
  { 'dungeons': [ 0x042B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 7 (ForestA1) (Custom)
  { 'dungeons': [ 0x042D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 9 (ForestA1) (Custom)
  { 'dungeons': [ 0x042E, 0b0111 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (ForestA1) (Custom)
  { 'dungeons': [ 0x0431, 0b0000 ], 'java': [ 'minecraft:stone_brick_slab', { 'type': 'double' } ] }, # Stone Bricks Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0434, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 1 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0434, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 1 Double Slab (ForestA1) (Custom) (Unsure why this exists as Double Slabs don't store Top/Bottom State)
  { 'dungeons': [ 0x0435, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 2 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0436, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 3 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0437, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 4 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0437, 0b1011 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 4 Double Slab (ForestA1) (Custom) (Unsure why this exists as Double Slabs don't store Top/Bottom State)
  { 'dungeons': [ 0x0438, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 5 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0438, 0b1100 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 5 Double Slab (ForestA1) (Custom) (Unsure why this exists as Double Slabs don't store Top/Bottom State)
  { 'dungeons': [ 0x0439, 0b1101 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 6 Double Slab (ForestA1) (Custom) (Unsure why this exists as Double Slabs don't store Top/Bottom State)
  { 'dungeons': [ 0x043A, 0b1110 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 7 Double Slab (ForestA1) (Custom) (Unsure why this exists as Double Slabs don't store Top/Bottom State)
  { 'dungeons': [ 0x043B, 0b0000 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'double' } ] }, # Spruce Planks Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x043B, 0b0101 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'double' } ] }, # Spruce Planks Double Slab (ForestA1) (Custom) (Unsure why this exists as Double Slabs don't store Top/Bottom State)
  { 'dungeons': [ 0x0442, 0b0000 ], 'java': [ 'minecraft:gravel' ] }, # Gravel (ForestA1) (Custom)
  { 'dungeons': [ 0x0443, 0b0000 ], 'java': [ 'minecraft:terracotta' ] }, # Terracotta (ForestA1) (Custom)
  { 'dungeons': [ 0x0445, 0b0000 ], 'java': [ 'minecraft:infested_mossy_stone_bricks' ] }, # Infested Mossy Stone Bricks (ForestA1) (Custom)
  { 'dungeons': [ 0x0445, 0b0001 ], 'java': [ 'minecraft:infested_mossy_stone_bricks' ] }, # Infested Mossy Stone Bricks (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0448, 0b0000 ], 'java': [ 'minecraft:infested_stone' ] }, # Infested Stone (ForestA1) (Custom)
  { 'dungeons': [ 0x044A, 0b0000 ], 'java': [ 'minecraft:mycelium' ] }, # Mycelium (ForestA1) (Custom)
  { 'dungeons': [ 0x044C, 0b0000 ], 'java': [ 'minecraft:podzol' ] }, # Podzol (ForestA1) (Custom)
  { 'dungeons': [ 0x0453, 0b0000 ], 'java': [ 'minecraft:white_terracotta' ] }, # White Terracotta (ForestA1) (Custom)
  { 'dungeons': [ 0x0455, 0b0000 ], 'java': [ 'minecraft:magenta_terracotta' ] }, # Magenta Terracotta (ForestA1) (Custom)
  { 'dungeons': [ 0x0455, 0b0010 ], 'java': [ 'minecraft:magenta_terracotta' ] }, # Magenta Terracotta (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0456, 0b0000 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (ForestA1) (Custom)
  { 'dungeons': [ 0x0456, 0b0011 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x045A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 9 (ForestA1) (Custom)
  { 'dungeons': [ 0x045A, 0b1111 ], 'java': [ 'minecraft:bedrock' ] }, # Stone Floor 9 (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x045C, 0b0000 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x045C, 0b0001 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x045C, 0b0010 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x045C, 0b0011 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x045C, 0b0100 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x045C, 0b0101 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x045C, 0b0110 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x045C, 0b0111 ], 'java': [ 'minecraft:dark_oak_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Dark Oak Plank Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0468, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Slab (Grass Top) (ForestA1) (Custom)
  { 'dungeons': [ 0x046F, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 0 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0470, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 1 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0471, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 2 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0473, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 4 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0475, 0b0110 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 6 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0476, 0b0111 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 7 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0477, 0b0000 ], 'java': [ 'minecraft:spruce_slab' ] }, # Spruce Planks Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0477, 0b0101 ], 'java': [ 'minecraft:spruce_slab' ] }, # Spruce Planks Slab (ForestA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Bottom Half)
  { 'dungeons': [ 0x047A, 0b0000 ], 'java': [ 'minecraft:spruce_fence' ] }, # Spruce Planks Fence (ForestA1) (Custom)
  { 'dungeons': [ 0x06C1, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 9 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x06C2, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Magenta Terracotta Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0337, 0b0001 ], 'java': [ 'minecraft:bedrock' ] }, # Stone 1 (Town) (Custom)
  { 'dungeons': [ 0x034E, 0b0000 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Spruce Plank Stairs (Town) (Custom)
  { 'dungeons': [ 0x034E, 0b0001 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Spruce Plank Stairs (Town) (Custom)
  { 'dungeons': [ 0x034E, 0b0010 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Spruce Plank Stairs (Town) (Custom)
  { 'dungeons': [ 0x034E, 0b0011 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Spruce Plank Stairs (Town) (Custom)
  { 'dungeons': [ 0x034E, 0b0100 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Spruce Plank Stairs (Town) (Custom)
  { 'dungeons': [ 0x034E, 0b0110 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Spruce Plank Stairs (Town) (Custom)
  { 'dungeons': [ 0x034E, 0b0111 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Spruce Plank Stairs (Town) (Custom)
  { 'dungeons': [ 0x0359, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 0 Slab (Town) (Custom)
  { 'dungeons': [ 0x036D, 0b0001 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log (Town) (Custom)
  { 'dungeons': [ 0x036D, 0b0101 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'x' } ] }, # Spruce Log (Town) (Custom)
  { 'dungeons': [ 0x036D, 0b1001 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'z' } ] }, # Spruce Log (Town) (Custom)
  { 'dungeons': [ 0x039A, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 4 Double Slab (PlainsA1) (Custom)

  # ForestA1-DangerZone

  { 'dungeons': [ 0x040B, 0b0000 ], 'java': [ 'minecraft:white_wool' ] }, # White Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x040D, 0b0010 ], 'java': [ 'minecraft:magenta_wool' ] }, # Magenta Wool (ForestA1) (Custom)
  { 'dungeons': [ 0x041C, 0b0000 ], 'java': [ 'minecraft:coal_ore' ] }, # Coal Ore (ForestA1) (Custom)
  { 'dungeons': [ 0x0422, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 12 (ForestA1) (Custom)
  { 'dungeons': [ 0x0435, 0b1001 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 2 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x043A, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 7 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0454, 0b0000 ], 'java': [ 'minecraft:orange_terracotta' ] }, # Orange Terracotta (ForestA1) (Custom)
  { 'dungeons': [ 0x0454, 0b0001 ], 'java': [ 'minecraft:orange_terracotta' ] }, # Orange Terracotta (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0470, 0b0001 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 1 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0471, 0b1010 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Floor 2 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0471, 0b0010 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 2 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0471, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Floor 2 Slab (ForestA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Top Half)
  { 'dungeons': [ 0x0473, 0b0100 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 4 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0474, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 5 Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x047C, 0b1101 ], 'java': [ 'minecraft:spruce_leaves', { 'persistent': 'true' } ] }, # Spruce Leaves (ForestA1) (Custom)
  { 'dungeons': [ 0x047D, 0b0000 ], 'java': [ 'minecraft:birch_leaves' ] }, # Birch Leaves (ForestA1) (Custom)
  { 'dungeons': [ 0x047D, 0b1110 ], 'java': [ 'minecraft:birch_leaves', { 'persistent': 'true' } ] }, # Birch Leaves (ForestA1) (Custom)
  { 'dungeons': [ 0x0482, 0b1101 ], 'java': [ 'minecraft:oak_trapdoor', { 'open': 'true', 'half': 'top', 'facing': 'west' } ] }, # Oak Trapdoor (ForestA1) (Custom)
  { 'dungeons': [ 0x08AD, 0b0000 ], 'java': [ 'minecraft:spruce_log' ] }, # Spruce Log (DesertA1) (Custom)
  { 'dungeons': [ 0x0311, 0b0001 ], 'java': [ 'minecraft:spruce_slab' ] }, # Spruce Slab (Town) (Custom)
  { 'dungeons': [ 0x032C, 0b0110 ], 'java': [ 'minecraft:pink_terracotta' ] }, # Pink Terracotta (Town) (Custom)
  { 'dungeons': [ 0x0334, 0b1110 ], 'java': [ 'minecraft:red_terracotta' ] }, # Red Terracotta (Town) (Custom)
  { 'dungeons': [ 0x035F, 0b0001 ], 'java': [ 'minecraft:spruce_slab' ] }, # Spruce Slab (Town) (Custom)
  { 'dungeons': [ 0x035F, 0b1001 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'top' } ] }, # Spruce Slab (Town) (Custom)

  # ForestA1-OutpostZone

  { 'dungeons': [ 0x042E, 0b0001 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (ForestA1) (Custom)
  { 'dungeons': [ 0x0436, 0b1010 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 3 Double Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x0439, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 6 Double Slab (ForestA1) (Custom) 
  { 'dungeons': [ 0x0446, 0b0010 ], 'java': [ 'minecraft:infested_stone_bricks' ] }, # Infested Stone Bricks (ForestA1) (Custom) 
  { 'dungeons': [ 0x0447, 0b0000 ], 'java': [ 'minecraft:infested_chiseled_stone_bricks' ] }, # Infested Chiseled Stone Bricks (ForestA1) (Custom) 
  { 'dungeons': [ 0x0463, 0b0000 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0463, 0b0001 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0463, 0b0010 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0463, 0b0011 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0465, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Cracked Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0465, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Cracked Stone Brick Stairs (ForestA1) (Custom)
  { 'dungeons': [ 0x0473, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Floor 4 Slab (ForestA1) (Custom) 
  { 'dungeons': [ 0x0475, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 6 Slab (ForestA1) (Custom) 
  { 'dungeons': [ 0x0484, 0b0000 ], 'java': [ 'minecraft:snow', { 'layers': '1' } ] }, # Clay Layer (ForestA1) (Custom) 
  { 'dungeons': [ 0x0484, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': '2' } ] }, # Clay Layer (ForestA1) (Custom) 
  { 'dungeons': [ 0x0484, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Clay Layer (ForestA1) (Custom) 
  { 'dungeons': [ 0x0484, 0b0011 ], 'java': [ 'minecraft:snow', { 'layers': '4' } ] }, # Clay Layer (ForestA1) (Custom) 
  { 'dungeons': [ 0x0484, 0b0100 ], 'java': [ 'minecraft:snow', { 'layers': '5' } ] }, # Clay Layer (ForestA1) (Custom) 
  { 'dungeons': [ 0x0313, 0b0011 ], 'java': [ 'minecraft:jungle_slab', { 'type': 'double' } ] }, # Jungle Planks Double Slab (Town) (Custom)

  # ForestA1-Waterfall

  { 'dungeons': [ 0x041D, 0b0011 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (ForestA1) (Custom) 
  { 'dungeons': [ 0x046F, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Floor 0 Slab (ForestA1) (Custom) 
  { 'dungeons': [ 0x0473, 0b1100 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Floor 4 Slab (ForestA1) (Custom) 
  { 'dungeons': [ 0x0476, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Floor 7 Slab (ForestA1) (Custom) 
  { 'dungeons': [ 0x08BC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mud (ForestA1) (Custom) 
  { 'dungeons': [ 0x08BD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mud Dirt 1 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08BE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mud Dirt 2 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08BF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mud Dirt 3 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08C0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 1 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08C2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 3 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08C3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 4 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08C4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 5 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08C5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 6 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08C6, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Spruce Log Root (PlainsA1) (Custom)
  { 'dungeons': [ 0x08C6, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Spruce Log Root (PlainsA1) (Custom)
  { 'dungeons': [ 0x08C6, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Spruce Log Root (PlainsA1) (Custom)
  { 'dungeons': [ 0x08C7, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Spruce Log Root 1 (PlainsA1) (Custom)
  { 'dungeons': [ 0x08C8, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Spruce Log Root 2 (PlainsA1) (Custom)
  { 'dungeons': [ 0x08C8, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Spruce Log Root 2 (PlainsA1) (Custom)
  { 'dungeons': [ 0x08C9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 7 (ForestA1) (Custom) 
  { 'dungeons': [ 0x08CA, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Spruce Log Root 3 (ForestA1) (Custom)

  # ForestA1-WitchZone

  { 'dungeons': [ 0x041B, 0b0001 ], 'java': [ 'minecraft:clay' ] }, # Clay (ForestA1) (Custom) 
  { 'dungeons': [ 0x041B, 0b0010 ], 'java': [ 'minecraft:clay' ] }, # Clay (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x041B, 0b0011 ], 'java': [ 'minecraft:clay' ] }, # Clay (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x041B, 0b0100 ], 'java': [ 'minecraft:clay' ] }, # Clay (ForestA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0730, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Cinder Slab (PeaksA1) (Custom)
  { 'dungeons': [ 0x0788, 0b0000 ], 'java': [ 'minecraft:mossy_stone_brick_wall' ] }, # Mossy Stone Brick Wall (CampA1) (Custom)

  # ForestA1_SpiderCaves

  { 'dungeons': [ 0x0467, 0b0000 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Cobblestone Stairs (ForestA1) (Custom) 
  { 'dungeons': [ 0x046A, 0b0000 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (ForestA1) (Custom)
  { 'dungeons': [ 0x046A, 0b0011 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (ForestA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Bottom Half)
  { 'dungeons': [ 0x046A, 0b1000 ], 'java': [ 'minecraft:cobblestone_slab', { 'type': 'top' } ] }, # Cobblestone Slab  (ForestA1) (Custom)
  { 'dungeons': [ 0x046A, 0b1011 ], 'java': [ 'minecraft:cobblestone_slab', { 'type': 'top' } ] }, # Cobblestone Slab (ForestA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Top Half)
  { 'dungeons': [ 0x08C1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 2 (ForestA1) (Custom)
  { 'dungeons': [ 0x08C3, 0b1000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 4 (ForestA1) (Custom)
  { 'dungeons': [ 0x08C4, 0b1000 ], 'java': [ 'minecraft:bedrock' ] }, # Limestone 5 (ForestA1) (Custom)
  { 'dungeons': [ 0x0393, 0b0000 ], 'java': [ 'minecraft:oak_slab', { 'type': 'double' } ] }, # Oak Planks Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x0398, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 2 Double Slab (PlainsA1) (Custom)

  # ForestA1_Witch_Int

  { 'dungeons': [ 0x04E0, 0b0000 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (Deep Dark) (Custom)

  # HoneycombFields-NE

  { 'dungeons': [ 0x03EC, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Dirt Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03F0, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 4 Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03F0, 0b0100 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 4 Slab (PlainsA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Bottom Half)
  { 'dungeons': [ 0x03F3, 0b0001 ], 'java': [ 'minecraft:spruce_slab' ] }, # Spruce Planks Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03F3, 0b1001 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'top' } ] }, # Spruce Planks Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03FA, 0b0000 ], 'java': [ 'minecraft:oak_fence' ] }, # Oak Planks Fence (PlainsA1) (Custom)
  { 'dungeons': [ 0x03FB, 0b0001 ], 'java': [ 'minecraft:spruce_fence' ] }, # Spruce Planks Fence (PlainsA1) (Custom)
  { 'dungeons': [ 0x0403, 0b0000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'y' } ] }, # Oak Log (PlainsA1) (Custom)
  { 'dungeons': [ 0x0403, 0b0100 ], 'java': [ 'minecraft:oak_log', { 'axis': 'x' } ] }, # Oak Log (PlainsA1) (Custom)
  { 'dungeons': [ 0x0403, 0b1000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'z' } ] }, # Oak Log (PlainsA1) (Custom)
  { 'dungeons': [ 0x0404, 0b1001 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'z' } ] }, # Spruce Log (PlainsA1) (Custom)
  { 'dungeons': [ 0x0376, 0b0000 ], 'java': [ 'minecraft:bricks' ] }, # Bricks (PlainsA1) (Custom)
  { 'dungeons': [ 0x038A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 1 (PlainsA1) (Custom)
  { 'dungeons': [ 0x0394, 0b0000 ], 'java': [ 'minecraft:stone_brick_slab', { 'type': 'double' } ] }, # Stone Bricks Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x0397, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Stone Floor 1 Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x039C, 0b0001 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'double' } ] }, # Spruce Planks Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x039C, 0b1001 ], 'java': [ 'minecraft:spruce_slab', { 'type': 'double' } ] }, # Spruce Planks Double Slab (PlainsA1) (Custom) (Unsure why this exists as Double Slabs don't store Top/Bottom State)
  { 'dungeons': [ 0x03BF, 0b0011 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03C2, 0b0110 ], 'java': [ 'minecraft:pink_terracotta' ] }, # Pink Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DE, 0b0000 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Spruce Planks Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DE, 0b0010 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Spruce Planks Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DE, 0b0011 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Spruce Planks Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DE, 0b0110 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Spruce Planks Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DE, 0b0111 ], 'java': [ 'minecraft:spruce_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Spruce Planks Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03E4, 0b0000 ], 'java': [ 'minecraft:stone_slab' ] }, # Stone Slab (PlainsA1) (Custom)

  # HoneycombFields-NW

  { 'dungeons': [ 0x03E9, 0b0000 ], 'java': [ 'minecraft:stone_brick_slab' ] }, # Stone Bricks Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03E9, 0b1000 ], 'java': [ 'minecraft:stone_brick_slab', { 'type': 'top' } ] }, # Stone Bricks Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03EE, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 2 Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03F0, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Stone Floor 4 Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x0407, 0b0000 ], 'java': [ 'minecraft:hay_block' ] }, # Hay Bale (PlainsA1) (Custom)
  { 'dungeons': [ 0x069E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mid Grass (PlainsA1) (Custom)
  { 'dungeons': [ 0x06A4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Hay Dirt (PlainsA1) (Custom)
  { 'dungeons': [ 0x06A8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Hay Dirt High (PlainsA1) (Custom)
  { 'dungeons': [ 0x037D, 0b0000 ], 'java': [ 'minecraft:pink_wool' ] }, # Pink Wool (PlainsA1) (Custom)
  { 'dungeons': [ 0x0381, 0b0000 ], 'java': [ 'minecraft:purple_wool' ] }, # Purple Wool (PlainsA1) (Custom)
  { 'dungeons': [ 0x0388, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (PlainsA1) (Custom)
  { 'dungeons': [ 0x038C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 3 (PlainsA1) (Custom)
  { 'dungeons': [ 0x038E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 5 (PlainsA1) (Custom)
  { 'dungeons': [ 0x039F, 0b0000 ], 'java': [ 'minecraft:acacia_slab', { 'type': 'double' } ] }, # Acacia Planks Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x039F, 0b0100 ], 'java': [ 'minecraft:acacia_slab', { 'type': 'double' } ] }, # Acacia Planks Double Slab (PlainsA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Bottom Half)
  { 'dungeons': [ 0x03AC, 0b0000 ], 'java': [ 'minecraft:infested_cracked_stone_bricks' ] }, # Infested Cracked Stone Bricks (PlainsA1) (Custom)
  { 'dungeons': [ 0x03B9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Sandstone 1 (PlainsA1) (Custom)
  { 'dungeons': [ 0x03BF, 0b0000 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03C0, 0b0000 ], 'java': [ 'minecraft:yellow_terracotta' ] }, # Yellow Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03C1, 0b0000 ], 'java': [ 'minecraft:lime_terracotta' ] }, # Lime Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03C4, 0b0000 ], 'java': [ 'minecraft:light_gray_terracotta' ] }, # Light Gray Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03C7, 0b0000 ], 'java': [ 'minecraft:blue_terracotta' ] }, # Blue Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03C9, 0b0000 ], 'java': [ 'minecraft:green_terracotta' ] }, # Green Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03C9, 0b1101 ], 'java': [ 'minecraft:green_terracotta' ] }, # Green Terracotta (PlainsA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x03CA, 0b1110 ], 'java': [ 'minecraft:red_terracotta' ] }, # Red Terracotta (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0000 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0001 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0010 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0011 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0100 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0101 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0110 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D7, 0b0111 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03E1, 0b0000 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Stone Brick Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03E6, 0b0000 ], 'java': [ 'minecraft:oak_slab' ] }, # Oak Planks Slab (PlainsA1) (Custom)

  # HoneycombFields-SE

  { 'dungeons': [ 0x03A0, 0b0101 ], 'java': [ 'minecraft:dark_oak_slab', { 'type': 'double' } ] }, # Dark Oak Planks Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D1, 0b0000 ], 'java': [ 'minecraft:polished_andesite' ] }, # Polished Andesite (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D1, 0b0110 ], 'java': [ 'minecraft:polished_andesite' ] }, # Polished Andesite (PlainsA1) (Custom)

  # HoneycombFields-SW

  { 'dungeons': [ 0x03F4, 0b1000 ], 'java': [ 'minecraft:birch_slab', { 'type': 'top' } ] }, # Birch Planks Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x08B1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Path Rock Blend (PlainsA1) (Custom)
  { 'dungeons': [ 0x034A, 0b0000 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x034A, 0b0001 ], 'java': [ 'minecraft:oak_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Oak Plank Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03BD, 0b0001 ], 'java': [ 'minecraft:bedrock' ] }, # 
  { 'dungeons': [ 0x03DF, 0b0100 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Stone Brick Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DF, 0b0101 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Stone Brick Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DF, 0b0110 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Stone Brick Stairs (PlainsA1) (Custom)
  { 'dungeons': [ 0x03DF, 0b0111 ], 'java': [ 'minecraft:stone_brick_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Stone Brick Stairs (PlainsA1) (Custom)

  # KillboxTestWorld

  { 'dungeons': [ 0x00D4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 

  # Lush_Anchor_Boss

  { 'dungeons': [ 0x0525, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone 1 (LushT1) (Custom)
  { 'dungeons': [ 0x0563, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone 1 Flat (LushT1) (Custom)
  { 'dungeons': [ 0x0574, 0b0000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'y' } ] }, # Oak Log (LushT1) (Custom)
  { 'dungeons': [ 0x0574, 0b0100 ], 'java': [ 'minecraft:oak_log', { 'axis': 'x' } ] }, # Oak Log (LushT1) (Custom)
  { 'dungeons': [ 0x0574, 0b1000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'z' } ] }, # Oak Log (LushT1) (Custom)
  { 'dungeons': [ 0x06C4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 1 (LushT1) (Custom)
  { 'dungeons': [ 0x06C5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 2 (LushT1) (Custom)
  { 'dungeons': [ 0x06C7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Gravel (LushT1) (Custom)
  { 'dungeons': [ 0x06C9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Dirt (LushT1) (Custom)
  { 'dungeons': [ 0x06CA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 1 + Dirt (LushT1) (Custom)
  { 'dungeons': [ 0x06CB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Dirt + Stone 1 (LushT1) (Custom)
  { 'dungeons': [ 0x06CC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 1 + Moss (LushT1) (Custom)
  { 'dungeons': [ 0x06D0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Moss Flat (LushT1) (Custom)
  { 'dungeons': [ 0x06D1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Dirt Flat (LushT1) (Custom)
  { 'dungeons': [ 0x06D2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Dirt + Moss (LushT1) (Custom)
  { 'dungeons': [ 0x06D4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Gravel Flat (LushT1) (Custom)
  { 'dungeons': [ 0x06E0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone + Moss Side (LushT1) (Custom)
  { 'dungeons': [ 0x06E1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Dirt + Moss Side (LushT1) (Custom)
  { 'dungeons': [ 0x06E6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Moss + Dirt Blend (LushT1) (Custom)
  { 'dungeons': [ 0x0701, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Dark Moss (LushT1) (Custom)
  { 'dungeons': [ 0x0702, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone + Dark Moss Side (LushT1) (Custom)
  { 'dungeons': [ 0x0703, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 1 + Dark Moss (LushT1) (Custom)

  # MA2_Fortress_Anc_001

  { 'dungeons': [ 0x0522, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Box 10 (Custom)
  { 'dungeons': [ 0x07FE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Red Cliff (MeadowA2) (Custom)
  { 'dungeons': [ 0x0801, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Soft Grass (MeadowA2) (Custom)
  { 'dungeons': [ 0x080F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Grass (MeadowA2) (Custom)
  { 'dungeons': [ 0x0812, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Cliff Purple Blend (MeadowA2) (Custom)
  { 'dungeons': [ 0x0817, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Red Cliff Top Blend 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0818, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Red Cliff Top Blend 4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x081C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Grass Sponge T4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x081D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Grass Sponge T5 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0827, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x082B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Grass Slab  (MeadowA2) (Custom)
  { 'dungeons': [ 0x0834, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Light 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0836, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Light 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0838, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Light 4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x083A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Light 5 (MeadowA2) (Custom)
  { 'dungeons': [ 0x083C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Light 6 (MeadowA2) (Custom)
  { 'dungeons': [ 0x083E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Light 7 (MeadowA2) (Custom)
  { 'dungeons': [ 0x083F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Light Concrete (MeadowA2) (Custom)
  { 'dungeons': [ 0x0844, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mid Concrete (MeadowA2) (Custom)
  { 'dungeons': [ 0x0848, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mid Concrete 4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x084A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Brick 1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x084B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Brick 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x084C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Brick 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x084D, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Light Concrete Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x084D, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Light Concrete Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x084D, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Light Concrete Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0852, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Mid Concrete Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0852, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Mid Concrete Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0852, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Mid Concrete Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0857, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Brick Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0857, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Brick Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0857, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Brick Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0857, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Brick Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0862, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard (MeadowA2) (Custom)
  { 'dungeons': [ 0x0866, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard 5 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0867, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard 6 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0868, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard 7 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0869, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 5 (MeadowA2) (Custom)
  { 'dungeons': [ 0x086A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 6 (MeadowA2) (Custom)
  { 'dungeons': [ 0x086B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 7 (MeadowA2) (Custom)

  # MeadowA1_CentralZone

  { 'dungeons': [ 0x052B, 0b0000 ], 'java': [ 'minecraft:bricks' ] }, # Bricks (MeadowA1) (Custom)
  { 'dungeons': [ 0x052D, 0b0000 ], 'java': [ 'minecraft:brick_slab' ] }, # Brick Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x052D, 0b0100 ], 'java': [ 'minecraft:brick_slab' ] }, # Brick Slab (MeadowA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Bottom Half)
  { 'dungeons': [ 0x052D, 0b1000 ], 'java': [ 'minecraft:brick_slab', { 'type': 'top' } ] }, # Brick Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x052E, 0b0000 ], 'java': [ 'minecraft:clay' ] }, # Clay (MeadowA1) (Custom)
  { 'dungeons': [ 0x052F, 0b0000 ], 'java': [ 'minecraft:cobblestone' ] }, # Cobblestone (MeadowA1) (Custom)
  { 'dungeons': [ 0x0531, 0b0000 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0532, 0b0000 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (MeadowA1) (Custom)
  { 'dungeons': [ 0x0533, 0b0000 ], 'java': [ 'minecraft:stone_slab', { 'type': 'double' } ] }, # Stone Double Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0534, 0b0000 ], 'java': [ 'minecraft:stone_slab' ] }, # Stone Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0534, 0b1000 ], 'java': [ 'minecraft:stone_slab', { 'type': 'top' } ] }, # Stone Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0537, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Orange Terracotta Double Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0539, 0b0000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Birch Log Double Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0539, 0b0010 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] }, # Birch Log Double Slab (MeadowA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Bottom Half)
  { 'dungeons': [ 0x053A, 0b0000 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053A, 0b0001 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053A, 0b0010 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053A, 0b0011 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053A, 0b0100 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053A, 0b0101 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053A, 0b0110 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053A, 0b0111 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Birch Plank Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x053C, 0b0000 ], 'java': [ 'minecraft:grass_block' ] }, # Grass (MeadowA1) (Custom)
  { 'dungeons': [ 0x053D, 0b0000 ], 'java': [ 'minecraft:terracotta' ] }, # Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0546, 0b0000 ], 'java': [ 'minecraft:podzol' ] }, # Podzol (MeadowA1) (Custom)
  { 'dungeons': [ 0x0547, 0b0000 ], 'java': [ 'minecraft:white_terracotta' ] }, # White Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0549, 0b0000 ], 'java': [ 'minecraft:magenta_terracotta' ] }, # Magenta Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0549, 0b0010 ], 'java': [ 'minecraft:magenta_terracotta' ] }, # Magenta Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x054A, 0b0000 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x054A, 0b0011 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x054B, 0b0000 ], 'java': [ 'minecraft:yellow_terracotta' ] }, # Yellow Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x054B, 0b0100 ], 'java': [ 'minecraft:yellow_terracotta' ] }, # Yellow Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x054C, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Yellow Terracotta Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x054C, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Yellow Terracotta Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x054D, 0b0000 ], 'java': [ 'minecraft:lime_terracotta' ] }, # Lime Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x054D, 0b0101 ], 'java': [ 'minecraft:lime_terracotta' ] }, # Lime Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x054E, 0b0000 ], 'java': [ 'minecraft:pink_terracotta' ] }, # Pink Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x054E, 0b0110 ], 'java': [ 'minecraft:pink_terracotta' ] }, # Pink Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x054F, 0b0000 ], 'java': [ 'minecraft:gray_terracotta' ] }, # Gray Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x054F, 0b0111 ], 'java': [ 'minecraft:gray_terracotta' ] }, # Gray Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0550, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Gray Terracotta Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0550, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Gray Terracotta Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0551, 0b0000 ], 'java': [ 'minecraft:light_gray_terracotta' ] }, # Light Gray Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0551, 0b1000 ], 'java': [ 'minecraft:light_gray_terracotta' ] }, # Light Gray Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0552, 0b0000 ], 'java': [ 'minecraft:cyan_terracotta' ] }, # Cyan Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0552, 0b1001 ], 'java': [ 'minecraft:cyan_terracotta' ] }, # Cyan Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0553, 0b0000 ], 'java': [ 'minecraft:purple_terracotta' ] }, # Purple Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0553, 0b1010 ], 'java': [ 'minecraft:purple_terracotta' ] }, # Purple Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0554, 0b0000 ], 'java': [ 'minecraft:blue_terracotta' ] }, # Blue Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0554, 0b1011 ], 'java': [ 'minecraft:blue_terracotta' ] }, # Blue Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0557, 0b0000 ], 'java': [ 'minecraft:cobblestone_wall' ] }, # Cobblestone Wall (MeadowA1) (Custom)
  { 'dungeons': [ 0x055C, 0b0000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log (MeadowA1) (Custom)
  { 'dungeons': [ 0x055C, 0b0001 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'y' } ] }, # Spruce Log (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x055C, 0b0100 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'x' } ] }, # Spruce Log (MeadowA1) (Custom)
  { 'dungeons': [ 0x055C, 0b1000 ], 'java': [ 'minecraft:spruce_log', { 'axis': 'z' } ] }, # Spruce Log (MeadowA1) (Custom)
  { 'dungeons': [ 0x055E, 0b0001 ], 'java': [ 'minecraft:snow', { 'layers': '2' } ] }, # Clay Layer (MeadowA1) (Custom)
  { 'dungeons': [ 0x055E, 0b0010 ], 'java': [ 'minecraft:snow', { 'layers': '3' } ] }, # Clay Layer (MeadowA1) (Custom)
  { 'dungeons': [ 0x055E, 0b0101 ], 'java': [ 'minecraft:snow', { 'layers': '6' } ] }, # Clay Layer (MeadowA1) (Custom)
  { 'dungeons': [ 0x055E, 0b0110 ], 'java': [ 'minecraft:snow', { 'layers': '7' } ] }, # Clay Layer (MeadowA1) (Custom)
  { 'dungeons': [ 0x06B6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Purple Terracotta 2 (MeadowA1) (Custom)
  { 'dungeons': [ 0x06B7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Purple Terracotta 3 (MeadowA1) (Custom)
  { 'dungeons': [ 0x074B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Brick Vines 1 (MeadowA1) (Custom)
  { 'dungeons': [ 0x074C, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Brick Vines 2 (MeadowA1) (Custom)
  { 'dungeons': [ 0x074D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Brick Vines 3 (MeadowA1) (Custom)
  { 'dungeons': [ 0x074E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Brick Vines 4 (MeadowA1) (Custom)

  # MeadowA1_EastZone
  
  { 'dungeons': [ 0x052C, 0b0000 ], 'java': [ 'minecraft:brick_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Brick Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x052C, 0b0001 ], 'java': [ 'minecraft:brick_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Brick Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x052C, 0b0011 ], 'java': [ 'minecraft:brick_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Brick Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x052C, 0b0100 ], 'java': [ 'minecraft:brick_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Brick Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x052C, 0b0110 ], 'java': [ 'minecraft:brick_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Brick Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x052C, 0b0111 ], 'java': [ 'minecraft:brick_stairs', { 'facing': 'north', 'half': 'top' } ] }, # Brick Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x0530, 0b0000 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Cobblestone Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x0530, 0b0001 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Cobblestone Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x0530, 0b0010 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Cobblestone Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x0530, 0b0011 ], 'java': [ 'minecraft:cobblestone_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Cobblestone Stairs (MeadowA1) (Custom)
  { 'dungeons': [ 0x0531, 0b1000 ], 'java': [ 'minecraft:cobblestone_slab' ] }, # Cobblestone Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0538, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 1 Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0538, 0b0001 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 1 Slab (MeadowA1) (Custom) (Unsure why a Duplicate Exists as Blockstate is still Bottom Half)
  { 'dungeons': [ 0x053B, 0b0000 ], 'java': [ 'minecraft:birch_slab' ] }, # Birch Planks Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0548, 0b0000 ], 'java': [ 'minecraft:orange_terracotta' ] }, # Orange Terracotta (MeadowA1) (Custom)
  { 'dungeons': [ 0x0548, 0b0001 ], 'java': [ 'minecraft:orange_terracotta' ] }, # Orange Terracotta (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x0556, 0b0000 ], 'java': [ 'minecraft:granite' ] }, # Granite (MeadowA1) (Custom)
  { 'dungeons': [ 0x0556, 0b0001 ], 'java': [ 'minecraft:granite' ] }, # Granite (MeadowA1) (Custom)
  { 'dungeons': [ 0x0558, 0b0000 ], 'java': [ 'minecraft:brick_wall' ] }, # Brick Wall (MeadowA1) (Custom)
  { 'dungeons': [ 0x055B, 0b0000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'y' } ] }, # Oak Log (MeadowA1) (Custom)
  { 'dungeons': [ 0x055B, 0b1000 ], 'java': [ 'minecraft:oak_log', { 'axis': 'z' } ] }, # Oak Log (MeadowA1) (Custom)
  { 'dungeons': [ 0x055D, 0b0000 ], 'java': [ 'minecraft:birch_log', { 'axis': 'y' } ] }, # Birch Log (MeadowA1) (Custom)
  { 'dungeons': [ 0x055D, 0b0010 ], 'java': [ 'minecraft:birch_log', { 'axis': 'y' } ] }, # Birch Log (MeadowA1) (Custom) (Unsure why this exists as Solid Blocks shouldn't have an extra Blockstate)
  { 'dungeons': [ 0x055D, 0b0100 ], 'java': [ 'minecraft:birch_log', { 'axis': 'x' } ] }, # Birch Log (MeadowA1) (Custom)
  { 'dungeons': [ 0x055D, 0b1000 ], 'java': [ 'minecraft:birch_log', { 'axis': 'z' } ] }, # Birch Log (MeadowA1) (Custom)

  # MeadowA1_NatInterior

  { 'dungeons': [ 0x0576, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # White Box 2 Slab (MeadowA1) (Custom)
  { 'dungeons': [ 0x0576, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # White Box 2 Slab (MeadowA1) (Custom)

  # MeadowA1_PortalTile

  { 'dungeons': [ 0x0545, 0b0000 ], 'java': [ 'minecraft:mycelium' ] }, # Mycelium (MeadowA1) (Custom)
  { 'dungeons': [ 0x0555, 0b0000 ], 'java': [ 'minecraft:stone' ] }, # Stone (MeadowA1) (Custom)
  { 'dungeons': [ 0x011F, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # 

  # MeadowA1_TopZone

  { 'dungeons': [ 0x0544, 0b0000 ], 'java': [ 'minecraft:infested_stone' ] }, # Infested Stone (MeadowA1) (Custom)
  { 'dungeons': [ 0x06B8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Yellow Moss 8 (FungusA1) (Custom)
  { 'dungeons': [ 0x06B9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Yellow Moss 9 (FungusA1) (Custom)
  { 'dungeons': [ 0x06BA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Yellow Moss 10 (FungusA1) (Custom)
  { 'dungeons': [ 0x06BB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Yellow Moss 11 (FungusA1) (Custom)
  { 'dungeons': [ 0x06BD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass Purple 1 (MeadowA1) (Custom)
  { 'dungeons': [ 0x06BE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass Purple 2 (MeadowA1) (Custom)
  { 'dungeons': [ 0x06BF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass Purple 3 (MeadowA1) (Custom)
  { 'dungeons': [ 0x06C0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Bricks 2 (MeadowA1) (Custom)

  # MeadowA2_FortressExt

  { 'dungeons': [ 0x0803, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Soft Grass 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0805, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass (MeadowA2) (Custom)
  { 'dungeons': [ 0x0810, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Grass Sponge (MeadowA2) (Custom)
  { 'dungeons': [ 0x0813, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Red Cliff Top Blend 1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0814, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Red Cliff Top Blend 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0815, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Purple Cliff Down Blend 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0816, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Grass Sponge T2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0819, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x081A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0822, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pillar 4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0825, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0829, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Flag Dark 4 (MeadowA2) (Custom)
  { 'dungeons': [ 0x082B, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Orange Grass Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x0839, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Flag Light 4 Slab (MeadowA2) (Custom)
  { 'dungeons': [ 0x0847, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Mid Concrete 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x084E, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Light Concrete 1 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0859, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Brick 2 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0859, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Brick 2 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0859, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Brick 2 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0859, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Brick 2 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x085A, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Brick 3 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x085A, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Brick 3 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x085A, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Brick 3 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x085A, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Brick 3 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x085E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Dark Concrete 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0863, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0864, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0865, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Checkerboard 4 (MeadowA2) (Custom)

  # MeadowA2_Islands

  { 'dungeons': [ 0x07EC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Buff Clay (MeadowA2) (Custom)
  { 'dungeons': [ 0x07ED, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Buff Clay 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x07EE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Buff Clay 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x07F5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Sponge 2 T1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x07F6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Sponge 2 T2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x07F9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pink Spiral Soft Grass 2 White (MeadowA2) (Custom)
  { 'dungeons': [ 0x07FA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pink Spiral Grass (MeadowA2) (Custom)
  { 'dungeons': [ 0x07FF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Red Cliff Down (MeadowA2) (Custom)
  { 'dungeons': [ 0x0800, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Red Cliff Up (MeadowA2) (Custom)
  { 'dungeons': [ 0x0804, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Soft Grass 2 T1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0811, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass Cliff (MeadowA2) (Custom)

  # MeadowA2_Ravaged

  { 'dungeons': [ 0x0542, 0b0000 ], 'java': [ 'minecraft:infested_chiseled_stone_bricks' ] }, # Infested Chiseled Stone Bricks(MeadowA2) (Custom)
  { 'dungeons': [ 0x07EF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Orange Grass T1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0802, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Soft Grass T1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0806, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass T1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0807, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass T2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0808, 0b0000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'y' } ] }, # Wellspring Log (MeadowA2) (Custom)
  { 'dungeons': [ 0x0808, 0b0100 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'x' } ] }, # Wellspring Log (MeadowA2) (Custom)
  { 'dungeons': [ 0x0808, 0b1000 ], 'java': [ 'minecraft:stripped_acacia_log', { 'axis': 'z' } ] }, # Wellspring Log (MeadowA2) (Custom)
  { 'dungeons': [ 0x0809, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass 2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x080A, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass 2 T1 (MeadowA2) (Custom)
  { 'dungeons': [ 0x080B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Spiral Grass 2 T2 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0821, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pillar 3 (MeadowA2) (Custom)
  { 'dungeons': [ 0x0858, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Brick 1 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0858, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Brick 1 Stairs (MeadowA2) (Custom)
  { 'dungeons': [ 0x0858, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Brick 1 Stairs (MeadowA2) (Custom)

  # Meadow_Anchor_001

  { 'dungeons': [ 0x07A2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07A3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 2 (Ravines) (Custom)
  { 'dungeons': [ 0x07A4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 3 (Ravines) (Custom)
  { 'dungeons': [ 0x07A5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 4 (Ravines) (Custom)
  { 'dungeons': [ 0x07A6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 5 (Ravines) (Custom)
  { 'dungeons': [ 0x07A7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 6 (Ravines) (Custom)
  { 'dungeons': [ 0x07A8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 7 (Ravines) (Custom)
  { 'dungeons': [ 0x07A9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 8 (Ravines) (Custom)
  { 'dungeons': [ 0x07AA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 9 (Ravines) (Custom)
  { 'dungeons': [ 0x07AB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 10 (Ravines) (Custom)
  { 'dungeons': [ 0x07AC, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 11 (Ravines) (Custom)
  { 'dungeons': [ 0x07AD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 12 (Ravines) (Custom)
  { 'dungeons': [ 0x07AE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 13 (Ravines) (Custom)
  { 'dungeons': [ 0x07AF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 14 (Ravines) (Custom)
  { 'dungeons': [ 0x07B0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 15 (Ravines) (Custom)
  { 'dungeons': [ 0x07B1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 16 (Ravines) (Custom)
  { 'dungeons': [ 0x07B2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 17 (Ravines) (Custom)
  { 'dungeons': [ 0x07B3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 18 (Ravines) (Custom)
  { 'dungeons': [ 0x07B5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Wall Block 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07B6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Wall Block 3 (Ravines) (Custom)
  { 'dungeons': [ 0x07B7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Wall Block 4 (Ravines) (Custom)
  { 'dungeons': [ 0x07B8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ground Block 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07B9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Ground Block 2 (Ravines) (Custom)
  { 'dungeons': [ 0x07BD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pink Grass 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07BE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pink Grass 2 (Ravines) (Custom)
  { 'dungeons': [ 0x07BF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pink Grass 3 (Ravines) (Custom)
  { 'dungeons': [ 0x07C3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Yellow Grass 2 (Ravines) (Custom)
  { 'dungeons': [ 0x07CF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 25 (Ravines) (Custom)
  { 'dungeons': [ 0x07D0, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 26 (Ravines) (Custom)
  { 'dungeons': [ 0x07D1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 27 (Ravines) (Custom)
  { 'dungeons': [ 0x07D5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 28 (Ravines) (Custom)
  { 'dungeons': [ 0x07D6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 29 (Ravines) (Custom)
  { 'dungeons': [ 0x0377, 0b0000 ], 'java': [ 'minecraft:white_wool' ] }, # White Wool (PlainsA1) (Custom)
  { 'dungeons': [ 0x0382, 0b0000 ], 'java': [ 'minecraft:blue_wool' ] }, # Blue Wool (PlainsA1) (Custom)
  { 'dungeons': [ 0x00CD, 0b0011 ], 'java': [ 'minecraft:light_blue_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b0100 ], 'java': [ 'minecraft:yellow_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b0101 ], 'java': [ 'minecraft:lime_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b0110 ], 'java': [ 'minecraft:pink_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b0111 ], 'java': [ 'minecraft:gray_stained_glass' ] }, #

  # Meadow_Pool_1

  { 'dungeons': [ 0x07B4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Wall Block 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07C1, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Yellow Grass 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07D7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 30 (Ravines) (Custom)
  { 'dungeons': [ 0x07D8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 31 (Ravines) (Custom)
  { 'dungeons': [ 0x07D9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 32 (Ravines) (Custom)
  { 'dungeons': [ 0x00CD, 0b1010 ], 'java': [ 'minecraft:purple_stained_glass' ] }, # 

  # Meadow_Pool_2

  { 'dungeons': [ 0x009F, 0b0000 ], 'java': [ 'minecraft:white_terracotta' ] }, # White Terracotta
  { 'dungeons': [ 0x009F, 0b0010 ], 'java': [ 'minecraft:magenta_terracotta' ] }, # Magenta Terracotta
  { 'dungeons': [ 0x009F, 0b0110 ], 'java': [ 'minecraft:pink_terracotta' ] }, # Pink Terracotta
  { 'dungeons': [ 0x009F, 0b1011 ], 'java': [ 'minecraft:blue_terracotta' ] }, # Blue Terracotta

  # MovementAndCombat

  { 'dungeons': [ 0x0089, 0b0010 ], 'java': [ 'minecraft:command_block' ] }, # Command Block
  { 'dungeons': [ 0x008F, 0b0010 ], 'java': [ 'minecraft:spruce_button' ] }, # Spruce Button
  { 'dungeons': [ 0x0090, 0b0010 ], 'java': [ 'minecraft:skeleton_skull', { 'rotation': '2' } ] }, # Skull
  { 'dungeons': [ 0x0090, 0b0100 ], 'java': [ 'minecraft:skeleton_skull', { 'rotation': '4' } ] }, # Skull
  { 'dungeons': [ 0x0001, 0b0110 ], 'java': [ 'minecraft:polished_andesite' ] }, # Polished Andesite
  { 'dungeons': [ 0x0005, 0b0000 ], 'java': [ 'minecraft:oak_planks' ] }, # Oak Planks
  { 'dungeons': [ 0x0005, 0b0100 ], 'java': [ 'minecraft:acacia_planks' ] }, # Acacia Planks
  { 'dungeons': [ 0x0055, 0b0101 ], 'java': [ 'minecraft:oak_fence' ] }, # Oak Fence

  # Noteblock_PlainsA2

  { 'dungeons': [ 0x0516, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Deepslate Brick Tr1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0738, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Checkerboard Cinder 1 Slab (PeaksA1) (Custom)

  # PlainsA1_ScoutPoint

  { 'dungeons': [ 0x03A7, 0b0000 ], 'java': [ 'minecraft:dirt_path' ] }, # Dirt Path (PlainsA1) (Custom)

  # PlainsA2_CampTMID

  { 'dungeons': [ 0x08D1, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D1, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D1, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D1, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D1, 0b0100 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'top' } ] }, # Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D1, 0b0110 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'top' } ] }, # Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D2, 0b0000 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Cracked Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D2, 0b0001 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'bottom' } ] }, # Cracked Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D2, 0b0010 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'south', 'half': 'bottom' } ] }, # Cracked Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x08D2, 0b0011 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'north', 'half': 'bottom' } ] }, # Cracked Light Concrete Stairs (DesertA1) (Custom)
  { 'dungeons': [ 0x03D0, 0b0000 ], 'java': [ 'minecraft:andesite' ] }, # Andesite (PlainsA1) (Custom)

  # PlainsA2_Camp_T

  { 'dungeons': [ 0x0389, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 0 (PlainsA1) (Custom)

  # PlainsA2_East

  { 'dungeons': [ 0x071B, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Bricks 1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x071D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Decorative 1 (Deep Dark) (Custom)
  { 'dungeons': [ 0x071E, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Deepslate Decorative 2 (Deep Dark) (Custom)
  { 'dungeons': [ 0x072F, 0b0101 ], 'java': [ 'minecraft:prismarine_stairs', { 'facing': 'west', 'half': 'top' } ] }, # Deepslate Brick 1 Stairs (Deep Dark) (Custom)
  { 'dungeons': [ 0x0399, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor 3 Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03BB, 0b0000 ], 'java': [ 'minecraft:snow_block' ] }, # Snow Block (PlainsA1) (Custom)

  # PlainsA2_NatInterior

  { 'dungeons': [ 0x0528, 0b0000 ], 'java': [ 'minecraft:gravel' ] }, # Gravel (LushT1) (Custom)
  { 'dungeons': [ 0x0562, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Stone 1 + Gravel (LushT1) (Custom)
  { 'dungeons': [ 0x06C3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Moss (LushT1) (Custom)
  { 'dungeons': [ 0x06C6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 3 (LushT1) (Custom)
  { 'dungeons': [ 0x06C8, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Clay (LushT1) (Custom)
  { 'dungeons': [ 0x06CD, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 1 + Gravel (LushT1) (Custom)
  { 'dungeons': [ 0x06CE, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 1 Flat (LushT1) (Custom)
  { 'dungeons': [ 0x06CF, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 2 Flat (LushT1) (Custom)
  { 'dungeons': [ 0x06D5, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Saturated Stone 1 Slab (LushT1) (Custom)
  { 'dungeons': [ 0x06D5, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Saturated Stone 1 Slab (LushT1) (Custom)
  { 'dungeons': [ 0x06D6, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Saturated Stone 1 Flat Slab (LushT1) (Custom)
  { 'dungeons': [ 0x06D7, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Saturated Moss Slab (LushT1) (Custom)
  { 'dungeons': [ 0x06D9, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Saturated Dirt Flat Slab (LushT1) (Custom)
  { 'dungeons': [ 0x06DA, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Saturated Gravel Flat Slab (LushT1) (Custom)
  { 'dungeons': [ 0x06DB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Gravel Flat Layered (LushT1) (Custom)
  { 'dungeons': [ 0x06DB, 0b0001 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Gravel Flat Layered (LushT1) (Custom)
  { 'dungeons': [ 0x06E2, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Trim 1 Side (LushT1) (Custom)
  { 'dungeons': [ 0x06E4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Trim 3 Side (LushT1) (Custom)
  { 'dungeons': [ 0x06E5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Trim 4 Side (LushT1) (Custom)
  { 'dungeons': [ 0x06E7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Saturated Stone 3 + Moss (LushT1) (Custom)
  { 'dungeons': [ 0x03AD, 0b0000 ], 'java': [ 'minecraft:infested_chiseled_stone_bricks' ] }, # Infested Chiseled Stone Bricks (PlainsA1) (Custom)

  # PlainsA2_NorthWest

  { 'dungeons': [ 0x08D6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 3 (PlainsA2) (Custom)
  { 'dungeons': [ 0x08D7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 6 (PlainsA2) (Custom)
  { 'dungeons': [ 0x08D8, 0b0000 ], 'java': [ 'minecraft:light_blue_terracotta' ] }, # Light Blue Terracotta (PlainsA2) (Custom)
  { 'dungeons': [ 0x08D9, 0b0000 ], 'java': [ 'minecraft:lime_terracotta' ] }, # Lime Terracotta (PlainsA2) (Custom)
  { 'dungeons': [ 0x08DA, 0b0000 ], 'java': [ 'minecraft:yellow_terracotta' ] }, # Yellow Terracotta (PlainsA2) (Custom)
  { 'dungeons': [ 0x08DB, 0b0000 ], 'java': [ 'minecraft:podzol' ] }, # Podzol (PlainsA2) (Custom)
  { 'dungeons': [ 0x0387, 0b0000 ], 'java': [ 'minecraft:clay' ] }, # Clay (PlainsA1) (Custom)
  { 'dungeons': [ 0x039D, 0b0000 ], 'java': [ 'minecraft:birch_slab', { 'type': 'double' } ] }, # Birch Planks Double Slab (PlainsA1) (Custom)
  { 'dungeons': [ 0x03D3, 0b0000 ], 'java': [ 'minecraft:birch_stairs', { 'facing': 'east', 'half': 'bottom' } ] }, # Birch Stairs (PlainsA1) (Custom)

  # PlainsA2_RavagerTMID

  { 'dungeons': [ 0x0491, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Paving Stone 4x Tr2 Slab (Deep Dark) (Custom)

  # PlainsA2_SouthWest

  { 'dungeons': [ 0x03EF, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Stone Floor Slab 3 (PlainsA1) (Custom)
  { 'dungeons': [ 0x057D, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Blue Rock 1 (FungusA1) (Custom)
  { 'dungeons': [ 0x08D5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Custom 1 (PlainsA2) (Custom)
  { 'dungeons': [ 0x03C5, 0b0000 ], 'java': [ 'minecraft:cyan_terracotta' ] }, # Cyan Terracotta (PlainsA1) (Custom)

  # Ravines_Anchor_001

  { 'dungeons': [ 0x07BA, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Clay Slab (Ravines) (Custom)
  { 'dungeons': [ 0x07BB, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Snow Slab (Ravines) (Custom)
  { 'dungeons': [ 0x07C0, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Pink Grass Slab 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07C2, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Yellow Grass Slab 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07C7, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Pink Grass Slab 2 (Ravines) (Custom)
  { 'dungeons': [ 0x07C8, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Yellow Grass Slab 2 (Ravines) (Custom)
  { 'dungeons': [ 0x07C9, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 22 (Ravines) (Custom)
  { 'dungeons': [ 0x07CA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 23 (Ravines) (Custom)
  { 'dungeons': [ 0x07CB, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 24 (Ravines) (Custom)
  { 'dungeons': [ 0x07CC, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Wall Slab 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07CC, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Wall Slab 1 (Ravines) (Custom)
  { 'dungeons': [ 0x07CD, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Wall Slab 2 (Ravines) (Custom)
  { 'dungeons': [ 0x07CE, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Wall Slab 3 (Ravines) (Custom)
  { 'dungeons': [ 0x07CE, 0b1000 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'top' } ] }, # Wall Slab 3 (Ravines) (Custom)

  # Ravines_Anchor_Boss

  { 'dungeons': [ 0x00CD, 0b1011 ], 'java': [ 'minecraft:blue_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b1100 ], 'java': [ 'minecraft:brown_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b1101 ], 'java': [ 'minecraft:green_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b1110 ], 'java': [ 'minecraft:red_stained_glass' ] }, # 
  { 'dungeons': [ 0x00CD, 0b1111 ], 'java': [ 'minecraft:black_stained_glass' ] }, # 

  # Ravines_Pool_1

  { 'dungeons': [ 0x07C4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 19 (Ravines) (Custom)
  { 'dungeons': [ 0x07C5, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 20 (Ravines) (Custom)
  { 'dungeons': [ 0x07DA, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Pink Grass Slab 4 (Ravines) (Custom)

  # Ravines_Pool_2

  { 'dungeons': [ 0x07C6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Transition Block 21 (Ravines) (Custom)
  { 'dungeons': [ 0x07D2, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Purple Terracotta Slab (Ravines) (Custom)
  { 'dungeons': [ 0x07D3, 0b0000 ], 'java': [ 'minecraft:prismarine_slab' ] }, # Blue Terracotta Slab (Ravines) (Custom)

  # SpookyBarn_Basement

  { 'dungeons': [ 0x037A, 0b0000 ], 'java': [ 'minecraft:light_blue_wool' ] }, # Light Blue Wool (PlainsA1) (Custom)
  { 'dungeons': [ 0x0384, 0b0000 ], 'java': [ 'minecraft:green_wool' ] }, # Green Wool (PlainsA1) (Custom)
  { 'dungeons': [ 0x0385, 0b0000 ], 'java': [ 'minecraft:red_wool' ] }, # Red Wool (PlainsA1) (Custom)
  { 'dungeons': [ 0x0386, 0b0000 ], 'java': [ 'minecraft:black_wool' ] }, # Black Wool (PlainsA1) (Custom)

  # TA_ForestA1_DesertA1

  { 'dungeons': [ 0x05C3, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # Grass 3 (DesertA1) (Custom)

  # TA_PlainsA2_ForestA1

  { 'dungeons': [ 0x08B4, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Stone Grass 1 (PlainsA1) (Custom)
  { 'dungeons': [ 0x0390, 0b0111 ], 'java': [ 'minecraft:dirt' ] }, # Dirt (PlainsA1) (Custom)

  # Town_Transition

  { 'dungeons': [ 0x08B6, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Stone Grass 3 (PlainsA1) (Custom)
  { 'dungeons': [ 0x08B7, 0b0000 ], 'java': [ 'minecraft:bedrock' ] }, # White Stone Grass 4 (PlainsA1) (Custom)
  { 'dungeons': [ 0x039E, 0b0011 ], 'java': [ 'minecraft:prismarine_slab', { 'type': 'double' } ] } # Podzol Double Slab (PlainsA1) (Custom)
]

blocks_by_java_id = {}
blocks_by_dungeons_id = {}

for i, b in enumerate(blocks):
  if b['java'][0] in blocks_by_java_id:
    blocks_by_java_id[b['java'][0]].append(b)
  else:
    blocks_by_java_id[b['java'][0]] = [b]

  if len(b['dungeons']) > 1:
    if len(b['dungeons']) > 2:
      for m in range(16):
        if m & b['dungeons'][2] == b['dungeons'][1]:
          blocks_by_dungeons_id[b['dungeons'][0] << 4 | m] = b
    else:
      blocks_by_dungeons_id[b['dungeons'][0] << 4 | b['dungeons'][1]] = b
  else:
    for m in range(16):
      blocks_by_dungeons_id[b['dungeons'][0] << 4 | m] = b

def find_java_block(block):
  namespaced_id = block.namespace + ':' + block.id
  if not namespaced_id in blocks_by_java_id:
    return None

  if len(block.properties) > 0:
    for b in blocks_by_java_id[namespaced_id]:
      if len(b['java']) > 1:
        matches = True
        for prop in b['java'][1]:
          if not prop in block.properties or b['java'][1][prop] != block.properties[prop].value:
            matches = False
            break
        if matches:
          return b
      else:
        return b
  else:
    return blocks_by_java_id[namespaced_id][0]

  return None

def find_dungeons_block(block_id, block_data=0):
  k = block_id << 4 | block_data
  if k in blocks_by_dungeons_id:
    return blocks_by_dungeons_id[k]
  else:
    return None