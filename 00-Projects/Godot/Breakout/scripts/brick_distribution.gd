extends Node2D

signal next_level(num)
signal emit_success


@export var brick_scene: PackedScene
var width = 64
var height = 32
var top_gap = 68 + height / 2
var left_gap = 16 + width / 2
var num_colors = 6
var bricks = 0
var level_num = 0

var level1= ["0101010", 
			  "1010101",
			  "1111111",
			  "1100011",
			  "1100011",
			  "1100011",
			  "1001001",
			  "1001001",
			  "1001001",
			  "1111111"]

var level2= ["1100011", 
			  "0001000",
			  "0010100",
			  "0101010",
			  "1010101",
			  "1010101",
			  "0101010",
			  "0010100",
			  "0001000",
			  "1100011"]

var level3= ["1010101", 
			 "0101010",
			 "1010101",
			 "0101010",
			 "1010101",
			 "0101010",
			 "1010101",
			 "0101010",
			 "1010101",
			 "0101010"]
			
var level4= ["0000111", 
			 "0001110",
			 "0011110",
			 "1111000",
			 "1111000",
			 "1111000",
			 "1111100",
			 "0111110",
			 "0001110",
			 "0000111"]
			
var level_TEST = ["0000000", 
			  "0000100",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000"]

var level5 = ["1111111", 
			  "1111111",
			  "1111111",
			  "1111111",
			  "1111111",
			  "1111111",
			  "1111111",
			  "1111111",
			  "1111111",
			  "1111111"]

var level_blank = ["0000000", 
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000",
			  "0000000"]

var levels = [level1, level2, level3, level4, level5, level_blank]

# Called when the node enters the scene tree for the first time.
func _ready():
	pass
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func spawn_bricks(level):
	var num_color = 0
	var num_line = 0
	for line in level:
		var num_element = 0
		for element in line:
			if element == "1":
				new_brick(num_element, num_line, num_color)
			num_element += 1
		if num_color >= num_colors - 1:
			num_color = 0
		else:
			num_color += 1
		num_line += 1

func new_brick(pos_x, pos_y, color):
	# Declara instancia para un ladrillo	
	var brick = brick_scene.instantiate()
	# Recupera el child sprite
	var brick_sprite = brick.get_child(0)
	# Recupera el listado de animaciones
	var color_animation = brick_sprite.sprite_frames.get_animation_names()
	# Posiciona el ladrillo si se ha dado una coordenada válida
	if position.x >= 0 and position.x <= 6 and position.y >=0 and position.y <= 9:
		brick.position.x = left_gap + pos_x * width
		brick.position.y = top_gap + pos_y * height
		# Da el color si se ha dado el índice correcto
		if color >= 0 and color <= num_colors - 1:
			brick_sprite.play(color_animation[color])
		else:
			brick_sprite.play("blue")
		add_child(brick)
		bricks += 1
		brick.brick_broken.connect(_on_brick_broken)
		var parent_main = get_parent()
		var hud_node = parent_main.get_node("HUD")
		hud_node.start_game.connect(brick._on_start_button)

func _on_brick_broken():
	bricks -= 1
	if bricks <= 0:
		# TODO: Aquí se pasa de nivel
		level_num += 1
		if level_num > 4:  ## SUCCESS
			emit_success.emit()
			level_num = 0
		else:
			next_level.emit(level_num + 1)
			$Timer.start()
		
func _on_timer_timeout():
		spawn_bricks(levels[level_num])
		
func _on_start_button():
	level_num = 0
	#next_level.emit(level_num + 1)
	spawn_bricks(levels[level_num])
