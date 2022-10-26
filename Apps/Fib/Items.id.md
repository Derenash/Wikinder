**Inventory IDs**

Skills (1 - 25):

ID - Name

01 = Fireball
02 = Flame Ring
03 = Flamethrower
04 = Flame Arrow
05 = ~Frostshard~
06 = Snowfall
07 = Pacify
08 = Healing Water
09 = Stoneshot
10 = Quicksand
11 = Tremor
12 = Stone Wall
13 = Zephyr 
14 = Quickstep
15 = Gust
16 = Whirlwind


Items (26 - 63): 

ID - Name 

--------------------fire--------------------
26 = Bone Claw (Decayed Dragon Bone Piece)
27 = Dragonfruit
28 = Phoenix's feather (Phoenix Down)
29 = Sipher's horn
30 = Ignis Stone
32 = Bat wings
--------------------water--------------------
33 = Coconut
34 = Crab/Fish/Oyster/Squid
35 = Crab/Fish/Oyster/Squid
36 = Decorative thing
37 = ~Cooked Food~
38 = ~Cooked Food~
39 = Ancient Manuscript/Puzzle Reward
40 = Perfect Lemon
41 = THE Lemonade
42 = ~Monster Heart~
--------------------earth--------------------
43 = Sacred Fruit
44 = Fireflies
45 = Hard ore
46 = Gemstone
47 = Immortal Golem Piece
48 = ~Item from Shop~
---------------------air---------------------
49 = Ostrich egg
50 = Pine Cone
51 = ~Windmill Product~
52 = ~Scroll 1 (Shop)~
53 = Wind Vane
54 = Air Rabbit paw (~sadge~)

**Game IDs**

Game Ids
 0    - 1    - Passável
 1    - 2    - Não passável 
 2    - 128  - Coisas que não guardam informações
 128  - 256  - Estado de coisas fixas que guardam informações mas n se mexem
 256  - 512  - Npcs      - Guardam sua posição - 16 bits pos
 512  - 1024 - Monstros  - Guardam sua posição - 16 bits pos 10 bits vida
 1024 - 4096 - Jogadores - Guardam sua posicão - 16 bits pos 10 bits vida 12 bits xp


Ns - Does not store information
Never needs parse
  002 -> Lava Cauldron
  022 -> Combiner Water town
  042 -> ??? Unused
  062 -> Windmills


Needs parse
Ncs - Npcs that does not save their positions
  128 -> Bat_cave 01 - (25, 154) & (25, 155)
  129 -> Bat_cave 02 - (37, 132) & (37, 133)
  130 -> Bat_cave 03 - (50, 136) & (51, 136)

  132 -> Bone Claw collection spot 01
  133 -> Bone Claw collection spot 02

  134 -> Phoenix

  148 -> Blessed Lake

  168 -> Group bush with fireflies at night 01
  169 -> Group bush with fireflies at night 02
  170 -> Group bush with fireflies at night 03
  171 -> Group bush with fireflies at night 04
  172 -> Group bush with fireflies at night 05

Needs parse
Npcs
  256 -> Shop, Fire Town Bottom left
  257 -> Shop, Fire Town Bottom right
  258 -> Shop, Fire Town Middle left
  259 -> Shop, Fire Town Top    left
  260 -> Shop, Fire Town Top    right
  
  261 -> Ignis Collection spot 01
  262 -> Ignis Collection spot 02
  263 -> Ignis Collection spot 03
  264 -> Ignis Collection spot 04
  
  296 -> Collect spot Water town a 01
  297 -> Collect spot Water town a 02
  298 -> Collect spot Water town a 03
  299 -> Collect spot Water town a 04
  300 -> Collect spot Water town a 05
  301 -> Collect spot Water town a 06

  302 -> Collect spot Water town b 01
  303 -> Collect spot Water town b 02
  304 -> Collect spot Water town b 03
  305 -> Collect spot Water town b 04
  306 -> Collect spot Water town b 05
  307 -> Collect spot Water town b 06

  308 -> Collect spot Water town c 01
  309 -> Collect spot Water town c 02
  310 -> Collect spot Water town c 03
  311 -> Collect spot Water town c 04
  312 -> Collect spot Water town c 05
  313 -> Collect spot Water town c 06

  314 -> Minigame stone a 01
  315 -> Minigame stone a 02
  316 -> Minigame stone a 03

  317 -> Minigame stone b 01
  318 -> Minigame stone b 02
  319 -> Minigame stone b 03

  320 -> Minigame stone c 01
  321 -> Minigame stone c 02
  322 -> Minigame stone c 03

  323 -> Minigame stone d 01
  324 -> Minigame stone d 02
  325 -> Minigame stone d 03

  326 -> Shop, Water town a 01
  327 -> Shop, Water town a 02

  328 -> Cook, Water Town a 01
  329 -> Cook, Water Town a 02
  330 -> Cook, Water Town a 03

  331 -> Man that wants THE Lemonade 01
  332 -> Man that wants THE Lemonade 02
  333 -> Man that wants THE Lemonade 03

  336 -> Tree that can be blessed 01
  337 -> Tree that can be blessed 02
  338 -> Tree that can be blessed 03
  339 -> Tree that can be blessed 04
  340 -> Tree that can be blessed 05
  341 -> Tree that can be blessed 06
  342 -> Tree that can be blessed 07
  343 -> Tree that can be blessed 08
  344 -> Tree that can be blessed 09
  345 -> Tree that can be blessed 10

  346 -> Mining Spot a 01
  347 -> Mining Spot a 02
  348 -> Mining Spot a 03
  349 -> Mining Spot a 04
  350 -> Mining Spot a 05
  
  351 -> Mining Spot b 01
  352 -> Mining Spot b 02
  353 -> Mining Spot b 03
  354 -> Mining Spot b 04
  355 -> Mining Spot b 05

  376 -> Pine Tree 01
  377 -> Pine Tree 02
  378 -> Pine Tree 03
  379 -> Pine Tree 04
  380 -> Pine Tree 05
  381 -> Pine Tree 06
  382 -> Pine Tree 07
  383 -> Pine Tree 08
  384 -> Pine Tree 09
  385 -> Pine Tree 10

  386 -> Mill 01
  387 -> Mill 02
  388 -> Mill 03

  389 -> Shop magics, Air Town 01
  390 -> Shop magics, Air Town 02
  391 -> Shop magics, Air Town 03

Need parse
Monsters
  512 -> Bat from Batcave 01
  513 -> Bat from Batcave 02
  514 -> Bat from Batcave 03

  562 -> Poro 01
  563 -> Poro 02
  564 -> Poro 03
  565 -> Poro 04
  566 -> Poro 05
  567 -> Poro 06

  612 -> Golem earth town 01
  613 -> Golem earth town 02
  614 -> Golem earth town 03

  652 -> Egg Defensor 01
  653 -> Egg Defensor 02
  654 -> Egg Defensor 03

  655 -> Fragile creature air town 01
  656 -> Fragile creature air town 02
  657 -> Fragile creature air town 03
  658 -> Fragile creature air town 04
  659 -> Fragile creature air town 05
  660 -> Fragile creature air town 06
  661 -> Fragile creature air town 07
  662 -> Fragile creature air town 08
  663 -> Fragile creature air town 09
  664 -> Fragile creature air town 10

Players 1024 -> 4095


  Shop Generic function
    Used to determine which items are sold for which price at the shop
    Should receive a (List Pair U120 U120), the first one being the item id, and the second being the price?
    Should return a Function, that receives the interact data and returns the interaction to buy chosen item
      (data: U120) -> (interaction: Apps.Fib.Interaction Unit)

  Generic Collect Item function
    Collects if out of cd and places on cd
    Should receive the cooldown and a item as args

  Generic reaction function
    Creature that attacks back at x range
    Should receive damage and range as args
  
  Generic death function to modify player
    Rewards player with anything after a kill
    Should receive a Player -> Player

  Generic death function to add Exp Gold Item to a player
    Rewards player with exp gold or/and items after a kill
    Should receive Exp Gold and List of Items
  
  Generic combine function
    Used to determine which items are needed for the available trades of an NPC
    Like shop's generic function, it should return a function
    Should receive a (List (Pair (List U120) U120)), A list of possible combinations of n itens to get another one
    Should return a Function, that receives the interact data and returns the interaction to combine certain items to create the selected item
      (data: U120) -> (interaction: Apps.Fib.Interaction Unit)
    Basically the function should decide which Apps.Fib.Interaction.item.combine function should be used
